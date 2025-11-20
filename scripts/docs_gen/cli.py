import argparse
import logging

from .config import GITHUB_FILE_LINK_MAPPINGS, load_docs_copy_excludes, load_gitignore_spec
from .copying import clean_docs, copy_repo_tree_to_docs
from .index_pages import top_level_pages
from .logging_utils import setup_logging
from .requirements import copy_requirements
from .rtm import copy_rtm, generate_traceability_matrix
from .srs import copy_srs

logger = logging.getLogger(__name__)


def print_mappings():
    if not GITHUB_FILE_LINK_MAPPINGS:
        logger.info("No GitHub file link mappings configured.")
        return
    logger.info("Active GitHub file link mappings:")
    for mapping in GITHUB_FILE_LINK_MAPPINGS:
        logger.info(
            "  - repo=%s local_root=%s branch=%s sub=%s",
            mapping.get("repo"),
            mapping.get("local_root"),
            mapping.get("branch"),
            mapping.get("repo_root_subpath"),
        )


def build_docs(verbose: bool):
    clean_docs()

    extra_excludes = load_docs_copy_excludes()
    if extra_excludes:
        logger.debug("Additional copy excludes from config: %s", extra_excludes)
    ignore_spec = load_gitignore_spec(extra_patterns=extra_excludes)
    copy_repo_tree_to_docs(ignore_spec)

    copy_srs()
    req_meta = copy_requirements()
    generate_traceability_matrix(verbose=verbose)
    copy_rtm(verbose=verbose)
    top_level_pages(req_meta)
    logger.info("Docs tree generated.")


def main():
    parser = argparse.ArgumentParser(description="Generate docs (SRS, requirements, RTM)")
    parser.add_argument(
        "--print-mappings",
        action="store_true",
        help="Print active GitHub file link mappings and exit",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Verbose output (diagnostics section in RTM page)",
    )
    args = parser.parse_args()

    setup_logging(verbose=args.verbose)
    logger.debug("Starting docs generation (verbose=%s)", args.verbose)

    if args.print_mappings:
        print_mappings()
        return

    build_docs(verbose=args.verbose)


__all__ = ["main", "build_docs", "print_mappings"]
