"""Metre identification with vidyut-chandas, plus a syllable-count check for the shloka."""

from __future__ import annotations

from typing import Any, Sequence

from mayur import lipi, resources

LIGHT, HEAVY = "लघु", "गुरु"
_WEIGHT = {"L": "ल", "G": "ग"}


def weights(line: str) -> str:
    """Syllable weights of a line, ल (laghu) or ग (guru) per syllable."""
    match = resources.chandas().classify(lipi.to_code(line))
    return "".join(_WEIGHT[a.weight] for row in match.aksharas for a in row)


def _vidyut_name(text: str) -> str:
    padya = resources.chandas().classify(lipi.to_code(text)).padya
    return "" if padya is None else lipi.from_code(str(getattr(padya, "name", padya)))


def _is_shloka_half(w: str) -> bool:
    """Two padas of eight syllables; in the even pada syllable 5 is light and 6 heavy."""
    return len(w) == 16 and w[12] == "ल" and w[13] == "ग"


def identify(lines: Sequence[str]) -> dict[str, Any]:
    """{"name", "basis", "weights"} for a verse given as half-verses in Devanagari."""
    per_line = [weights(line) for line in lines]
    name = _vidyut_name(" ".join(lines))
    if name:
        return {"name": name, "basis": "vidyut-chandas", "weights": per_line}
    if per_line and all(_is_shloka_half(w) for w in per_line):
        return {"name": "अनुष्टुभ् (श्लोक)", "basis": "syllable count: 8 + 8 per half-verse", "weights": per_line}
    return {"name": "", "basis": "not identified", "weights": per_line}
