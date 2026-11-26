"""Noun-phrase and clause rendering (the renderer behind ``mayur.translate``)."""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from . import english, lipi
from .model import Alignment, Reading

Piece = tuple[str, Optional[int], str]  # (text, word index or None, separator before it)

_PREP = {"करण": "by", "सम्प्रदान": "to", "अपादान": "from", "अधिकरण": "in", "सम्बन्ध": "of"}
_CONNECTIVES = {"and", "but", "or", "then", "now", "thus", "if", "when", "so", "as"}
_NEGATIONS = {"not", "no"}
_NO_PLURAL = {"all", "this", "that", "other", "much", "many", "one", "who", "which"}
_MODAL = {"लृट्": "will", "लुट्": "will", "विधिलिङ्": "should", "आशीर्लिङ्": "may", "लृङ्": "would",
          "लेट्": "shall"}
_PAST = {"लिट्", "लङ्", "लुङ्"}
_PASSIVE = {"कर्मणि", "भावे"}
_LIKE = {"सदृश", "सम", "तुल्य"}  # take their standard in the instrumental/genitive: "like X", "equal to X"
_TO = {"सम", "तुल्य"}
_AGENT_KRT = {"तृच्", "तृन्", "तृ"}
_ADJ_FIRST = {"great", "good", "firm", "long", "big", "small", "excellent", "best", "white", "black",
              "red", "very", "many", "beautiful", "noble", "mighty", "strong", "high", "broad", "large"}
_PAIRED = {"arm", "eye", "hand", "shoulder", "ear", "foot", "tooth", "leg", "thigh", "cheek"}


def _p(text: str, idx: Optional[int] = None, sep: str = " ") -> Piece:
    return (text, idx, sep)


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
        if w.role == "विशेषण" and w.morph.lemma == "पर":
            return "supreme"
        return w.gloss or lipi.iast(w.morph.stem or w.morph.lemma) or "⟨" + lipi.iast(w.form) + "⟩"

    def members(self, i: int) -> list[int]:
        if self.words[i].in_compound:
            return []
        for c in self.reading.compounds:
            if c.members and c.members[-1] == i:
                return list(c.members[:-1])
        return []

    def bahuvrihi(self, i: int) -> bool:
        """True for the final member of a bahuvrihi whose first member is an adjective or prefix."""
        if self.words[i].in_compound:
            return False
        for c in self.reading.compounds:
            if c.samasa in ("बहुव्रीहि", "bahuvrihi") and len(c.members) > 1 and c.members[-1] == i:
                f = self.words[c.members[0]]
                return bool(f.morph and (f.morph.kind == "avyaya" or f.gloss in _ADJ_FIRST))
        return False

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
            if m.krt in ("तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्") and self.members(i):
                return g  # a noun that merely ends like a gerundive, inside a compound
            g = english.krt_form(m.krt, g)
            if m.krt not in _AGENT_KRT:
                return g
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
        std: list[Piece] = []
        for k in (self.children.get(i, []) if kids is None else kids):
            r = self.role(k)
            km = self.words[k].morph
            if k in self.used:
                continue
            if r == "विशेषण" and pron_head:
                after += [_p(",", None, "")] + self.np(k)
                continue
            if km is not None and km.lemma == "नाम" and r == "अव्यय":
                self.used.add(k)
                after.append(_p("by name", k))
                continue
            if r == "विशेषण" and self.bahuvrihi(k):
                after += self.np(k)
                continue
            if im is not None and im.lemma in _LIKE and r in ("करण", "सम्बन्ध", "सम्प्रदान", "कर्म"):
                std += ([_p("to")] if im.lemma in _TO else []) + self.np(k)
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
        bv = self.bahuvrihi(i)
        glue = " " if bv else "-"
        ed = bv and self.noun_text(i) in _PAIRED
        if bv and not ed:
            core.append(_p("of"))
        for j in mem:
            self.used.add(j)
            core.append(_p(self.text(j), j, glue if core and not (bv and len(core) == 1) else " "))
        last = self.noun_text(i)
        if ed:
            last = english.past(last)
            glue = "-"
        if ed and len(core) == 0:
            pass
        core.append(_p(last, i, glue if core and not (bv and not ed and len(core) == 1) else " "))
        return poss + adjs + core + std + after

    def case_phrase(self, i: int) -> list[Piece]:
        r = self.role(i)
        prep = _PREP.get(r)
        if r == "अधिकरण" and self.words[i].morph and self.words[i].morph.vacana == "बहुवचन":
            prep = "among"
        head = [_p(prep)] if prep else []
        body = self.np(i)
        lead = 0
        while lead < len(body) and body[lead][1] is not None and self.role(body[lead][1]) == "अव्यय" \
                and body[lead][0] in _CONNECTIVES:
            lead += 1
        return body[:lead] + head + body[lead:]  # "and" goes before the whole phrase

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
            txt = g if (m is None or w.arsha or not m.krt) else english.krt_form(m.krt, g)
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

    def clause(self, v: int, keep_conn: bool = True) -> list[Piece]:
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
                    if keep_conn:  # a clause-initial 'and' of the first clause would dangle
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
            preds = [c for c in self.children.get(k, []) if self.role(c) == "विधेय" and c not in self.used]
            spieces += self.np(k, [c for c in self.children.get(k, []) if c not in preds])
            for c in preds:
                objs.append(c)
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


