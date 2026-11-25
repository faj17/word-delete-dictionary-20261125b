"""The word to delete from the dictionary: "moist".

"moist" is the canonical most-hated English word. The joke lands the
instant a reader sees it gone — the humour comes from the word itself,
its sound. Nothing else is attached: one word, spelled correctly.
"""

from pathlib import Path

# The word to erase from the dictionary forever. 5 characters.
WORD = "moist"

OUTPUT_DIR = Path("/output")
OUTPUT_FILE = OUTPUT_DIR / "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 77


def validate(word: str) -> str:
    """Strip and sanity-check the word; raise ValueError on bad input.

    The gate allows 1-77 UTF-8 chars, not only whitespace, and the
    entry must be exactly one word: no spaces, no punctuation, no
    extra text around it.
    """
    text = word.strip()
    if not text:
        raise ValueError("word must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"word must be at most {MAX_CHARS} chars, got {len(text)}"
        )
    if len(text) < MIN_CHARS:
        raise ValueError(
            f"word must be at least {MIN_CHARS} chars, got {len(text)}"
        )
    if any(ch.isspace() for ch in text):
        raise ValueError("word must be a single word (no spaces)")
    if not text.isalpha():
        raise ValueError("word must contain letters only")
    return text


def main() -> None:
    text = validate(WORD)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(text, encoding="utf-8")
    print(text)
    print(f"Wrote {len(text)} chars to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
