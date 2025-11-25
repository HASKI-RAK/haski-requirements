from __future__ import annotations

import csv
import logging
import re
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from .config import GITHUB_FILE_LINK_MAPPINGS, effective_ref
from .paths import DOCS, RTM_SRC, TRACEABILITY_CONFIG
from .copying import write
from .requirements import read_front_matter

logger = logging.getLogger(__name__)


def generate_traceability_matrix(verbose: bool = False):
    """Invoke the traceability builder to refresh ``RTM.csv`` before copying.

    This keeps docs generation self-contained: running ``scripts/generate_docs.py``
    will also regenerate the traceability matrix from the latest test reports.
    """

    if not TRACEABILITY_CONFIG.exists():
        logger.warning("Traceability config not found at %s; skipping matrix generation", TRACEABILITY_CONFIG)
        return

    try:
        from traceability.build import build_matrix
    except Exception as exc:  # noqa: BLE001 - surface any import/runtime issues
        logger.warning("Traceability module unavailable; RTM not updated (%s)", exc)
        return

    logger.info("Generate traceability matrix")
    build_matrix(str(TRACEABILITY_CONFIG), debug=verbose)

    if not RTM_SRC.exists():
        logger.warning("Traceability generation finished but RTM.csv missing at %s", RTM_SRC)


