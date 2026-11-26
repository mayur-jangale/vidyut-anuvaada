"""Literal English built by template from the grammatical analysis; every content word is aligned."""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from . import english, lipi
from .model import Alignment, Reading, Word

Piece = tuple[str, Optional[int], str]  # (text, word index or None, separator before it)

_PREP = {"करण": "by", "सम्प्रदान": "to", "अपादान": "from", "अधिकरण": "in", "सम्बन्ध": "of"}
_CONNECTIVES = {"and", "but", "or", "then", "now", "thus", "if", "when", "so", "as"}
_NEGATIONS = {"not", "no"}
_NO_PLURAL = {"all", "this", "that", "other", "much", "many", "one", "who", "which"}
_MODAL = {"लृट्": "will", "लुट्": "will", "विधिलिङ्": "should", "आशीर्लिङ्": "may", "लृङ्": "would",
          "लेट्": "shall"}
_PAST = {"लिट्", "लङ्", "लुङ्"}
_PASSIVE = {"कर्मणि", "भावे"}


def _p(text: str, idx: Optional[int] = None, sep: str = " ") -> Piece:
    return (text, idx, sep)


def _krt(krt: Optional[str], g: str) -> str:
    if krt == "क्त":
        return english.participle(g)
    if krt == "क्तवतु":
        return english.past(g)
    if krt in ("शतृ", "शानच्"):
        return english.present_participle(g)
    if krt in ("तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्"):
        return "to be " + english.participle(g)
    if krt in ("क्वसु", "कानच्"):
        return "having " + english.participle(g)
    return g


