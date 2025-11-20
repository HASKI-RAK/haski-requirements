from pathlib import Path


# Repository roots
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SRS_SRC = ROOT / "srs" / "SRS.md"
REQS_SRC = ROOT / "srs" / "srs-requirements"
RTM_SRC = ROOT / "traceability" / "RTM.csv"

# Config paths
TRACEABILITY_CONFIG = ROOT / "traceability" / "config.yaml"

__all__ = [
    "ROOT",
    "DOCS",
    "SRS_SRC",
    "REQS_SRC",
    "RTM_SRC",
    "TRACEABILITY_CONFIG",
]
