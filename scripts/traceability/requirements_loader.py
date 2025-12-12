import os
import re
from dataclasses import dataclass
from typing import Dict

import yaml


FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
SKIP_MARKERS = {"skip", "skipped", "ignore", "ignored", "n/a", "na", "not-testable", "non-testable"}


@dataclass
class Requirement:
    id: str
    title: str
    path: str
    skip_traceability: bool = False


def _is_traceability_skipped(meta: Dict) -> bool:
    """Return True when a requirement explicitly opts out of RTM status scoring.

    Supported frontmatter keys:
      - traceability: skip
      - traceability_skip: true
      - rtm_skip: true
    """

    if not isinstance(meta, dict):
        return False

    raw = meta.get("traceability")
    if isinstance(raw, dict):
        raw = raw.get("status") or raw.get("action") or raw.get("value")
    if isinstance(raw, str) and raw.strip().lower() in SKIP_MARKERS:
        return True

    for key in ("traceability_skip", "rtm_skip"):
        value = meta.get(key)
        if isinstance(value, bool) and value:
            return True
        if isinstance(value, str) and value.strip().lower() in SKIP_MARKERS:
            return True

    return False


def load(directory: str) -> Dict[str, Requirement]:
    """Load requirements with YAML front matter from a directory."""
    requirements: Dict[str, Requirement] = {}
    for root, _dirs, files in os.walk(directory):
        for fname in files:
            if not fname.endswith('.md'):
                continue
            path = os.path.join(root, fname)
            with open(path, 'r', encoding='utf-8') as handle:
                text = handle.read()
            match = FRONT_MATTER_RE.search(text)
            if not match:
                continue
            try:
                metadata = yaml.safe_load(match.group(1)) or {}
            except yaml.YAMLError:
                continue
            req_id = metadata.get('id')
            title = metadata.get('title', '')
            skip_traceability = _is_traceability_skipped(metadata)
            if req_id:
                requirements[req_id] = Requirement(
                    id=req_id,
                    title=title,
                    path=path,
                    skip_traceability=skip_traceability,
                )
    return requirements
