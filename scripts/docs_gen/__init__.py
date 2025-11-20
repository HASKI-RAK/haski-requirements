"""Utilities for generating the ephemeral MkDocs ``docs/`` tree.

The public entry point is :func:`main`, mirrored by ``scripts/generate_docs.py``.
"""

from .cli import main

__all__ = ["main"]
