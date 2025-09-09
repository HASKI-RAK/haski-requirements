"""Generate a traceability matrix from requirements and test reports."""

import argparse
import csv
import os
from typing import List

import yaml

from adapters import jest
from requirements_loader import load as load_requirements


def gather_tests(test_reports: List[dict], debug: bool = False):
    tests = []
    for report in test_reports:
        rtype = report.get("type")
        path = report.get("path") or ""
        if not path:
            if debug:
                print(f"[traceability][WARN] Empty report path for type={rtype}")
            continue
        if rtype == "jest":
            parsed = jest.parse(path)
            if debug:
                if not os.path.exists(path):
                    print(f"[traceability][WARN] Jest report not found: {path}")
                else:
                    print(
                        f"[traceability] Parsed {len(parsed)} jest test(s) from {path}"
                    )
            tests.extend(parsed)
        else:
            if debug:
                print(f"[traceability][WARN] Unsupported report type: {rtype} ({path})")
    return tests


def build_matrix(config_path: str, debug: bool = False):
    with open(config_path, "r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle)

    base_dir = os.path.dirname(os.path.abspath(config_path))

    req_dir = os.path.join(base_dir, config["requirements_dir"])
    test_reports = []
    for report in config.get("test_reports", []):
        r = dict(report)
        r["path"] = os.path.join(base_dir, report.get("path", ""))
        test_reports.append(r)

    reqs = load_requirements(req_dir)
    if debug:
        print(f"[traceability] Loaded {len(reqs)} requirement(s) from {req_dir}")
    tests = gather_tests(test_reports, debug=debug)
    if debug:
        print(f"[traceability] Total test cases parsed: {len(tests)}")

    rows = []
    matched_tests = 0
    for test in tests:
        if not test.requirements:
            continue
        matched_tests += 1
        for req_id in test.requirements:
            req = reqs.get(req_id)
            rows.append(
                {
                    "requirement_id": req_id,
                    "requirement_title": req.title if req else "",
                    "test_name": test.name,
                    "test_file": test.file,
                    "test_line": test.line,
                    "status": test.status,
                }
            )
    if debug:
        print(f"[traceability] Tests referencing requirements: {matched_tests}")
        print(f"[traceability] Matrix rows to write: {len(rows)}")

    output = os.path.join(base_dir, config.get("output", "RTM.csv"))
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "requirement_id",
                "requirement_title",
                "test_name",
                "test_file",
                "test_line",
                "status",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build traceability matrix")
    parser.add_argument(
        "--config",
        default=os.path.join(os.path.dirname(__file__), "config.yaml"),
        help="Path to configuration YAML",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable verbose diagnostic output",
    )
    args = parser.parse_args()
    build_matrix(args.config, debug=args.debug)
