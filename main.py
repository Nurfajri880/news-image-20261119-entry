#!/usr/bin/env python3
"""news-image-20261119 entry: publish the day's front page.

The image (entry.png, in this repository) is a newspaper front page that
sums up world news of Thursday 19 November 2026: 35 stories across 6
continents, 11 featured with drawn illustrations, a world map with numbered
pins, and 24 more briefs. It was drawn for this competition and verified
against the day's reporting (AP, Reuters, AFP, BBC, Al Jazeera, UN News).

This program does one thing: copy that image to the output directory the
grader reads, then check the written file is a real PNG inside the 1 MiB
limit. Standard library only, no network, deterministic: two runs write
the same bytes.
"""
import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
LIMIT = 1024 * 1024  # 1 MiB, the competition maximum
EXPECT_W, EXPECT_H = 1024, 1024


def png_size(path):
    """Read width and height from the PNG IHDR chunk (bytes 16..24)."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if len(head) < 24 or head[:8] != PNG_MAGIC:
        return None
    w, h = struct.unpack(">II", head[16:24])
    return w, h


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    with open(dest, "rb") as fh:
        magic = fh.read(8)
    size = os.path.getsize(dest)
    if magic != PNG_MAGIC:
        print("error: output is not a PNG file", file=sys.stderr)
        return 1
    if size > LIMIT:
        print(f"error: output is {size} bytes, over the 1 MiB limit",
              file=sys.stderr)
        return 1
    dims = png_size(dest)
    if dims != (EXPECT_W, EXPECT_H):
        print(f"error: output is {dims}, expected "
              f"{EXPECT_W}x{EXPECT_H}", file=sys.stderr)
        return 1
    print(f"wrote {dest} ({size} bytes, valid PNG, 1024x1024)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
