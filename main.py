"""One Star, Five Stars for the Food.

Writes a single-sentence alien tourist's one-star review of Earth that
still compliments the food, to /output/entry.txt (the gate requires
1-200 UTF-8 characters, not only whitespace).
"""

import os
import sys

# The review: one sentence, an alien's grievance plus a food compliment.
REVIEW = (
    "One star: your gravity bruised all four of my knees, your weather "
    "changes its mind hourly, and yet the noodles were so good I called off "
    "my invasion to finish the bowl."
)

MAX_CHARS = 200


def validate(text: str) -> str | None:
    """Return an error message if the review breaks the gate, else None."""
    if not text or text != text.strip():
        return "review must not be empty or padded with whitespace"
    if "\n" in text or "\r" in text:
        return "review must be a single line"
    if text.count(".") != 1 or not text.endswith("."):
        return "review must be exactly one sentence"
    if "  " in text:
        return "review must not contain double spaces"
    return None


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = REVIEW.strip()
    error = validate(text)
    if error is not None:
        print(f"invalid review: {error}", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"review is {len(text)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
