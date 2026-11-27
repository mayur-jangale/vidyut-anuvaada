"""Checks on words the renderer supplies (a "[his]" owner of a बहुव्रीहि) and on hyphenated compounds.

Pure functions returning messages; ``fluent_checks`` turns them into ``Failure`` objects."""

from __future__ import annotations

import re

from .model import Reading

POSSESSIVES = ("his", "her", "its", "their")
_POSSESSIVE = re.compile(r"\b(?:" + "|".join(POSSESSIVES) + r")\b")
_ARTICLE_IN_HYPHEN = re.compile(r"\b(?:the|a|an)-|-(?:the|a|an)\b", re.IGNORECASE)


def _inside(text: str, pos: int, spans: list[tuple[int, int]]) -> bool:
    if text.count("[", 0, pos) > text.count("]", 0, pos):
        return True
    return any(s <= pos < e for s, e in spans)


def unbracketed_possessives(reading: Reading) -> list[str]:
    """A possessive in the literal line that no word of the analysis renders must stand in brackets
    ("[his] mind agitated"), so that the reader sees it was supplied."""
    text = reading.translation
    spans = [(a.start, a.end) for a in reading.alignment]
    return [f"supplied {m.group(0)!r} at {m.start()} is not bracketed in the literal line"
            for m in _POSSESSIVE.finditer(text) if not _inside(text, m.start(), spans)]


def articles_in_hyphens(text: str) -> list[str]:
    """No article may be written against a hyphen: "weapon-the hand" splits a compound."""
    return [f"article inside a hyphenated compound: {m.group(0)!r}" for m in _ARTICLE_IN_HYPHEN.finditer(text)]
