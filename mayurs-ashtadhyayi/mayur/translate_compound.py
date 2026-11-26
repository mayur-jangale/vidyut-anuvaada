"""Compound rendering by type for the template renderer (a mixin of ``translate_core._Renderer``)."""

from __future__ import annotations

from . import english
from .translate_words import ADJ_ENDINGS, ADJ_FIRST, NOMINAL_SUFFIXES

Piece = tuple[str, "int | None", str]


def _p(text: str, idx=None, sep: str = " ") -> Piece:
    return (text, idx, sep)


class CompoundMixin:
    def samasa(self, i: int) -> str:
        for c in self.reading.compounds:
            if c.members and c.members[-1] == i:
                return c.samasa
        return ""

    def nominal(self, i: int) -> bool:
        w = self.words[i]
        return bool(w.morph and w.morph.kind == "subanta" and not w.morph.krt and w.role not in ("विशेषण", "विधेय")
                    and not english.is_pronoun(w.morph.lemma))

    def compound_pieces(self, i: int, mem: list[int], ctype: str, inner=None) -> list[Piece]:
        """A compound read off its type: determinative 'Y of X', descriptive 'X Y' (adjective first),
        copulative 'X, Y and Z'. Empty when the type does not fit, so the hyphen form stays."""
        texts = [(j, self.text(j)) for j in mem]
        last = self.noun_text(i)
        if last in NOMINAL_SUFFIXES and len(mem) == 1:  # तद्धित -ता / -त्व: "hero" + "ness"
            self.used.update(mem)
            base = texts[0][1]
            if last == "ness" and base.endswith("y"):
                base = base[:-1] + "i"
            return [_p(base, mem[0]), _p(last, i, "")]
        if ctype == "द्वन्द्व":
            out = [_p(t, j, ", " if n else " ") for n, (j, t) in enumerate(texts)]
            self.used.update(mem)
            return out + [_p(last, i, " and ")]
        first = texts[0][1]
        if ctype == "कर्मधारय":
            if len(mem) == 1 and (first in ADJ_FIRST or first.endswith(ADJ_ENDINGS)) and not first[:1].isupper():
                self.used.update(mem)
                return [_p(first, mem[0]), _p(last, i)]
            return []
        if any(t[:1].isupper() and " " in t for _, t in texts):
            return []
        self.used.update(mem)
        return [_p(last, i), _p("of")] + [_p(t, j, "-" if n else " ") for n, (j, t) in enumerate(texts)]
