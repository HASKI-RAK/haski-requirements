import logging

from .copying import write
from .paths import DOCS, SRS_SRC

logger = logging.getLogger(__name__)


def copy_srs():
    if SRS_SRC.exists():
        logger.info("Copy SRS -> docs/srs/SRS.md")
        dst = DOCS / "srs" / "SRS.md"
        content = SRS_SRC.read_text(encoding="utf-8")
        banner = "# Software Requirements Specification (SRS)\n\n<!-- Generated copy from srs/SRS.md -->\n\n"
        if not content.lstrip().startswith("#"):
            banner = ""
        write(dst, banner + content)
    else:
        logger.warning("SRS source not found at %s", SRS_SRC)


__all__ = ["copy_srs"]
