"""Entry program for u-motasimfuad-have-you-tried-turning-it-off-154a938b.

Writes one funny tech-support line to entry.txt in MAKEFUN_OUTPUT_DIR.
"""

import os
import stat

ENTRY_TEXT = "I turned it off and on again 47 times in 6 minutes \u2014 the good news is it worked, the bad news is I turned off the wrong server."

# Gate (kit competition.yaml): /output/entry.txt must be UTF-8 text of
# 1 to 199 characters, not only white space, one line.
assert 1 <= len(ENTRY_TEXT) <= 199, len(ENTRY_TEXT)
assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
assert "\n" not in ENTRY_TEXT, "entry must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
