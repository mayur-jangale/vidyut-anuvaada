"""Noun phrases for the template renderer (a mixin of ``translate_core._Renderer``).

A phrase is: possessive pronoun, demonstrative, adjectives, a title noun (before a name), the head,
then what trails: a one-word name in apposition, genitives, case phrases, and a participle (or any
qualifier) that has dependents of its own, set off by commas ("that king Daśaratha, bound by the noose of
dharma, ...")."""

from __future__ import annotations

from typing import Optional

from . import english
from .translate_words import FINAL as _FINAL, PERSON_NOUNS, TITLE_NOUNS, WITH_LEMMAS

Piece = tuple[str, Optional[int], str]
_PAIRED = {"arm", "eye", "hand", "shoulder", "ear", "foot", "tooth", "leg", "thigh", "cheek"}
_LIKE = {"सदृश", "सम", "तुल्य"}
_TO = {"सम", "तुल्य"}


def _p(text: str, idx: Optional[int] = None, sep: str = " ") -> Piece:
    return (text, idx, sep)


def possessive(pieces: list[Piece]) -> list[Piece]:
    """The same pieces with 's on the last one: [Daśaratha] -> [Daśaratha's]."""
    if not pieces:
        return pieces
    t, idx, sep = pieces[-1]
    return pieces[:-1] + [(t + ("'" if t.endswith("s") else "'s"), idx, sep)]


class NounPhraseMixin:
    def is_person(self, k: int) -> bool:
        w = self.words[k]
        g = (w.gloss or "").lower()
        return bool(w.gloss) and (w.gloss[:1].isupper() or g in PERSON_NOUNS) and not w.in_compound

    def heavy(self, k: int) -> bool:
        """A qualifier with dependents of its own (an object, an instrument, a genitive...)."""
        return any(self.role(c) not in ("विशेषण", "अव्यय") and c not in self.used for c in self.children.get(k, []))

    def qual_slot(self, k: int, head_name: bool) -> str:
        km = self.words[k].morph
        g = (self.words[k].gloss or "").lower()
        if self.heavy(k):
            return "trail"
        if km is not None and english.is_pronoun(km.lemma):
            return "dem"
        if head_name and g in TITLE_NOUNS and not (km and km.krt):
            return "title"
        return "adj"

    def np(self, i: int, kids: Optional[list[int]] = None) -> list[Piece]:
        if i in self.used:
            return []
        self.used.add(i)
        mem = self.members(i)
        poss: list[Piece] = []
        dems: list[Piece] = []
        adjs: list[Piece] = []
        titles: list[Piece] = []
        after: list[Piece] = []
        trail: list[Piece] = []
        im = self.words[i].morph
        pron_head = im is not None and english.is_pronoun(im.lemma)
        head_name = self.words[i].gloss[:1].isupper() and not mem
        participle = im is not None and im.krt in ("क्त", "क्तवतु")
        std: list[Piece] = []
        kidlist = self.children.get(i, []) if kids is None else kids
        quals = [k for k in kidlist if self.role(k) == "विशेषण" and k not in self.used]
        plain = [k for k in quals if self.qual_slot(k, head_name) == "adj"]
        appose = len(plain) > 2 and head_name and not pron_head
        inner: list[Piece] = []
        for k in kidlist:
            r = self.role(k)
            km = self.words[k].morph
            if k in self.used:
                continue
            if r == "विशेषण" and (appose or pron_head):
                after += [_p(",", None, "")] + self.np(k)
                continue
            if km is not None and km.lemma == "नाम" and r == "अव्यय":
                self.used.add(k)
                after.append(_p("by name", k))
                continue
            if r == "विशेषण" and self.bahuvrihi(k):
                after += self.np(k)
                continue
            if r == "विशेषण" and self.words[k].gloss[:1].isupper() and not head_name and not self.heavy(k) \
                    and not self.members(k):
                after += self.np(k)  # a name in apposition follows a common noun: "king Daśaratha"
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
            elif r == "सम्बन्ध" and self.is_person(k) and not self.heavy(k) and not self.children.get(k):
                if mem and self.samasa(i) == "तत्पुरुष" and len(mem) == 1:
                    inner += possessive(self.np(k))  # "command of father's word"
                else:
                    poss += possessive(self.np(k))  # "Rāma's wife"
            elif r == "विशेषण":
                slot = self.qual_slot(k, head_name)
                piece = self.np(k)
                if slot == "trail":
                    trail += [_p(",", None, "")] + piece + [_p(",", None, "")]
                elif slot == "dem":
                    dems += piece
                elif slot == "title":
                    titles += piece
                else:
                    adjs += piece
            elif r == "अव्यय":
                adjs += self.np(k)
            else:
                after += self.case_phrase(k)
        after = after + trail
        front = poss + dems + adjs + titles
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
            return front + core + std + after
        bv = self.bahuvrihi(i)
        if bv and mem and self.words[mem[0]].morph and self.words[mem[0]].morph.lemma in ("स", "सह") \
                and self.text(mem[0]) == "with":
            self.used.add(mem[0])  # "together with X": the first member is a preposition
            core.append(_p("with", mem[0]))
            for j in mem[1:]:
                self.used.add(j)
                core.append(_p(self.text(j), j))
            core.append(_p(self.noun_text(i), i))
            return front + core + std + after
        ctype = self.samasa(i)
        if mem and not bv and ctype in ("तत्पुरुष", "कर्मधारय", "द्वन्द्व", "तद्धित") and self.nominal(i):
            made = self.compound_pieces(i, mem, ctype, inner)
            if made:
                return front + made + std + after
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
        core.append(_p(last, i, glue if core and not (bv and not ed and len(core) == 1) else " "))
        return inner + front + core + std + after
