"""One Word From Grandma: the single word a grandma would text about AI.

Entry word: Witchcraft

A grandma faced with a machine that talks back would not reach for
tech jargon. She would call it what every new marvel has always been
called at her kitchen table: witchcraft. Warm, a little baffled, and
funny in a single word -- exactly how she would text it.
"""

import os

ENTRY = "Witchcraft"


def validate_entry(word: str) -> str:
    """Enforce the competition gate: exactly one word, 1-30 UTF-8 chars."""
    if not word or word.strip() != word:
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(word) <= 30:
        raise ValueError("entry must be 1-30 characters")
    word.encode("utf-8")
    return word


def output_path() -> str:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def write_entry() -> str:
    word = validate_entry(ENTRY)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    return path


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
