from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Dict, List

from .copying import write
from .paths import DOCS, ROOT

logger = logging.getLogger(__name__)


def _rel_link(from_path: Path, to_path: Path) -> str:
    return os.path.relpath(to_path, from_path.parent).replace(os.sep, "/")


def copy_stakeholder_requirements(system_index: Dict[str, Path], stakeholder_children: Dict[str, List[str]]):
    """Rewrite StRS files into docs/ with generated traceability links."""

    base = ROOT / "strs" / "stakeholder-requirements"
    if not base.exists():
        logger.warning("Stakeholder requirements directory missing at %s", base)
        return

    logger.info("Enhance StRS files with traceability links")

    for src in base.glob("StRS-*.md"):
        content = src.read_text(encoding="utf-8")
        # Fix legacy RTM links when copying
        content = content.replace("../../rtm/RTM.md", "../../rtm/")

        rid = src.stem
        dst = DOCS / src.relative_to(ROOT)
        dst.parent.mkdir(parents=True, exist_ok=True)

        children = sorted(set(stakeholder_children.get(rid, [])))

        trace_lines: List[str] = ["## Traceability", ""]
        if children:
            trace_lines.append("**System Requirements**")
            for cid in children:
                target = system_index.get(cid)
                if target:
                    rel = _rel_link(dst, target)
                    trace_lines.append(f"- [{cid}]({rel})")
                else:
                    trace_lines.append(f"- {cid}")
            trace_lines.append("")
        else:
            trace_lines.append("_Keine System Requirements verknüpft._")
            trace_lines.append("")

        rel_rtm = _rel_link(dst, DOCS / "rtm" / "index.md")
        trace_lines.append(f"**RTM**: [Traceability Matrix]({rel_rtm})")

        output = "\n".join([content.rstrip(), "", *trace_lines]).rstrip() + "\n"
        write(dst, output)


__all__ = ["copy_stakeholder_requirements"]
