"""Sentence-level joins of the template renderer (a mixin of ``translate_core._Renderer``): the locative
absolute, relative-correlative pairs (यः ... सः "he who ..."), यदा ... तदा "when ..., then ...", and direct
speech with इति (the clause is quoted, the verb of saying stays outside)."""

from __future__ import annotations

from . import english
from .translate_words import CORRELATIVES, SAYING, SUBORDINATORS

Piece = tuple[str, "int | None", str]
_PAST = {"लिट्", "लङ्", "लुङ्"}


def _p(text: str, idx=None, sep: str = " ") -> Piece:
    return (text, idx, sep)


class JoinMixin:
    def lemma_at(self, idx) -> str:
        m = self.words[idx].morph if idx is not None else None
        return m.lemma if m is not None else ""

    def clause(self, v: int, keep_conn: bool = True) -> list[Piece]:
        """The clause of verb ``v``; a locative absolute ("when Rāma had gone,") opens it."""
        kids = self.children.get(v, [])
        absolute = [k for k in kids if self.role(k) == "भावलक्षण" and k not in self.used and self.participle_of(k)]
        pre: list[Piece] = []
        if absolute:
            self.children[v] = [k for k in kids if k not in absolute]
            for k in absolute:
                pre += self.locative_absolute(k, v)
        out = self.clause_core(v, keep_conn)
        if absolute:
            self.children[v] = kids
        lead = 0
        while lead < len(out) and out[lead][1] is not None and self.role(out[lead][1]) == "अव्यय" \
                and out[lead][0] in ("and", "but", "or", "then", "now"):
            lead += 1
        return out[:lead] + pre + out[lead:]

    def participle_of(self, k: int):
        for c in self.children.get(k, []):
            m = self.words[c].morph
            if self.role(c) == "विशेषण" and m is not None and m.krt in ("क्त", "शतृ", "शानच्", "क्तवतु") and c not in self.used:
                return c
        return None

    def locative_absolute(self, k: int, v: int) -> list[Piece]:
        c = self.participle_of(k)
        self.used.add(c)
        vm = self.words[v].morph
        past_main = vm is not None and vm.lakara in _PAST
        g = self.text(c)
        if self.words[c].morph.krt in ("क्त", "क्तवतु"):
            text = ("had " if past_main else "has ") + english.participle(g)
        else:
            text = ("was " if past_main else "is ") + english.present_participle(g)
        return [_p("when")] + self.np(k, [x for x in self.children.get(k, []) if x != c]) + [_p(text, c)] + self.tail(c) + [_p(",", None, "")]

    # ---- joins ---------------------------------------------------------------------
    def quote_of(self, v: int):
        return next((k for k in self.children.get(v, []) if self.role(k) == "अव्यय" and self.lemma_at(k) == "इति"), None)

    def join_clauses(self, items: list[tuple[int, list[Piece]]]) -> list[Piece]:
        quoted = [it for it in items if self.quote_of(it[0]) is not None]
        if quoted and len(items) > 1:
            q = quoted[0]
            rest = [it for it in items if it is not q]
            near = [it for it in rest if (self.text(it[0]).lower().split() or [""])[0] in SAYING] or rest
            main = min(near, key=lambda it: abs(self.pos[it[0]] - self.pos[q[0]]))
            merged = (main[0], main[1] + [_p(",", None, ""), _p("“", None, " ")] + self.tidy_quote(q[1])
                      + [_p(".”", None, "")])
            rest = [merged if it is main else it for it in rest]
            return self.join_clauses(rest) if len(rest) > 1 else list(rest[0][1])
        out: list[Piece] = []
        for n, (v, cl) in enumerate(items):
            cl = list(cl)
            sep = _p(";", None, "")
            if n:
                prev = out
                rel = next((x for x, p in enumerate(prev) if self.lemma_at(p[1]) == "यद्"), None)
                tad = next((x for x, p in enumerate(cl) if p[1] is not None and self.lemma_at(p[1]) == "तद्"
                            and not self.words[p[1]].in_compound), None)
                adjectival = rel is not None and self.role(prev[rel][1]) == "विशेषण"  # "the man who ...": stays after its noun
                if adjectival and tad is not None:
                    sep = _p(",", None, "")  # "The man who gives up his body, he attains greatness"
                elif rel is not None and tad is not None:  # "he who reads, obtains ...": the correlative leads
                    piece = cl.pop(tad)
                    out[rel:rel] = [(piece[0], piece[1], " ")]
                    sep = _p(",", None, "")
                    if tad == 0 and cl:
                        cl[0] = (cl[0][0], cl[0][1], " ")
                elif self.opens_with(prev, SUBORDINATORS) and self.opens_with(cl, CORRELATIVES):
                    sep = _p(",", None, "")
                out.append(sep)
            out += cl
        return out

    def opens_with(self, pieces: list[Piece], words) -> bool:
        for t, idx, _ in pieces:
            if idx is not None and self.role(idx) == "अव्यय" and t in words:
                return True
            if t in ("O", ","):
                continue
            return False
        return False

    def tidy_quote(self, pieces: list[Piece]) -> list[Piece]:
        pieces = [p for p in pieces if p[0] not in ("thus",) or p[1] is None]
        while pieces and pieces[-1][0] in (",", ";"):
            pieces.pop()
        if pieces:
            pieces[0] = (pieces[0][0], pieces[0][1], "")
        return pieces
