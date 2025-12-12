"""Parse TypeScript sources and treat requirement tags as passing tests.

The adapter walks a directory (or single file) and looks for occurrences of
``HASKI-REQ-XXXX`` (or ``HASKI_REQ_XXXX``) inside ``.ts`` files. Each located
tag is reported as a passing "test" so the traceability matrix can link
requirements to annotated source files even without executing a test suite.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass
from typing import List, Optional, Set, Tuple

REQ_PATTERN = re.compile(r"HASKI[_-]REQ[_-]\d+")


@dataclass
class TestResult:
    """Represents a requirement tag found in source code."""

    name: str
    file: str
    line: Optional[int]
    status: str
    requirements: List[str]


TS_EXTENSIONS = (".ts", ".tsx", ".mts", ".cts")


def _iter_ts_files(path: str):
    """Yield TypeScript-family files under ``path`` (skips heavy vendor dirs)."""

    if os.path.isfile(path):
        if path.endswith(TS_EXTENSIONS):
            yield path
        return

    skip_dirs = {"node_modules", ".git", "dist", "build", "out", "coverage"}
    for dirpath, dirnames, filenames in os.walk(path):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fname in filenames:
            if fname.endswith(TS_EXTENSIONS):
                yield os.path.join(dirpath, fname)


def _line_for_offset(text: str, offset: int) -> int:
    """Convert character offset into 1-based line number."""

    return text.count("\n", 0, offset) + 1


def parse(path: str) -> List[TestResult]:
    """Scan TypeScript sources for requirement tags.

    Parameters
    ----------
    path: str
        Directory (preferred) or single file to scan. Non-existent paths
        yield an empty list.
    """

    if not os.path.exists(path):
        return []

    root_dir = path if os.path.isdir(path) else os.path.dirname(path)
    results: List[TestResult] = []
    seen: Set[Tuple[str, str]] = set()  # (rel_path, req_id)

    for file_path in _iter_ts_files(path):
        try:
            with open(file_path, "r", encoding="utf-8") as handle:
                content = handle.read()
        except (OSError, UnicodeDecodeError):
            continue

        rel_path = os.path.relpath(file_path, root_dir) if root_dir else file_path

        for match in REQ_PATTERN.finditer(content):
            req_id = match.group(0).replace("_", "-")
            key = (rel_path, req_id)
            if key in seen:
                continue  # avoid duplicate rows for repeated tags in same file
            seen.add(key)

            line_no = _line_for_offset(content, match.start())
            name = f"{rel_path} – tag {req_id}"

            results.append(
                TestResult(
                    name=name,
                    file=rel_path,
                    line=line_no,
                    status="passed",  # presence of tag is sufficient
                    requirements=[req_id],
                )
            )

    return results
