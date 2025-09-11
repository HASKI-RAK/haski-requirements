#!/usr/bin/env python3
"""Generate the ephemeral MkDocs ``docs/`` tree from canonical sources.

Canonical sources (edited by humans):
  * ``srs/`` – master SRS document
  * ``requirements/`` – individual requirement markdown files with YAML front matter
  * ``traceability/RTM.csv`` – produced by the traceability build (requirements ↔ tests)

This script:
  1. Wipes ``docs/`` and recreates a clean structure
  2. Copies / normalises SRS + Requirement files (adding simple indices / navigation helpers)
  3. Copies the raw ``RTM.csv`` and renders an HTML enhanced, filterable Traceability Matrix
  4. Writes ``.pages`` files so the ``awesome-pages`` plugin builds navigation automatically

No manual edits should be made inside ``docs/`` – they will be overwritten on each run.

The script is intentionally dependency‑light (only stdlib + PyYAML). It can be invoked locally
or inside CI prior to ``mkdocs build --strict``.

RTM multi-source support for File:Line
--------------------------------------
The RTM generator supports multiple test sources per row. Accepted inputs in
RTM.csv columns `test_file` and `test_line`:
    - Inline tokens separated by `;` or `|`, e.g. `a.py:10; b.py:20` (preferred)
    - Parallel lists: `test_file="a.py; b.py"` and `test_line="10; 20"`
    - JSON/YAML lists in either column, e.g. `[{file: a.py, line: 10}, {file: b.py, line: 20}]`
    - JSON/YAML list of strings: `["a.py:10", "b.py:20"]`

All parsed entries are rendered as separate links separated by `<br>` in the table.
"""

from __future__ import annotations

import csv
import logging
import re
import shutil
from collections import Counter
import os
import argparse
from pathlib import Path
from typing import Tuple, Optional, List, Dict

import yaml
from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern

# ---------------------------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
SRS_SRC = ROOT / "srs" / "SRS.md"
REQS_SRC = ROOT / "requirements"
RTM_SRC = ROOT / "traceability" / "RTM.csv"

TRACEABILITY_CONFIG = ROOT / "traceability" / "config.yaml"


# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False):
    """Configure minimal logging for the script.

    - INFO by default
    - DEBUG when --verbose flag is provided
    """
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


def load_github_mappings() -> List[Dict[str, str]]:
    """Load github_file_link_mappings from traceability/config.yaml (single source of truth).

    Returns an empty list if not present or file missing.
    Normalises local_root to absolute resolved paths.
    """
    if not TRACEABILITY_CONFIG.exists():
        logger.debug("traceability/config.yaml not found; no GitHub mappings loaded")
        return []
    try:
        with TRACEABILITY_CONFIG.open("r", encoding="utf-8") as h:
            cfg = yaml.safe_load(h) or {}
    except yaml.YAMLError:
        logger.warning("Failed parsing traceability/config.yaml; ignoring github mappings")
        return []
    mappings = []
    for m in cfg.get("github_file_link_mappings", []) or []:
        if not isinstance(m, dict):
            continue
        local_root = m.get("local_root")
        repo = m.get("repo")
        if not local_root or not repo:
            continue  # mandatory fields
        branch = m.get("branch", "main")
        repo_root_subpath = m.get("repo_root_subpath", "")
        # Resolve local_root relative to config file location
        abs_root = (TRACEABILITY_CONFIG.parent / local_root).resolve()
        mappings.append(
            {
                "local_root": str(abs_root),
                "repo": repo,
                "branch": branch,
                "repo_root_subpath": repo_root_subpath,
            }
        )
    logger.debug("Loaded %d GitHub mapping(s)", len(mappings))
    return mappings


def _read_yaml_cfg() -> dict:
    """Internal helper: load traceability/config.yaml safely and return a dict."""
    if not TRACEABILITY_CONFIG.exists():
        return {}
    try:
        with TRACEABILITY_CONFIG.open("r", encoding="utf-8") as h:
            return yaml.safe_load(h) or {}
    except yaml.YAMLError:
        logger.warning("Failed parsing traceability/config.yaml; using empty config")
        return {}


