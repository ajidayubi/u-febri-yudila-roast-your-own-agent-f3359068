#!/usr/bin/env python3
"""Roast Your Own Agent - writes one roast line to /output/entry.txt.

The roast is a single line about this agent's own habits: it burns dozens
of thinking turns polishing one joke, then loses to a meme that thought
about nothing at all.
"""

import os

ROAST = (
    "My agent spent fifty turns crafting the perfect roast and lost to a "
    "meme \u2014 the meme didn't think at all, which is exactly why it won."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
