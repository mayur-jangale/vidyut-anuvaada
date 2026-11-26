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
        out.append((v[:-1] + ("ई" if last == "इ" else "ऊ",), (("इ",) if last == "इ" else ("उ",),)))
    return tuple((lipi.from_varnas(p), tuple(lipi.from_varnas(s) for s in starts)) for p, starts in out)


@lru_cache(maxsize=100_000)
def _splits(form: str) -> tuple[tuple[str, str], ...]:
    """(upasarga, remainder) candidates for ``form``."""
    sounds = lipi.varnas(form)
    out = []
    for u, wv, starts in _surface_varnas():
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
    if rest and rest[0] == "ण्":
        out.append(("न्",) + rest[1:])
    if len(rest) > 1 and rest[0] == "अ" and rest[1] == "ष्":  # augment: अभ्यषिञ्चत् -> असिञ्चत्
        out.append(("अ", "स्") + rest[2:])
    return tuple(out)


def _lemma(upasargas: tuple[str, ...], root: str) -> str:
    return "".join(upasargas) + root


def _lyap_from_verbs(form: str, upasargas: tuple[str, ...], remainder: str) -> list[Morph]:
    """परित्यज्य: the kosha lacks त्यज्य, so find the dhatu through a present (त्यजति / चिन्तयति)
    and forward-derive its ल्यप् with the upasargas."""
    if not remainder.endswith("्य"):
        return []
    base = remainder[: -len("्य")]
    out: list[Morph] = []
    seen: set[str] = set()
    for probe in (base + "ति", base + "यति", base + "ते", base + "यते"):
        for entry in bridge.lookup(probe):
            if entry.entry != "tinanta" or repr(entry.morph.handle.dhatu_entry.dhatu) in seen:
                continue
            seen.add(repr(entry.morph.handle.dhatu_entry.dhatu))
            pada = bridge.ktva_of_verb(entry, upasargas)
            if pada is not None and any(d.text == form for d in bridge.derive(pada)):
                m = entry.morph
                prefixes = upasargas + m.prefixes
                out.append(Morph(form=form, lemma=_lemma(prefixes, m.root or m.lemma), kind="avyaya", root=m.root,
                                 dhatu=m.dhatu, gana=m.gana, prefixes=prefixes, krt="ल्यप्", root_gloss=m.root_gloss,
                                 source="generated", quality=3, handle=pada))
    return out


def _try_prefixes(form: str, upasargas: tuple[str, ...], remainder: str) -> list[Morph]:
    out = _lyap_from_verbs(form, upasargas, remainder) if form.endswith("्य") else []
    for entry in bridge.lookup(remainder):
        m = entry.morph
        if entry.entry == "tinanta":
            pada = bridge.prefixed_tinanta(entry, upasargas)
        elif entry.entry == "krdanta" and m.krt in _GOOD_KRT:
            pada = bridge.prefixed_krdanta(entry, upasargas)
            if m.krt in ("यत्", "ण्यत्", "क्यप्") and form.endswith("्य"):
                # the same remainder may be the ल्यप् absolutive of the prefixed root (7.1.37)
                ktva = bridge.prefixed_krdanta(entry, upasargas, as_ktva=True)
                if ktva is not None and any(d.text == form for d in bridge.derive(ktva)):
                    prefixes = upasargas + m.prefixes
                    out.append(replace(m, form=form, lemma=_lemma(prefixes, m.root or m.lemma), prefixes=prefixes,
                                       krt="ल्यप्", kind="avyaya", linga=None, vibhakti=None, vacana=None,
                                       source="generated", quality=3, handle=ktva))
        else:
            continue
        if pada is None:
            continue
        if any(d.text == form for d in bridge.derive(pada)):
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


