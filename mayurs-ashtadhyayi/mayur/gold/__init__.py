"""Gold data: DCS analyses of Valmiki Ramayana, Bala-kanda sarga 1 (CC BY 4.0)."""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path


@lru_cache(maxsize=1)
def load() -> dict:
    with open(Path(__file__).with_name("ramayana_bala_1.json"), encoding="utf-8") as f:
        return json.load(f)


def verse(number: int) -> dict:
    for v in load()["verses"]:
        if v["number"] == number:
            return v
    raise KeyError(number)


def verse_text(number: int) -> str:
    """Compact Devanagari input: half-verses joined by ' । ', ending ' ॥'."""
    lines = [ln["compact_deva"] for ln in verse(number)["lines"]]
    return " । ".join(lines) + " ॥"
