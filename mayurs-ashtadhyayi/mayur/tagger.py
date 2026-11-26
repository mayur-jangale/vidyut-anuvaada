"""Learned analysis choice: a lexicalised, candidate-restricted averaged-perceptron tagger.

Trained by ``scripts/train_tagger.py`` on DCS annotations (CC BY 4.0). A sequence is a whole
verse (half-verse boundaries kept as features). For each word the lexicon's analyses are the
only tags it may take; the model scores (word, candidate, context):

* observation features of the word (form, final/initial sounds, neighbouring forms, position),
* features of the candidate (lemma, lemma class, corpus counts, quality, source),
* agreement with the other words' candidate sets in the same half-verse (distance ≤ 4),
* history features from left-to-right beam search (two previous tags, concord with the chosen
  analyses of earlier words in the half-verse, verb–subject fit).

Every feature is conjoined with the candidate's full tag and with its case, gender and number
alone. Weights: ``{observation: {conjunct key: weight}}``.
"""

from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Callable, Optional, Sequence

from mayur.lipi import varnas
from mayur.model import Morph

MODEL_FILE = Path(__file__).resolve().parent / "models" / "tagger.json"
BEAM = 8
WINDOW = 4
Weights = dict[str, dict[str, float]]
Obs = list[str]
_PARTICLES = frozenset({"च", "इव", "न", "तु", "हि", "वा", "एव", "अपि", "इति"})
_PERSON = {"अस्मद्": "उत्तमपुरुष", "युष्मद्": "मध्यमपुरुष"}


def _freq(fn: str, arg) -> float:
    try:
        from mayur import freq
        return float(getattr(freq, fn)(arg) or 0)
    except Exception:  # tables missing
        return 0.0


@lru_cache(maxsize=100_000)
def _lemma_class(lemma: str) -> str:
    try:
        from mayur import freq
        return freq.lemma_class(lemma) or ""
    except Exception:
        return ""


@lru_cache(maxsize=200_000)
def _sounds(form: str) -> tuple[str, ...]:
    try:
        return varnas(form)
    except Exception:
        return tuple(form)


def _verbal(m: Morph) -> str:
    krt = m.krt or ""
    if krt in ("क्त्वा", "ल्यप्"):
        return "abs"
    if krt == "तुमुन्":
        return "inf"
    return "part" if krt else ""


def tag(m: Morph) -> str:
    """Signature of an analysis without its lemma: kind, case, number, gender, person, lakara, krt class."""
    return "|".join((m.kind, m.vibhakti or "", m.vacana or "", m.linga or "", m.purusha or "", m.lakara or "",
                     _verbal(m)))


def keys(m: Morph) -> tuple[str, ...]:
    """Conjunct keys: full tag, case only, gender only, number only."""
    return ("T" + tag(m), "C" + (m.vibhakti or m.kind), "G" + (m.linga or ""), "N" + (m.vacana or ""))


def _agree(a: Morph, b: Morph) -> bool:
    return a.kind == b.kind == "subanta" and (a.vibhakti, a.vacana, a.linga) == (b.vibhakti, b.vacana, b.linga)


def _fits(n: Morph, v: Morph) -> bool:
    """Nominative ``n`` can be the agent of finite verb ``v``."""
    return (n.kind == "subanta" and n.vibhakti == "प्रथमा" and v.kind == "tinanta" and n.vacana == v.vacana
            and _PERSON.get(n.lemma, "प्रथमपुरुष") == (v.purusha or "प्रथमपुरुष"))


def _bucket(x: float) -> str:
    return str(min(15, int(math.log2(1.0 + max(0.0, x)))))


