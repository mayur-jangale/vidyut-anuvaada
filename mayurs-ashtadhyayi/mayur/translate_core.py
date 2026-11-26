"""Noun-phrase and clause rendering (the renderer behind ``mayur.translate``)."""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from . import english, lipi
from .translate_clause import ClauseMixin
from .translate_compound import CompoundMixin
from .translate_words import ADJ_FIRST as _ADJ_FIRST, ADJ_SENSE, WITH_LEMMAS, FINAL as _FINAL, PAIRED as _PAIRED, WITH_WORDS, is_latin_binomial, is_motion, is_question_lemma, name_plural
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
def _p(text: str, idx: Optional[int] = None, sep: str = " ") -> Piece:
    return (text, idx, sep)


class _Renderer(CompoundMixin, ClauseMixin):
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
        if w.role == "विधेय" and w.gloss in ADJ_SENSE:
            return ADJ_SENSE[w.gloss]
        if w.gloss and not is_latin_binomial(w.gloss):
            return w.gloss
        return lipi.iast(w.morph.stem or w.morph.lemma) or "⟨" + lipi.iast(w.form) + "⟩"

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

    def final_pattern(self, i: int):
        m = self.words[i].morph
        if m is None or not self.members(i):
            return None
        return _FINAL.get(m.stem) or _FINAL.get(m.lemma) or _FINAL.get(m.lemma.rstrip("म्"))

    def noun_text(self, i: int) -> str:
        w = self.words[i]
        m = w.morph
        g = self.text(i)
        if m is None or w.arsha or w.in_compound or (m.kind == "avyaya" and not m.vibhakti):
            return g
        pron = english.pronoun(m.lemma, m.linga, m.vacana, m.vibhakti,
                               demonstrative=w.role == "विशेषण", force_acc=i in self.acc)
        if pron is not None:
            return "what" if m.lemma in ("किम्", "क") and w.form == "किम्" and i not in self.acc else pron
        if m.krt and w.gloss_source != "own":
            if m.krt in ("तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्") and self.members(i):
                return g  # a noun that merely ends like a gerundive, inside a compound
            g = english.krt_form(m.krt, g)
            if m.krt not in _AGENT_KRT:
                return g
        if g[:1].isupper() and m.vacana == "बहुवचन" and " " not in g:
            return name_plural(g)
        if (w.role in ("विशेषण", "विधेय") or g[:1].isupper() or g in _NO_PLURAL or " of " in g
                or m.vacana not in ("बहुवचन", "द्विवचन") or (g.endswith("s") and not g.endswith("ss"))):
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
        kidlist = self.children.get(i, []) if kids is None else kids
        quals = [k for k in kidlist if self.role(k) == "विशेषण" and k not in self.used]
        appose = len(quals) > 2 and not pron_head
        for k in kidlist:
            r = self.role(k)
            km = self.words[k].morph
            if k in self.used:
                continue
            if r == "विशेषण" and appose:
                after += [_p(",", None, "")] + self.np(k)
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
            if r == "विशेषण" and self.words[k].gloss[:1].isupper() and any(
                    self.role(c) == "अव्यय" and self.text(c) == "and" for c in self.children.get(k, [])):
                after += self.np(k)  # "X and Y": a coordinated name follows its partner
                continue
            if r == "अव्यय" and km is not None and km.lemma == "एव":
                self.used.add(k)
                after.append(_p("indeed", k))
                continue
            if im is not None and im.lemma in WITH_LEMMAS and r in ("सम्बन्ध", "करण", "कर्म"):
                std += self.np(k)  # "with Sītā": the dependent of सह / विना takes no preposition of its own
                continue
            if im is not None and im.lemma in _LIKE and r in ("करण", "सम्बन्ध", "सम्प्रदान", "कर्म"):
                if self.members(i):
                    std += [_p("in")] + self.np(k)
                else:
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
        pat = self.final_pattern(i)
        if pat is not None:
            head_text, joiner, plur = pat
            core.append(_p(head_text, i))
            for n_, j in enumerate(mem):
                self.used.add(j)
                t = self.text(j)
                if plur and n_ == len(mem) - 1 and not t[:1].isupper():
                    t = english.plural(t)
                core.append(_p(t, j, " " if n_ == 0 else joiner if joiner != "-" else "-"))
            return poss + adjs + core + std + after
        bv = self.bahuvrihi(i)
        if bv and mem and self.words[mem[0]].morph and self.words[mem[0]].morph.lemma in ("स", "सह") \
                and self.text(mem[0]) == "with":
            self.used.add(mem[0])  # "together with X": the first member is a preposition
            core.append(_p("with", mem[0]))
            for j in mem[1:]:
                self.used.add(j)
                core.append(_p(self.text(j), j))
            core.append(_p(self.noun_text(i), i))
            return poss + adjs + core + std + after
        ctype = self.samasa(i)
        if mem and not bv and ctype in ("तत्पुरुष", "कर्मधारय", "द्वन्द्व") and self.nominal(i):
            made = self.compound_pieces(i, mem, ctype)
            if made:
                return poss + adjs + made + std + after
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
        if lead < len(body) and body[lead][1] is not None and self.role(body[lead][1]) == "अव्यय" \
                and body[lead][0] in WITH_WORDS:
            head = []  # सह / विना are the preposition: "with Sītā", never "by with Sītā"
        return body[:lead] + head + body[lead:]  # "and" goes before the whole phrase
