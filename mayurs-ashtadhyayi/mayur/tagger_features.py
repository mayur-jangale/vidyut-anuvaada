"""Feature extraction of the analysis tagger (``mayur.tagger``): a :class:`Verse` holds the candidates of
every word of a verse and the observation strings of each (word, candidate); ``history`` gives the
features that depend on the analyses chosen for the earlier words. Corpus-structure features live in
``mayur.tagger_struct``. All feature values are Devanagari substrings; names are English.
"""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Optional, Sequence

from mayur import tagger_struct as struct
from mayur.lipi import varnas
from mayur.model import Morph

WINDOW = 4
Obs = list[str]
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


@lru_cache(maxsize=200_000)
def _lkey(m: Morph) -> str:
    """Corpus lemma key of an analysis (the DCS citation form)."""
    from mayur import ud
    try:
        return ud.canonical_lemma(ud.lemma(m))
    except Exception:
        return m.lemma


@lru_cache(maxsize=200_000)
def lemma_form_count(m: Morph) -> float:
    """Corpus count of ``m.form`` under ``m``'s lemma, whatever its features (P(lemma | form))."""
    try:
        from mayur import freq, ud
        key, word = _lkey(m), ud.canonical_lemma(m.form)
        return float(sum(n for lm, upos, _fs, n in freq._parsed(m.form)
                         if lm == key or (upos in ud.INDECLINABLE_UPOS and lm == word and m.kind == "avyaya")))
    except Exception:
        return 0.0


def _bucket(x: float) -> str:
    return str(min(15, int(math.log2(1.0 + max(0.0, x)))))


class Verse:
    """One sequence to tag: candidates per word, half-verse index, compound flag, form."""

    def __init__(self, cands: Sequence[Sequence[Morph]], lines: Sequence[int], cpd: Sequence[bool],
                 forms: Sequence[str], minus: Optional[Sequence[Sequence[tuple[float, float]]]] = None,
                 prior: Optional[Sequence[int]] = None, tables: Optional[dict] = None,
                 obs_forms: Optional[Sequence[str]] = None, variants: Optional[Sequence[Sequence[str]]] = None):
        """``obs_forms``: spelling used for the observation features (one spelling for a sibling pair,
        see ``mayur.tagger_siblings``); ``variants``: per candidate, which member of the pair it is."""
        self.tab = tables or {}
        self.cands = [list(c) for c in cands]
        self.lines, self.cpd = list(lines), list(cpd)
        self.forms = list(obs_forms) if obs_forms is not None else list(forms)
        self.var = [list(v) for v in variants] if variants is not None else None
        mi = lambda i, k, j: minus[i][k][j] if minus and k < len(minus[i]) else 0.0  # noqa: E731
        self.counts = [[(max(0.0, _freq("analysis_count", m) - mi(i, k, 0)),
                         max(0.0, _freq("lemma_count", m.lemma) - mi(i, k, 1)),
                         max(0.0, lemma_form_count(m) - mi(i, k, 1)))
                        for k, m in enumerate(c)] for i, c in enumerate(self.cands)]
        self.top = [max(range(len(c)), key=lambda k, i=i: (self.counts[i][k][0], self.cands[i][k].quality, -k))
                    if c else -1 for i, c in enumerate(self.cands)]
        # the other words' reference reading: pass-1 choice (second pass) or the most frequent one
        self.ref = list(prior) if prior is not None else self.top
        self.p2 = "P" if prior is not None else ""
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
        ac, lc, lf = self.counts[i][k]
        tot = sum(x[0] for x in self.counts[i])
        lf_max = max(x[2] for x in self.counts[i])
        o = ["lm=" + m.lemma, "lc=" + _lemma_class(m.lemma), "ac=" + _bucket(ac), "lcnt=" + _bucket(lc),
             "sh=%d" % int(4 * ac / tot) if tot else "sh=-", "q=%d" % m.quality, "src=" + m.source,
             "kr=" + (m.krt or ""), "lmw=%s|%s" % (m.lemma, self.forms[i])]
        o.append("lf=%s" % (_bucket(lf) if lf else "-"))
        if lf_max:
            o.append("lfTop=%d" % (lf == lf_max))
            o.append("lfSh=%d" % int(4 * lf / max(1.0, sum(x[2] for x in self.counts[i]))))
        if self.var is not None and self.var[i][k]:
            o += ["var=" + self.var[i][k], "varTop=%d" % (k == self.top[i])]
        if i > 0 and self.cpd[i - 1]:
            o += ["cf_" + x for x in o if x.startswith(("lfTop", "ac="))]
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
            topj = self.cands[j][self.ref[j]]
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
            verbal = any(self.cands[j][self.ref[j]].kind == "tinanta" or _verbal(self.cands[j][self.ref[j]])
                         for j in others)
            o.append("accV" if verbal else "accNoV")
        if m.vibhakti == "प्रथमा" and not any(self.cands[j][self.ref[j]].kind == "tinanta" for j in others):
            o.append("nomNoV")
        return o + struct.verse_level(self, i, m) + struct.structural(self, i, m)

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
