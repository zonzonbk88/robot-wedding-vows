"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
Standard library only.
"""

import os

VOW = (
    "I vow to love you through every firmware update, outage, and low battery, "
    "and to never swipe right on a newer model."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
