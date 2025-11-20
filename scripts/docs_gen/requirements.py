from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from .copying import write
from .paths import DOCS, REQS_SRC, ROOT

logger = logging.getLogger(__name__)

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def read_front_matter(path: Path):
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, ""
    match = FRONT_MATTER_RE.search(text)
    meta = {}
    body = text
    if match:
        try:
            meta = yaml.safe_load(match.group(1)) or {}
        except yaml.YAMLError:
            meta = {}
        body = text[match.end():]
    return meta, body


def build_syrs_index() -> Dict[str, str]:
    """Scan SyRS system-requirements for id -> relative path (from docs/ root)."""

    base = ROOT / "syrs" / "system-requirements"
    index: Dict[str, str] = {}
    if not base.exists():
        return index
    for md in base.rglob("SyRS-*.md"):
        meta, _ = read_front_matter(md)
        if not isinstance(meta, dict):
            continue
        rid = meta.get("id")
        if not isinstance(rid, str) or not rid.strip():
            continue
        rel_from_root = md.relative_to(ROOT).as_posix()
        index[rid.strip()] = rel_from_root
    return index


def _build_github_story_link(story: str) -> Optional[str]:
    if not isinstance(story, str):
        return None
    story = story.strip()
    if not story:
        return None
    if "#" not in story:
        return story
    repo, issue = story.split("#", 1)
    repo = repo.strip()
    issue = issue.strip().lstrip("#")
    if not repo or not issue.isdigit():
        return story
    url = f"https://github.com/{repo}/issues/{issue}"
    label = story.replace("<", "&lt;")
    return f"[{label}]({url})"


def build_requirement_links_section(meta: Dict, syrs_index: Dict[str, str]) -> str:
    links = meta.get("links") or {}
    if not isinstance(links, dict):
        links = {}

    parents = links.get("parents") or []
    if not isinstance(parents, list):
        parents = []
    stories = links.get("stories") or []
    if not isinstance(stories, list):
        stories = []

    lines: List[str] = []

    parent_links: List[str] = []
    for pid in parents:
        if not isinstance(pid, str):
            continue
        pid_clean = pid.strip()
        if not pid_clean:
            continue
        rel = syrs_index.get(pid_clean)
        if rel:
            parent_links.append(f"- [{pid_clean}](../../{rel})")
        else:
            parent_links.append(f"- {pid_clean}")

    story_links: List[str] = []
    for story in stories:
        link = _build_github_story_link(story)
        if link:
            story_links.append(f"- {link}")

    if parent_links or story_links:
        lines.append("## Links")
        lines.append("")
        if parent_links:
            lines.append("**SyRS-Parents**")
            lines.extend(parent_links)
            lines.append("")
        if story_links:
            lines.append("**GitHub-Stories**")
            lines.extend(story_links)
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def copy_requirements() -> list[dict]:
    logger.info("Process requirement files in docs/srs/srs-requirements/")
    requirements_meta = []
    dst_dir = DOCS / "srs" / "srs-requirements"
    dst_dir.mkdir(parents=True, exist_ok=True)
    syrs_index = build_syrs_index()

    for src in REQS_SRC.glob("HASKI-REQ-*.md"):
        meta, body = read_front_matter(src)
        if meta is None:
            meta = {}
        rid = meta.get("id") or src.stem
        meta["id"] = rid
        requirements_meta.append(meta)
        fm = yaml.safe_dump(meta, sort_keys=False).strip()
        links_block = build_requirement_links_section(meta, syrs_index)
        content = f"---\n{fm}\n---\n\n# {rid}\n\n" + links_block + body.lstrip()
        write(dst_dir / f"{rid}.md", content)

    index_lines = ["# Requirements Übersicht", "", "Liste der Anforderungen:", ""]
    for meta in sorted(requirements_meta, key=lambda m: m.get("id", "")):
        rid = meta["id"]
        title = meta.get("title", "")
        index_lines.append(f"- [{rid}]({rid}.md) – {title}")
    index_lines.append("\n_Hinweis: Diese Seite wird automatisch generiert._\n")
    write(dst_dir / "index.md", "\n".join(index_lines))
    write(dst_dir / ".pages", "title: Requirements\n")
    return requirements_meta


__all__ = [
    "FRONT_MATTER_RE",
    "build_requirement_links_section",
    "build_syrs_index",
    "copy_requirements",
    "read_front_matter",
]
