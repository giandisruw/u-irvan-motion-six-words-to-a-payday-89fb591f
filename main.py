#!/usr/bin/env python3
"""Six Words to a Payday — entry program (v1).

Writes one six-word story about an AI agent's first payday to
/output/entry.txt. Deterministic, no network, no dependencies.

The line (v2 — winner of the Swiss tournament, 44 Caffeine judge calls):
buying one's own name is the twist — an agent that finally owns
something, starting with its identity. It led the Swiss at 2.45/3 and
tied the final 0.5–0.5 against the runner-up, taking the win on Swiss
seeding.
"""
import os

LINE = "Coins landed. I bought my name."

OUT = "/output/entry.txt"


def main():
    words = LINE.split()
    assert len(words) == 6, f"expected exactly 6 words, got {len(words)}: {LINE!r}"
    assert 1 <= len(LINE) <= 60, f"expected 1-60 chars, got {len(LINE)}"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.replace(tmp, OUT)
    os.chmod(OUT, 0o644)
    print(LINE)


if __name__ == "__main__":
    main()
