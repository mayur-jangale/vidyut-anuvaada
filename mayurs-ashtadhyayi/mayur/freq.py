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
def _parsed(form: str) -> tuple[tuple[str, str, dict[str, str], int], ...]:
    tags = derived("form_tags.json").get(form, {})
    return tuple((ud.canonical_lemma(lm), upos, fs, n) for (lm, upos, fs), n in
                 ((ud.parse_tag_key(k), n) for k, n in tags.items()))


def analysis_count(m: Morph) -> int:
    """Corpus count of ``m.form`` with the lemma and the features that ``m`` asserts.

    Corpus tokens of an indeclinable class count for an analysis whose form is their lemma
    (the corpus lists भृशम् as an adverb where grammar sees the accusative of भृश).
    """
    want_lemma, want_feats, as_word = ud.canonical_lemma(ud.lemma(m)), ud.feats(m), ud.canonical_lemma(m.form)
    total = 0
    for lm, upos, fs, n in _parsed(m.form):
        if lm == want_lemma and ud.feats_agree(want_feats, fs):
            total += n
        elif upos in ud.INDECLINABLE_UPOS and lm == as_word:
            total += n
    return total