class Verse:
    """One sequence to tag: candidates per word, half-verse index, compound flag, form."""

    def __init__(self, cands: Sequence[Sequence[Morph]], lines: Sequence[int], cpd: Sequence[bool],
                 forms: Sequence[str], minus: Optional[Sequence[Sequence[tuple[float, float]]]] = None):
        self.cands = [list(c) for c in cands]
        self.lines, self.cpd, self.forms = list(lines), list(cpd), list(forms)
        self.counts = [[(max(0.0, _freq("analysis_count", m) - (minus[i][k][0] if minus else 0.0)),
                         max(0.0, _freq("lemma_count", m.lemma) - (minus[i][k][1] if minus else 0.0)))
                        for k, m in enumerate(c)] for i, c in enumerate(self.cands)]
        self.top = [max(range(len(c)), key=lambda k, i=i: (self.counts[i][k][0], self.cands[i][k].quality, -k))
                    if c else -1 for i, c in enumerate(self.cands)]
        self.static = []
        for i, c in enumerate(self.cands):
            wobs = self._word_obs(i) if c else []
            self.static.append([wobs + self._static(i, k) for k in range(len(c))])

    def _word_obs(self, i: int) -> Obs:
        f, s, n = self.forms[i], _sounds(self.forms[i]), len(self.forms)
        o = ["b", "w=" + f, "ncand=" + str(min(len(self.cands[i]), 6))]
        o += ["s%d=%s" % (k, "".join(s[-k:])) for k in range(1, 6) if len(s) >= k]
        o += ["p%d=%s" % (k, "".join(s[:k])) for k in range(1, 3) if len(s) >= k]
        line = self.lines[i]
        same = [j for j in range(n) if self.lines[j] == line]
        if same and i == same[0]:
            o.append("first")
        if same and i == same[-1]:
            o.append("last")
        o.append("half=%d" % min(line % 2, 1))
        for d, tagname in ((-1, "pw"), (1, "nw"), (-2, "pw2"), (2, "nw2")):
            j = i + d
            if 0 <= j < n:
                g, gs = self.forms[j], _sounds(self.forms[j])
                o.append(tagname + "=" + g)
                if abs(d) == 1:
                    o += ["%ss%d=%s" % (tagname, k, "".join(gs[-k:])) for k in range(1, 4) if len(gs) >= k]
                    if self.cpd[j]:
                        o.append(tagname + "cpd")
            elif abs(d) == 1:
                o.append(tagname + "=<>")
        if i > 0 and self.cpd[i - 1] and not self.cpd[i]:
            o.append("cpdfinal")
            k = i - 1
            while k > 0 and self.cpd[k - 1]:
                k -= 1
            o.append("cpdlen=%d" % min(i - k, 3))
            o.append("cpdfirst=" + self.forms[k])
        if self.cpd[i]:
            o.append("incpd")
        return o

    def _static(self, i: int, k: int) -> Obs:
        m, c = self.cands[i][k], self.cands[i]
        ac, lc = self.counts[i][k]
        tot = sum(x[0] for x in self.counts[i])
        o = ["lm=" + m.lemma, "lc=" + _lemma_class(m.lemma), "ac=" + _bucket(ac), "lcnt=" + _bucket(lc),
             "sh=%d" % int(4 * ac / tot) if tot else "sh=-", "q=%d" % m.quality, "src=" + m.source,
             "kr=" + (m.krt or ""), "lmw=%s|%s" % (m.lemma, self.forms[i])]
        if k == self.top[i]:
            o.append("top")
        if ac == 0:
            o.append("ac0")
        if m.quality == max(x.quality for x in c):
            o.append("qtop")
        return o + self._agreement(i, m)

    def _agreement(self, i: int, m: Morph) -> Obs:
        o: Obs = []
        n, line = len(self.forms), self.lines[i]
        others = [j for j in range(n) if j != i and self.lines[j] == line and not self.cpd[j] and self.cands[j]]
        for j in others:
            d = j - i
            topj = self.cands[j][self.top[j]]
            if abs(d) <= WINDOW and m.kind == "subanta":
                dd = "%+d" % d
                if any(_agree(m, x) for x in self.cands[j]):
                    o.append("agAny" + dd)
                if _agree(m, topj):
                    o.append("agTop" + dd)
                if abs(d) == 1 and topj.kind == "subanta":
                    o.append("nbNom%+d" % d)
            if m.vibhakti == "प्रथमा":
                if _fits(m, topj):
                    o.append("vfitTop")
                elif any(_fits(m, x) for x in self.cands[j]):
                    o.append("vfitAny")
            if m.kind == "tinanta" and _fits(topj, m):
                o.append("kartaTop")
            if abs(d) == 1:
                o.append("nbT%+d=%s" % (d, tag(topj)))
            if topj.kind == "tinanta" and m.kind == "subanta":
                o.append("vlm=" + topj.lemma)
                o.append("vpr=%s|%s" % (topj.prayoga or "", topj.vacana or ""))
        if m.vibhakti == "द्वितीया":
            verbal = any(self.cands[j][self.top[j]].kind == "tinanta" or _verbal(self.cands[j][self.top[j]])
                         for j in others)
            o.append("accV" if verbal else "accNoV")
        if m.vibhakti == "प्रथमा" and not any(self.cands[j][self.top[j]].kind == "tinanta" for j in others):
            o.append("nomNoV")
        return o

    def history(self, i: int, k: int, path: Sequence[int]) -> Obs:
        """Features that depend on the analyses already chosen for words 0..i-1."""
        m = self.cands[i][k]
        prev = [self.cands[j][path[j]] for j in (i - 2, i - 1) if j >= 0 and path[j] >= 0]
        t1 = tag(prev[-1]) if prev else "<s>"
        t2 = tag(prev[0]) if len(prev) == 2 else "<s>"
        o = ["t1=" + t1, "t2=%s_%s" % (t2, t1)]
        if i > 0 and self.lines[i - 1] != self.lines[i]:
            o.append("t1line")
        line = self.lines[i]
        for j in range(max(0, i - WINDOW), i):
            if self.lines[j] != line or self.cpd[j] or path[j] < 0:
                continue
            x = self.cands[j][path[j]]
            if _agree(m, x):
                o.append("hag%d" % (i - j))
            if _fits(m, x) or _fits(x, m):
                o.append("hfit")
        return o


