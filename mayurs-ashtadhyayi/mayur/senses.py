"""Word sense in context: naive-Bayes choice among the DCS sense labels of an ambiguous lemma.

The model table (data/derived/sense_model.json, built by scripts/build_senses.py from the TRAIN
split only) holds, for every ambiguous lemma, prior counts per sense label and counts of context
features seen together with each label:
  w:  lemma of another word of the half-verse (window of 4 either side)
  s:  most frequent sense label of such a neighbour lemma
  g:  own case and number ("Nom/Sing"; "Cpd" for a compound member)      u: coarse word class
  m:  the word is a non-final compound member                            n:/p: lemma of the next / previous member
  v:  lemma of the finite verb of the half-verse
Without the table every function returns the "unknown" answer ("", 0.0).
"""

from __future__ import annotations

import math
from typing import Any, NamedTuple, Optional, Sequence

from mayur import resources, ud
from mayur.model import Morph, Reading

WINDOW = 4
DEFAULT_PARAMS: dict[str, Any] = {"k": 0.3, "weights": {}}
_NOUNISH = frozenset({"NOUN", "ADJ", "PROPN"})


class Slot(NamedTuple):
    """What the model knows of one word of a half-verse."""

    lemma: str
    upos: str  # coarse: V | N | other DCS class
    case: str  # "Nom/Sing", "Cpd", "-/Sing" ...
    member: bool  # non-final compound member
    finite: bool


class SenseContext(NamedTuple):
    neighbours: tuple[str, ...] = ()
    case: str = ""
    upos: str = ""
    member: bool = False
    nxt: str = ""
    prv: str = ""
    verb: str = ""


def coarse_upos(upos: str) -> str:
    return "V" if upos == "VERB" else "N" if upos in _NOUNISH else upos


def _case_key(case: str, number: str) -> str:
    return f"{case or '-'}/{number or '-'}"


def slot_of_token(tok: dict) -> Slot:
    """Slot of a parsed DCS token (``mayur.dcs.iter_sentences``)."""
    feats = tok.get("feats", {})
    member = bool(tok.get("compound_member"))
    case = "Cpd" if member else _case_key(feats.get("Case", ""), feats.get("Number", ""))
    return Slot(ud.canonical_lemma(tok["lemma"]), coarse_upos(tok["upos"]), case, member,
                tok["upos"] == "VERB" and "Person" in feats)


def slot_of_morph(m: Morph, in_compound: bool = False) -> Slot:
    """Slot of an analysed word, in the same conventions as ``slot_of_token``."""
    feats = ud.feats(m)
    member = in_compound or m.kind == "stem"
    case = "Cpd" if member else _case_key(feats.get("Case", ""), feats.get("Number", ""))
    return Slot(ud.canonical_lemma(ud.lemma(m)), coarse_upos(ud.upos(m)), case, member, m.kind == "tinanta")


def context_at(slots: Sequence[Slot], index: int) -> SenseContext:
    """Context of ``slots[index]`` within its half-verse."""
    me = slots[index]
    lo, hi = max(0, index - WINDOW), min(len(slots), index + WINDOW + 1)
    near = tuple(s.lemma for i, s in enumerate(slots[lo:hi], lo) if i != index and s.lemma)
    verbs = [(abs(i - index), s.lemma) for i, s in enumerate(slots) if s.finite and i != index]
    nxt = slots[index + 1].lemma if me.member and index + 1 < len(slots) else ""
    prv = slots[index - 1].lemma if index > 0 and slots[index - 1].member else ""
    return SenseContext(near, me.case, me.upos, me.member, nxt, prv, min(verbs)[1] if verbs else "")


def context_of(reading: Reading, word_index: int) -> SenseContext:
    """Context of ``reading.words[word_index]``: the other words of its half-verse."""
    word = reading.words[word_index]
    line = [(i, w) for i, w in enumerate(reading.words) if w.line == word.line and w.morph is not None]
    where = [i for i, _ in line]
    if word_index not in where:
        return SenseContext()
    return context_at([slot_of_morph(w.morph, w.in_compound) for _, w in line], where.index(word_index))


def features(ctx: SenseContext, top: dict[str, str], vocab: Optional[set[str]] = None) -> list[str]:
    """Feature names of a context; ``top`` maps a lemma to its most frequent label."""
    near = {x for x in ctx.neighbours if vocab is None or x in vocab}
    out = [f"w:{x}" for x in sorted(near)]
    out += [f"s:{lab}" for lab in sorted({top[x] for x in ctx.neighbours if x in top})]
    out += [f"g:{ctx.case}", f"u:{ctx.upos}"]
    out += ["m:1"] if ctx.member else []
    out += [f"n:{ctx.nxt}"] if ctx.nxt else []
    out += [f"p:{ctx.prv}"] if ctx.prv else []
    out += [f"v:{ctx.verb}"] if ctx.verb else []
    return out


def scores(entry: dict, feats: Sequence[str], params: dict[str, Any]) -> dict[str, float]:
    """Log score of each label of a lemma entry ``{"p": {label: n}, "f": {feature: {label: n}}}``."""
    k, weights = float(params.get("k", 0.3)), params.get("weights", {})
    prior = entry["p"]
    total, labels = sum(prior.values()), len(prior)
    table = entry.get("f", {})
    out = {}
    for label, n in prior.items():
        s = math.log((n + 1.0) / (total + labels))
        for f in feats:
            counts = table.get(f)
            if counts is not None:
                s += float(weights.get(f[0], 1.0)) * math.log((counts.get(label, 0.0) + k) / (n + 2 * k))
        out[label] = s
    return out


def posterior(logs: dict[str, float]) -> dict[str, float]:
    top = max(logs.values())
    exp = {lab: math.exp(v - top) for lab, v in logs.items()}
    z = sum(exp.values())
    return {lab: v / z for lab, v in exp.items()}


def _model() -> dict:
    return resources.derived("sense_model.json") or {}


def choose(lemma: str, context: SenseContext, model: Optional[dict] = None) -> tuple[str, float]:
    """(label, confidence) of the most probable sense of an ambiguous lemma; ("", 0.0) when the
    lemma is unknown or unambiguous in the model."""
    model = _model() if model is None else model
    entry = model.get("lemmas", {}).get(ud.canonical_lemma(lemma))
    if not entry or not entry.get("p"):
        return "", 0.0
    probs = posterior(scores(entry, features(context, model.get("top", {})), model.get("params", DEFAULT_PARAMS)))
    label = max(probs, key=lambda lab: (probs[lab], lab))
    return label, probs[label]


def gloss_of(label: str, model: Optional[dict] = None) -> str:
    """Cleaned short English gloss of a sense label (the label itself when none is stored)."""
    model = _model() if model is None else model
    return model.get("gloss", {}).get(label, label)
