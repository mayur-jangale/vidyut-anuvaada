"""Forward-derived analyses for forms the kosha does not list (source "generated").

Every candidate here is only a guess at vidyut ARGUMENTS; it is kept only when a forward
vidyut-prakriya derivation from those arguments yields exactly the form.
"""

from __future__ import annotations

import time
from dataclasses import replace

from mayur import bridge, lipi
from mayur.model import Morph
from mayur.terms import NONFINITE_KRT, PARTICIPLE_KRT

_GOOD_KRT = frozenset(PARTICIPLE_KRT) | frozenset(NONFINITE_KRT)

_VOWEL_SIGNS = {"ा": "आ", "ि": "इ", "ी": "ई", "ु": "उ", "ू": "ऊ", "ृ": "ऋ", "े": "ए", "ै": "ऐ", "ो": "ओ", "ौ": "औ"}
_STOP_FINALS = ("स्", "ष्", "र्", "ः", "द्", "त्", "न्", "ण्", "ञ्", "ङ्", "म्", "ं", "ज्", "च्", "ल्", "ब्", "भ्")


def _surfaces(upasarga: str) -> tuple[tuple[str, tuple[str, ...]], ...]:
    """(written prefix, possible starts of the remainder) pairs for ``upasarga`` in sandhi.

    The varna lists are joined back into Devanagari; starts are prepended to the rest."""
    v = lipi.varnas(upasarga)
    out: list[tuple[tuple[str, ...], tuple[tuple[str, ...], ...]]] = [(v, ((),))]
    last = v[-1]
    if last.endswith("्"):
        base = v[:-1]
        for c in _STOP_FINALS:
            out.append((base + (c,), ((),)))
        out.append((base, ((),)))
    elif last in ("इ", "ई"):
        out.append((v[:-1] + ("य्",), ((),)))
    elif last in ("उ", "ऊ"):
        out.append((v[:-1] + ("व्",), ((),)))
    elif last in ("अ", "आ"):
        out.append((v[:-1] + ("आ",), (("अ",), ("आ",))))
        out.append((v[:-1] + ("ए",), (("इ",), ("ई",), ("ए",))))
        out.append((v[:-1] + ("ओ",), (("उ",), ("ऊ",), ("ओ",))))
        out.append((v[:-1] + ("अ", "र्"), (("ऋ",),)))
        out.append((v[:-1] + ("ऐ",), (("ए",), ("ऐ",))))
        out.append((v[:-1] + ("औ",), (("ओ",), ("औ",))))
    if last in ("इ", "उ"):
        out.append((v[:-1] + ("ई" if last == "इ" else "ऊ",), (("इ",) if last == "इ" else ("उ",),)))
    return tuple((lipi.from_varnas(p), tuple(lipi.from_varnas(s) for s in starts)) for p, starts in out)


def _splits(form: str) -> list[tuple[str, str]]:
    """(upasarga, remainder) candidates for ``form``."""
    sounds = lipi.varnas(form)
    out = []
    for u in bridge.UPASARGA_CODE:
        for written, starts in _surfaces(u):
            wv = lipi.varnas(written)
            if len(wv) < len(sounds) and sounds[:len(wv)] == wv:
                rest = sounds[len(wv):]
                for s in starts:
                    rem = lipi.from_varnas(lipi.varnas(s) + rest) if s else lipi.from_varnas(rest)
                    out.append((u, rem))
    return list(dict.fromkeys(out))


def _lemma(upasargas: tuple[str, ...], root: str) -> str:
    return "".join(upasargas) + root


def _try_prefixes(form: str, upasargas: tuple[str, ...], remainder: str) -> list[Morph]:
    out = []
    for entry in bridge.lookup(remainder):
        m = entry.morph
        if entry.entry == "tinanta":
            pada = bridge.prefixed_tinanta(entry, upasargas)
        elif entry.entry == "krdanta" and m.krt in _GOOD_KRT:
            pada = bridge.prefixed_krdanta(entry, upasargas)
        else:
            continue
        if pada is None:
            continue
        if any(d.text == form for d in bridge.derive(pada)):
            prefixes = upasargas + m.prefixes
            out.append(replace(m, form=form, lemma=_lemma(prefixes, m.root or m.lemma), prefixes=prefixes,
                               source="generated", quality=3, handle=pada))
    return out


def prefixed(form: str) -> tuple[Morph, ...]:
    """Verbs with one or two upasargas that the kosha lacks, forward-derived with the prefixes."""
    found: list[Morph] = []
    for u1, rem1 in _splits(form):
        found.extend(_try_prefixes(form, (u1,), rem1))
        if not found:
            for u2, rem2 in _splits(rem1):
                found.extend(_try_prefixes(form, (u1, u2), rem2))
    return tuple(found)


# (ending of form, ending of stem, genders to try)
_ENDINGS = (
    ("अस्", "अ", ("पुंलिङ्ग",)), ("अम्", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")), ("एन", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")),
    ("आय", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")), ("आत्", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")),
    ("अस्य", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")), ("ए", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")),
    ("आस्", "अ", ("पुंलिङ्ग",)), ("आन्", "अ", ("पुंलिङ्ग",)), ("ऐस्", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")),
    ("आनि", "अ", ("नपुंसकलिङ्ग",)), ("आनाम्", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")), ("एषु", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")),
    ("आ", "आ", ("स्त्रीलिङ्ग",)), ("आम्", "आ", ("स्त्रीलिङ्ग",)), ("अया", "आ", ("स्त्रीलिङ्ग",)),
    ("इस्", "इ", ("पुंलिङ्ग", "स्त्रीलिङ्ग")), ("इम्", "इ", ("पुंलिङ्ग", "स्त्रीलिङ्ग")),
    ("एण", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")), ("आणाम्", "अ", ("पुंलिङ्ग", "नपुंसकलिङ्ग")),
    ("आणि", "अ", ("नपुंसकलिङ्ग",)), ("ईस्", "इन्", ("पुंलिङ्ग",)), ("ई", "इन्", ("पुंलिङ्ग",)),
    ("ई", "ई", ("स्त्रीलिङ्ग",)), ("ईम्", "ई", ("स्त्रीलिङ्ग",)), ("उस्", "उ", ("पुंलिङ्ग", "स्त्रीलिङ्ग")),
)
_BUDGET_S = 0.005


def generated_nominals(form: str) -> tuple[Morph, ...]:
    sounds = lipi.varnas(form)
    start = time.perf_counter()
    found: list[Morph] = []
    for ending, stem_end, lingas in _ENDINGS:
        ev = lipi.varnas(ending)
        if len(sounds) <= len(ev) + 1 or sounds[-len(ev):] != ev:
            continue
        stem = lipi.from_varnas(sounds[:-len(ev)] + lipi.varnas(stem_end))
        for linga in lingas:
            for pada, template in bridge.subanta_paradigm(stem, linga):
                if time.perf_counter() - start > _BUDGET_S:
                    return tuple(found)
                if any(d.text == form for d in bridge.derive(pada)):
                    found.append(replace(template, form=form))
    return tuple(found)
