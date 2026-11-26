"""Corpus frequencies from the DCS Ramayana tables (data/derived/). Missing tables give 0 / ""."""

from __future__ import annotations

from functools import lru_cache

from mayur import ud
from mayur.model import Morph
from mayur.resources import derived


def form_count(form: str) -> int:
    return int(derived("freq.json").get("forms", {}).get(form, 0))


def lemma_count(lemma: str) -> int:
    return int(derived("freq.json").get("lemmas", {}).get(lemma, 0))


def total_tokens() -> int:
    return int(derived("freq.json").get("tokens", 0))


def lemma_class(lemma: str) -> str:
    """"noun" | "adjective" | "pronoun" | "verb" | "indeclinable", or "" when unseen."""
    return str(derived("lemma_class.json").get(lemma, ""))


@lru_cache(maxsize=None)
def _parsed(form: str) -> tuple[tuple[str, dict[str, str], int], ...]:
    tags = derived("form_tags.json").get(form, {})
    return tuple((lm, fs, n) for lm, _, fs, n in ((*ud.parse_tag_key(k), n) for k, n in tags.items()))


def analysis_count(m: Morph) -> int:
    """Corpus count of ``m.form`` with the lemma and the features that ``m`` asserts."""
    want_lemma, want_feats = ud.lemma(m), ud.feats(m)
    return sum(n for lm, fs, n in _parsed(m.form) if lm == want_lemma and ud.feats_agree(want_feats, fs))
