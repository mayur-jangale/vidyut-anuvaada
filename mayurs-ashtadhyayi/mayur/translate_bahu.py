"""बहुव्रीहि qualifiers and नञ्-adjectives for the template renderer (a mixin of ``translate_core._Renderer``).

A बहुव्रीहि names what its owner has, so it is read off its type (``Compound.samasa``) and the class of its
members, and set after the noun it qualifies:

* स-/सह- + noun (सपुत्र)                      "king with son"
* क्त participle + noun (जितेन्द्रिय)         ", [his] sense conquered,"; with a noun before the participle
  (शोकसंविग्नमानस)                            ", [his] mind agitated by grief,"
* adjective + noun (महाबल)                    "Bhīma of great strength"; with a body part "great-armed" before
* noun + body part (शस्त्रपाणि, पद्मनेत्र)       ", with weapon in hand," / ", lotus-eyed,"

The supplied possessive ("[his]") is the owner's: the noun qualified. A compound that fits none of these keeps
its hyphen form (the caller falls through): nothing is guessed."""

from __future__ import annotations

from typing import Optional

from . import english
from .translate_words import ADJ_ENDINGS, ADJ_FIRST, HELD_PARTS, PARTS_ED, POSSESSIVES

Piece = tuple[str, Optional[int], str]
_BAHUVRIHI = ("बहुव्रीहि", "bahuvrihi")
_SA = ("स", "सह")
_OWNER = {"पुंलिङ्ग": "his", "स्त्रीलिङ्ग": "her", "नपुंसकलिङ्ग": "its"}
_PLURAL = ("बहुवचन", "द्विवचन")


def _p(text: str, idx: Optional[int] = None, sep: str = " ") -> Piece:
    return (text, idx, sep)


def _comma() -> Piece:
    return _p(",", None, "")


class BahuvrihiMixin:
    def bahu_compound(self, k: int):
        """The बहुव्रीहि whose final word is ``k`` (a word of its own, not a member), or None."""
        if self.words[k].in_compound:
            return None
        return next((c for c in self.reading.compounds
                     if c.samasa in _BAHUVRIHI and len(c.members) > 1 and c.members[-1] == k), None)

    def owner_pronoun(self, h: int) -> str:
        """The possessive of the noun ``h`` that owns what a बहुव्रीहि names ("his", "their", "my"), else ''."""
        m = self.words[h].morph
        if m is None or m.kind != "subanta":
            return ""
        if english.is_pronoun(m.lemma):
            pron = english.pronoun(m.lemma, m.linga, m.vacana, "षष्ठी")
            return pron if pron in POSSESSIVES else ""
        return "their" if m.vacana in _PLURAL else _OWNER.get(m.linga or "", "")

    def plain_noun(self, j: int) -> bool:
        """A member that is an ordinary noun: a stem with a gloss, no suffix, not a prefix, not an adjective."""
        w = self.words[j]
        m = w.morph
        g = (w.gloss or "").lower()
        return bool(m and m.kind in ("stem", "subanta") and not m.krt and g and m.lemma not in _SA
                    and g not in ADJ_FIRST and not g.endswith(ADJ_ENDINGS) and not w.gloss[:1].isupper())

    def adjective_member(self, j: int) -> bool:
        w = self.words[j]
        m = w.morph
        g = (w.gloss or "").lower()
        return bool(m and m.kind in ("stem", "subanta") and not m.krt and not w.gloss[:1].isupper()
                    and (g in ADJ_FIRST or g.endswith(ADJ_ENDINGS)))

    def bahu_qualifier(self, k: int, head: int) -> Optional[tuple[str, list[Piece]]]:
        """('adj' | 'after', pieces) for a बहुव्रीहि ``k`` qualifying ``head``, or None to keep the hyphen form."""
        comp = self.bahu_compound(k)
        if comp is None or not self.words[k].gloss or self.role(k) != "विशेषण":
            return None
        mem = list(comp.members)
        for rule in (self.bahu_sa, self.bahu_participle, self.bahu_body, self.bahu_adjective):
            made = rule(mem, head)
            if made is not None:
                self.used.update(mem)
                return made
        return None

    def bahu_sa(self, mem: list[int], head: int):
        """स-/सह- + noun: "with X" straight after the noun."""
        first = self.words[mem[0]].morph
        if len(mem) != 2 or first is None or first.lemma not in _SA or self.text(mem[0]) != "with":
            return None
        return "after", [_p("with", mem[0]), _p(self.noun_text(mem[1]), mem[1])]

    def bahu_participle(self, mem: list[int], head: int):
        """[noun] + क्त participle + noun: "[his] N P-ed (by X)"."""
        if len(mem) not in (2, 3):
            return None
        part = self.words[mem[-2]]
        owner = self.owner_pronoun(head)
        if not owner or part.morph is None or part.morph.krt != "क्त" or part.morph.kind not in ("stem", "subanta") \
                or not part.gloss:
            return None
        out = [_comma(), _p(f"[{owner}]"), _p(self.noun_text(mem[-1]), mem[-1]),
               _p(english.krt_form("क्त", self.text(mem[-2])), mem[-2])]
        if len(mem) == 3:
            if not self.plain_noun(mem[0]):
                return None
            out += [_p("by"), _p(self.text(mem[0]), mem[0])]
        return "after", out + [_comma()]

    def bahu_body(self, mem: list[int], head: int):
        """noun + part of the body: "with X in hand" for the hand, "X-eyed" for the others."""
        part = (self.words[mem[-1]].gloss or "").lower()
        if len(mem) != 2 or not self.plain_noun(mem[0]) or not (part in HELD_PARTS or part in PARTS_ED):
            return None
        x = _p(self.text(mem[0]), mem[0])
        if part in HELD_PARTS:
            return "after", [_comma(), _p("with"), x, _p("in"), _p(self.text(mem[1]), mem[1]), _comma()]
        return "after", [_comma(), x, _p(english.past(self.text(mem[1])), mem[1], "-"), _comma()]

    def bahu_adjective(self, mem: list[int], head: int):
        """adjective + noun: "A-N-ed" before the noun for a paired body part, else "of A N" after it."""
        if len(mem) != 2 or not self.adjective_member(mem[0]) or (self.words[mem[1]].gloss or "").endswith("ing"):
            return None  # "terrible-seeing" is not "having terrible seeing"
        a, n = _p(self.text(mem[0]), mem[0]), self.noun_text(mem[1])
        if n in PARTS_ED:
            return "adj", [a, _p(english.past(n), mem[1], "-")]
        return "after", [_p("of"), a, _p(n, mem[1])]

    # ---- नञ्-adjectives ---------------------------------------------------------------
    def is_without(self, k: int) -> bool:
        """A qualifier whose gloss is "without X" (अशस्त्र) with nothing hanging on it."""
        w = self.words[k]
        return (self.role(k) == "विशेषण" and not w.in_compound and (w.gloss or "").lower().startswith("without ")
                and not self.heavy(k) and not self.members(k))

    def without_group(self, ks: list[int], set_off: bool) -> list[Piece]:
        """"without X" and "without Y" after the noun; commas around the group after a name or pronoun."""
        out: list[Piece] = [_comma()] if set_off else []
        for n, k in enumerate(ks):
            if n:
                out += [_comma()] if n < len(ks) - 1 else [_p("and")]
            out += self.np(k)
        return out + ([_comma()] if set_off else [])
