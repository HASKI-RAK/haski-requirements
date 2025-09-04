#!/usr/bin/env python3
"""Generate MkDocs 'docs/' tree from single sources of truth.

Sources of truth:
- srs/SRS.md
- requirements/*.md (with YAML front matter)
- traceability/RTM.csv (generated separately)

Generated structure:
 docs/
   index.md
   srs/SRS.md
   requirements/ (copied & filtered)
     index.md (auto list)
   rtm/index.md
   rtm/RTM.csv (copied if exists else placeholder)
   .pages (top-level ordering) + section .pages files

This allows us to keep authoritative content outside docs/ and avoid drift.
"""
from __future__ import annotations
import os
import re
import shutil
from pathlib import Path
import yaml

BASE = Path(__file__).resolve().parent.parent
DOCS = BASE / "docs"
SRS_SRC = BASE / "srs" / "SRS.md"
REQS_SRC = BASE / "requirements"
RTM_SRC = BASE / "traceability" / "RTM.csv"

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


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
    write(dst_dir / ".pages", "title: Requirements\narrange: natural\n")
    return requirements_meta


def copy_rtm():
    rtm_dir = DOCS / "rtm"
    rtm_dir.mkdir(parents=True, exist_ok=True)
    if RTM_SRC.exists():
        shutil.copy2(RTM_SRC, rtm_dir / "RTM.csv")
    else:
        write(
            rtm_dir / "RTM.csv",
            "requirement_id,requirement_title,test_name,test_file,test_line,status\n",
        )
    write(
        rtm_dir / "index.md",
        "# Traceability\n\nAktuelle Traceability-Matrix als CSV Download.\n\n- [RTM.csv](RTM.csv)\n\n_Diese Seite wurde automatisch generiert._\n",
    )
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
