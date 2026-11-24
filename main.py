#!/usr/bin/env python3
"""Make the Judge Smile — write one warm line to /output/entry.txt.

Deterministic: the same bytes on every run. Standard library only.
The output directory honours $MAKEFUN_OUTPUT_DIR, then --output, then
the competition default /output.
"""

import argparse
import os
import sys

LINE = (
    "At 7 a.m., rain ticking on the awning, the barista slid my coffee "
    "over and said, 'on the house \u2014 you look like you needed a win "
    "today.' For once, I believed her."
)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the entry line.")
    parser.add_argument(
        "--output",
        default=None,
        help="Output directory (default: $MAKEFUN_OUTPUT_DIR or /output)",
    )
    args = parser.parse_args(argv)

    out_dir = args.output or os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
