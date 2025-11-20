import json
import os
import re
from dataclasses import dataclass
from typing import List, Optional, Union

REQ_PATTERN = re.compile(r"HASKI[_-]REQ[_-]\d+")


@dataclass
class TestResult:
    """Represents a single test case parsed from a report."""

    name: str
    file: str
    line: Optional[int]
    status: str
    requirements: List[str]


def _extract_file_and_line(
    nodeid: str, location: Optional[Union[list, dict]], lineno: Optional[int] = None
) -> tuple[str, Optional[int]]:
    """
    Extract file path and line number from pytest JSON fields.

    Priority:
    1) lineno field (from pytest-json-report)
    2) location (if provided by pytest-json-report): ["path", lineno, domain] or {"lineno": int, "path": str}
    3) nodeid split: "path::node::subnode" -> take first segment as file path, no line info
    """
    file_name = ""
    line = lineno  # Use direct lineno field first

    if isinstance(location, list) and len(location) >= 2:
        file_name = str(location[0] or "")
        if line is None:  # Only use location line if lineno wasn't provided
            try:
                line = int(location[1]) if location[1] is not None else None
            except (TypeError, ValueError):
                line = None
    elif isinstance(location, dict):
        file_name = str(location.get("path", "") or "")
        if line is None:  # Only use location line if lineno wasn't provided
            loc_line = location.get("lineno")
            try:
                line = int(loc_line) if loc_line is not None else None
            except (TypeError, ValueError):
                line = None

    if not file_name:
        # Fall back to nodeid "tests/test_api.py::TestClass::test_foo"
        file_name = nodeid.split("::", 1)[0] if nodeid else ""

    return file_name, line


def parse(report_path: str) -> List[TestResult]:
    """
    Parse a pytest JSON report (from pytest-json-report plugin) and return extracted test cases.

    Expected generation command (in backend repo):
        pytest --json-report --json-report-file=reports/pytest-report.json

    The adapter extracts:
    - name: the test nodeid (e.g., tests/test_api.py::TestClass::test_foo[param])
    - file: source file for the test
    - line: line number (if available from 'location')
    - status: 'passed' | 'failed' | 'skipped' | ...
    - requirements: all HASKI-REQ-#### IDs found in the name
    """
    if not os.path.exists(report_path):
        return []
    try:
        with open(report_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return []

    results: List[TestResult] = []
    for test in data.get("tests", []):
        nodeid = test.get(
            "nodeid", ""
        )  # e.g. "tests/test_api.py::test_store_config[case1]"
        outcome = test.get("outcome", "unknown")
        location = test.get(
            "location"
        )  # often ["path", lineno, "domain"] with pytest-json-report
        lineno = test.get("lineno")  # Direct line number field from pytest-json-report

        file_name, line = _extract_file_and_line(nodeid, location, lineno)
        req_ids = REQ_PATTERN.findall(nodeid) if nodeid else []

        # Normalize requirement IDs to standard format (replace underscores with hyphens)
        req_ids = [req_id.replace("_", "-") for req_id in req_ids]

        # Fallback: also look in file name (if teams encode ID there)
        if not req_ids and file_name:
            file_req_ids = REQ_PATTERN.findall(file_name)
            req_ids = [req_id.replace("_", "-") for req_id in file_req_ids]

        results.append(
            TestResult(
                name=nodeid or "",
                file=file_name,
                line=line,
                status=outcome,
                requirements=req_ids,
            )
        )

    return results
