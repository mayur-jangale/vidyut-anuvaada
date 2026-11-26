"""Compound rendering by type for the template renderer (a mixin of ``translate_core._Renderer``).

Three or more members follow the bracketing named in ``Compound.basis`` ("[सर्व-भूत]-हित"; without it the
members are grouped from the left). A determinative group reads "Y of X", a copulative group "X, Y and Z"."""

from __future__ import annotations

import re

from . import english
from .translate_words import ADJ_ENDINGS, ADJ_FIRST, NOMINAL_SUFFIXES

Piece = tuple[str, "int | None", str]
_BRACKETING = re.compile(r"bracketing ([^;]*)")


def _p(text: str, idx=None, sep: str = " ") -> Piece:
    return (text, idx, sep)


def _fold(items: list) -> object:
    """[a, b, c] -> (a b) c, grouped from the left."""
    node = items[0]
    for x in items[1:]:
        node = ("det", node, x)
    return node


def parse_bracketing(text: str, count: int):
    """'[पुत्र-पौत्र]-समन्वित (inner द्वन्द्व)' -> nested tuples of member numbers 0..count-1, or None."""
    dv = "द्वन्द्व" in text
    src = text.split("(")[0].strip()
    pos, leaf = 0, [0]

    def seq() -> list:
        nonlocal pos
        items = []
        while pos < len(src) and src[pos] != "]":
            if src[pos] == "[":
                pos += 1
                group = seq()
                pos += 1  # the closing bracket
                items.append(("dv", group) if dv and not any(isinstance(x, tuple) for x in items) and not items
                             and all(isinstance(g, int) for g in group) else _fold(group))
            elif src[pos] == "-":
                pos += 1
            else:
                while pos < len(src) and src[pos] not in "-[]":
                    pos += 1
                items.append(leaf[0])
                leaf[0] += 1
        return items

    try:
        items = seq()
    except IndexError:
        return None
    return _fold(items) if items and leaf[0] == count else None


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

    def tree(self, i: int, members: list[int]):
        """Nested grouping of ``members`` (the compound's members, with or without its final word)."""
        comp = next((c for c in self.reading.compounds if c.members and c.members[-1] == i), None)
        full = list(comp.members) if comp else members
        node = None
        found = _BRACKETING.search(comp.basis) if comp else None
        if found:
            node = parse_bracketing(found.group(1), len(full))
        if node is None:
            node = _fold(list(range(len(full))))
        return node, full

    def render_node(self, node, full: list[int], inner=None) -> list[Piece]:
        if isinstance(node, int):
            j = full[node]
            self.used.add(j)
            return [_p(self.text(j), j)]
        if node[0] == "dv":
            parts = [self.render_node(x, full) for x in node[1]]
            out = list(parts[0])
            for n, part in enumerate(parts[1:], 1):
                out += [(part[0][0], part[0][1], " and " if n == len(parts) - 1 else ", ")] + part[1:]
            return out
        _, left, right = node
        return self.render_node(right, full) + [_p("of")] + (inner or []) + self.render_node(left, full)

    def left_pieces(self, i: int, mem: list[int], flat: str = "det") -> list[Piece]:
        """The members before the final word, grouped by the bracketing: 'story of Rāma', 'son and grandson'."""
        if len(mem) == 1:
            self.used.add(mem[0])
            return [_p(self.text(mem[0]), mem[0])]
        node, full = self.tree(i, mem + [i])
        comp = next((c for c in self.reading.compounds if c.members and c.members[-1] == i), None)
        if flat == "dv" and not (comp and "bracketing" in comp.basis):
            return self.render_node(("dv", list(range(len(mem)))), full)
        if isinstance(node, tuple) and node[0] == "det" and node[2] == len(full) - 1:
            return self.render_node(node[1], full)
        return self.render_node(_fold(list(range(len(mem)))), full)

    def adi(self, i: int) -> bool:
        m = self.words[i].morph
        return bool(m and (m.stem or m.lemma) == "आदि" and self.members(i))

    def adi_pieces(self, i: int, mem: list[int]) -> list[Piece]:
        self.used.add(i)
        return self.left_pieces(i, mem) + [_p("and the rest", i)]

    def compound_pieces(self, i: int, mem: list[int], ctype: str, inner=None) -> list[Piece]:
        """A compound read off its type: determinative 'Y of X', descriptive 'X Y' (adjective first),
        copulative 'X, Y and Z'. Empty when the type does not fit, so the hyphen form stays."""
        texts = [(j, self.text(j)) for j in mem]
        last = self.noun_text(i)
        comp = next((c for c in self.reading.compounds if c.members and c.members[-1] == i), None)
        if last in NOMINAL_SUFFIXES and len(mem) == 1:  # तद्धित -ता / -त्व: "hero" + "ness", one word
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
            if not (comp and " एव " in f" {comp.vigraha} "):
                return []
        if any(t[:1].isupper() and " " in t for _, t in texts):
            return []
        if len(mem) == 1:
            self.used.update(mem)
            return [_p(last, i), _p("of")] + (inner or []) + [_p(texts[0][1], mem[0])]
        node, full = self.tree(i, mem + [i])
        if isinstance(node, tuple) and node[0] == "det" and node[2] == len(full) - 1:
            self.used.add(i)
            return [_p(last, i), _p("of")] + self.render_node(node[1], full)
        return []
