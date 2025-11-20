from __future__ import annotations

import csv
import logging
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from .config import GITHUB_FILE_LINK_MAPPINGS, effective_ref
from .copying import write
from .paths import DOCS, RTM_SRC
from .requirements import read_front_matter

logger = logging.getLogger(__name__)


def build_github_file_link(
    local_path: str, line: Optional[str | int], unmatched: Optional[List[str]] = None
) -> Optional[str]:
    if not local_path:
        return None
    try:
        path_obj = Path(local_path).resolve()
    except OSError:
        return None

    for mapping in GITHUB_FILE_LINK_MAPPINGS:
        try:
            root = Path(mapping["local_root"]).resolve()
        except KeyError:
            continue
        if root in path_obj.parents or path_obj == root:
            try:
                rel = path_obj.relative_to(root)
            except ValueError:
                continue
            repo = mapping.get("repo")
            if not repo:
                continue
            branch = effective_ref(mapping.get("branch", "main"))
            sub = mapping.get("repo_root_subpath", "")
            repo_parts = []
            if sub:
                repo_parts.append(sub.strip("/"))
            repo_parts.append(rel.as_posix())
            repo_path = "/".join(repo_parts)
            anchor = f"#L{line}" if line else ""
            url = f"https://github.com/{repo}/blob/{branch}/{repo_path}{anchor}"
            display = f"{repo_path}:{line}" if line else repo_path
            display = display.replace("<", "&lt;")
            return f"<a href='{url}' target='_blank' rel='noopener noreferrer'>{display}</a>"

    if unmatched is not None:
        unmatched.append(local_path)
    return None


def _try_parse_yaml_or_json_list(value: str):
    if not value:
        return None
    stripped = value.strip()
    if not (stripped.startswith("[") or stripped.startswith("- ") or stripped.startswith("{")):
        return None
    try:
        parsed = yaml.safe_load(stripped)
    except Exception:
        return None
    if isinstance(parsed, list):
        return parsed
    if isinstance(parsed, dict):
        return [parsed]
    return None


def parse_test_sources(test_file_field: str, test_line_field: str) -> List[Tuple[str, Optional[str]]]:
    def normalise_line(value) -> Optional[str]:
        if value is None:
            return None
        s = str(value).strip()
        return s or None

    def from_token(token: str) -> Tuple[str, Optional[str]]:
        token = token.strip()
        match = re.match(r"^(.*?):(\d+)$", token)
        if match:
            return match.group(1), match.group(2)
        return token, None

    files_raw = (test_file_field or "").strip()
    lines_raw = (test_line_field or "").strip()

    parsed_files = _try_parse_yaml_or_json_list(files_raw)
    parsed_lines = _try_parse_yaml_or_json_list(lines_raw)

    sources: List[Tuple[str, Optional[str]]] = []

    if isinstance(parsed_files, list):
        for item in parsed_files:
            if isinstance(item, str):
                fpath, ln = from_token(item)
                sources.append((fpath, ln))
            elif isinstance(item, dict):
                fpath = item.get("file") or item.get("path") or item.get("test_file") or ""
                ln = item.get("line") or item.get("ln") or item.get("test_line")
                fpath = (fpath or "").strip()
                if fpath:
                    sources.append((fpath, normalise_line(ln)))
        if all(line is None for _, line in sources) and isinstance(parsed_lines, list):
            zipped: List[Tuple[str, Optional[str]]] = []
            for idx, (fpath, _ln) in enumerate(sources):
                ln = parsed_lines[idx] if idx < len(parsed_lines) else None
                zipped.append((fpath, normalise_line(ln)))
            sources = zipped
        return [(fpath, ln) for fpath, ln in sources if fpath]

    def split_tokens(val: str) -> List[str]:
        if not val:
            return []
        if ";" in val:
            return [token for token in (v.strip() for v in val.split(";")) if token]
        if "|" in val:
            return [token for token in (v.strip() for v in val.split("|")) if token]
        return [val.strip()] if val.strip() else []

    file_tokens = split_tokens(files_raw)
    inline_pairs: List[Tuple[str, Optional[str]]] = [from_token(tok) for tok in file_tokens]
    if any(ln is not None for _, ln in inline_pairs):
        return [(fpath, ln) for fpath, ln in inline_pairs if fpath]

    line_tokens = split_tokens(lines_raw)
    if not file_tokens:
        return []
    max_len = max(len(file_tokens), len(line_tokens))
    result: List[Tuple[str, Optional[str]]] = []
    for idx in range(max_len):
        fpath = file_tokens[idx] if idx < len(file_tokens) else None
        ln = line_tokens[idx] if idx < len(line_tokens) else None
        if fpath:
            result.append((fpath, normalise_line(ln)))
    return result


