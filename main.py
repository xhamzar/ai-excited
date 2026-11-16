#!/usr/bin/env python3
"""Write this entry's image to the make.fun output directory.

The entry is a single image, entry.png, stored beside this script. This
program copies it byte-for-byte to $MAKEFUN_OUTPUT_DIR/entry.png (default
/output/entry.png). It is fully deterministic: the same input file always
produces the same output bytes, it uses only the standard library, and it
never touches the network.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)
    return 0


if __name__ == "__main__":
    sys.exit(main())
