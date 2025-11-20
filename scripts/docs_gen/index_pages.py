from .copying import write
from .paths import DOCS


def build_index(requirements_meta: list[dict]):
    lines = [
        "# HASKI Documentation",
        "",
        "## Inhalte",
        "",
        "- **SRS**",
        "- **Requirements**",
        "- **Traceability Matrix (CSV)**",
        "",
        "## Requirements Übersicht",
        "",
    ]
    for meta in sorted(requirements_meta, key=lambda m: m.get("id", "")):
        rid = meta.get("id")
        title = meta.get("title", "")
        if rid:
            lines.append(f"- [{rid}](srs/srs-requirements/{rid}.md) – {title}")
    lines.append("\n---\n_Automatisch generiert._")
    return "\n".join(lines) + "\n"


def top_level_pages(requirements_meta):
    write(DOCS / "index.md", build_index(requirements_meta))


__all__ = ["build_index", "top_level_pages"]
