"""Lazy access to corpus frequency tables (data/derived/freq.json)."""

from __future__ import annotations

import json
from functools import lru_cache

from mayur.resources import derived_dir


@lru_cache(maxsize=1)
def _table() -> dict:
    try:
        with open(derived_dir() / "freq.json", encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {"forms": {}, "lemmas": {}, "tokens": 0}


def form_count(form: str) -> int:
    return int(_table().get("forms", {}).get(form, 0))


def lemma_count(lemma: str) -> int:
    return int(_table().get("lemmas", {}).get(lemma, 0))


def total_tokens() -> int:
    return int(_table().get("tokens", 0))


def reload() -> None:
    _table.cache_clear()
