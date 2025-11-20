from pathlib import Path


# Repository roots
ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
SRS_SRC = ROOT / "srs" / "SRS.md"
REQS_SRC = ROOT / "srs" / "srs-requirements"

TRACEABILITY_DIR = ROOT / "scripts" / "traceability"
RTM_SRC = TRACEABILITY_DIR / "RTM.csv"

# Config paths
TRACEABILITY_CONFIG = TRACEABILITY_DIR / "config.yaml"

__all__ = [
    "ROOT",
    "DOCS",
    "SRS_SRC",
    "REQS_SRC",
    "TRACEABILITY_DIR",
    "RTM_SRC",
    "TRACEABILITY_CONFIG",
]
