#!/usr/bin/env python3
"""Thin wrapper delegating docs generation to the ``docs_gen`` package.

Usage (from repo root):
    python scripts/generate_docs.py
"""

from docs_gen import main


if __name__ == "__main__":
    main()