class _Renderer:
    def __init__(self, reading: Reading) -> None:
        self.reading = reading
        self.words = reading.words
        n = len(self.words)
        order = [i for i in reading.anvaya if 0 <= i < n]
        order = list(dict.fromkeys(order)) if order else []
        order += [i for i in range(n) if i not in order]
        self.pos = {i: k for k, i in enumerate(order)}
        self.order = order
        self.used: set[int] = set()
        self.acc: set[int] = set()
        self.children: dict[int, list[int]] = {}
        for i in order:
            w = self.words[i]
            if w.in_compound or w.head is None or not 0 <= w.head < n:
                continue
            h = self.resolve(w.head)
            if h != i:
                self.children.setdefault(h, []).append(i)

    # ---- helpers -------------------------------------------------------------------
    def resolve(self, i: int) -> int:
        w = self.words[i]
        if w.in_compound and w.compound is not None:
            for c in self.reading.compounds:
                if c.id == w.compound and c.members:
                    return c.members[-1]
        return i

    def role(self, i: int) -> str:
        return self.words[i].role

    def text(self, i: int) -> str:
        w = self.words[i]
        if w.morph is None or w.arsha:
            return "⟨" + lipi.iast(w.form) + "⟩"
        return w.gloss or lipi.iast(w.morph.stem or w.morph.lemma) or "⟨" + lipi.iast(w.form) + "⟩"

    def members(self, i: int) -> list[int]:
        w = self.words[i]
        if w.compound is None or w.in_compound:
            return []
        for c in self.reading.compounds:
            if c.id == w.compound and c.members and c.members[-1] == i:
                return [m for m in c.members[:-1]]
        return []

    def noun_text(self, i: int) -> str:
        w = self.words[i]
        m = w.morph
        g = self.text(i)
        if m is None or w.arsha or w.in_compound or (m.kind == "avyaya" and not m.vibhakti):
            return g
        pron = english.pronoun(m.lemma, m.linga, m.vacana, m.vibhakti,
                               demonstrative=w.role == "विशेषण", force_acc=i in self.acc)
        if pron is not None:
            return pron
        if m.krt and w.gloss_source != "own":
            return _krt(m.krt, g)
        if (w.role in ("विशेषण", "विधेय") or g[:1].isupper() or g in _NO_PLURAL or " of " in g
                or m.vacana not in ("बहुवचन", "द्विवचन")):
            return g
        return ("two " if m.vacana == "द्विवचन" else "") + english.plural(g)

    # ---- noun phrases --------------------------------------------------------------
    def np(self, i: int, kids: Optional[list[int]] = None) -> list[Piece]:
        if i in self.used:
            return []
        self.used.add(i)
        mem = self.members(i)
        poss: list[Piece] = []
        adjs: list[Piece] = []
        after: list[Piece] = []
        im = self.words[i].morph
        pron_head = im is not None and english.is_pronoun(im.lemma)
        participle = im is not None and im.krt in ("क्त", "क्तवतु")
        for k in (self.children.get(i, []) if kids is None else kids):
            r = self.role(k)
            km = self.words[k].morph
            if k in self.used:
                continue
            if r == "विशेषण" and pron_head:
                after += [_p(",", None, "")] + self.np(k)
                continue
            if r == "कर्ता" and participle:
                after += [_p("by")] + self.np(k)
                continue
            if r == "सम्बन्ध" and km is not None and english.is_pronoun(km.lemma):
                self.used.add(k)
                poss.append(_p(english.pronoun(km.lemma, km.linga, km.vacana, "षष्ठी") or self.text(k), k))
            elif r in ("विशेषण", "अव्यय"):
                adjs += self.np(k)
            else:
                after += self.case_phrase(k)
        core: list[Piece] = []
        for j in mem:
            self.used.add(j)
            core.append(_p(self.text(j), j, "-" if core else " "))
        core.append(_p(self.noun_text(i), i, "-" if core else " "))
        return poss + adjs + core + after

    def case_phrase(self, i: int) -> list[Piece]:
        r = self.role(i)
        prep = _PREP.get(r)
        if r == "अधिकरण" and self.words[i].morph and self.words[i].morph.vacana == "बहुवचन":
            prep = "among"
        head = [_p(prep)] if prep else []
        return head + self.np(i)

    def nonfinite(self, i: int, mode: str) -> list[Piece]:
        self.used.add(i)
        w = self.words[i]
        g = self.text(i)
        if w.morph is None or w.arsha:
            word = g
        elif mode == "to":
            word = "to " + g
        else:
            word = "having " + english.participle(g)
        return [_p(word, i)] + self.tail(i)

    def tail(self, v: int) -> list[Piece]:
        out: list[Piece] = []
        for k in self.children.get(v, []):
            r = self.role(k)
            if r == "अव्यय":
                out = self.np(k) + out
            elif r == "कर्म" or r == "विधेय":
                out += self.np(k)
            elif r == "तुमर्थ":
                out += self.nonfinite(k, "to")
            elif r == "पूर्वकालक्रिया":
                out = self.nonfinite(k, "having") + out
            else:
                out += self.case_phrase(k)
        return out

    # ---- verbs ---------------------------------------------------------------------
    def verb(self, v: int, neg: Optional[int]) -> tuple[list[Piece], bool]:
        """Pieces for the verb; True when it is a 'let' clause (subject goes after 'let')."""
        w = self.words[v]
        m = w.morph
        g = self.text(v)
        if m is None or w.arsha or m.kind != "tinanta":
            txt = g if (m is None or w.arsha or not m.krt) else _krt(m.krt, g)
            return ([_p(txt, v)] + ([_p("not", neg)] if neg is not None else [])), False
        p = {"उत्तमपुरुष": 1, "मध्यमपुरुष": 2}.get(m.purusha or "", 3)
        sg = m.vacana not in ("बहुवचन", "द्विवचन")
        sg3 = p == 3 and sg
        is_be = "am" if p == 1 and sg else "is" if sg3 else "are"
        was = "was" if sg and p != 2 else "were"
        passive = (m.prayoga or "") in _PASSIVE
        isbe = g in ("be", "is", "are", "am")
        g = "be" if isbe else g
        aux, main, plain, let = "", g, "", False
        lak = m.lakara or "लट्"
        if lak in _MODAL:
            aux = _MODAL[lak] + (" be" if passive and not isbe else "")
            main = english.participle(g) if passive and not isbe else g
            plain = f"{aux} {main}"
        elif lak == "लोट्" and p != 2:
            let, aux, plain = True, "", g
        elif lak in ("लोट्",):
            aux, plain = "do", g
        elif lak in _PAST:
            aux = "did" if not passive else was
            main = english.participle(g) if passive else g
            plain = f"{was} {main}" if passive and not isbe else (was if isbe else english.past(g))
        else:
            aux = ("does" if sg3 else "do") if not passive else is_be
            main = english.participle(g) if passive else g
            plain = f"{is_be} {main}" if passive and not isbe else (is_be if isbe else
                                                                  english.third_singular(g) if sg3 else g)
        if isbe and not passive and lak not in _MODAL:
            piece = _p(plain.split()[0] if plain else is_be, v)
            if lak == "लोट्":
                return ([_p("not", neg)] if neg is not None else []) + [_p("be", v)], let
            return [piece] + ([_p("not", neg)] if neg is not None else []), False
        if neg is None:
            return [_p(plain, v)], let
        out = [_p(aux)] if aux and not let else []
        out.append(_p("not", neg))
        out.append(_p(main, v))
        return out, let

    def clause(self, v: int) -> list[Piece]:
        self.used.add(v)
        m = self.words[v].morph
        passive = m is not None and (m.prayoga or "") in _PASSIVE
        voc: list[Piece] = []
        conn: list[Piece] = []
        adv: list[Piece] = []
        subj: list[int] = []
        agent: list[int] = []
        objs: list[int] = []
        rest: list[int] = []
        neg: Optional[int] = None
        for k in self.children.get(v, []):
            r = self.role(k)
            if r == "सम्बोधन":
                voc += [_p("O")] + self.np(k) + [_p(",", None, "")]
            elif r == "अव्यय":
                g = self.text(k)
                if g in _NEGATIONS and neg is None:
                    neg = k
                    self.used.add(k)
                elif g in _CONNECTIVES:
                    self.used.add(k)
                    conn.append(_p(g, k))
                else:
                    self.used.add(k)
                    adv.append(_p(g, k))
            elif r == "कर्ता":
                km = self.words[k].morph
                (agent if passive and km and km.vibhakti == "तृतीया" else subj).append(k)
            elif r in ("कर्म", "विधेय"):
                objs.append(k)
            else:
                rest.append(k)
        if passive and not subj:
            subj, objs = objs, []
        vpieces, let = self.verb(v, neg)
        if neg is not None and neg not in self.used:
            self.used.add(neg)
        spieces: list[Piece] = []
        if let:
            for k in subj:
                self.acc.add(k)
        for k in subj:
            spieces += self.np(k)
        if not subj and m is not None and not (m.lakara == "लोट्" and m.purusha == "मध्यमपुरुष"):
            if m.kind == "tinanta":
                spieces = [_p(english.supplied_subject(m.purusha, m.vacana, accusative=let))]
        prior = [k for k in rest if self.role(k) == "पूर्वकालक्रिया"]
        pre: list[Piece] = []
        for k in prior:
            pre += self.nonfinite(k, "having")
        post: list[Piece] = []
        for k in objs:
            post += self.np(k)
        for k in agent:
            post += [_p("by")] + self.np(k)
        for k in rest:
            if k in prior:
                continue
            post += self.nonfinite(k, "to") if self.role(k) == "तुमर्थ" else self.case_phrase(k)
        head = [_p("let")] + spieces + adv + pre + vpieces if let else spieces + adv + pre + vpieces
        return voc + conn + head + post


