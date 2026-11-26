"""Forward sandhi between two padas, every result tagged with the sutras that license it.

Only the forward direction exists here: ``outcomes(left, right)`` says what the text becomes.
The segmenter inverts nothing by hand; it indexes these outcomes.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Sequence

from mayur.lipi import from_varnas as _lipi_from_varnas
from mayur.lipi import varnas

Varnas = tuple[str, ...]

SHORT = ("अ", "इ", "उ", "ऋ", "ऌ")
LONG = ("आ", "ई", "ऊ", "ॠ")
DIPH = ("ए", "ऐ", "ओ", "औ")
VOWELS = SHORT + LONG + DIPH
SAVARNA = {"अ": "आ", "आ": "आ", "इ": "ई", "ई": "ई", "उ": "ऊ", "ऊ": "ऊ", "ऋ": "ॠ", "ॠ": "ॠ", "ऌ": "ॠ"}
VARGAS = (
    ("क्", "ख्", "ग्", "घ्", "ङ्"),
    ("च्", "छ्", "ज्", "झ्", "ञ्"),
    ("ट्", "ठ्", "ड्", "ढ्", "ण्"),
    ("त्", "थ्", "द्", "ध्", "न्"),
    ("प्", "फ्", "ब्", "भ्", "म्"),
)
VARGA_OF = {c: (g, i) for g, row in enumerate(VARGAS) for i, c in enumerate(row)}
STOPS = frozenset(c for row in VARGAS for c in row[:4])
NASALS = frozenset(row[4] for row in VARGAS)
SEMIVOWELS = ("य्", "र्", "ल्", "व्")
SIBILANTS = ("श्", "ष्", "स्")
CONSONANTS = tuple(c for row in VARGAS for c in row) + SEMIVOWELS + SIBILANTS + ("ह्",)
VOICED = frozenset(c for row in VARGAS for c in row[2:]) | frozenset(SEMIVOWELS) | {"ह्"}
SPECIAL_PRONOUNS = ("सस्", "एषस्")  # 6.1.132 एतत्तदोः सुलोपोऽकोरनञ्समासे हलि
ANUSVARA, VISARGA, AVAGRAHA, CHANDRABINDU = "ं", "ः", "ऽ", "ँ"
PRAGRHYA = ("ई", "ऊ", "ए")  # 1.1.11 ईदूदेद्द्विवचनं प्रगृह्यम् (only dual forms; the form alone cannot tell)
# Hiatus left across a pāda boundary (metrical licence in epic verse; no sūtra). The segmenter
# accepts it only where the text writes a space.
# Saṃhitā between the words of a sentence is optional (the kārikā on 1.4.109 परः संनिकर्षः संहिता:
# "वाक्ये तु सा विवक्षामपेक्षते"): a word may stand in pausa before the next, or a vowel may meet a
# vowel unjoined (e.g. across a pāda boundary). The segmenter accepts this only where the text
# writes a space.
PADA_HIATUS = "१.४.१०९"
# Pada-final palatals and ह् become stops before sandhi: 8.2.30 चोः कुः, 8.2.36 व्रश्च... (श्/ष्, and
# राज्-type ज्), 8.2.31 हो ढः.
PALATAL_FINAL = {
    "च्": (("क्", "८.२.३०"),),
    "ज्": (("क्", "८.२.३०"), ("ट्", "८.२.३६")),
    "श्": (("ट्", "८.२.३६"), ("क्", "८.२.६२")),
    "ष्": (("ट्", "८.२.३९"),),
    "ह्": (("ट्", "८.२.३१"), ("क्", "८.२.३२")),
}


def from_varnas(seq) -> str:
    """``lipi.from_varnas``, but a vowel after a vowel (hiatus) is written as an independent letter.

    (The underlying transliteration merges some such pairs, e.g. ए + आ.)
    """
    seq = tuple(seq)
    cuts = [i for i in range(1, len(seq)) if is_vowel(seq[i]) and is_vowel(seq[i - 1])]
    bounds = [0] + cuts + [len(seq)]
    return "".join(_lipi_from_varnas(seq[a:b]) for a, b in zip(bounds, bounds[1:]))


@dataclass(frozen=True)
class Outcome:
    text: str
    sutras: tuple[str, ...]


def is_vowel(v: str) -> bool:
    return v in VOWELS


def _o(seq: Varnas, *sutras: str) -> tuple[Varnas, tuple[str, ...]]:
    return (tuple(seq), tuple(sutras))


def _vowel_vowel(a: str, b: str) -> list:
    """Final vowel ``a`` meets initial vowel ``b``: list of (replacement varnas for a+b, sutras)."""
    if a in SAVARNA and b in SAVARNA and SAVARNA[a] == SAVARNA[b]:
        return [_o((SAVARNA[a],), "६.१.१०१")]
    if a in ("अ", "आ"):
        guna = {"इ": ("ए",), "ई": ("ए",), "उ": ("ओ",), "ऊ": ("ओ",), "ऋ": ("अ", "र्"), "ॠ": ("अ", "र्"),
                "ऌ": ("अ", "ल्")}
        if b in guna:
            return [_o(guna[b], "६.१.८७")]
        vrddhi = {"ए": "ऐ", "ऐ": "ऐ", "ओ": "औ", "औ": "औ"}
        return [_o((vrddhi[b],), "६.१.८८")]
    yan = {"इ": "य्", "ई": "य्", "उ": "व्", "ऊ": "व्", "ऋ": "र्", "ॠ": "र्", "ऌ": "ल्"}
    if a in yan:
        return [_o((yan[a], b), "६.१.७७")]
    if a in ("ए", "ओ"):
        if b == "अ":
            return [_o((a, AVAGRAHA), "६.१.१०९"), _o((a,), "६.१.१०९")]
        semi = "य्" if a == "ए" else "व्"
        return [_o(("अ", semi, b), "६.१.७८"), _o(("अ", b), "६.१.७८", "८.३.१९")]
    if a == "ऐ":
        return [_o(("आ", "य्", b), "६.१.७८"), _o(("आ", b), "६.१.७८", "८.३.१९")]
    if a == "औ":
        return [_o(("आ", "व्", b), "६.१.७८")]
    return [_o((a, b))]


def _final_s_or_r(left: Varnas, right: Varnas, word: str) -> list:
    """``left`` ends in स् or र्; returns (full joined varnas, sutras) pairs."""
    stem, fin = left[:-1], left[-1]
    pen = stem[-1] if stem else ""
    b = right[0]
    rest = right[1:]
    is_s = fin == "स्"
    if is_s and word in SPECIAL_PRONOUNS and not is_vowel(b):
        return [_o(stem + right, "६.१.१३२")]
    if is_vowel(b):
        if is_s and pen == "अ":
            if b == "अ":
                return [_o(stem[:-1] + ("ओ", AVAGRAHA) + rest, "६.१.११३", "६.१.८७", "६.१.१०९"),
                        _o(stem[:-1] + ("ओ",) + rest, "६.१.११३", "६.१.८७", "६.१.१०९")]
            return [_o(stem + right, "८.३.१७", "८.३.१९")]
        if is_s and pen == "आ":
            return [_o(stem + right, "८.३.१७", "८.३.१९")]
        return [_o(stem + ("र्",) + right, "८.२.६६") if is_s else _o(left + right)]
    if b in VOICED:
        if is_s and pen == "अ":
            return [_o(stem[:-1] + ("ओ",) + right, "८.२.६६", "६.१.११४", "६.१.८७")]
        if is_s and pen == "आ":
            # 8.3.17 makes रु into य्, which 8.3.22 drops before a consonant.
            return [_o(stem + right, "८.२.६६", "८.३.१७", "८.३.२२")]
        base = ("८.२.६६",) if is_s else ()
        if b == "र्":
            longer = stem[:-1] + (SAVARNA.get(pen, pen),) if pen in SAVARNA else stem
            return [_o(longer + right, *base, "८.३.१४", "६.३.१११")]
        return [_o(stem + ("र्",) + right, *base)]
    base = ("८.२.६६", "८.३.१५") if is_s else ("८.३.१५",)
    if b in ("च्", "छ्"):
        return [_o(stem + ("श्",) + right, *base, "८.३.३४", "८.४.४०")]
    if b in ("ट्", "ठ्"):
        return [_o(stem + ("ष्",) + right, *base, "८.३.३४", "८.४.४१")]
    if b in ("त्", "थ्"):
        return [_o(stem + ("स्",) + right, *base, "८.३.३४")]
    if b in SIBILANTS:
        same = (b,) if b != "स्" else ("स्",)
        assim = "८.४.४०" if b == "श्" else ("८.४.४१" if b == "ष्" else "८.३.३४")
        return [_o(stem + (VISARGA,) + right, *base, "८.३.३६"),
                _o(stem + same + right, *base, "८.३.३४", assim)]
    return [_o(stem + (VISARGA,) + right, *base)]


def _final_n(left: Varnas, right: Varnas) -> list:
    stem = left[:-1]
    b = right[0]
    if is_vowel(b):
        if len(stem) >= 1 and stem[-1] in SHORT:
            return [_o(left + ("न्",) + right, "८.३.३२")]
        return [_o(left + right)]
    if b in ("च्", "छ्"):
        return [_o(stem + (ANUSVARA, "श्") + right, "८.३.७", "८.३.२३", "८.४.४०")]
    if b in ("ट्", "ठ्"):
        return [_o(stem + (ANUSVARA, "ष्") + right, "८.३.७", "८.३.२३", "८.४.४१")]
    if b in ("त्", "थ्"):
        return [_o(stem + (ANUSVARA, "स्") + right, "८.३.७", "८.३.२३")]
    if b in ("ज्", "झ्"):
        return [_o(stem + ("ञ्",) + right, "८.४.४०")]
    if b == "श्":
        rest = right[1:]
        return [_o(stem + ("ञ्",) + right, "८.४.४०"),
                _o(stem + ("ञ्", "छ्") + rest, "८.४.४०", "८.४.६३"),
                _o(stem + ("ञ्", "च्", "छ्") + rest, "८.३.३१", "८.४.४०", "८.४.६३")]
    if b in ("ड्", "ढ्"):
        return [_o(stem + ("ण्",) + right, "८.४.४१")]
    if b == "ल्":
        return [_o(stem + (CHANDRABINDU, "ल्") + right, "८.४.६०"),
                _o(stem + (ANUSVARA, "ल्") + right, "८.४.६०", "८.३.४")]
    return [_o(left + right)]


def _final_stop(left: Varnas, right: Varnas) -> list:
    stem, fin = left[:-1], left[-1]
    g, _ = VARGA_OF[fin]
    row = VARGAS[g]
    b = right[0]
    rest = right[1:]
    voiced, plain = row[2], row[0]
    if is_vowel(b):
        return [_o(stem + (voiced,) + right, "८.२.३९")]
    if b in NASALS:
        return [_o(stem + (voiced,) + right, "८.२.३९"), _o(stem + (row[4],) + right, "८.२.३९", "८.४.४५")]
    if b == "ह्":
        return [_o(stem + (voiced,) + right, "८.२.३९"),
                _o(stem + (voiced, row[3]) + rest, "८.२.३९", "८.४.६२")]
    if g == 3 and b in VARGA_OF and VARGA_OF[b][0] in (1, 2):  # dental before palatal/retroflex
        gb, ib = VARGA_OF[b]
        new = VARGAS[gb][0] if ib < 2 else VARGAS[gb][2]
        return [_o(stem + (new,) + right, "८.२.३९", "८.४.४०" if gb == 1 else "८.४.४१")]
    if g == 3 and b == "ल्":
        return [_o(stem + ("ल्",) + right, "८.२.३९", "८.४.६०")]
    if b == "श्":
        cut = ("च्",) if g == 3 else (plain,)
        assim = ("८.४.४०",) if g == 3 else ()
        return [_o(stem + cut + right, "८.२.३९", *assim, "८.४.५५"),
                _o(stem + cut + ("छ्",) + rest, "८.२.३९", *assim, "८.४.५५", "८.४.६३")]
    if b in VOICED:
        return [_o(stem + (voiced,) + right, "८.२.३९", "८.४.५३")]
    return [_o(stem + (plain,) + right, "८.२.३९", "८.४.५५")]


@lru_cache(maxsize=100_000)
def _outcomes_v(left: Varnas, right: Varnas, word: str, samasa: bool) -> tuple[tuple[Varnas, tuple[str, ...]], ...]:
    if not left or not right:
        return ((left + right, ()),)
    a, b = left[-1], right[0]
    extra = ("१.४.१४", "२.४.७१") if samasa else ()
    if a in PALATAL_FINAL:
        raw = []
        for stop, rule in PALATAL_FINAL[a]:
            raw.extend((seq, (rule,) + s) for seq, s in _outcomes_v(left[:-1] + (stop,), right, word, False))
        return tuple((seq, tuple(dict.fromkeys(extra + s))) for seq, s in raw)
    if is_vowel(a):
        if is_vowel(b):
            raw = [(left[:-1] + seq + right[1:], s) for seq, s in _vowel_vowel(a, b)]
            if a in PRAGRHYA:  # dual ई ऊ ए are pragṛhya and stay unjoined
                raw.append((left + right, ("१.१.११", "६.१.१२५")))

        elif b == "छ्":
            raw = [(left + ("च्",) + right, ("६.१.७३",) if a in SHORT else ("६.१.७६",))]
            if a not in SHORT:
                raw.append((left + right, ()))
        else:
            raw = [(left + right, ())]
    elif a in ("स्", "र्"):
        raw = _final_s_or_r(left, right, word)
    elif a == "म्":
        raw = [(left + right, ())] if is_vowel(b) else [(left[:-1] + (ANUSVARA,) + right, ("८.३.२३",))]
    elif a == "न्" and samasa and is_vowel(b):
        raw = [(left + right, ("६.३.७४",))]  # नञ् as अन् before a vowel: no doubling (8.3.32 is pada-final)
    elif a == "न्":
        raw = _final_n(left, right)
    elif a in STOPS:
        raw = _final_stop(left, right)
    else:
        raw = [(left + right, ())]
    if not samasa:
        raw = list(raw) + [(varnas(p) + right, (PADA_HIATUS,)) for p in pausa_forms(from_varnas(left))]
    return tuple((seq, tuple(dict.fromkeys(extra + tuple(s)))) for seq, s in raw)


def outcomes(left: str, right: str, samasa: bool = False) -> tuple[Outcome, ...]:
    """Every legitimate surface of pada ``left`` followed by ``right`` (no space between)."""
    found = _outcomes_v(varnas(left), varnas(right), left, samasa)
    seen: dict[str, tuple[str, ...]] = {}
    for seq, sutras in found:
        seen.setdefault(from_varnas(seq), sutras)
    return tuple(Outcome(t, s) for t, s in seen.items())


def pausa_forms(pada: str) -> tuple[str, ...]:
    """A pada at the end of a line: स्/र् → ः (8.3.15); म् or ं; final stop voiced or not (8.4.56)."""
    v = varnas(pada)
    if not v:
        return (pada,)
    fin = v[-1]
    if fin in ("स्", "र्"):
        return (from_varnas(v[:-1] + (VISARGA,)),)
    if fin == "म्":
        return (pada, from_varnas(v[:-1] + (ANUSVARA,)))
    if fin in PALATAL_FINAL:
        out: list[str] = []
        for stop, _ in PALATAL_FINAL[fin]:
            out.extend(pausa_forms(from_varnas(v[:-1] + (stop,))))
        return tuple(dict.fromkeys(out))
    if fin in STOPS:
        g, _ = VARGA_OF[fin]
        return tuple(dict.fromkeys(from_varnas(v[:-1] + (VARGAS[g][i],)) for i in (0, 2)))
    return (pada,)


def rejoin(forms: Sequence[str], compound_flags: Sequence[bool]) -> set[str]:
    """All surface strings the word sequence can become (left fold, last word in pausa)."""
    if not forms:
        return {""}
    flags = list(compound_flags) + [False] * (len(forms) - len(compound_flags))
    # state: (frozen surface varnas, current word's varnas as changed at its left edge, its pada form)
    states = {((), varnas(forms[0]), forms[0])}
    for i in range(1, len(forms)):
        nv = varnas(forms[i])
        keep = max(len(nv) - 1, 1)
        nxt = set()
        for done, cur, word in states:
            for seq, _ in _outcomes_v(cur, nv, word, flags[i - 1]):
                nxt.add((done + seq[:-keep], seq[-keep:], forms[i]))
        states = nxt
    result: set[str] = set()
    for done, cur, word in states:
        fin = varnas(word)[-1:]
        for p in pausa_forms(from_varnas(cur)) if cur[-1:] == fin else (from_varnas(cur),):
            result.add(from_varnas(done + varnas(p)))
    return result


def rejoin_matching(forms: Sequence[str], compound_flags: Sequence[bool], text: str) -> str | None:
    """A re-join of ``forms`` whose ``canon`` equals ``canon(text)``, or None.

    The same fold as :func:`rejoin`, but states that already disagree with the text are dropped,
    so long lines with many optional rules stay cheap.
    """
    target = canon_varnas(text)
    if not forms:
        return "" if not target else None
    flags = list(compound_flags) + [False] * (len(forms) - len(compound_flags))

    def alive(done: Varnas) -> bool:
        cv = canon_varnas(from_varnas(done)) if done else ()
        cut = max(len(cv) - 1, 0)
        return target[:cut] == cv[:cut]

    states = {((), varnas(forms[0]), forms[0])}
    for i in range(1, len(forms)):
        nv = varnas(forms[i])
        keep = max(len(nv) - 1, 1)
        nxt = set()
        for done, cur, word in states:
            for seq, _ in _outcomes_v(cur, nv, word, flags[i - 1]):
                new_done = done + seq[:-keep]
                if alive(new_done):
                    nxt.add((new_done, seq[-keep:], forms[i]))
        states = nxt
    for done, cur, word in states:
        fin = varnas(word)[-1:]
        for p in pausa_forms(from_varnas(cur)) if cur[-1:] == fin else (from_varnas(cur),):
            cand = from_varnas(done + varnas(p))
            if canon_varnas(cand) == target:
                return cand
    return None


def _stop_nasal(v: str) -> str | None:
    g = VARGA_OF.get(v)
    return VARGAS[g[0]][4] if g and v in STOPS else None


def canon(text: str) -> str:
    """The one normalisation for comparing a re-join with an input line.

    1. Spaces are removed.
    2. Anusvara before a stop is written as the homorganic nasal (पुंगव = पुङ्गव, 8.4.58/59).
    3. A line-final ं is written म् (final म् ≡ ं, 8.3.23 is optional in pausa); a म् written
       unassimilated before a non-labial stop counts as the homorganic nasal (8.3.23 + 8.4.59).
    Avagraha is not normalised: sandhi outcomes are produced with and without it.
    """
    return from_varnas(canon_varnas(text))


def canon_varnas(text: str, keep_spaces: bool = False) -> Varnas:
    """``canon`` as a varna sequence; with ``keep_spaces`` the spaces stay (as " ")."""
    raw = [v for v in varnas(text.strip()) if v != "‌"]
    out: list[str] = []
    for i, v in enumerate(raw):
        if v == " " and (not out or out[-1] == " "):
            continue
        if v in (ANUSVARA, "म्"):
            j = i + 1
            while j < len(raw) and raw[j] == " ":
                j += 1
            nasal = _stop_nasal(raw[j]) if j < len(raw) else None
            if v == ANUSVARA and nasal:
                v = nasal
            elif v == "म्" and nasal and nasal != "म्":  # unassimilated म् before a stop (युक्तम्गुणैः)
                v = nasal
            elif j >= len(raw):
                v = "म्"
        out.append(v)
    while out and out[-1] == " ":
        out.pop()
    return tuple(out) if keep_spaces else tuple(x for x in out if x != " ")