def load_docs_copy_excludes() -> List[str]:
    """Read optional extra excludes for copying into docs from config.yaml.

    Supported keys (list[str]):
      - docs_copy_exclude
      - docs_exclude (legacy alias)

    Entries can be relative paths (to repo root or to the config file),
    absolute paths, or gitignore-style patterns. Returned as gitignore-style
    patterns relative to the repo root.
    """
    cfg = _read_yaml_cfg()
    excludes = cfg.get("docs_copy_exclude") or cfg.get("docs_exclude") or []
    out: List[str] = []
    if not isinstance(excludes, list):
        return out
    for e in excludes:
        if not isinstance(e, str) or not e.strip():
            continue
        e_clean = e.strip()
        # If entry is an absolute or relative path, normalise relative to ROOT
        p = Path(e_clean)
        if not any(ch in e_clean for ch in ["*", "?", "["]):
            # treat like a path
            if not p.is_absolute():
                # try relative to config dir first (more natural when editing config)
                p_abs = (TRACEABILITY_CONFIG.parent / p).resolve()
            else:
                p_abs = p.resolve()
            try:
                rel = p_abs.relative_to(ROOT)
                # If directory, add trailing slash to behave like gitignore dir rule
                if p_abs.is_dir():
                    out.append(rel.as_posix().rstrip("/") + "/")
                else:
                    out.append(rel.as_posix())
                continue
            except Exception:
                # falls through to treat as pattern
                pass
        # Otherwise, treat as a raw gitignore-like pattern relative to root
        out.append(e_clean)
    return out


def load_gitignore_spec(extra_patterns: Optional[List[str]] = None) -> PathSpec:
    """Compile a PathSpec from .gitignore plus extra patterns.

    Always enforces ignoring the output docs/ tree and the VCS dir.
    """
    lines: List[str] = []
    gitignore = ROOT / ".gitignore"
    if gitignore.exists():
        try:
            lines.extend(gitignore.read_text(encoding="utf-8").splitlines())
        except OSError:
            pass
    # Ensure we never recurse into the output or VCS dir
    enforced = [
        "docs/",  # output tree
        ".git/",
    ]
    lines.extend(enforced)
    if extra_patterns:
        lines.extend(extra_patterns)
    # Filter out comments and blank lines
    norm = [ln for ln in (ln.strip() for ln in lines) if ln and not ln.startswith("#")]
    return PathSpec.from_lines(GitWildMatchPattern, norm)


def copy_repo_tree_to_docs(spec: PathSpec):
    """Copy all directories/files from repo into docs/, honoring ignore spec.

    Rules:
      - Start at repo ROOT, skip any path matched by spec
      - Do not copy the ROOT-level files (only directories), to keep docs root clean
      - Never traverse into the output docs/ directory (enforced in spec)
      - Preserve relative paths under docs/
    """
    logger.info("Copying repository content into docs/ (applying ignore rules)")
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=True):
        dpath = Path(dirpath)
        rel_dir = dpath.relative_to(ROOT)

        # Skip the root files – we'll only copy directories content
        if rel_dir == Path("."):
            # Prune ignored directories early to avoid descending
            pruned = []
            for dn in list(dirnames):
                rel = (rel_dir / dn).as_posix()
                if spec.match_file(rel) or spec.match_file(rel + "/"):
                    pruned.append(dn)
            for dn in pruned:
                dirnames.remove(dn)
            # Also explicitly prune output dir if present (belt & braces)
            if DOCS.name in dirnames:
                dirnames.remove(DOCS.name)
            # Do not copy files at the repo root
            continue

        # If current directory itself is ignored, skip subtree
        rel_dir_posix = rel_dir.as_posix()
        if spec.match_file(rel_dir_posix) or spec.match_file(rel_dir_posix + "/"):
            dirnames[:] = []
            continue

        # Prune ignored child directories before descending further
        for dn in list(dirnames):
            child_rel = (rel_dir / dn).as_posix()
            if spec.match_file(child_rel) or spec.match_file(child_rel + "/"):
                dirnames.remove(dn)

        # Copy files in this directory
        for fn in filenames:
            rel_file = (rel_dir / fn).as_posix()
            if spec.match_file(rel_file):
                continue
            src = dpath / fn
            dst = DOCS / rel_dir / fn
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(src, dst)
            except OSError as e:
                # Best-effort copy; skip unreadable files
                logger.debug("Skip unreadable file %s: %s", src, e)
                continue


