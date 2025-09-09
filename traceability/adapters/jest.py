import json
import os
import re
from dataclasses import dataclass
from typing import List, Optional


REQ_PATTERN = re.compile(r"HASKI-REQ-\d+")


@dataclass
class TestResult:
    """Represents a single test case parsed from a report."""

    name: str
    file: str
    line: Optional[int]
    status: str
    requirements: List[str]


def parse(report_path: str) -> List[TestResult]:
    """Parse a Jest JSON report and return extracted test cases.

    Parameters
    ----------
    report_path: str
        Path to the Jest JSON report generated with ``--json`` and
        ``--testLocationInResults``.
    """
    if not os.path.exists(report_path):
        return []
    try:
        with open(report_path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return []

    results: List[TestResult] = []
    for suite in data.get("testResults", []):
        file_name = suite.get("name", "")
        for assertion in suite.get("assertionResults", []):
            full_name = " ".join(assertion.get("ancestorTitles", []) + [assertion.get("title", "")])
            status = assertion.get("status", "unknown")
            location = assertion.get("location") or {}
            line = location.get("line") if isinstance(location, dict) else None
            req_ids = REQ_PATTERN.findall(full_name)
            # Fallback: also look in file name (some teams encode ID there)
            if not req_ids:
                req_ids = REQ_PATTERN.findall(file_name)
            results.append(
                TestResult(
                    name=full_name,
                    file=file_name,
                    line=line,
                    status=status,
                    requirements=req_ids,
                )
            )
    return results