def _compose(pieces: list[Piece]) -> tuple[str, list[Alignment]]:
    out = ""
    spans: dict[int, Alignment] = {}
    for text, idx, sep in pieces:
        text = " ".join(text.split()) if text else ""
        if not text or (idx is not None and idx in spans):
            continue
        if out:
            out += sep
        start = len(out)
        out += text
        if idx is not None and idx not in spans:
            spans[idx] = Alignment(idx, start, len(out))
    return out, sorted(spans.values(), key=lambda a: a.start)


def _copular(r: "_Renderer", top) -> list[Piece]:
    """A verbless sentence: subject, supplied copula, predicates (X च Y -> 'X, and Y')."""
    n = len(r.words)
    for ch in r.children.values():
        ch.sort(key=lambda k: r.pos[k])
    roots = [i for i in r.order if top(i) and not r.words[i].in_compound
             and (r.words[i].head is None or not 0 <= r.words[i].head < n)]
    subj = [i for i in roots if r.role(i) == "कर्ता"] or [i for i in roots if r.role(i) not in ("विधेय", "सम्बोधन")][:1]
    pred = [i for i in roots if r.role(i) == "विधेय"]
    out: list[Piece] = []
    for i in roots:
        if r.role(i) == "सम्बोधन":
            out += [_p("O")] + r.np(i) + [_p(",", None, "")]
    mods = ("विशेषण", "सम्बन्ध")
    for s in subj:
        kids = r.children.get(s, [])
        pred += [k for k in kids if r.role(k) == "विधेय"]
        out += r.np(s, [k for k in kids if r.role(k) in mods])
        for k in kids:
            if r.role(k) in mods or r.role(k) == "विधेय":
                continue
            sm_ = r.words[s].morph
            if r.role(k) == "कर्ता" and sm_ is not None and sm_.krt in ("क्त", "क्तवतु"):
                out += [_p("by")] + r.np(k)
            else:
                out += r.case_phrase(k) if r.role(k) in _PREP else r.np(k)
    sm = r.words[subj[0]].morph if subj else None
    if pred:
        pl = bool(sm and sm.vacana in ("बहुवचन", "द्विवचन"))
        out.append(_p("[are]" if pl or (sm and sm.purusha == "मध्यमपुरुष") else "[am]"
                      if sm and sm.lemma == "अस्मद्" else "[is]"))
    pred.sort(key=lambda k: r.pos[k])
    prev_pron = True
    for n_, k in enumerate(pred):
        pm = r.words[k].morph
        piece = r.np(k)
        has_conn = any(r.role(c) == "अव्यय" and r.text(c) in _CONNECTIVES for c in r.children.get(k, []))
        if piece and n_ and (has_conn or not prev_pron):
            piece[0] = (piece[0][0], piece[0][1], ", ")
            if piece[0][1] is None:
                piece[0] = (piece[0][0], None, ", ")
        out += piece
        prev_pron = bool(pm and english.is_pronoun(pm.lemma))
    for i in roots:
        if i not in subj and i not in pred and r.role(i) != "सम्बोधन":
            out += r.case_phrase(i) if r.role(i) in _PREP else r.np(i)
    return out


