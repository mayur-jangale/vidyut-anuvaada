"""Learned analysis choice: a linear model over generic features, trained by
``scripts/train_tagger.py`` (averaged perceptron on DCS annotations, CC BY 4.0).

Score of a sequence of analyses = Σ unary features + Σ adjacent-pair features +
half-verse features (nominative–verb agreement, accusative with a verb). Decoding:
Viterbi over the adjacent pairs, then coordinate ascent with the half-verse features.
No word identities are used as features.
"""

from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Optional

from mayur.model import Morph, Word

MODEL_FILE = Path(__file__).resolve().parent / "models" / "tagger.json"
SWEEPS = 2
Feats = dict[str, float]


def _freq(fn: str, arg) -> float:
    try:
        from mayur import freq
        return float(getattr(freq, fn)(arg) or 0)
    except Exception:  # tables missing
        return 0.0


@lru_cache(maxsize=200_000)
def _lemma_class(lemma: str) -> str:
    try:
        from mayur import freq
        return freq.lemma_class(lemma) or ""
    except Exception:
        return ""


def _verbal(m: Morph) -> str:
    krt = m.krt or ""
    if krt in ("क्त्वा", "ल्यप्"):
        return "abs"
    if krt == "तुमुन्":
        return "inf"
    if krt:
        return "part"
    return ""


def unary(m: Morph) -> Feats:
    case = m.vibhakti or m.kind
    f: Feats = {
        "bias": 1.0,
        "lac": math.log1p(_freq("analysis_count", m)),
        "llc": math.log1p(_freq("lemma_count", m.lemma)),
        f"q{m.quality}": 1.0,
        f"kind:{m.kind}": 1.0,
        f"src:{m.source}": 1.0,
        f"cls:{_lemma_class(m.lemma)}": 1.0,
        f"case:{case}": 1.0,
        f"num:{m.vacana}": 1.0,
        f"gen:{m.linga}": 1.0,
        f"vb:{_verbal(m)}": 1.0,
        f"cls_case:{_lemma_class(m.lemma)}:{case}": 1.0,
        f"kind_vb:{m.kind}:{_verbal(m)}": 1.0,
    }
    if m.vibhakti == "सम्बोधन":
        f["voc"] = 1.0
    return f


def unary_all(cands: list[Morph]) -> list[Feats]:
    """Unary features plus features relative to the word's other candidates."""
    fs = [unary(m) for m in cands]
    top_lac = max(f["lac"] for f in fs)
    top_q = max(m.quality for m in cands)
    for f, m in zip(fs, cands):
        f["lac_gap"] = f["lac"] - top_lac
        if f["lac"] == top_lac:
            f["lac_top"] = 1.0
        if m.quality == top_q:
            f["q_top"] = 1.0
        f["ncand"] = math.log(len(cands))
    return fs


def _agree(a: Morph, b: Morph) -> bool:
    return a.kind == b.kind == "subanta" and (a.vibhakti, a.vacana, a.linga) == (b.vibhakti, b.vacana, b.linga)


def pair(a: Morph, b: Morph) -> Feats:
    """Features of two adjacent analyses (a before b)."""
    f: Feats = {f"cp:{a.vibhakti or a.kind}>{b.vibhakti or b.kind}": 1.0}
    if _agree(a, b):
        f["agree"] = 1.0
    if a.vibhakti == "षष्ठी" and b.kind == "subanta":
        f["gen>nom"] = 1.0
    return f


def _person(m: Morph) -> str:
    return {"अस्मद्": "उत्तमपुरुष", "युष्मद्": "मध्यमपुरुष"}.get(m.lemma, "प्रथमपुरुष")


def sentence(ms: list[Morph]) -> Feats:
    """Half-verse features: does each finite verb have an agreeing nominative, etc."""
    f: Feats = {}
    verbs = [m for m in ms if m.kind == "tinanta"]
    for v in verbs:
        ok = any(m.vibhakti == "प्रथमा" and m.vacana == v.vacana and _person(m) == (v.purusha or "प्रथमपुरुष")
                 for m in ms)
        key = "karta" if ok else "nokarta"
        f[key] = f.get(key, 0.0) + 1.0
    verbal = bool(verbs) or any(_verbal(m) in ("abs", "inf") for m in ms)
    accs = sum(1 for m in ms if m.vibhakti == "द्वितीया")
    if accs:
        f["acc_verb" if verbal else "acc_noverb"] = float(accs)
    f[f"nverbs:{min(len(verbs), 2)}"] = 1.0
    return f


def dot(w: dict[str, float], f: Feats) -> float:
    return sum(w.get(k, 0.0) * v for k, v in f.items())


def decode(cands: list[list[Morph]], w: dict[str, float]) -> list[int]:
    """Best candidate index per position (every position must have ≥ 1 candidate)."""
    n = len(cands)
    if n == 0:
        return []
    un = [[dot(w, f) for f in unary_all(c)] for c in cands]
    best = [list(un[0])]
    back: list[list[int]] = [[0] * len(cands[0])]
    for i in range(1, n):
        row, ptr = [], []
        for b, mb in enumerate(cands[i]):
            scores = [best[-1][a] + dot(w, pair(ma, mb)) for a, ma in enumerate(cands[i - 1])]
            a = max(range(len(scores)), key=scores.__getitem__)
            row.append(scores[a] + un[i][b])
            ptr.append(a)
        best.append(row)
        back.append(ptr)
    path = [max(range(len(best[-1])), key=best[-1].__getitem__)]
    for i in range(n - 1, 0, -1):
        path.append(back[i][path[-1]])
    path.reverse()

    def total(p: list[int]) -> float:
        ms = [cands[i][p[i]] for i in range(n)]
        s = sum(un[i][p[i]] for i in range(n)) + sum(dot(w, pair(ms[i - 1], ms[i])) for i in range(1, n))
        return s + dot(w, sentence(ms))

    for _ in range(SWEEPS):
        changed = False
        for i in range(n):
            if len(cands[i]) < 2:
                continue
            k = max(range(len(cands[i])), key=lambda c: total(path[:i] + [c] + path[i + 1:]))
            if k != path[i]:
                path[i], changed = k, True
        if not changed:
            break
    return path


def features(cands: list[list[Morph]], path: list[int]) -> Feats:
    """Global feature vector of one analysed half-verse (for training)."""
    out: Feats = {}
    ms = [c[i] for c, i in zip(cands, path)]
    parts = [unary_all(c)[i] for c, i in zip(cands, path)] + [pair(ms[i - 1], ms[i]) for i in range(1, len(ms))] + [sentence(ms)]
    for f in parts:
        for k, v in f.items():
            out[k] = out.get(k, 0.0) + v
    return out


@lru_cache(maxsize=1)
def load(path: Optional[str] = None) -> Optional[dict]:
    p = Path(path) if path else MODEL_FILE
    if not p.exists():
        return None
    data = json.loads(p.read_text(encoding="utf-8"))
    return data if data.get("enabled", True) else None


def choose(words: list[Word], candidates) -> Optional[list[int]]:
    """Chosen analysis index per word with the learned model; None when no model."""
    model = load()
    if model is None:
        return None
    w = model["weights"]
    idx = [candidates(x) for x in words]
    # each half-verse is decoded on its own; words without analyses are skipped
    chosen = [x.chosen for x in words]
    for line in sorted({x.line for x in words}):
        pos = [i for i, x in enumerate(words) if x.line == line and idx[i]]
        path = decode([[words[i].analyses[j] for j in idx[i]] for i in pos], w)
        for i, k in zip(pos, path):
            chosen[i] = idx[i][k]
    return chosen
