"""Forward-derived analyses for forms the kosha does not list (source "generated").

Every candidate here is only a guess at vidyut ARGUMENTS; it is kept only when a forward
vidyut-prakriya derivation from those arguments yields exactly the form.
"""

from __future__ import annotations

import time
from dataclasses import replace
from functools import lru_cache

from mayur import bridge, lipi
from mayur.model import Morph
from mayur.terms import NONFINITE_KRT, PARTICIPLE_KRT

_GOOD_KRT = frozenset(PARTICIPLE_KRT) | frozenset(NONFINITE_KRT)

_VOWEL_SIGNS = {"ा": "आ", "ि": "इ", "ी": "ई", "ु": "उ", "ू": "ऊ", "ृ": "ऋ", "े": "ए", "ै": "ऐ", "ो": "ओ", "ौ": "औ"}
_STOP_FINALS = ("स्", "ष्", "र्", "ः", "द्", "त्", "न्", "ण्", "ञ्", "ङ्", "म्", "ं", "ज्", "च्", "ल्", "ब्", "भ्")


@lru_cache(maxsize=None)
def _surfaces_by_first() -> dict[str, tuple]:
    table: dict[str, list] = {}
    for u, wv, starts in _surface_varnas():
        table.setdefault(wv[0], []).append((u, wv, starts))
    return {k: tuple(v) for k, v in table.items()}


@lru_cache(maxsize=None)
def _surface_varnas() -> tuple[tuple[str, tuple[str, ...], tuple[tuple[str, ...], ...]], ...]:
    """(upasarga, written prefix varnas, remainder-start varnas) for all upasargas, computed once."""
    return tuple((u, lipi.varnas(w), tuple(lipi.varnas(s) for s in starts))
                 for u in bridge.UPASARGA_CODE for w, starts in _surfaces(u))


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
        long_ = "ई" if last == "इ" else "ऊ"
        out.append((v[:-1] + (long_,), ((last,), (long_,))))  # परि + ईक्ष् -> परीक्ष्
    return tuple((lipi.from_varnas(p), tuple(lipi.from_varnas(s) for s in starts)) for p, starts in out)


@lru_cache(maxsize=100_000)
def _splits(form: str) -> tuple[tuple[str, str], ...]:
    """(upasarga, remainder) candidates for ``form``."""
    sounds = lipi.varnas(form)
    out = []
    for u, wv, starts in _surfaces_by_first().get(sounds[0] if sounds else "", ()):
        if len(wv) < len(sounds) and sounds[:len(wv)] == wv:
            rest = sounds[len(wv):]
            for s in starts:
                out.append((u, lipi.from_varnas(s + rest)))
            for undone in _unretroflex(rest):
                out.append((u, lipi.from_varnas(undone)))
    return tuple(dict.fromkeys(out))


_DENTAL = {"ट्": "त्", "ठ्": "थ्", "ण्": "न्"}


def _unretroflex(rest: tuple[str, ...]) -> tuple[tuple[str, ...], ...]:
    """The remainder as the root stands alone, before the prefix's ष / ण (8.3.65 उपसर्गात् सुनोति...,
    8.4.14 उपसर्गादसमासेऽपि णोपदेशस्य): ष्ठित -> स्थित, णम -> नम. Forward derivation checks it."""
    out = []
    if rest and rest[0] == "ष्":
        tail = rest[1:]
        if tail and tail[0] in _DENTAL:
            tail = (_DENTAL[tail[0]],) + tail[1:]
        out.append(("स्",) + tail)
        if "ण्" in tail[:4]:  # 8.4.1 after the restored ष: विषण्ण -> सन्न (वि + सद् + क्त)
            out.append(("स्",) + tuple("न्" if s == "ण्" else s for s in tail[:4]) + tail[4:])
    if rest and rest[0] == "ण्":
        out.append(("न्",) + rest[1:])
    if len(rest) > 1 and rest[0] == "च्" and rest[1] == "छ्":  # 6.1.73 छे च: प्र + छादि -> प्रच्छाद्य
        out.append(rest[1:])
    if len(rest) > 1 and rest[0] == "अ" and rest[1] == "ष्":  # augment: अभ्यषिञ्चत् -> असिञ्चत्
        out.append(("अ", "स्") + rest[2:])
    return tuple(out)


