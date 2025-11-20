import logging


logger = logging.getLogger(__name__)


def setup_logging(verbose: bool = False):
    """Configure minimal logging for the script.

    - INFO by default
    - DEBUG when --verbose flag is provided
    """

    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")


__all__ = ["logger", "setup_logging"]
