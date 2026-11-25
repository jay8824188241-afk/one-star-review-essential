#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes a single deadpan one-star review of sleep to /output/entry.txt
and prints it to stdout. Standard library only, deterministic, no network.
"""

import os
import sys

REVIEW = (
    "One star. Sleep demands eight hours a night, returns nothing but "
    "a sore neck, and still has the nerve to leave me tired."
)

# Harness runs in a sandbox and reads /output/entry.txt; allow an
# override so the same program can be verified locally.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not 1 <= len(REVIEW) <= 160:
        print(f"review is {len(REVIEW)} characters, must be 1-160",
              file=sys.stderr)
        raise SystemExit(1)
    if REVIEW != REVIEW.strip() or "\n" in REVIEW:
        print("review must be a single line with no surrounding whitespace",
              file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w",
              encoding="utf-8") as f:
        f.write(REVIEW)
    print(REVIEW)


if __name__ == "__main__":
    main()
