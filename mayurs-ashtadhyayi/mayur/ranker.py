"""Trained reranker over the segmenter's valid splits (validity stays rule-based).

``features(line, split)`` is shared by training (scripts/train_ranker.py) and inference;
``rerank(line, splits)`` reorders splits by a linear model stored in mayur/models/split_ranker.json.
Model weights were trained on Digital Corpus of Sanskrit annotations (CC BY 4.0).
"""

from __future__ import annotations

import dataclasses
import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional, Sequence

from mayur import freq, lexicon, ud
from mayur.segmenter import Split, _prepare

MODEL_FILE = Path(__file__).with_name("models") / "split_ranker.json"
_VOWEL_SIGNS = frozenset("ािीुूृॄेैोौ")
_VOWELS = frozenset("अआइईउऊऋॠऌएऐओऔ")
_VIRAMA = "्"
_START_TAG, _END_TAG = "<S>", "</S>"


def _optional(name: str):
    return getattr(freq, name, None)


def syllables(form: str) -> int:
    """Number of vowels (akshara nuclei) in a Devanagari form."""
    n = 0
    for i, ch in enumerate(form):
        if ch in _VOWELS or ch in _VOWEL_SIGNS:
            n += 1
        elif "क" <= ch <= "ह" and (i + 1 == len(form) or form[i + 1] not in _VOWEL_SIGNS | {_VIRAMA, "़"}):
            n += 1  # inherent a
    return n


@lru_cache(maxsize=200_000)
def _best(form: str, in_compound: bool) -> Optional[Any]:
    ms = lexicon.stems(form) if in_compound else lexicon.padas(form)
    if not ms and in_compound:
        ms = lexicon.padas(form)
    return ms[0] if ms else None


def lemma_of(form: str, in_compound: bool) -> str:
    m = _best(form, in_compound)
    return ud.lemma(m) if m is not None else ""


@lru_cache(maxsize=200_000)
def word_tag(form: str, in_compound: bool) -> str:
    """Coarse tag: "CPD" for compound members, else kind (+ vibhakti for subanta)."""
    if in_compound:
        return "CPD"
    m = _best(form, False)
    if m is None:
        return "UNK"
    return f"{m.kind}:{m.vibhakti}" if m.kind == "subanta" else m.kind


@lru_cache(maxsize=200_000)
def _word_feats(form: str, in_compound: bool) -> tuple[tuple[str, float], ...]:
    m = _best(form, in_compound)
    fc = freq.form_count(form)
    out: dict[str, float] = {
        "w_logform": math.log1p(fc),
        "w_unseen": float(fc == 0),
        "w_nomorph": float(m is None),
        f"w_syl_{min(syllables(form), 6)}": 1.0,
    }
    if m is not None:
        out["w_loglemma"] = math.log1p(freq.lemma_count(m.lemma))
        out[f"w_q{m.quality}"] = 1.0
        out[f"w_kind_{m.kind}"] = 1.0
    if in_compound:
        out["w_member"] = 1.0
        member_count = _optional("member_count")
        if member_count is not None:
            out["w_logmember"] = math.log1p(member_count(form))
    return tuple(out.items())


def _add(acc: dict[str, float], key: str, value: float) -> None:
    acc[key] = acc.get(key, 0.0) + value


def features(line: str, split: Split, tag_table: Optional[dict[str, float]] = None) -> dict[str, float]:
    """Generic (identity-free) features of one split of ``line``; deterministic."""
    table = tag_table if tag_table is not None else _model().get("tag_bigram", {})
    words = split.words
    acc: dict[str, float] = {"seg_score": float(split.score), "n_words": float(len(words)),
                             "n_compounds": 0.0, "has_finite_verb": 0.0}
    spaces = _spaces(line)
    for w in words:
        for k, v in _word_feats(w.form, w.in_compound):
            _add(acc, k, v)
    tags = [word_tag(w.form, w.in_compound) for w in words]
    acc["has_finite_verb"] = float("tinanta" in tags)
    acc["n_compounds"] = float(sum(1 for i, w in enumerate(words)
                                   if w.in_compound and (i == 0 or not words[i - 1].in_compound)))
    for j in split.junctions:
        left = words[j.left]
        right = words[j.left + 1] if j.left + 1 < len(words) else None
        kind = "cpd" if j.in_compound else ("space" if left.end in spaces else "inner")
        _add(acc, f"j_{kind}", 1.0)
        _add(acc, f"j_{kind}_{'sandhi' if j.sutras else 'plain'}", 1.0)
        if kind == "inner" and (syllables(left.form) <= 2 or (right and syllables(right.form) <= 2)):
            _add(acc, "j_inner_short", 1.0)
    bigram_count = _optional("bigram_count")
    seq = [_START_TAG, *tags, _END_TAG]
    for a, b in zip(seq, seq[1:]):
        _add(acc, "tag_bigram", table.get(f"{a}|{b}", table.get("<unk>", -8.0)))
    for i in range(len(words) - 1):
        a, b = words[i], words[i + 1]
        if bigram_count is not None:
            _add(acc, "pair_logbigram", math.log1p(bigram_count(a.form, b.form)))
        ta, tb = tags[i], tags[i + 1]
        if ta.startswith("subanta:") and tb.startswith("subanta:"):
            _add(acc, "pair_case_agree" if ta == tb else "pair_case_differ", 1.0)
    return acc


@lru_cache(maxsize=4096)
def _spaces(line: str) -> frozenset:
    """Varna positions of written spaces (the lattice's own coordinates)."""
    try:
        return frozenset(_prepare(line)[1])
    except Exception:  # noqa: BLE001 - feature extraction must never fail
        return frozenset()


@lru_cache(maxsize=1)
def _model() -> dict[str, Any]:
    try:
        return json.loads(MODEL_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def score(feats: dict[str, float], model: dict[str, Any]) -> float:
    w, mean, std = model.get("weights", {}), model.get("mean", {}), model.get("std", {})
    return sum(w.get(k, 0.0) * (v - mean.get(k, 0.0)) / (std.get(k, 1.0) or 1.0) for k, v in feats.items())


def rerank(line: str, splits: Sequence[Split], model: Optional[dict[str, Any]] = None) -> list[Split]:
    """The same splits, best first by the trained model (stable); identity if no enabled model."""
    m = model if model is not None else _model()
    if not m or not m.get("enabled", False) or not m.get("weights"):
        return list(splits)
    table = m.get("tag_bigram", {})
    scored = [(score(features(line, s, table), m), i, s) for i, s in enumerate(splits)]
    scored.sort(key=lambda t: (-t[0], t[1]))
    return [dataclasses.replace(s, score=sc) for sc, _, s in scored]