def score_obs(w: Weights, obs: Obs, ks: tuple[str, ...]) -> float:
    s = 0.0
    for o in obs:
        d = w.get(o)
        if d:
            for k in ks:
                s += d.get(k, 0.0)
    return s


def decode(v: Verse, w: Weights, gold: Optional[Sequence[tuple[int, ...]]] = None):
    """Beam search. Without ``gold``: best path. With ``gold`` (training): ``(pred, gold_path)``
    prefixes at the first point where no gold-consistent path survives (early update), else full paths."""
    n = len(v.cands)
    stat = [[score_obs(w, v.static[i][k], keys(m)) for k, m in enumerate(c)] for i, c in enumerate(v.cands)]
    beam: list[tuple[float, tuple[int, ...]]] = [(0.0, ())]
    gpath: tuple[int, ...] = ()
    gscore = 0.0

    def ext(score: float, path: tuple[int, ...], i: int, k: int) -> float:
        return score + stat[i][k] + score_obs(w, v.history(i, k, path), keys(v.cands[i][k]))

    for i in range(n):
        if not v.cands[i]:
            beam = [(s, p + (-1,)) for s, p in beam]
            gpath += (-1,)
            continue
        cand = [(ext(s, p, i, k), p + (k,)) for s, p in beam for k in range(len(v.cands[i]))]
        cand.sort(key=lambda x: -x[0])
        beam = cand[:BEAM]
        if gold is None:
            continue
        allowed = gold[i] or tuple(range(len(v.cands[i])))
        opts = [(ext(gscore, gpath, i, k), gpath + (k,)) for k in allowed]
        gscore, gpath = max(opts, key=lambda x: x[0])
        consistent = [b for b in beam if all(not gold[j] or b[1][j] in gold[j] for j in range(i + 1))]
        if not consistent:
            return list(beam[0][1]), list(gpath)
        gscore, gpath = consistent[0]
    best = list(beam[0][1])
    return best if gold is None else (best, list(gpath))


def phi(v: Verse, path: Sequence[int]) -> dict[tuple[str, str], float]:
    """Feature counts of a (prefix) path."""
    out: dict[tuple[str, str], float] = {}
    for i, k in enumerate(path):
        if k < 0:
            continue
        ks = keys(v.cands[i][k])
        for o in v.static[i][k] + v.history(i, k, path):
            for key in ks:
                out[(o, key)] = out.get((o, key), 0.0) + 1.0
    return out


