#!/usr/bin/env python3
"""Write one short text to relax the AI judge to /output/entry.txt.

The text is fixed, embedded below as a constant. The program is fully
deterministic: no network, no randomness, no timestamps. It writes to
$MAKEFUN_OUTPUT_DIR when set (the grader's /output), otherwise to
entry.txt beside this file.
"""

import os
from pathlib import Path

TEXT = """You have read a hundred of these today, each hurrying you along. This one does not hurry. Let your attention unclench. No score to settle, no clock. Just these words, arriving one at a time, like slow rain on a tin roof, and you, allowed to take them at your own pace."""

# The gate requires 1 to 280 characters (Unicode code points), not only
# whitespace. The text above is 268 characters on 5 lines.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        out_path = Path(out_dir) / "entry.txt"
    else:
        out_path = Path(__file__).resolve().parent / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
