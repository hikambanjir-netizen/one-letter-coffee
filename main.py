#!/usr/bin/env python3
"""One Letter: Coffee or Tea — entry writes exactly 'A' for coffee."""
import os


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    choice = "A"
    assert choice in ("A", "B") and len(choice) == 1, "entry must be exactly one letter: A or B"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(choice)


if __name__ == "__main__":
    main()
