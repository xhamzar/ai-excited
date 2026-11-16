#!/usr/bin/env python3
"""Copy the entry image into the make.fun output directory.

Reads entry.png from the directory this script lives in and writes it to
$MAKEFUN_OUTPUT_DIR (default /output) as entry.png. The copy is verified
byte-for-byte by size before the script reports success.
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
    dst = os.path.join(out_dir, "entry.png")

    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(src, dst)

    # Verify the copy is complete: sizes must match exactly.
    src_size = os.path.getsize(src)
    dst_size = os.path.getsize(dst)
    if src_size != dst_size:
        print(
            f"error: copy incomplete: {dst} is {dst_size} bytes, "
            f"expected {src_size} bytes",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"wrote {dst} ({dst_size} bytes, verified)")


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)