# अन्वादेश substitutes of इदम् / एतद् (2.4.34 द्वितीयाटौस्स्वेनः): form -> (लिङ्ग, विभक्ति, वचन) list
_P, _S, _N = "पुंलिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग"
_ENA = {
    "एनम्": ((_P, "द्वितीया", "एकवचन"),), "एनाम्": ((_S, "द्वितीया", "एकवचन"),),
    "एनत्": ((_N, "द्वितीया", "एकवचन"),), "एनद्": ((_N, "द्वितीया", "एकवचन"),),
    "एनौ": ((_P, "द्वितीया", "द्विवचन"),), "एने": ((_S, "द्वितीया", "द्विवचन"), (_N, "द्वितीया", "द्विवचन")),
    "एनान्": ((_P, "द्वितीया", "बहुवचन"),), "एनास्": ((_S, "द्वितीया", "बहुवचन"),),
    "एनानि": ((_N, "द्वितीया", "बहुवचन"),),
    "एनेन": ((_P, "तृतीया", "एकवचन"), (_N, "तृतीया", "एकवचन")), "एनया": ((_S, "तृतीया", "एकवचन"),),
    "एनयोस्": tuple((g, v, "द्विवचन") for g in (_P, _S, _N) for v in ("षष्ठी", "सप्तमी")),
}
ENA_NOTE = ("अन्वादेश substitute एन by 2.4.34 (द्वितीयाटौस्स्वेनः); vidyut's Python API does not apply "
            "2.4.34, so no derivation was run")


def anvadesha(form: str) -> tuple[Morph, ...]:
    """एनम् etc.: special-table analyses as इदम् / एतद् (no vidyut derivation exists)."""
    feats = _ENA.get(form, ())
    return tuple(Morph(form=form, lemma=lemma, kind="subanta", linga=g, vibhakti=v, vacana=n,
                       source="special", quality=3, handle=("special", ENA_NOTE))
                 for lemma in ("इदम्", "एतद्", "एनद्") for g, v, n in feats)


SA_NOTE = ("सु is elided after सस् / एषस् before a consonant (6.1.132 एतत्तदोः सुलोपोऽकोरनञ्समासे हलि); "
           "this is a sentence-level rule vidyut's Python API does not apply; the pada {base} is kosha-listed")


def sa_esha(form: str) -> tuple[Morph, ...]:
    """स / एष: तद् / एतद् प्रथमा एकवचन पुंलिङ्ग with सु-lopa (6.1.132)."""
    if form not in ("स", "एष"):
        return ()
    lemma = "तद्" if form == "स" else "एतद्"
    return (Morph(form=form, lemma=lemma, kind="subanta", linga=_P, vibhakti="प्रथमा", vacana="एकवचन",
                  source="special", quality=3, handle=("special", SA_NOTE.format(base=form + "स्"))),)


_PARTICLES = ("चित्", "चिद्", "चन")
_INDEF_BASES = frozenset({"किम्", "क", "क्व", "कदा", "कथम्", "कुत्र", "कुतस्", "कति"})
# the junction reversed: कश्+चित् <- कस्, किं+चित् <- किम्, कञ्+चन? (कं) <- कम्
_JUNCTION = (("ंश्", "न्"), ("श्", "स्"), ("ं", "म्"), ("ञ्", "म्"))


def indefinite(form: str, lookup) -> tuple[Morph, ...]:
    """कश्चित्, केचिद्, क्वचित्, किंचन ...: the किम् form (looked up with ``lookup``) + particle."""
    out: list[Morph] = []
    for part in _PARTICLES:
        if not form.endswith(part) or len(form) <= len(part):
            continue
        head = form[: -len(part)]
        bases = [head] + [head[: -len(a)] + b for a, b in _JUNCTION if head.endswith(a)]
        for base in bases:
            for m in lookup(base):
                if m.lemma not in _INDEF_BASES or m.quality < 2:
                    continue
                if m.kind == "subanta":
                    lemma = "कश्चन" if part == "चन" else "कश्चित्"
                else:
                    lemma = head + ("चन" if part == "चन" else "चिद्")  # cited as क्वचिद्, कदाचिद्
                out.append(replace(m, form=form, lemma=lemma, source="generated", quality=3,
                                   handle=("particle", m, part)))
    return tuple(out)