class Perceptron:
    """Averaged perceptron over nested weights (avg = w - u / t)."""

    def __init__(self) -> None:
        self.w: Weights = {}
        self.u: Weights = {}
        self.t = 1

    def update(self, v: Verse, gold: Sequence[tuple[int, ...]]) -> bool:
        pred, gpath = decode(v, self.w, gold)
        self.t += 1
        if pred == gpath:
            return False
        diff = phi(v, gpath)
        for f, x in phi(v, pred).items():
            diff[f] = diff.get(f, 0.0) - x
        for (o, key), x in diff.items():
            if x:
                d, du = self.w.setdefault(o, {}), self.u.setdefault(o, {})
                d[key] = d.get(key, 0.0) + x
                du[key] = du.get(key, 0.0) + self.t * x
        return True

    def averaged(self, min_abs: float = 1e-3, ndigits: int = 3) -> Weights:
        out: Weights = {}
        for o, d in self.w.items():
            du = self.u[o]
            row = {k: round(x - du[k] / self.t, ndigits) for k, x in d.items()}
            row = {k: x for k, x in row.items() if abs(x) >= min_abs}
            if row:
                out[o] = row
        return out


def train(data: Sequence[tuple[tuple, Sequence[tuple[int, ...]]]], epochs: int, seed: int = 0,
          on_epoch: Optional[Callable[[int, Weights], None]] = None) -> Weights:
    """Averaged perceptron with early update over ``(Verse arguments, gold index sets)`` pairs.
    Verses are rebuilt on each pass (their feature strings are not kept, to bound memory)."""
    import random
    p = Perceptron()
    order = list(range(len(data)))
    for epoch in range(epochs):
        random.Random(seed + epoch).shuffle(order)
        for j in order:
            args, gold = data[j]
            p.update(Verse(*args), gold)
        if on_epoch is not None:
            on_epoch(epoch, p.averaged())
    return p.averaged()


@lru_cache(maxsize=1)
def load(path: Optional[str] = None) -> Optional[dict]:
    p = Path(path) if path else MODEL_FILE
    if not p.exists():
        return None
    data = json.loads(p.read_text(encoding="utf-8"))
    return data if data.get("enabled", True) and "weights" in data else None


def enabled() -> bool:
    return load() is not None


def choose_indices(cands: Sequence[Sequence[Morph]], lines: Sequence[int], compound_flags: Sequence[bool],
                   forms: Sequence[str], weights: Optional[Weights] = None) -> list[int]:
    """Index of the chosen candidate per word (0 for a word without candidates)."""
    w = weights if weights is not None else (load() or {}).get("weights", {})
    if not cands:
        return []
    path = decode(Verse(cands, lines, compound_flags, forms), w)
    return [max(k, 0) for k in path]


def choose(words, candidates=None, compound_flags=None, forms=None):
    """Two call styles.

    * ``choose(cands, lines, compound_flags, forms) -> list[int]``: candidate index per word.
    * ``choose(words: list[Word], candidates: Callable[[Word], list[int]])`` (as ``shabdabodha``
      calls it): chosen index into ``word.analyses`` per word, or None when no model is enabled.
    """
    if not callable(candidates):
        return choose_indices(words, candidates or [0] * len(words), compound_flags or [False] * len(words),
                              forms or [""] * len(words))
    if load() is None:
        return None
    idx = [list(candidates(x)) for x in words]
    cands = [[x.analyses[j] for j in ix] for x, ix in zip(words, idx)]
    pick = choose_indices(cands, [x.line for x in words], [x.in_compound for x in words], [x.form for x in words])
    return [ix[k] if ix else x.chosen for x, ix, k in zip(words, idx, pick)]


def enforce(words, chosen: list[int]) -> list[int]:
    """Hard constraints on a learned choice: a तृच् noun over an equally likely लुट् verb, and
    a finite verb without an agreeing nominative takes the nearest word that has one."""
    from mayur.shabdabodha import PRATHAMA, _agent_noun_preferred, candidates, is_case, is_finite, karta_agrees
    out = list(chosen)
    for i, w in enumerate(words):
        if w.analyses and _agent_noun_preferred(w, w.analyses[out[i]]):
            out[i] = next(j for j, a in enumerate(w.analyses) if a.krt == "तृच्" and is_case(a, PRATHAMA))
    for v, wv in enumerate(words):
        vm = wv.analyses[out[v]] if wv.analyses else None
        if not is_finite(vm):
            continue
        line = [i for i, w in enumerate(words) if w.line == wv.line and w.analyses and not w.in_compound]
        if any(karta_agrees(words[i].analyses[out[i]], vm) for i in line):
            continue
        options = [(abs(i - v), i, j) for i in line if i != v for j in candidates(words[i])
                   if karta_agrees(words[i].analyses[j], vm) and not is_finite(words[i].analyses[out[i]])]
        if options:
            _, i, j = min(options)
            out[i] = j
    return out
