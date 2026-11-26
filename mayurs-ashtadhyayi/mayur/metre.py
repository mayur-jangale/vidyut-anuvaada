"""Metre identification with vidyut-chandas, plus a syllable-count check for the shloka."""

from __future__ import annotations

from typing import Any, Sequence

from mayur import resources


def _weights(line: str) -> str:
    match = resources.chandas().classify(line)
    return "".join(a.weight for row in match.aksharas for a in row)


def _vidyut_name(text: str) -> str | None:
    padya = resources.chandas().classify(text).padya
    return None if padya is None else str(getattr(padya, "name", padya))


def _is_shloka_half(weights: str) -> bool:
    """Two 8-syllable padas; syllable 5 light and 6 heavy in the even pada (the stable part of the rule)."""
    return len(weights) == 16 and weights[12] == "L" and weights[13] == "G"


def identify(lines: Sequence[str]) -> dict[str, Any]:
    """Return {"name", "basis", "weights"}; ``weights`` holds one L/G string per line."""
    weights = [_weights(line) for line in lines]
    name = _vidyut_name(" ".join(lines))
    if name:
        return {"name": name, "basis": "vidyut-chandas", "weights": weights}
    if weights and all(_is_shloka_half(w) for w in weights):
        return {"name": "anuzwuB (Sloka)", "basis": "syllable count 8+8 per half-verse", "weights": weights}
    return {"name": "", "basis": "not identified", "weights": weights}
