#!/usr/bin/env python3
"""Entrypoint for the make.fun ai-excited-01 entry.

The entry is a single image, entry.png, stored in this repository.
This program copies it to the output directory the grader reads:
$MAKEFUN_OUTPUT_DIR when set, otherwise /output. It creates the
output directory if needed and prints the path and size of the copy.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print(f"error: entry image not found: {src}", file=sys.stderr)
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"Wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
