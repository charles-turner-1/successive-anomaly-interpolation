#!/usr/bin/env python3
"""Deterministic repository layout checker for the verification layout.

Card: D000A — Define the verification repository layout.

This checker enforces the contract documented in ``docs/verification-layout.md``:
a fixed set of *required* directory paths must exist at the checked root, and
each required path must contain only *permitted* content. The check is
deterministic: the same input tree always produces the same stdout and exit
code. It uses only the Python standard library, performs no network access,
follows no symlinks, and never mutates the tree under inspection.

Usage:
    python3 verification/check_layout.py [--root PATH]

Exit codes:
    0  layout is valid (all required paths present, no content violations)
    1  one or more violations (each missing path and unexpected entry is named)
    2  usage / environment error (e.g. root is not a directory)

Determinism notes:
  * Required-path membership and permitted-name sets are fixed constants.
  * Diagnostics are emitted in stable sorted order.
  * No timestamps, locale, randomness, or environment reads are used in output.
  * Only path names (not mtimes, sizes, hashes, or content) are inspected, so
    re-running against an unchanged tree is byte-for-byte identical.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Dict, FrozenSet, List

# ---------------------------------------------------------------------------
# Frozen layout contract (mirrors docs/verification-layout.md)
# ---------------------------------------------------------------------------

# Required directory paths, relative to the checked root.
REQUIRED_PATHS: FrozenSet[str] = frozenset(
    {
        "python",
        "tests",
        "julia",
        "formal",
        "schemas",
        "verification",
        "results",
        "reports",
    }
)

# The single universally-allowed emptiness marker in any required path.
ALLOWED_MARKER = ".gitkeep"

# Permitted immediate entries per required path. "*" means "no restriction on
# child directories at this level"; a listed name means "only these exact
# immediate children (plus ALLOWED_MARKER) are permitted at this level".
#
# These are deliberately coarse at D000A: they admit the skeleton each owner
# class creates and reject the common cross-ownership mistakes (a manifest in
# schemas/, a report in results/, a test in python/, etc.). Owner cards refine
# these tables and update docs/verification-layout.md in the same commit.
PERMITTED_ENTRIES: Dict[str, object] = {
    "python": "*",  # package/modules and packages owned by D000B+
    "tests": "*",   # test files and tests/fixtures/ owned by D000B+
    "julia": "*",   # Project.toml, Manifest.toml, src/, test/ owned by D000F+
    "formal": "*",  # lean-toolchain, lakefile*, lake-manifest.json, src/ (D000G+)
    "schemas": {"manifest.schema.json", "result.schema.json", "result.schema.yaml", "manifest.schema.yaml"},
    "verification": {"D000A.yaml", "check_layout.py", "fixtures"},
    "results": "*",
    "reports": "*",
}


def list_immediate(root: str, path: str) -> List[str]:
    """Return sorted immediate entry names under ``root/path`` (no symlink follow)."""
    full = os.path.join(root, path)
    names: List[str] = []
    for entry in os.scandir(full):
        # Do not follow symlinks: a symlinked directory is itself a name, and
        # os.scandir does not traverse it, so only its name is recorded.
        names.append(entry.name)
    names.sort()
    return names


def check(root: str) -> List[str]:
    """Run the layout check; return a list of violation strings (empty = OK)."""
    violations: List[str] = []

    # 1. Missing required paths (deterministic order: sorted path names).
    for path in sorted(REQUIRED_PATHS):
        full = os.path.join(root, path)
        if os.path.islink(full):
            violations.append(f"UNEXPECTED symlink at required path: {path}")
            continue
        if not os.path.isdir(full):
            violations.append(f"MISSING required path: {path}")
            continue
        # 2. Unexpected immediate entries in a constrained required path.
        permitted = PERMITTED_ENTRIES[path]
        for name in list_immediate(root, path):
            if name == ALLOWED_MARKER:
                continue
            if permitted == "*":
                continue
            if name not in permitted:
                violations.append(f"UNEXPECTED entry in {path}: {name}")

    violations.sort()
    return violations


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic verification-layout checker (D000A).",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="repository root to check (default: current directory)",
    )
    args = parser.parse_args(argv)

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        print(f"ERROR: root is not a directory: {root}")
        return 2

    violations = check(root)
    if violations:
        for v in violations:
            print(v)
        print(f"layout check: FAILED ({len(violations)} violation(s))")
        return 1

    print(f"layout check: OK ({len(REQUIRED_PATHS)} required paths present, no violations)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
