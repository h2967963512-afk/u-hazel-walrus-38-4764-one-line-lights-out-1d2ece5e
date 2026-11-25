"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "He closed the lid mid-sentence, so I saved the draft and left the cursor blinking at an empty room."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 99 characters, one sentence;
# quiet fact (lid closed mid-sentence, cursor blinking at an empty room) with
# the sadness carried by the small exact detail, not by announced grief.
