from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Dict, List, Tuple

import yaml

from .copying import write
from .paths import DOCS, ROOT
from .requirements import read_front_matter

logger = logging.getLogger(__name__)


def _rel_link(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, from_path.parent).replace(os.sep, "/")


def _build_stakeholder_index() -> Dict[str, Path]:
    base = ROOT / "strs" / "stakeholder-requirements"
    index: Dict[str, Path] = {}
    if not base.exists():
        return index
    for md in base.glob("StRS-*.md"):
        index[md.stem] = DOCS / "strs" / "stakeholder-requirements" / md.name
    return index


def _build_software_index(requirements_meta: List[dict]) -> Dict[str, Path]:
    index: Dict[str, Path] = {}
    for meta in requirements_meta:
        rid = meta.get("id")
        if isinstance(rid, str) and rid.strip():
            index[rid.strip()] = DOCS / "srs" / "srs-requirements" / f"{rid.strip()}.md"
    return index


def _normalise_links(raw_links) -> Dict[str, List[str]]:
    if not isinstance(raw_links, dict):
        return {"parents": [], "children": []}
    parents = raw_links.get("parents") or []
    children = raw_links.get("children") or []
    if not isinstance(parents, list):
        parents = []
    if not isinstance(children, list):
        children = []
    return {
        "parents": [str(p).strip() for p in parents if str(p).strip()],
        "children": [str(c).strip() for c in children if str(c).strip()],
    }


def copy_system_requirements(requirements_meta: List[dict]) -> Tuple[Dict[str, Path], Dict[str, List[str]]]:
    """Rewrite SyRS files into docs/ with generated traceability links.

    Returns:
        system_index: map SyRS id -> docs path
        stakeholder_children: map StRS id -> list of SyRS ids referencing it
    """

    logger.info("Enhance SyRS files with traceability links")
    stakeholder_index = _build_stakeholder_index()
    software_index = _build_software_index(requirements_meta)

    base = ROOT / "syrs" / "system-requirements"
    system_index: Dict[str, Path] = {}
    stakeholder_children: Dict[str, List[str]] = {}

    if not base.exists():
        logger.warning("System requirements directory missing at %s", base)
        return system_index, stakeholder_children

    for src in base.rglob("SyRS-*.md"):
        meta, body = read_front_matter(src)
        if not isinstance(meta, dict):
            meta = {}
        rid = str(meta.get("id") or src.stem).strip()
        system_index[rid] = DOCS / src.relative_to(ROOT)

        links = _normalise_links(meta.get("links"))
        parents = links["parents"]
        children = links["children"]

        for parent_id in parents:
            stakeholder_children.setdefault(parent_id, []).append(rid)

        trace_lines: List[str] = ["## Traceability", ""]

        if parents:
            trace_lines.append("**Stakeholder-Parents**")
            for pid in parents:
                target = stakeholder_index.get(pid)
                if target:
                    rel = _rel_link(system_index[rid], target)
                    trace_lines.append(f"- [{pid}]({rel})")
                else:
                    trace_lines.append(f"- {pid}")
            trace_lines.append("")

        if children:
            trace_lines.append("**Software-Children**")
            for cid in children:
                target = software_index.get(cid)
                if target:
                    rel = _rel_link(system_index[rid], target)
                    trace_lines.append(f"- [{cid}]({rel})")
                else:
                    trace_lines.append(f"- {cid}")
            trace_lines.append("")

        rel_rtm = _rel_link(system_index[rid], DOCS / "rtm" / "index.md")
        trace_lines.append(f"**RTM**: [Traceability Matrix]({rel_rtm})")
        trace_block = "\n".join(trace_lines).strip() + "\n"

        fm = yaml.safe_dump(meta, sort_keys=False).strip()
        output_parts = []
        if fm:
            output_parts.append(f"---\n{fm}\n---\n\n")
        output_parts.append(body.lstrip())
        if not body.endswith("\n"):
            output_parts.append("\n")
        output_parts.append("\n")
        output_parts.append(trace_block)

        dst = system_index[rid]
        write(dst, "".join(output_parts).rstrip() + "\n")

    return system_index, stakeholder_children


__all__ = ["copy_system_requirements"]