def _lemma(upasargas: tuple[str, ...], root: str) -> str:
    return "".join(upasargas) + root


def _lyap_from_verbs(form: str, upasargas: tuple[str, ...], remainder: str) -> list[Morph]:
    """परित्यज्य: the kosha lacks त्यज्य, so find the dhatu through a present (त्यजति / चिन्तयति)
    and forward-derive its ल्यप् with the upasargas."""
    if remainder.endswith("्य"):
        base = remainder[: -len("्य")]
        probes: tuple[str, ...] = (base + "ति", base + "यति", base + "ते", base + "यते")
    elif remainder.endswith("य") and len(remainder) > 2:  # ज्ञाय: a vowel-final root, find it via ज्ञात्वा
        base = remainder[:-1]
        probes = (base + "त्वा", base + "ति", base + "यति")
    else:
        return []
    out: list[Morph] = []
    seen: set[str] = set()
    for probe in probes:
        for entry in bridge.lookup(probe):
            if entry.entry == "basic" or (entry.entry == "krdanta" and entry.morph.krt != "क्त्वा"):
                continue
            if any(u in _GATI_WITH_KR for u in upasargas) and (entry.morph.root or entry.morph.lemma) != "कृ":
                continue
            key = repr(bridge.dhatu_of(entry))
            if key in seen:
                continue
            seen.add(key)
            pada = bridge.ktva_of_verb(entry, upasargas)
            if pada is not None and any(t == form for t in bridge.derived_texts(pada)):
                m = entry.morph
                prefixes = upasargas + m.prefixes
                out.append(Morph(form=form, lemma=_lemma(prefixes, m.root or m.lemma), kind="avyaya", root=m.root,
                                 dhatu=m.dhatu, gana=m.gana, prefixes=prefixes, krt="ल्यप्", root_gloss=m.root_gloss,
                                 source="generated", quality=3, handle=pada))
    return out


# सत्, अलम् and नमस् are gatis only before कृ (1.4.63 आदरानादरयोः सदसती, 1.4.64 भूषणेऽलम्,
# 1.4.74 साक्षात्प्रभृतीनि च): सत्कृत्य, अलंकृत, नमस्कृत्य; never सत् + गमय.
_GATI_WITH_KR = frozenset({"सत्", "अलम्", "नमस्"})


def _try_prefixes(form: str, upasargas: tuple[str, ...], remainder: str) -> list[Morph]:
    out = _lyap_from_verbs(form, upasargas, remainder) if form.endswith("य") else []
    for entry in bridge.lookup(remainder):
        m = entry.morph
        if any(u in _GATI_WITH_KR for u in upasargas) and (m.root or m.lemma) != "कृ":
            continue
        if entry.entry == "tinanta":
            pada = bridge.prefixed_tinanta(entry, upasargas)
        elif entry.entry == "krdanta" and m.krt in _GOOD_KRT:
            pada = bridge.prefixed_krdanta(entry, upasargas)
            if m.krt in ("यत्", "ण्यत्", "क्यप्") and form.endswith("्य"):
                # the same remainder may be the ल्यप् absolutive of the prefixed root (7.1.37)
                ktva = bridge.prefixed_krdanta(entry, upasargas, as_ktva=True)
                if ktva is not None and any(t == form for t in bridge.derived_texts(ktva)):
                    prefixes = upasargas + m.prefixes
                    out.append(replace(m, form=form, lemma=_lemma(prefixes, m.root or m.lemma), prefixes=prefixes,
                                       krt="ल्यप्", kind="avyaya", linga=None, vibhakti=None, vacana=None,
                                       source="generated", quality=3, handle=ktva))
        else:
            continue
        if pada is None:
            continue
        if any(t == form for t in bridge.derived_texts(pada)):
            prefixes = upasargas + m.prefixes
            krt = "ल्यप्" if m.krt == "क्त्वा" else m.krt
            out.append(replace(m, form=form, lemma=_lemma(prefixes, m.root or m.lemma), prefixes=prefixes, krt=krt,
                               source="generated", quality=3, handle=pada))
    return out


