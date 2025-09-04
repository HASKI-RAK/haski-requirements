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
"""

from __future__ import annotations

import csv
import re
import shutil
from collections import Counter
from pathlib import Path
from typing import Tuple

import yaml

# ---------------------------------------------------------------------------
# Paths & constants
# ---------------------------------------------------------------------------
ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs"
SRS_SRC = ROOT / "srs" / "SRS.md"
REQS_SRC = ROOT / "requirements"
RTM_SRC = ROOT / "traceability" / "RTM.csv"

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


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
        for item in DOCS.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
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
            lines.append(f"- [{rid}](requirements/{rid}.md) – {title}")
    lines.append("\n---\n_Automatisch generiert._")
    return "\n".join(lines) + "\n"


def copy_srs():
    if SRS_SRC.exists():
        dst = DOCS / "srs" / "SRS.md"
        content = SRS_SRC.read_text(encoding="utf-8")
        banner = "# Software Requirements Specification (SRS)\n\n<!-- Generated copy from srs/SRS.md -->\n\n"
        if not content.lstrip().startswith("#"):
            # keep original if proper heading missing
            banner = ""
        write(dst, banner + content)


def copy_requirements():
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
        index_lines.append(f"- [{rid}]({rid}.md) – {title}")
    index_lines.append("\n_Hinweis: Diese Seite wird automatisch generiert._\n")
    write(dst_dir / "index.md", "\n".join(index_lines))
    # .pages config
    # awesome-pages: remove invalid scalar arrange; natural order is default
    write(dst_dir / ".pages", "title: Requirements\n")
    return requirements_meta


def copy_rtm():
    rtm_dir = DOCS / "rtm"
    rtm_dir.mkdir(parents=True, exist_ok=True)
    csv_path = rtm_dir / "RTM.csv"
    if RTM_SRC.exists():
        shutil.copy2(RTM_SRC, csv_path)
    else:
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

    def link_req(rid: str) -> str:
        if not rid:
            return ""
        return f"[{rid}](../requirements/{rid}.md)"

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
            "<thead><tr><th>Requirement</th><th>Title</th><th>Test Name"
            "</th><th>File:Line</th><th>Status</th></tr></thead>"
        )
        table_lines.append("<tbody>")
        for r in rows:
            file_line = (
                f"{r.get('test_file','')}:{r.get('test_line','')}"
                if r.get("test_file")
                else ""
            )
            st = r.get("status", "")
            table_lines.append(
                "<tr data-status='{}'>".format(st)
                + f"<td>{link_req(r.get('requirement_id',''))}</td>"
                + f"<td>{(r.get('requirement_title') or '').replace('<','&lt;')}</td>"
                + f"<td>{(r.get('test_name') or '').replace('<','&lt;')}</td>"
                + f"<td>{file_line}</td>"
                + f"<td>{badge(st)}</td>"
                + "</tr>"
            )
        table_lines.append("</tbody></table>")
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


def main():
    clean_docs()
    copy_srs()
    req_meta = copy_requirements()
    copy_rtm()
    top_level_pages(req_meta)
    print("Docs tree generated.")


if __name__ == "__main__":
    main()