def build_github_file_link(
    local_path: str, line: Optional[str | int], unmatched: Optional[List[str]] = None
) -> Optional[str]:
    if not local_path:
        return None
    try:
        path_obj = Path(local_path).resolve()
    except OSError:
        path_obj = None

    for mapping in GITHUB_FILE_LINK_MAPPINGS:
        try:
            root = Path(mapping["local_root"]).resolve()
        except KeyError:
            continue
        repo = mapping.get("repo")
        if not repo:
            continue
        branch = effective_ref(mapping.get("branch", "main"))
        repo_root_subpath = mapping.get("repo_root_subpath", "").strip("/")

        # Primary match: on-disk paths inside local_root
        if path_obj and (root in path_obj.parents or path_obj == root):
            try:
                rel = path_obj.relative_to(root)
            except ValueError:
                rel = None
            if rel:
                repo_parts = []
                if repo_root_subpath:
                    repo_parts.append(repo_root_subpath)
                repo_parts.append(rel.as_posix())
                repo_path = "/".join(repo_parts)
                anchor = f"#L{line}" if line else ""
                url = f"https://github.com/{repo}/blob/{branch}/{repo_path}{anchor}"
                display = f"{repo_path}:{line}" if line else repo_path
                display = display.replace("<", "&lt;")
                return f"<a href='{url}' target='_blank' rel='noopener noreferrer'>{display}</a>"

        # Fallback: absolute paths that contain the repo name (e.g. /home/runner/work/HASKI-Frontend/HASKI-Frontend/src/...)
        repo_name = repo.split("/", 1)[1] if "/" in repo else repo
        marker = f"/{repo_name}/"
        if marker in str(local_path):
            after = str(local_path).split(marker, 1)[1]
            # Some CI paths embed the repo name twice; drop the second occurrence if present
            if after.startswith(f"{repo_name}/"):
                after = after[len(repo_name) + 1 :]
            after = after.lstrip("/")
            if repo_root_subpath and after.startswith(repo_root_subpath):
                repo_path = after
            else:
                repo_parts = [p for p in [repo_root_subpath, after] if p]
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
        return f"[{rid}](../srs/srs-requirements/{rid}/)"

    def html_escape(value: str) -> str:
        return (value or "").replace("<", "&lt;").replace(">", "&gt;")

    def collapse_list(summary_label: str, items: List[str]) -> str:
        if not items:
            return ""
        return (
            "<details class='rtm-collapse'>"
            "<summary>"
            + summary_label
            + "</summary><ul>"
            + "".join(f"<li>{item}</li>" for item in items)
            + "</ul></details>"
        )

    def build_excerpt(body: str) -> str:
        if not body:
            return ""
        lines = body.splitlines()
        body_lines: List[str] = []
        skip_heading = True
        for line in lines:
            stripped = line.strip()
            if skip_heading:
                if stripped.startswith("# "):
                    continue
                if stripped == "" or stripped.startswith("---"):
                    continue
                skip_heading = False
            if not skip_heading and stripped:
                body_lines.append(stripped)
                break
        excerpt = body_lines[0] if body_lines else ""
        if len(excerpt) > 180:
            excerpt = excerpt[:177] + "..."
        return excerpt.replace('"', "&quot;").replace("'", "&#39;")

    requirement_meta: Dict[str, Dict[str, str]] = {}
    excerpt_cache: Dict[str, str] = {}
    req_dir = DOCS / "srs" / "srs-requirements"
    for req_file in req_dir.glob("HASKI-REQ-*.md"):
        meta, body = read_front_matter(req_file)
        if not isinstance(meta, dict):
            meta = {}
        rid = str(meta.get("id") or req_file.stem).strip()
        if not rid:
            continue
        title = str(meta.get("title") or "").strip()
        excerpt = build_excerpt(body or "")
        requirement_meta[rid] = {"title": title}
        excerpt_cache[rid] = excerpt

    # Group tests per requirement so we render a single row per requirement.
    grouped: Dict[str, Dict[str, object]] = {}
    for row in rows:
        rid = row.get("requirement_id", "") or ""
        tests = grouped.setdefault(
            rid,
            {
                "requirement_id": rid,
                "requirement_title": row.get("requirement_title", ""),
                "tests": [],
            },
        )
        if not tests.get("requirement_title") and row.get("requirement_title"):
            tests["requirement_title"] = row.get("requirement_title", "")
        tests["tests"].append(
            {
                "name": row.get("test_name", ""),
                "file": row.get("test_file", ""),
                "line": row.get("test_line", ""),
                "status": row.get("status", ""),
            }
        )

    # Ensure every requirement file is represented, even without linked tests.
    for rid, meta in requirement_meta.items():
        group = grouped.setdefault(
            rid,
            {
                "requirement_id": rid,
                "requirement_title": meta.get("title", ""),
                "tests": [],
            },
        )
        if not group.get("requirement_title") and meta.get("title"):
            group["requirement_title"] = meta.get("title", "")

    # Derive aggregated status per requirement (single status if all same, otherwise "mixed").
    status_counter: Counter[str] = Counter()
    for _rid, group in grouped.items():
        tests = group.get("tests", []) or []
        statuses = {t.get("status", "") for t in tests if t.get("status")}
        if not tests:
            agg_status = "untested"
        elif not statuses:
            agg_status = "unknown"
        elif len(statuses) == 1:
            agg_status = statuses.pop()
        else:
            agg_status = "mixed"
        group["aggregate_status"] = agg_status
        if agg_status:
            status_counter[agg_status] += 1

    status_order = sorted(status_counter.keys())
    status_lines: List[str] = []
    total_requirements = len(grouped)

    def badge(status: str) -> str:
        if not status:
            return ""
        cls = status.lower().replace(" ", "-")
        return f"<span class='rtm-badge rtm-badge--{cls}'>{status}</span>"

    if total_requirements:
        status_lines.append("### Status Übersicht")
        status_lines.append("")
        items = []
        for status in status_order:
            count = status_counter[status]
            percentage = count / total_requirements if total_requirements else 0
            items.append(f"{badge(status)} {count} ({percentage:.0%})")
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

        for rid in sorted(grouped.keys() or [""]):
            group = grouped[rid]
            tests = group.get("tests", []) or []
            agg_status = group.get("aggregate_status", "")

            file_entries: List[str] = []
            for test in tests:
                raw_file = test.get("file", "") or ""
                raw_line = test.get("line", "") or ""
                sources = parse_test_sources(raw_file, raw_line)
                if sources:
                    for fpath, line in sources:
                        link = build_github_file_link(fpath, line or "", unmatched=unmatched_files)
                        if link:
                            file_entries.append(link)
                        else:
                            display = f"{fpath}:{line}" if (line and str(line).strip()) else f"{fpath}" if fpath else ""
                            file_entries.append(html_escape(display))
                else:
                    link = build_github_file_link(raw_file, raw_line, unmatched=unmatched_files)
                    if link:
                        file_entries.append(link)
                    else:
                        display = (
                            f"{raw_file}:{raw_line}"
                            if (raw_line and str(raw_line).strip())
                            else f"{raw_file}"
                            if raw_file
                            else ""
                        )
                        file_entries.append(html_escape(display))

            test_labels: List[str] = []
            for test in tests:
                label = html_escape(test.get("name", ""))
                t_status = test.get("status", "")
                if t_status and t_status != agg_status:
                    label += f" {badge(t_status)}"
                test_labels.append(label)

            if test_labels:
                test_cell = collapse_list(f"{len(test_labels)} Test(s)", test_labels)
            else:
                test_cell = "<em>Keine Tests verknüpft</em>"

            if file_entries:
                file_cell = collapse_list(f"{len(file_entries)} File/Line(s)", file_entries)
            else:
                file_cell = "<em>Keine Test-Dateien</em>"

            title_raw = group.get("requirement_title", "") or ""
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
                req_cell = f"<a href='../srs/srs-requirements/{rid}/'{tooltip_attr}>{combined_label}</a>"
            else:
                req_cell = title_display or ""

            table_lines.append(
                "<tr data-status='{}'>".format(agg_status)
                + f"<td>{req_cell}</td>"
                + f"<td>{test_cell}</td>"
                + f"<td>{file_cell}</td>"
                + f"<td>{badge(agg_status)}</td>"
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
    "generate_traceability_matrix",
    "build_github_file_link",
    "copy_rtm",
    "parse_test_sources",
]
