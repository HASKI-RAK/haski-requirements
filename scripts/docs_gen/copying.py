from __future__ import annotations

import logging
import os
import shutil
from pathlib import Path

from pathspec import PathSpec

from .paths import DOCS, ROOT

logger = logging.getLogger(__name__)


def copy_repo_tree_to_docs(spec: PathSpec):
    """Copy all directories/files from repo into docs/, honoring ignore spec."""

    logger.info("Copying repository content into docs/ (applying ignore rules)")
    for dirpath, dirnames, filenames in os.walk(ROOT, topdown=True):
        dpath = Path(dirpath)
        rel_dir = dpath.relative_to(ROOT)

        if rel_dir == Path("."):
            pruned = []
            for dn in list(dirnames):
                rel = (rel_dir / dn).as_posix()
                if spec.match_file(rel) or spec.match_file(rel + "/"):
                    pruned.append(dn)
            for dn in pruned:
                dirnames.remove(dn)
            if DOCS.name in dirnames:
                dirnames.remove(DOCS.name)
            continue

        rel_dir_posix = rel_dir.as_posix()
        if spec.match_file(rel_dir_posix) or spec.match_file(rel_dir_posix + "/"):
            dirnames[:] = []
            continue

        for dn in list(dirnames):
            child_rel = (rel_dir / dn).as_posix()
            if spec.match_file(child_rel) or spec.match_file(child_rel + "/"):
                dirnames.remove(dn)

        for fn in filenames:
            rel_file = (rel_dir / fn).as_posix()
            if spec.match_file(rel_file):
                continue
            src = dpath / fn
            dst = DOCS / rel_dir / fn
            dst.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(src, dst)
            except OSError as exc:
                logger.debug("Skip unreadable file %s: %s", src, exc)
                continue


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


__all__ = ["clean_docs", "copy_repo_tree_to_docs", "write"]
