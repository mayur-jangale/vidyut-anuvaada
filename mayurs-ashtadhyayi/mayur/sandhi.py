"""Forward sandhi between padas (and between compound members), with sutra licences.

Every junction is produced by a rule ``Rule(le, rs, left, right, sutras)``: when the
first word ends in ``le`` and the second begins with ``rs``, ``le`` is written as
``left`` and ``rs`` as ``right``.  ``le`` is the word's final letter, or -- for words
ending in ``s``/``r``/``n`` -- that letter with its preceding vowel (``as``, ``Is``,
``ar``, ``in`` ...), so the left context of every rule is explicit.  ``rs`` is the
second word's first letter ("" = pausa).  The same table is used by the segmenter to
propose splits; acceptance always goes through :func:`join` / :func:`rejoin` forward.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable, Optional, Sequence

VOWELS = "aAiIuUfFxXeEoO"
SIMPLE = {"a": "a", "A": "a", "i": "i", "I": "i", "u": "u", "U": "u", "f": "f", "F": "f", "x": "x", "X": "x"}
LONG = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
SEMIVOWEL = {"i": "y", "u": "v", "f": "r", "x": "l"}
GUNA = {"i": "e", "u": "o", "f": "ar", "x": "al"}
VRDDHI = {"e": "E", "E": "E", "o": "O", "O": "O"}
AYAV = {"e": ("a", "ay"), "o": ("a", "av"), "E": ("A", "Ay"), "O": ("A", "Av")}
ROWS = ("kKgGN", "cCjJY", "wWqQR", "tTdDn", "pPbBm")
STOPS = "".join(r[:4] for r in ROWS)
NASAL_OF = {ch: row[4] for row in ROWS for ch in row[:4]}
CONSONANTS = "kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh"
VOICED_CONS = "gGNjJYqQRdDnbBmyrlvh"
NASALS = "NYRnm"
STOP_FINALS = {"k": "kg", "g": "kg", "c": "kg", "j": "kg", "w": "wq", "q": "wq",
               "t": "td", "d": "td", "p": "pb", "b": "pb"}
PALATAL_TO_VELAR = "8.2.30"  # coH kuH
SAS = frozenset({"sas", "ezas"})
# Optional (chandas-licensed) rules: 6.1.115 prakftyAntaHpAdam avyapare keeps e/o + a
# in hiatus inside a metrical line, as epic texts often do.  Rankers may penalise them.
MARKED_SUTRAS = frozenset({"6.1.115"})


@dataclass(frozen=True)
class Junction:
    text: str
    sutras: tuple[str, ...]


@dataclass(frozen=True)
class Rule:
    le: str
    rs: str
    left: str
    right: str
    sutras: tuple[str, ...]
    only: Optional[frozenset] = None  # rule applies only to these first words
    exclude: frozenset = frozenset()  # rule never applies to these first words

    def applies_to(self, first: str) -> bool:
        if self.only is not None:
            return first in self.only
        return first not in self.exclude


def final_of(word: str) -> str:
    """The rule-table key for the end of ``word`` (see module docstring)."""
    if len(word) >= 2 and word[-1] in "srn" and word[-2] in VOWELS:
        return word[-2:]
    return word[-1:]


# ---------------------------------------------------------------- rule builders

def _vowel_vowel(a: str, b: str) -> list[tuple[str, str, tuple[str, ...]]]:
    """(left, right, sutras) for vowel ``a`` + vowel ``b``."""
    if a in SIMPLE and b in SIMPLE and SIMPLE[a] == SIMPLE[b]:
        return [(LONG[SIMPLE[a]], "", ("6.1.101",))]
    if a in "aA":
        if b in GUNA or b in "IUFX":
            sut = ("6.1.87", "1.1.51") if SIMPLE[b] in "fx" else ("6.1.87",)
            return [(GUNA[SIMPLE[b]], "", sut)]
        return [(VRDDHI[b], "", ("6.1.88",))]
    if a in SIMPLE:
        return [(SEMIVOWEL[SIMPLE[a]], b, ("6.1.77",))]
    if a in "eo" and b == "a":
        return [(a, "'", ("6.1.109",)), (a, "a", ("6.1.115",))]
    short, full = AYAV[a]
    return [(short, b, ("6.1.78", "8.3.19")), (full, b, ("6.1.78",))]


def _visarga_voiceless(v: str, rs: str, base: tuple[str, ...]) -> list[tuple[str, str, tuple[str, ...]]]:
    if rs in "kKpP":
        return [(v + "H", rs, base + ("8.3.15",))]
    if rs in "cC":
        return [(v + "S", rs, base + ("8.3.15", "8.3.34", "8.4.40"))]
    if rs in "wW":
        return [(v + "z", rs, base + ("8.3.15", "8.3.34", "8.4.41"))]
    if rs in "tT":
        return [(v + "s", rs, base + ("8.3.15", "8.3.34"))]
    sib = {"S": "S", "z": "z", "s": "s"}[rs]
    return [(v + "H", rs, base + ("8.3.15", "8.3.36")), (v + sib, rs, base + ("8.3.15", "8.3.34", "8.3.36"))]


def _s_final(v: str, rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    ru = ("8.2.66",)
    if rs == "":
        return [(v + "H", "", ru + ("8.3.15",))]
    if rs not in VOWELS and rs not in VOICED_CONS:
        return _visarga_voiceless(v, rs, ru)
    if v == "a":
        if rs == "a":
            return [("o", "'", ru + ("6.1.113", "6.1.87", "6.1.109")),
                    ("o", "a", ru + ("6.1.113", "6.1.87", "6.1.115"))]
        if rs in VOWELS:
            return [("a", rs, ru + ("8.3.17", "8.3.19"))]
        return [("o", rs, ru + ("6.1.114", "6.1.87"))]
    if v == "A":
        return [("A", rs, ru + (("8.3.17", "8.3.19") if rs in VOWELS else ("8.3.17", "8.3.22")))]
    if rs == "r":
        return [(LONG.get(v, v), rs, ru + ("8.3.14", "6.3.111"))]
    return [(v + "r", rs, ru)]


def _r_final(v: str, rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    if rs == "":
        return [(v + "H", "", ("8.3.15",))]
    if rs == "r":
        return [(LONG.get(v, v), rs, ("8.3.14", "6.3.111"))]
    if rs in VOWELS or rs in VOICED_CONS:
        return [(v + "r", rs, ())]
    return _visarga_voiceless(v, rs, ())


def _n_final(v: str, rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    n = v + "n"
    if rs == "":
        return [(n, "", ())]
    if rs in VOWELS:
        return [(v + "nn", rs, ("8.3.32",))] if v in "aiufx" else [(n, rs, ())]
    if rs in "cC":
        return [(v + "MS", rs, ("8.3.7", "8.3.4", "8.3.15", "8.3.34", "8.4.40"))]
    if rs in "tT":
        return [(v + "Ms", rs, ("8.3.7", "8.3.4", "8.3.15", "8.3.34"))]
    if rs in "wW":
        return [(v + "Mz", rs, ("8.3.7", "8.3.4", "8.3.15", "8.3.34", "8.4.41"))]
    if rs in "jJ":
        return [(v + "Y", rs, ("8.4.40",))]
    if rs == "S":
        return [(v + "Y", "C", ("8.4.40", "8.4.63")), (v + "Y", "S", ("8.4.40",))]
    if rs in "qQ":
        return [(v + "R", rs, ("8.4.41",))]
    return [(n, rs, ())]


def _stop_final(le: str, rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    pre = (PALATAL_TO_VELAR,) if le in "cj" else ()
    hard, soft = STOP_FINALS[le]
    jas = pre + ("8.2.39",)
    if rs == "":
        return [(hard, "", jas + ("8.4.56",)), (soft, "", jas)]
    if hard == "t" and rs in "cCjJwWqQlS":
        if rs == "l":
            return [("l", rs, jas + ("8.4.60",))]
        pal = rs in "cCjJS"
        new = ("c" if rs in "cCS" else "j") if pal else ("w" if rs in "wW" else "q")
        sut = jas + (("8.4.40",) if pal else ("8.4.41",)) + (("8.4.55",) if rs in "cCwWS" else ())
        if rs == "S":
            return [(new, "C", sut + ("8.4.63",)), (new, "S", sut)]
        return [(new, rs, sut)]
    if rs in "mn":
        nasal = {"k": "N", "w": "R", "t": "n", "p": "m"}[hard]
        return [(nasal, rs, jas + ("8.4.45",)), (soft, rs, jas)]
    if rs == "h":
        aspirate = {"g": "G", "q": "Q", "d": "D", "b": "B"}[soft]
        return [(soft, aspirate, jas + ("8.4.62",)), (soft, rs, jas)]
    if rs in VOWELS or rs in VOICED_CONS:
        return [(soft, rs, jas)]
    return [(hard, rs, jas + ("8.4.55",))]


def _m_final(rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    if rs == "" or rs in VOWELS:
        return [("m", rs, ())]
    out = [("M", rs, ("8.3.23",))]
    if rs in STOPS:
        out.append((NASAL_OF[rs], rs, ("8.3.23", "8.4.59")))
    return out


def _vowel_final(v: str, rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    if rs in VOWELS:
        return _vowel_vowel(v, rs)
    if rs == "C":
        if v in "aiufx":
            return [(v + "c", rs, ("6.1.73", "8.4.40"))]
        return [(v + "c", rs, ("6.1.76", "8.4.40")), (v, rs, ())]
    return [(v, rs, ())]


def _outcomes(le: str, rs: str) -> list[tuple[str, str, tuple[str, ...]]]:
    if le in VOWELS:
        return [(le, "", ())] if rs == "" else _vowel_final(le, rs)
    if len(le) == 2 and le[1] == "s":
        return _s_final(le[0], rs)
    if len(le) == 2 and le[1] == "r":
        return _r_final(le[0], rs)
    if len(le) == 2 and le[1] == "n":
        return _n_final(le[0], rs)
    if le == "m":
        return _m_final(rs)
    if le in STOP_FINALS:
        return _stop_final(le, rs)
    return [(le, rs, ())]


FINALS = tuple(VOWELS) + tuple(v + c for c in "srn" for v in VOWELS) + tuple("m" + "kgcjwqtdpb" + "NYRylvShKGTDBzP")


@lru_cache(maxsize=1)
def rules() -> tuple[Rule, ...]:
    """The complete junction table (every final x every initial, plus pausa)."""
    out: list[Rule] = []
    for le in FINALS:
        for rs in tuple(VOWELS) + tuple(CONSONANTS) + ("",):
            if le == "as" and rs in CONSONANTS:
                out.append(Rule(le, rs, "a", rs, ("6.1.132",), only=SAS))
                out.extend(Rule(le, rs, lf, rt, s, exclude=SAS) for lf, rt, s in _outcomes(le, rs))
                continue
            out.extend(Rule(le, rs, lf, rt, s) for lf, rt, s in _outcomes(le, rs))
    return tuple(out)


@lru_cache(maxsize=None)
def _rules_for(le: str, rs: str) -> tuple[Rule, ...]:
    return tuple(r for r in rules() if r.le == le and r.rs == rs)


def _sep(left: str, right: str, compound: bool) -> str:
    if compound or not left or not right:
        return ""
    if right[0] in VOWELS and left[-1] not in VOWELS and left[-1] not in "HM":
        return ""
    return " "


def _pieces(first: str, second: str, compound: bool) -> list[tuple[str, str, tuple[str, ...]]]:
    """(replacement for first's final, replacement for second's initial, sutras)."""
    le, rs = final_of(first), second[:1]
    out: list[tuple[str, str, tuple[str, ...]]] = []
    for r in _rules_for(le, rs):
        if r.applies_to(first):
            sep = "" if rs == "" else _sep(r.left, r.right, compound)
            out.append((r.left, sep + r.right, r.sutras))
    if not out:  # no rule for this final: plain juxtaposition
        out.append((le, ("" if compound or not second else " ") + rs, ()))
    return out


def join(first: str, second: str, compound: bool = False) -> list[Junction]:
    """All surface outcomes of ``first`` followed by ``second`` ("" = pausa)."""
    le, rs = final_of(first), second[:1]
    found: dict[str, tuple[str, ...]] = {}
    for left, right, sut in _pieces(first, second, compound):
        found.setdefault(first[: len(first) - len(le)] + left + right + second[len(rs):], sut)
    return [Junction(t, s) for t, s in found.items()]


def pausa(word: str) -> list[Junction]:
    return join(word, "")


def rejoin(forms: Sequence[str], compound_flags: Sequence[bool]) -> set[str]:
    """Every surface string the word sequence can produce (last word in pausa)."""
    return {j.text for j in rejoin_traced(forms, compound_flags)}


def rejoin_traced(forms: Sequence[str], compound_flags: Sequence[bool], limit: int = 4096) -> list[Junction]:
    """Like :func:`rejoin`, keeping the sutras of every boundary (in order, flattened)."""
    if not forms:
        return [Junction("", ())]
    if len(compound_flags) != len(forms):
        raise ValueError("compound_flags must have one flag per form")
    # state: (text before the current word, current word as altered on its left, sutras)
    states: dict[tuple[str, str], tuple[str, ...]] = {("", forms[0]): ()}
    for i, word in enumerate(forms):
        second = forms[i + 1] if i + 1 < len(forms) else ""
        cut = len(final_of(word))
        nxt: dict[tuple[str, str], tuple[str, ...]] = {}
        for (before, cur), sut in states.items():
            stem = cur[: max(0, len(cur) - cut)]
            for left, right, s in _pieces(word, second, bool(compound_flags[i]) and bool(second)):
                key = (before + stem + left, right + second[1:])
                nxt.setdefault(key, sut + s)
        states = dict(list(nxt.items())[:limit])
    return [Junction(b + c, s) for (b, c), s in states.items()]


def canon(surface: str) -> str:
    """Normal form for comparing a re-joined string with the input.

    Equivalences (and nothing else):
    * whitespace is removed (word division in writing is not part of the form);
    * avagraha ``'`` is removed (its use is an orthographic option, 6.1.109);
    * a nasal homorganic with the following stop is written as anusvara ``M``
      (``puNgava`` = ``puMgava``: 8.4.58 anusvArasya yayi parasavarRaH, 8.4.59 vA padAntasya);
    * a string-final ``m`` (pausa) is written ``M`` (anusvara vs ``m`` at the line end).
    """
    return canon_with_map(surface)[0]


def canon_with_map(surface: str, final: bool = True) -> tuple[str, list[int]]:
    """:func:`canon` plus, for each output character, its index in ``surface``."""
    chars: list[str] = []
    index: list[int] = []
    for i, ch in enumerate(surface):
        if ch.isspace() or ch == "'":
            continue
        chars.append(ch)
        index.append(i)
    for k in range(len(chars) - 1):
        nxt = chars[k + 1]
        if chars[k] in NASALS and nxt in STOPS and NASAL_OF[nxt] == chars[k]:
            chars[k] = "M"
    if final and chars and chars[-1] == "m":
        chars[-1] = "M"
    return "".join(chars), index


def nasal_variants(form: str) -> list[str]:
    """Spellings of ``form`` with each anusvara before a stop as M or the homorganic nasal."""
    slots = [k for k in range(len(form) - 1) if form[k] == "M" and form[k + 1] in STOPS]
    if not slots:
        return [form]
    out = []
    for choice in itertools.product((True, False), repeat=min(len(slots), 4)):
        chars = list(form)
        for k, homorganic in zip(slots, choice):
            if homorganic:
                chars[k] = NASAL_OF[form[k + 1]]
        out.append("".join(chars))
    return out


def matches(forms: Sequence[str], flags: Sequence[bool], surface: str) -> Optional[str]:
    """The re-joined string equal to ``surface`` under :func:`canon`, if any."""
    target = canon(surface)
    for text in rejoin(forms, flags):
        if canon(text) == target:
            return text
    return None


def sutras_between(first: str, second: str, compound: bool, surface_piece: str) -> tuple[str, ...]:
    for j in join(first, second, compound):
        if canon(j.text) == canon(surface_piece):
            return j.sutras
    return ()


def all_rules_with(le: Iterable[str]) -> list[Rule]:
    keys = set(le)
    return [r for r in rules() if r.le in keys]
