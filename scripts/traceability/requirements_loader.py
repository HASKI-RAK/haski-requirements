import os
import re
from dataclasses import dataclass
from typing import Dict

import yaml


FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)


@dataclass
class Requirement:
    id: str
    title: str
    path: str


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
            if req_id:
                requirements[req_id] = Requirement(id=req_id, title=title, path=path)
    return requirements
