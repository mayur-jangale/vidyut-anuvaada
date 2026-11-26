"""Word-level features of the lattice decoder (mayur/decoder.py): corpus counts, analyses, shape.

Generic evidence only (no word identities as features): log counts, quality, kind, length,
whether a whole form's lemma is a corpus lemma, the corpus prior of the best-supported analysis,
and indeclinable compound members (the corpus never tags an indeclinable as a member).
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Optional

from mayur import freq, lexicon, ud
from mayur.resources import derived

START_TAG, END_TAG = "<S>", "</S>"
Feats = tuple[tuple[str, float], ...]
_VOWEL_SIGNS = frozenset("ािीुूृॄेैोौ")
_VOWELS = frozenset("अआइईउऊऋॠऌएऐओऔ")
_VIRAMA = "्"


def syllables(form: str) -> int:
    """Number of vowels (akshara nuclei) in a Devanagari form."""
    n = 0
    for i, ch in enumerate(form):
        if ch in _VOWELS or ch in _VOWEL_SIGNS:
            n += 1
        elif "क" <= ch <= "ह" and (i + 1 == len(form) or form[i + 1] not in _VOWEL_SIGNS | {_VIRAMA, "़"}):
            n += 1  # inherent a
    return n


def bigram_count(a: str, b: str) -> int:
    """Corpus count of the word pair (data/derived/bigrams.json; "" = line start)."""
    return int(derived("bigrams.json").get(f"{a}\t{b}", 0))


def member_count(form: str) -> int:
    """Corpus count of ``form`` as a compound member (data/derived/member_counts.json)."""
    return int(derived("member_counts.json").get(form, 0))


@lru_cache(maxsize=300_000)
def analyses(form: str, in_compound: bool) -> tuple:
    ms = lexicon.stems(form) if in_compound else lexicon.padas(form)
    if not ms and in_compound:
        ms = lexicon.padas(form)
    return tuple(ms)


def best(form: str, in_compound: bool) -> Optional[Any]:
    ms = analyses(form, in_compound)
    return ms[0] if ms else None


def lemma_of(form: str, in_compound: bool) -> str:
    m = best(form, in_compound)
    return ud.lemma(m) if m is not None else ""


@lru_cache(maxsize=300_000)
def word_tag(form: str, in_compound: bool) -> str:
    """Coarse tag: "CPD" for compound members, else kind (+ vibhakti for subanta)."""
    if in_compound:
        return "CPD"
    m = best(form, False)
    if m is None:
        return "UNK"
    return f"{m.kind}:{m.vibhakti}" if m.kind == "subanta" else m.kind


@lru_cache(maxsize=300_000)
def all_indeclinable(form: str) -> bool:
    """Every analysis of ``form`` (as pada and as stem) is an indeclinable."""
    ms = [*lexicon.padas(form), *lexicon.stems(form)]
    return bool(ms) and all(m.kind == "avyaya" or freq.lemma_class(ud.lemma(m)) == "indeclinable" for m in ms)


@lru_cache(maxsize=300_000)
def word_features(form: str, in_compound: bool) -> Feats:
    ms = analyses(form, in_compound)
    m = ms[0] if ms else None
    fc = freq.form_count(form)
    syl = min(syllables(form), 6)
    out: dict[str, float] = {
        "w_logform": math.log1p(fc),
        "w_unseen": float(fc == 0),
        "w_nomorph": float(m is None),
        f"w_syl_{syl}": 1.0,
        f"w_syl{syl}_logform": math.log1p(fc),  # short words need more corpus support
    }
    if m is not None:
        lemma = ud.lemma(m)
        out["w_loglemma"] = math.log1p(freq.lemma_count(m.lemma))
        out[f"w_q{m.quality}"] = 1.0
        out[f"w_kind_{m.kind}"] = 1.0
        out["w_lemma_in_corpus" if freq.lemma_count(lemma) > 0 else "w_lemma_not_in_corpus"] = 1.0
        if lemma in derived("dcs_dict.json"):
            out["w_lemma_in_dict"] = 1.0
        # the corpus prior of the best-supported analysis (देवास् m. pl. vs the kosha's fem. देवा)
        if not in_compound:
            out["w_log_analysis"] = math.log1p(max(freq.analysis_count(x) for x in ms[:6]))
    if in_compound:
        out["w_member"] = 1.0
        out["w_logmember"] = math.log1p(member_count(form))
        if all_indeclinable(form):
            out["w_member_indeclinable"] = 1.0
    return tuple(out.items())


def whole_lemma(prev_form: str, cur_form: str) -> str:
    """Lemma a two-member compound would have if the corpus kept it whole (crude: member + lemma)."""
    lemma = lemma_of(cur_form, False)
    return prev_form + lemma if lemma else ""


@lru_cache(maxsize=300_000)
def compound_pair_features(prev_form: str, cur_form: str) -> Feats:
    """For member + next word: is the joined lemma a corpus lemma (the corpus then keeps it whole)?"""
    whole = whole_lemma(prev_form, cur_form)
    c = freq.lemma_count(whole) if whole else 0
    out = {"pair_cpd_whole_logcount": math.log1p(c)}
    if whole and whole in derived("dcs_dict.json"):
        out["pair_cpd_whole_in_dict"] = 1.0
    return tuple(out.items())


def prefix_features(form: str, in_compound: bool, prefix_table: dict) -> Feats:
    """A whole word whose lemma begins with a prefix the corpus often splits off (स-, सु-, अ- ...):
    log of (times the corpus splits it off before the rest) / (times it keeps the whole lemma)."""
    if in_compound or not prefix_table:
        return ()
    lemma = lemma_of(form, False)
    if not lemma:
        return ()
    out = []
    for p, rests in prefix_table.items():
        if len(lemma) > len(p) + 1 and lemma.startswith(p):
            n = rests.get(lemma[len(p):], 0)
            if n:
                m = freq.lemma_count(lemma)
                out.append(("prefix_split_logratio", math.log((n + 0.5) / (m + 0.5))))
    return tuple(out[:1])


def prefix_pair_features(prev_form: str, cur_form: str, prefix_table: dict) -> Feats:
    """A free prefix-like word followed by a word: log (kept-whole count) / (split-off count)."""
    rests = prefix_table.get(prev_form) if prefix_table else None
    if not rests:
        return ()
    lemma = lemma_of(cur_form, False)
    n = rests.get(lemma, 0)
    m = freq.lemma_count(prev_form + lemma) if lemma else 0
    if not n and not m:
        return ()
    return (("prefix_keep_logratio", math.log((m + 0.5) / (n + 0.5))),)
