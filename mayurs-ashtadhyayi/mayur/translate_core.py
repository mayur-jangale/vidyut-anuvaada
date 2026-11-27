"""Noun-phrase and clause rendering (the renderer behind ``mayur.translate``)."""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from . import english, lipi
from .translate_bahu import BahuvrihiMixin
from .translate_clause import ClauseMixin
from .translate_compound import CompoundMixin
from .translate_join import JoinMixin
from .translate_np import NounPhraseMixin
from .translate_sense import SenseMixin
from .translate_words import ADJ_FIRST as _ADJ_FIRST, ADJ_SENSE, ON_NOUNS, WITH_LEMMAS, FINAL as _FINAL, PAIRED as _PAIRED, WITH_WORDS, is_latin_binomial, is_motion, is_question_lemma, name_plural
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


class _Renderer(NounPhraseMixin, BahuvrihiMixin, CompoundMixin, JoinMixin, ClauseMixin, SenseMixin):
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
        if w.morph is None or (w.arsha and not w.gloss):  # a labelled ārṣa form has its analysis and gloss
            return "⟨" + lipi.iast(w.form) + "⟩"
        if w.role == "विशेषण" and w.morph.lemma == "पर":
            return "supreme"
        if w.role == "विधेय" and w.gloss in ADJ_SENSE:
            return ADJ_SENSE[w.gloss]
        sense = self.context_sense(i)
        if sense:
            return sense
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
        if m is None or (w.arsha and not w.gloss) or w.in_compound or (m.kind == "avyaya" and not m.vibhakti):
            return g
        pron = english.pronoun(m.lemma, m.linga, m.vacana, m.vibhakti,
                               demonstrative=w.role == "विशेषण", force_acc=i in self.acc)
        if pron is not None:
            return "what" if m.lemma in ("किम्", "क") and w.form == "किम्" and i not in self.acc else pron
        noun = self.krt_noun(i)
        if noun:
            return noun if m.vacana not in ("बहुवचन", "द्विवचन") or noun[:1].isupper() else english.plural(noun)
        if self.possessed_noun(i):
            return g
        lexical_adj = m.krt in ("तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्") and g.endswith(("ful", "ous", "ble", "ive"))
        if m.krt and w.gloss_source != "own" and not lexical_adj:  # रम्य "delightful", not "to be delighted"
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

    def case_phrase(self, i: int) -> list[Piece]:
        r = self.role(i)
        prep = _PREP.get(r)
        if r == "अधिकरण" and self.words[i].morph and self.words[i].morph.vacana == "बहुवचन":
            prep = "among"
        elif r == "अधिकरण" and self.text(i).lower().split()[-1:] and self.text(i).lower().split()[-1] in ON_NOUNS:
            prep = "on"
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