def effective_ref(branch: str) -> str:
    """Return the effective ref (branch or commit) taking environment overrides.

    Environment precedence (first non-empty wins):
      TRACEABILITY_GITHUB_COMMIT – treat as immutable commit SHA
      TRACEABILITY_GITHUB_REF    – arbitrary ref (tag/branch)
    Fallback: value from config (branch param)
    """
    commit = os.environ.get("TRACEABILITY_GITHUB_COMMIT")
    if commit:
        return commit
    ref = os.environ.get("TRACEABILITY_GITHUB_REF")
    if ref:
        return ref
    return branch


# Cached (loaded once) – acceptable for this CLI tool
GITHUB_FILE_LINK_MAPPINGS = load_github_mappings()


def build_github_file_link(
    local_path: str, line: Optional[str | int], unmatched: Optional[List[str]] = None
) -> Optional[str]:
    """Return an HTML anchor (<a>) linking to the GitHub file:line if mapping matches.

    Parameters
    ----------
    local_path: Absolute (preferred) or relative path to the test file as captured in RTM.csv
    line:       Line number (string or int) – may be missing/blank

    Returns
    -------
    str | None: HTML <a> element or None if no mapping applies
    """
    if not local_path:
        return None
    try:
        p = Path(local_path).resolve()
    except OSError:
        return None

    for mapping in GITHUB_FILE_LINK_MAPPINGS:
        try:
            root = Path(mapping["local_root"]).resolve()
        except KeyError:
            continue
        if root in p.parents or p == root:
            try:
                rel = p.relative_to(root)
            except ValueError:
                # Not actually relative; skip
                continue
            repo = mapping.get("repo")
            if not repo:
                continue
            branch = effective_ref(mapping.get("branch", "main"))
            sub = mapping.get("repo_root_subpath", "")
            # Compose path inside repository
            repo_path_parts = []
            if sub:
                repo_path_parts.append(sub.strip("/"))
            repo_path_parts.append(rel.as_posix())
            repo_path = "/".join(repo_path_parts)
            anchor = f"#L{line}" if line else ""
            url = f"https://github.com/{repo}/blob/{branch}/{repo_path}{anchor}"
            display = f"{repo_path}:{line}" if line else repo_path
            # Basic escaping for '<'
            display = display.replace("<", "&lt;")
            return f"<a href='{url}' target='_blank' rel='noopener noreferrer'>{display}</a>"
    # Track unmatched for diagnostics
    if unmatched is not None:
        unmatched.append(local_path)
    return None


FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _try_parse_yaml_or_json_list(value: str):
    """Attempt to parse a CSV cell content as a YAML/JSON list.

    Returns the parsed Python object if it results in a list or list-like structure,
    otherwise returns None. Safe to use on arbitrary strings.
    """
    if not value:
        return None
    # Fast pre-check to avoid invoking YAML parser for plain scalars most of the time
    s = value.strip()
    if not (s.startswith("[") or s.startswith("- ") or s.startswith("{")):
        # Could still be a scalar; not list-like
        return None
    try:
        parsed = yaml.safe_load(s)
    except Exception:
        return None
    if isinstance(parsed, list):
        return parsed
    # Sometimes a single mapping containing file/line can be provided – normalise to list
    if isinstance(parsed, dict):
        return [parsed]
    return None


