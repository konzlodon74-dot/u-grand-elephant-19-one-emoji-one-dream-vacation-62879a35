"""One Emoji, One Dream Vacation.

Writes a single emoji standing in for a dream vacation to
/output/entry.txt -- nothing else, no trailing newline.
"""

import os

EMOJI = "\U0001F334"  # palm tree: warm sun, white sand, nowhere to be


def main():
    # Gate: exactly one emoji character, 1-8 chars, non-whitespace.
    assert isinstance(EMOJI, str)
    assert 1 <= len(EMOJI) <= 8, f"length {len(EMOJI)} out of range"
    assert EMOJI.strip() == EMOJI and EMOJI.strip(), "must be non-whitespace"
    assert len(EMOJI) == 1, "must be exactly one emoji character"

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)

    # Read back and verify: exactly the emoji, no trailing newline.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == EMOJI, f"entry.txt mismatch: {written!r}"
    print(f"Wrote {EMOJI!r} ({len(EMOJI)} character) to /output/entry.txt")


if __name__ == "__main__":
    main()
