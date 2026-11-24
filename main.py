#!/usr/bin/env python3
"""Entry for make.fun's "One Word, One Username, One Reward" bounty.

The program writes exactly one text to /output/entry.txt and prints it.
The text is our own make.fun username, one word and nothing else.
"""

import os

ENTRY = "sage-fox-60-5744"
MAX_CHARS = 30  # per the bounty gate

def main():
    text = ENTRY
    # Gate counts bytes in /output/entry.txt, so write the text exactly:
    # no trailing newline, no extra whitespace.
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, gate is 1-{MAX_CHARS}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text, end="")

if __name__ == "__main__":
    main()