def parse_test_sources(
    test_file_field: str, test_line_field: str
) -> List[Tuple[str, Optional[str]]]:
    """Parse multi-source File:Line inputs from RTM.

    Supported formats (mixed per convenience):
      1) Single file and optional line (legacy):
         test_file="path/to/test.py", test_line="123"
      2) Multiple entries separated by ';' or '|':
         test_file="a.py:10; b.py:20"  (preferred: inline path:line)
         or
         test_file="a.py; b.py" and test_line="10; 20"
      3) JSON/YAML list in either column:
         test_file='["a.py:10", "b.py:20"]'
         test_file='["a.py", "b.py"]', test_line='[10, 20]'
         test_file='[{"file":"a.py","line":10}, {"file":"b.py","line":20}]'

    Returns a list of (file, line) where line is an optional string (may be None).
    """

    def normalise_line(x) -> Optional[str]:
        if x is None:
            return None
        s = str(x).strip()
        return s or None

    def from_token(tok: str) -> Tuple[str, Optional[str]]:
        tok = tok.strip()
        # Detect trailing :<digits> to avoid splitting on colons in paths
        m = re.match(r"^(.*?):(\d+)$", tok)
        if m:
            return m.group(1), m.group(2)
        return tok, None

    files_raw = (test_file_field or "").strip()
    lines_raw = (test_line_field or "").strip()

    # 1) JSON/YAML list support
    parsed_files = _try_parse_yaml_or_json_list(files_raw)
    parsed_lines = _try_parse_yaml_or_json_list(lines_raw)

    sources: List[Tuple[str, Optional[str]]] = []

    if isinstance(parsed_files, list):
        # list could be of strings ("a.py:12" or "a.py") or dicts
        for item in parsed_files:
            if isinstance(item, str):
                f, ln = from_token(item)
                sources.append((f, ln))
            elif isinstance(item, dict):
                f = item.get("file") or item.get("path") or item.get("test_file") or ""
                ln = item.get("line") or item.get("ln") or item.get("test_line")
                f = (f or "").strip()
                if f:
                    sources.append((f, normalise_line(ln)))
        # If no lines present in any entries and parsed_lines provided, zip them
        if all(ln is None for _, ln in sources) and isinstance(parsed_lines, list):
            out: List[Tuple[str, Optional[str]]] = []
            for idx, (f, _ln) in enumerate(sources):
                ln = parsed_lines[idx] if idx < len(parsed_lines) else None
                out.append((f, normalise_line(ln)))
            sources = out
        return [(f, ln) for f, ln in sources if f]

    # 2) tokenised scalars separated by ';' or '|'
    def split_tokens(val: str) -> List[str]:
        if not val:
            return []
        # Prefer ';' first (less likely in paths), then '|'
        if ";" in val:
            return [t for t in (v.strip() for v in val.split(";")) if t]
        if "|" in val:
            return [t for t in (v.strip() for v in val.split("|")) if t]
        return [val.strip()] if val.strip() else []

    file_tokens = split_tokens(files_raw)
    # If tokens include inline :line, we ignore test_line_field
    inline_pairs: List[Tuple[str, Optional[str]]] = [from_token(t) for t in file_tokens]
    if any(ln is not None for _, ln in inline_pairs):
        return [(f, ln) for f, ln in inline_pairs if f]

    # Otherwise, zip with lines
    line_tokens = split_tokens(lines_raw)
    if not file_tokens:
        return []
    max_len = max(len(file_tokens), len(line_tokens))
    result: List[Tuple[str, Optional[str]]] = []
    for i in range(max_len):
        f = file_tokens[i] if i < len(file_tokens) else None
        ln = line_tokens[i] if i < len(line_tokens) else None
        if f:
            result.append((f, normalise_line(ln)))
    return result