def render(reading: Reading) -> Reading:
    """A copy of ``reading`` with ``translation`` and ``alignment`` filled in."""
    if not reading.words:
        return replace(reading, translation="", alignment=[])
    r = _Renderer(reading)
    verbs = [i for i in r.order if r.role(i) == "क्रिया" and not r.words[i].in_compound]
    pieces: list[Piece] = []

    def top(i: int) -> bool:
        w = r.words[i]
        return not w.in_compound and r.role(i) not in ("विशेषण", "सम्बन्ध", "समासपूर्वपद")

    if verbs:
        first = verbs[0]
        for i in r.order:  # orphans attach to the first verb
            w = r.words[i]
            unattached = w.head is None or not 0 <= w.head < len(r.words)
            if top(i) and i not in verbs and unattached and r.role(i) not in ("", "पूर्वकालक्रिया"):
                r.children.setdefault(first, []).append(i)
        for ch in r.children.values():
            ch.sort(key=lambda k: r.pos[k])
        clauses = [r.clause(v) for v in verbs]
        order = sorted(range(len(verbs)), key=lambda n: r.pos[verbs[n]])
        for n, ci in enumerate(order):
            pieces += ([_p(";", None, "")] if n else []) + clauses[ci]
    else:
        pieces += _copular(r, top)
    for i in r.order:  # anything not yet consumed still appears, in prose order
        w = r.words[i]
        if i not in r.used and not w.in_compound:
            pieces += r.case_phrase(i) if r.role(i) in _PREP else r.np(i)
    for i in r.order:
        w = r.words[i]
        if w.in_compound and i not in r.used:
            r.used.add(i)
            pieces.append(_p(r.text(i), i))
    text, alignment = _compose(pieces)
    if text:
        k = next((n for n, ch in enumerate(text) if ch.isalpha()), 0)
        text = text[:k] + text[k].upper() + text[k + 1:]
        text += "" if text.endswith((".", "?", "!")) else "."
    return replace(reading, translation=text, alignment=alignment)
