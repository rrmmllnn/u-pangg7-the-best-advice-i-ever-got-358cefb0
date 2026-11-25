#!/usr/bin/env python3
"""The Best Advice I Ever Got — writes one sentence to /output/entry.txt.

One sentence, at most 200 characters, about the best advice the writer
ever received: a named person, a concrete scene, one twist.
"""

import os

ENTRY = (
    "My grandfather, who lost his shop twice and rebuilt it twice, "
    "told me one morning over burnt toast: 'Start again before you're "
    "ready — waiting for ready is how you stay broke.'"
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if "\n" in text or text.count(".") != 1:
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