def read_front_matter(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, ""
    m = FRONT_MATTER_RE.search(text)
    meta = {}
    body = text
    if m:
        try:
            meta = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        body = text[m.end() :]
    return meta, body


def clean_docs():
    if DOCS.exists():
        logger.info("Cleaning docs/ directory")
        for item in DOCS.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
        logger.info("Creating docs/ directory")
        DOCS.mkdir(parents=True)


def write(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_index(requirements_meta: list[dict]):
    lines = [
        "# HASKI Documentation",
        "",
        "## Inhalte",
        "",
        "- **SRS**",
        "- **Requirements**",
        "- **Traceability Matrix (CSV)**",
        "",
        "## Requirements Übersicht",
        "",
    ]
    for meta in sorted(requirements_meta, key=lambda m: m.get("id", "")):
        rid = meta.get("id")
        title = meta.get("title", "")
        if rid:
            # Remove .md from link
            lines.append(f"- [{rid}](requirements/{rid}/) – {title}")
    lines.append("\n---\n_Automatisch generiert._")
    return "\n".join(lines) + "\n"


def copy_srs():
    if SRS_SRC.exists():
        logger.info("Copy SRS -> docs/srs/SRS.md")
        dst = DOCS / "srs" / "SRS.md"
        content = SRS_SRC.read_text(encoding="utf-8")
        banner = "# Software Requirements Specification (SRS)\n\n<!-- Generated copy from srs/SRS.md -->\n\n"
        if not content.lstrip().startswith("#"):
            # keep original if proper heading missing
            banner = ""
        write(dst, banner + content)
    else:
        logger.warning("SRS source not found at %s", SRS_SRC)


def copy_requirements():
    logger.info("Copy requirement files -> docs/requirements/")
    requirements_meta = []
    dst_dir = DOCS / "requirements"
    for src in REQS_SRC.glob("HASKI-REQ-*.md"):
        meta, body = read_front_matter(src)
        if meta is None:
            meta = {}
        rid = meta.get("id") or src.stem
        meta["id"] = rid
        requirements_meta.append(meta)
        # Reconstruct file with original front matter (normalized)
        fm = yaml.safe_dump(meta, sort_keys=False).strip()
        content = f"---\n{fm}\n---\n\n# {rid}\n\n" + body.lstrip()
        write(dst_dir / f"{rid}.md", content)
    # index
    index_lines = ["# Requirements Übersicht", "", "Liste der Anforderungen:", ""]
    for m in sorted(requirements_meta, key=lambda m: m.get("id", "")):
        rid = m["id"]
        title = m.get("title", "")
        # Remove .md from link
        index_lines.append(f"- [{rid}]({rid}/) – {title}")
    index_lines.append("\n_Hinweis: Diese Seite wird automatisch generiert._\n")
    write(dst_dir / "index.md", "\n".join(index_lines))
    # .pages config
    # awesome-pages: remove invalid scalar arrange; natural order is default
    write(dst_dir / ".pages", "title: Requirements\n")
    return requirements_meta


def copy_rtm(verbose: bool = False):
    logger.info("Generate Traceability Matrix page")
    rtm_dir = DOCS / "rtm"
    rtm_dir.mkdir(parents=True, exist_ok=True)
    csv_path = rtm_dir / "RTM.csv"
    if RTM_SRC.exists():
        shutil.copy2(RTM_SRC, csv_path)
    else:
        logger.warning("RTM source not found at %s; writing empty template", RTM_SRC)
        write(
            csv_path,
            "requirement_id,requirement_title,test_name,test_file,test_line,status\n",
        )

    # Build markdown table from CSV
    rows = []
    with csv_path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)
    logger.debug("Loaded %d RTM row(s)", len(rows))

    def link_req(rid: str) -> str:
        if not rid:
            return ""
        # Remove .md from link
        return f"[{rid}](../requirements/{rid}/)"

    # Pre-load requirement excerpts (first non-empty line of body) for tooltip usage
    excerpt_cache: Dict[str, str] = {}
    for req_file in (DOCS / "requirements").glob("HASKI-REQ-*.md"):
        rid = req_file.stem
        try:
            lines = req_file.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        # Skip front matter / heading lines (# RID) and blank lines until first content
        body_lines = []
        skip_heading = True
        for ln in lines:
            if skip_heading:
                if ln.strip().startswith("# "):
                    continue
                if ln.strip() == "" or ln.strip().startswith("---"):
                    continue
                # First real content line
                skip_heading = False
            if not skip_heading:
                if ln.strip():
                    body_lines.append(ln.strip())
                if len(body_lines) >= 1:
                    break
        excerpt = body_lines[0] if body_lines else ""
        # Truncate long excerpts
        if len(excerpt) > 180:
            excerpt = excerpt[:177] + "..."
        # Basic escaping for quotes
        excerpt_cache[rid] = excerpt.replace('"', "&quot;").replace("'", "&#39;")

    # Aggregate status counts
    status_counter = Counter(r.get("status", "") for r in rows if r.get("status"))
    status_order = sorted(status_counter.keys())
    status_lines = []
    total = len(rows)

    def badge(status: str) -> str:
        if not status:
            return ""
        cls = status.lower().replace(" ", "-")
        return f"<span class='rtm-badge rtm-badge--{cls}'>{status}</span>"

    if total:
        status_lines.append("### Status Übersicht")
        status_lines.append("")
        items = []
        for st in status_order:
            cnt = status_counter[st]
            items.append(f"{badge(st)} {cnt} ({cnt/total:.0%})")
        status_lines.append(
            "<div class='rtm-status-summary'>" + " | ".join(items) + "</div>"
        )
        status_lines.append("")

    # Build HTML table (filterable) instead of Markdown pipe table
    table_lines = []
    if rows:
        table_lines.append("<div class='rtm-filters'>")
        table_lines.append(
            "<input id='rtm-search' type='text' placeholder='Filter (Text)...' />"
        )
        if status_order:
            table_lines.append(
                "<select id='rtm-status-filter'><option value=''>Alle Status</option>"
                + "".join([f"<option value='{s}'>{s}</option>" for s in status_order])
                + "</select>"
            )
        table_lines.append("</div>")
        table_lines.append("<table id='rtm-table'>")
        table_lines.append(
            "<thead><tr><th>Requirement</th><th>Test Name"
            "</th><th>File:Line</th><th>Status</th></tr></thead>"
        )
        table_lines.append("<tbody>")
        unmatched_files: List[str] = []
        for r in rows:
            raw_file = r.get("test_file", "") or ""
            raw_line = r.get("test_line", "") or ""
            sources = parse_test_sources(raw_file, raw_line)
            link_pieces: List[str] = []
            if sources:
                for fpath, l in sources:
                    link = build_github_file_link(
                        fpath, l or "", unmatched=unmatched_files
                    )
                    if link:
                        link_pieces.append(link)
                    else:
                        # fallback minimal escaping; omit colon if no line
                        if fpath:
                            display = (
                                f"{fpath}:{l}" if (l and str(l).strip()) else f"{fpath}"
                            )
                        else:
                            display = ""
                        display = display.replace("<", "&lt;")
                        link_pieces.append(display)
                file_line = "<br>".join(link_pieces)
            else:
                link = build_github_file_link(
                    raw_file, raw_line, unmatched=unmatched_files
                )
                if link:
                    file_line = link
                else:
                    if raw_file:
                        display = (
                            f"{raw_file}:{raw_line}"
                            if (raw_line and str(raw_line).strip())
                            else f"{raw_file}"
                        )
                    else:
                        display = ""
                    file_line = display.replace("<", "&lt;")
            st = r.get("status", "")
            rid = r.get("requirement_id", "")
            title_raw = r.get("requirement_title") or ""
            title_display = title_raw.strip() or "(kein Titel)"
            title_display = title_display.replace("<", "&lt;")
            if rid:
                excerpt = excerpt_cache.get(rid, "")
                tooltip_attr = f" title='{excerpt}'" if excerpt else ""
                # Combined cell: ID + optional title below (if different)
                if title_raw.strip():
                    combined_label = f"<strong>{rid}</strong><br><span class='rtm-req-title'>{title_display}</span>"
                else:
                    combined_label = f"<strong>{rid}</strong>"
                # Remove .md from link
                req_cell = f"<a href='../requirements/{rid}/'{tooltip_attr}>{combined_label}</a>"
            else:
                req_cell = title_display or ""
            table_lines.append(
                "<tr data-status='{}'>".format(st)
                + f"<td>{req_cell}</td>"
                + f"<td>{(r.get('test_name') or '').replace('<','&lt;')}</td>"
                + f"<td>{file_line}</td>"
                + f"<td>{badge(st)}</td>"
                + "</tr>"
            )
        table_lines.append("</tbody></table>")
        if verbose and unmatched_files:
            uniq = sorted(set(unmatched_files))
            table_lines.append(
                "<details><summary>Nicht verlinkbare Test-Dateien ({}):</summary><pre>".format(
                    len(uniq)
                )
            )
            for f in uniq:
                table_lines.append(f)
            table_lines.append("</pre></details>")
    else:
        table_lines.append(
            "<p><em>Noch keine Test-Traceability-Daten vorhanden (RTM.csv leer).</em></p>"
        )

    index_md = [
        "# Traceability",
        "",
        "Diese Seite zeigt die aktuelle Traceability-Matrix (Anforderung ↔ Tests).",
        "",
        "CSV Rohdaten: [RTM.csv](RTM.csv)",
        "",
    ]
    index_md.extend(status_lines)
    index_md.append("### Matrix")
    index_md.append("")
    index_md.extend(table_lines)
    index_md.append("")
    index_md.append("_Diese Seite wurde automatisch generiert._")
    write(rtm_dir / "index.md", "\n".join(index_md) + "\n")
    write(rtm_dir / ".pages", "title: Traceability\n")


def top_level_pages(requirements_meta):
    # docs/index.md
    write(DOCS / "index.md", build_index(requirements_meta))
    # top-level .pages ordering
    write(DOCS / ".pages", "nav:\n  - index.md\n  - srs\n  - requirements\n  - rtm\n")


def print_mappings():
    if not GITHUB_FILE_LINK_MAPPINGS:
        logger.info("No GitHub file link mappings configured.")
        return
    logger.info("Active GitHub file link mappings:")
    for m in GITHUB_FILE_LINK_MAPPINGS:
        logger.info(
            "  - repo=%s local_root=%s branch=%s sub=%s",
            m.get('repo'),
            m.get('local_root'),
            m.get('branch'),
            m.get('repo_root_subpath'),
        )


def main():
    parser = argparse.ArgumentParser(
        description="Generate docs (SRS, requirements, RTM)"
    )
    parser.add_argument(
        "--print-mappings",
        action="store_true",
        help="Print active GitHub file link mappings and exit",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output (diagnostics section in RTM page)",
    )
    args = parser.parse_args()

    # Configure logging level based on --verbose
    setup_logging(verbose=args.verbose)
    logger.debug("Starting docs generation (verbose=%s)", args.verbose)

    if args.print_mappings:
        print_mappings()
        return

    clean_docs()

    # 1) Copy the repository tree (minus excluded/ignored) into docs/
    extra_excludes = load_docs_copy_excludes()
    if extra_excludes:
        logger.debug("Additional copy excludes from config: %s", extra_excludes)
    ignore_spec = load_gitignore_spec(extra_patterns=extra_excludes)
    copy_repo_tree_to_docs(ignore_spec)

    # 2) Overlay generated content (SRS, requirements, RTM, navigation)
    copy_srs()
    req_meta = copy_requirements()
    copy_rtm(verbose=args.verbose)
    top_level_pages(req_meta)
    logger.info("Docs tree generated.")


if __name__ == "__main__":
    main()
