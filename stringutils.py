"""Small, dependency-free string helpers."""

import re


def slugify(text: str) -> str:
    """Lowercase a string and turn runs of non-alphanumerics into single hyphens."""
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def truncate(text: str, length: int, suffix: str = "…") -> str:
    """Truncate text to `length` characters, appending `suffix` if shortened."""
    if len(text) <= length:
        return text
    return text[: max(0, length - len(suffix))] + suffix


def titlecase(text: str) -> str:
    """Capitalize the first letter of each whitespace-separated word."""
    return " ".join(word[:1].upper() + word[1:] for word in text.split())


def zfill_left(text, width):
    """Left-pad text with zeros to the given width."""
    return text.zfill(width)
