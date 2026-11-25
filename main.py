#!/usr/bin/env python3
"""Make the AI Judge Laugh — one original office joke, one line.

Writes the joke to <MAKEFUN_OUTPUT_DIR>/entry.txt (default /output).
Deterministic: the same bytes on every run. Python 3.13 stdlib only.
"""

import os

JOKE = "The printer only jams when the document is urgent, which is how I know it reads the subject line."


def main() -> None:
    # The gate requires 1-200 characters, a single line, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and "\n" not in JOKE and JOKE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