@lru_cache(maxsize=100_000)
def prefixed(form: str) -> tuple[Morph, ...]:
    """Verbs and participles with one or two upasargas, forward-derived with the prefixes."""
    found: list[Morph] = []
    for u1, rem1 in _splits(form):
        found.extend(_try_prefixes(form, (u1,), rem1))
        if not found:
            for u2, rem2 in _splits(rem1):
                found.extend(_try_prefixes(form, (u1, u2), rem2))
    return tuple(dict.fromkeys(found))


# endings of participles and absolutives (क्त, क्तवतु, शतृ, शानच्, ल्यप्, क्त्वा, तव्य, अनीयर्) in some case
_VERBAL_ENDING_SOUNDS = frozenset({"त्", "न्", "म्", "य्", "व्"})


def looks_verbal(form: str) -> bool:
    """Gate for the always-on prefixed search: begins with an upasarga, and a त/न/म/य/व
    (participle or absolutive suffix) stands in its last four sounds."""
    sounds = lipi.varnas(form)
    if len(sounds) < 5 or not _splits(form):
        return False
    return any(s in _VERBAL_ENDING_SOUNDS for s in sounds[-5:-1])


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
    ("उवि", "ऊ", ("स्त्रीलिङ्ग",)), ("उवस्", "ऊ", ("स्त्रीलिङ्ग",)), ("उवम्", "ऊ", ("स्त्रीलिङ्ग",)),
    ("ई", "ई", ("स्त्रीलिङ्ग",)), ("ईम्", "ई", ("स्त्रीलिङ्ग",)), ("उस्", "उ", ("पुंलिङ्ग", "स्त्रीलिङ्ग")),
    # proper names in the other cases (शण्डामर्कौ, दाशरथेस्, तुम्बरोस्, जनमेजयाभ्याम्)
    ("औ", "अ", ("पुंलिङ्ग",)), ("आभ्याम्", "अ", ("पुंलिङ्ग",)), ("अयोस्", "अ", ("पुंलिङ्ग",)),
    ("एभ्यस्", "अ", ("पुंलिङ्ग",)), ("एस्", "इ", ("पुंलिङ्ग",)), ("इना", "इ", ("पुंलिङ्ग",)),
    ("इणा", "इ", ("पुंलिङ्ग",)), ("उणा", "उ", ("पुंलिङ्ग",)),
    ("अये", "इ", ("पुंलिङ्ग",)), ("अयस्", "इ", ("पुंलिङ्ग",)), ("ईन्", "इ", ("पुंलिङ्ग",)),
    ("ओस्", "उ", ("पुंलिङ्ग",)), ("उना", "उ", ("पुंलिङ्ग",)), ("अवे", "उ", ("पुंलिङ्ग",)),
    ("उम्", "उ", ("पुंलिङ्ग",)), ("अवस्", "उ", ("पुंलिङ्ग",)), ("ऊन्", "उ", ("पुंलिङ्ग",)),
    ("आयास्", "आ", ("स्त्रीलिङ्ग",)), ("आयाम्", "आ", ("स्त्रीलिङ्ग",)), ("आयै", "आ", ("स्त्रीलिङ्ग",)),
    ("आसु", "आ", ("स्त्रीलिङ्ग",)), ("आभिस्", "आ", ("स्त्रीलिङ्ग",)),
)
_MIN_SOUNDS = 4  # never guess a stem for shorter forms
_BUDGET_S = 0.005


def generated_nominals(form: str) -> tuple[Morph, ...]:
    sounds = lipi.varnas(form)
    if len(sounds) < _MIN_SOUNDS:
        return ()
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
                if any(t == form for t in bridge.derived_texts(pada)):
                    found.append(replace(template, form=form))
    return tuple(found)


from mayur.lexicon_special import (  # noqa: E402,F401  (re-exported)
    anvadesha, avyaya_compound, indefinite, nanj_stems, numerals, sa_esha, tasi_forms)
