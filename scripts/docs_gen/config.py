from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Dict, List, Optional

import yaml
from pathspec import PathSpec
from pathspec.patterns.gitwildmatch import GitWildMatchPattern

from .paths import ROOT, TRACEABILITY_CONFIG

logger = logging.getLogger(__name__)


def _read_yaml_cfg() -> dict:
    """Load ``traceability/config.yaml`` safely and return a dict."""

    if not TRACEABILITY_CONFIG.exists():
        return {}
    try:
        with TRACEABILITY_CONFIG.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle) or {}
    except yaml.YAMLError:
        logger.warning("Failed parsing traceability/config.yaml; using empty config")
        return {}


def load_github_mappings() -> List[Dict[str, str]]:
    """Load ``github_file_link_mappings`` from ``traceability/config.yaml``.

    Returns an empty list if the file is missing or invalid. Normalises
    ``local_root`` to absolute resolved paths.
    """

    if not TRACEABILITY_CONFIG.exists():
        logger.debug("traceability/config.yaml not found; no GitHub mappings loaded")
        return []

    try:
        with TRACEABILITY_CONFIG.open("r", encoding="utf-8") as handle:
            cfg = yaml.safe_load(handle) or {}
    except yaml.YAMLError:
        logger.warning(
            "Failed parsing traceability/config.yaml; ignoring github mappings"
        )
        return []

    mappings = []
    for mapping in cfg.get("github_file_link_mappings", []) or []:
        if not isinstance(mapping, dict):
            continue
        local_root = mapping.get("local_root")
        repo = mapping.get("repo")
        if not local_root or not repo:
            continue
        branch = mapping.get("branch", "main")
        repo_root_subpath = mapping.get("repo_root_subpath", "")
        abs_root = (TRACEABILITY_CONFIG.parent / local_root).resolve()
        mappings.append(
            {
                "local_root": str(abs_root),
                "repo": repo,
                "branch": branch,
                "repo_root_subpath": repo_root_subpath,
            }
        )
    logger.debug("Loaded %d GitHub mapping(s)", len(mappings))
    return mappings


def load_docs_copy_excludes() -> List[str]:
    """Read optional extra excludes for copying into docs from config.yaml."""

    cfg = _read_yaml_cfg()
    excludes = cfg.get("docs_copy_exclude") or cfg.get("docs_exclude") or []
    output: List[str] = []
    if not isinstance(excludes, list):
        return output

    for entry in excludes:
        if not isinstance(entry, str) or not entry.strip():
            continue
        cleaned = entry.strip()
        path_obj = Path(cleaned)

        if not any(ch in cleaned for ch in ["*", "?", "["]):
            # Treat as path; normalise relative to ROOT
            if not path_obj.is_absolute():
                abs_path = (TRACEABILITY_CONFIG.parent / path_obj).resolve()
            else:
                abs_path = path_obj.resolve()
            try:
                rel = abs_path.relative_to(ROOT)
                if abs_path.is_dir():
                    output.append(rel.as_posix().rstrip("/") + "/")
                else:
                    output.append(rel.as_posix())
                continue
            except Exception:
                # Fall back to treating as glob pattern
                pass

        output.append(cleaned)

    return output


def load_gitignore_spec(extra_patterns: Optional[List[str]] = None) -> PathSpec:
    """Compile a PathSpec from .gitignore plus extra patterns.

    Always enforces ignoring the output docs/ tree and the VCS dir.
    """

    lines: List[str] = []
    gitignore = ROOT / ".gitignore"
    if gitignore.exists():
        try:
            lines.extend(gitignore.read_text(encoding="utf-8").splitlines())
        except OSError:
            pass

    enforced = ["docs/", ".git/"]
    lines.extend(enforced)
    if extra_patterns:
        lines.extend(extra_patterns)

    normalised = [ln for ln in (ln.strip() for ln in lines) if ln and not ln.startswith("#")]
    return PathSpec.from_lines(GitWildMatchPattern, normalised)


def effective_ref(branch: str) -> str:
    """Return the effective ref (branch or commit) taking environment overrides."""

    commit = os.environ.get("TRACEABILITY_GITHUB_COMMIT")
    if commit:
        return commit
    ref = os.environ.get("TRACEABILITY_GITHUB_REF")
    if ref:
        return ref
    return branch


# Cached (loaded once) – acceptable for this CLI tool
GITHUB_FILE_LINK_MAPPINGS = load_github_mappings()


__all__ = [
    "GITHUB_FILE_LINK_MAPPINGS",
    "TRACEABILITY_CONFIG",
    "effective_ref",
    "load_docs_copy_excludes",
    "load_github_mappings",
    "load_gitignore_spec",
]