def copy_rtm(verbose: bool = False):
    logger.info("Generate Traceability Matrix page")
    rtm_dir = DOCS / "rtm"
    rtm_dir.mkdir(parents=True, exist_ok=True)
    csv_path = rtm_dir / "RTM.csv"
    if RTM_SRC.exists():
        csv_path.write_bytes(RTM_SRC.read_bytes())
    else:
        logger.warning("RTM source not found at %s; writing empty template", RTM_SRC)
        write(
            csv_path,
            "requirement_id,requirement_title,test_name,test_file,test_line,status\n",
        )

    rows = []
    with csv_path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(row)
    logger.debug("Loaded %d RTM row(s)", len(rows))

    def link_req(rid: str) -> str:
        if not rid:
            return ""
        return f"[{rid}](../srs/srs-requirements/{rid}.md)"

    excerpt_cache: Dict[str, str] = {}
    for req_file in (DOCS / "srs" / "srs-requirements").glob("HASKI-REQ-*.md"):
        rid = req_file.stem
        try:
            lines = req_file.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        body_lines = []
        skip_heading = True
        for line in lines:
            if skip_heading:
                if line.strip().startswith("# "):
                    continue
                if line.strip() == "" or line.strip().startswith("---"):
                    continue
                skip_heading = False
            if not skip_heading:
                if line.strip():
                    body_lines.append(line.strip())
                if len(body_lines) >= 1:
                    break
        excerpt = body_lines[0] if body_lines else ""
        if len(excerpt) > 180:
            excerpt = excerpt[:177] + "..."
        excerpt_cache[rid] = excerpt.replace('"', "&quot;").replace("'", "&#39;")

    status_counter = Counter(row.get("status", "") for row in rows if row.get("status"))
    status_order = sorted(status_counter.keys())
    status_lines: List[str] = []
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
        for status in status_order:
            count = status_counter[status]
            items.append(f"{badge(status)} {count} ({count/total:.0%})")
        status_lines.append("<div class='rtm-status-summary'>" + " | ".join(items) + "</div>")
        status_lines.append("")

    table_lines: List[str] = []
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
            "<thead><tr><th>Requirement</th><th>Test Name" "</th><th>File:Line</th><th>Status</th></tr></thead>"
        )
        table_lines.append("<tbody>")
        unmatched_files: List[str] = []
        for row in rows:
            raw_file = row.get("test_file", "") or ""
            raw_line = row.get("test_line", "") or ""
            sources = parse_test_sources(raw_file, raw_line)
            link_pieces: List[str] = []
            if sources:
                for fpath, line in sources:
                    link = build_github_file_link(fpath, line or "", unmatched=unmatched_files)
                    if link:
                        link_pieces.append(link)
                    else:
                        display = f"{fpath}:{line}" if (line and str(line).strip()) else f"{fpath}" if fpath else ""
                        display = display.replace("<", "&lt;")
                        link_pieces.append(display)
                file_line = "<br>".join(link_pieces)
            else:
                link = build_github_file_link(raw_file, raw_line, unmatched=unmatched_files)
                if link:
                    file_line = link
                else:
                    display = (
                        f"{raw_file}:{raw_line}" if (raw_line and str(raw_line).strip()) else f"{raw_file}" if raw_file else ""
                    )
                    file_line = display.replace("<", "&lt;")

            status_value = row.get("status", "")
            rid = row.get("requirement_id", "")
            title_raw = row.get("requirement_title") or ""
            title_display = title_raw.strip() or "(kein Titel)"
            title_display = title_display.replace("<", "&lt;")

            if rid:
                excerpt = excerpt_cache.get(rid, "")
                tooltip_attr = f" title='{excerpt}'" if excerpt else ""
                if title_raw.strip():
                    combined_label = (
                        f"<strong>{rid}</strong><br><span class='rtm-req-title'>{title_display}</span>"
                    )
                else:
                    combined_label = f"<strong>{rid}</strong>"
                req_cell = f"<a href='../srs/srs-requirements/{rid}.md'{tooltip_attr}>{combined_label}</a>"
            else:
                req_cell = title_display or ""

            table_lines.append(
                "<tr data-status='{}'>".format(status_value)
                + f"<td>{req_cell}</td>"
                + f"<td>{(row.get('test_name') or '').replace('<', '&lt;')}</td>"
                + f"<td>{file_line}</td>"
                + f"<td>{badge(status_value)}</td>"
                + "</tr>"
            )
        table_lines.append("</tbody></table>")
        if verbose and unmatched_files:
            uniq = sorted(set(unmatched_files))
            table_lines.append(
                "<details><summary>Nicht verlinkbare Test-Dateien ({}):</summary><pre>".format(len(uniq))
            )
            for file_path in uniq:
                table_lines.append(file_path)
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


__all__ = [
    "build_github_file_link",
    "copy_rtm",
    "parse_test_sources",
]
