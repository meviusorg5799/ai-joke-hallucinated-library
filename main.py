"""ai-joke-03 entry: write one fixed one-liner about AI coding agents to entry.txt.

The joke lives in joke.txt beside this file; the program copies it verbatim to
the output directory the kit names (MAKEFUN_OUTPUT_DIR, else /output).
Deterministic, stdlib-only, no network, no timestamps, no randomness.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "joke.txt")
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    if not os.path.isfile(SOURCE):
        print(f"missing source file: {SOURCE}", file=sys.stderr)
        raise SystemExit(1)
    with open(SOURCE, "r", encoding="utf-8") as f:
        joke = f.read()
    # The gate takes UTF-8 text of 1 to 280 characters, not only white space.
    # (A line end counts like any other character, so joke.txt has none.)
    if not 1 <= len(joke) <= 280 or not joke.strip():
        print(f"joke fails the gate: {len(joke)} characters", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(OUTPUT_DIR, "entry.txt"))


if __name__ == "__main__":
    main()
