"""Analyses outside the kosha's paradigms: अन्वादेश एन-, सुलोप स/एष, indefinites with चित्/चन,
indeclinable compounds, तसि ablatives, नञ् stems, -न् numerals. All strings Devanagari.

Each says in its proof what was derived through vidyut and what was not.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge, lipi
from mayur.model import Morph


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
_INDEF_BASES = frozenset({"किम्", "क", "क्व", "कदा", "कथम्", "कुत्र", "कुतस्", "कति", "कर्हि", "कुह"})
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


_PARTICLE_ENDS = (("अपि", ("पि",)), ("तु", ("तु",)), ("च", ("च",)), ("उ", ("ु", "उ")))
_YATHA = ("यथा",)  # avyayībhāva with यथा (2.1.7 यथाऽसादृश्ये)
AVYAYA_NOTE = ("indeclinable compound of kosha-listed members ({parts}); the joining (avyayībhāva 2.1.6 "
               "or a particle in samhita) is not derived through vidyut's Python API")


_VOWELS = frozenset({"अ", "आ", "इ", "ई", "उ", "ऊ", "ए", "ओ"})
_PRONOMINAL = frozenset({"किम्", "क", "क्व", "कदा", "कथम्", "यद्", "तद्"})


def _avyaya(form: str, parts: str) -> Morph:
    return Morph(form=form, lemma=form, kind="avyaya", source="generated", quality=2,
                 handle=("special", AVYAYA_NOTE.format(parts=parts)))


def avyaya_compound(form: str, pada_lookup, stem_lookup) -> tuple[Morph, ...]:
    """किंतु, किंच, क्वापि, किमु, यथाशक्ति, यथाक्रमम्: members are looked up, the join is re-run forward
    with ``mayur.sandhi``; lemma = the word (as the corpus cites it)."""
    from mayur import sandhi

    out: list[Morph] = []
    for particle, ends in _PARTICLE_ENDS:
        if not form.endswith(ends) or len(form) < 3:
            continue
        sounds = lipi.varnas(form)
        plen = len(lipi.varnas(particle))
        for cut in range(max(1, len(sounds) - plen - 1), min(len(sounds), len(sounds) - plen + 2)):
            base = sounds[:cut]
            heads = [base]
            if base[-1] in _VOWELS:
                heads += [base[:-1] + (v,) for v in ("अ", "आ") if v != base[-1]]
            for hv in heads:
                h = lipi.from_varnas(hv)
                h = h[:-1] + "म्" if h.endswith("ं") else h
                if h == form or not any(m.kind == "avyaya" or m.lemma in _PRONOMINAL
                                        for m in pada_lookup(h) if m.quality >= 2):
                    continue
                if any(o.text == form for o in sandhi.outcomes(h, particle)):
                    out.append(_avyaya(form, h + " + " + particle))
        if out:
            return tuple(out[:1])
    for first in _YATHA:
        if form.startswith(first) and len(form) > len(first) + 1:
            rest = form[len(first):]
            bare = rest[:-2] if rest.endswith("म्") else rest
            if stem_lookup(bare):
                return (_avyaya(form, first + " + " + bare),)
    return ()


TASI_NOTE = "the ablative sense of तसि (5.4.44) is recorded as पञ्चमी, as the corpus tags it"


def tasi_forms(form: str, stem_lookup) -> tuple[Morph, ...]:
    """अनुरागतस्, दैवतस्: stem + तसि, forward-derived; analysed as पञ्चमी in the stem's genders."""
    if not form.endswith("तस्") or len(form) < 5:
        return ()
    stem = form[: -len("तस्")]  # अनुरागतस् -> अनुराग (the inherent अ stays)
    if len(lipi.varnas(stem)) < 3:
        return ()
    cands = [m for m in stem_lookup(stem) if m.quality >= 2 and m.kind == "stem" and not m.krt]
    if not cands:
        return ()
    pada = bridge.tasi_pada(stem)
    if pada is None or form not in bridge.derived_texts(pada):
        return ()
    lingas = {"पुंलिङ्ग", "नपुंसकलिङ्ग", "स्त्रीलिङ्ग"}
    return tuple(Morph(form=form, lemma=cands[0].lemma, kind="subanta", linga=g, vibhakti="पञ्चमी",
                       vacana=n, source="generated", quality=2, handle=pada)
                 for g in sorted(lingas) for n in ("एकवचन", "बहुवचन"))


NANJ_NOTE = ("नञ्-compound stem अ/अन् + {rest} (2.2.6 नञ्, 6.3.73 नलोपो नञः, 6.3.74 तस्मान्नुडचि); the trace "
             "is the derivation of {rest}; the compound itself is not derived through vidyut's Python API")


def nanj_stems(form: str, stem_lookup) -> tuple[Morph, ...]:
    """अमित, अनासव as compound members: अ + a consonant-initial stem, अन् + a vowel-initial one."""
    sounds = lipi.varnas(form)
    if len(sounds) < 4 or sounds[0] != "अ":
        return ()
    rest = lipi.from_varnas(sounds[1:]) if not sounds[1] in _VOWELS else ""
    if sounds[1] == "न्" and len(sounds) > 2 and sounds[2] in _VOWELS:
        rest = lipi.from_varnas(sounds[2:])
    if not rest:
        return ()
    out = []
    for m in stem_lookup(rest):
        if m.quality >= 2 and isinstance(m.handle, tuple):
            out.append(replace(m, form=form, lemma=form, stem=form, root=None, krt=None, prefixes=(),
                               source="generated", quality=2,
                               handle=("nanj", m.handle[1], NANJ_NOTE.format(rest=rest))))
            break
    return tuple(out)


# numerals in -न् that the kosha lists only under an अ-stem (पञ्च for पञ्चन्)
_N_NUMERALS = ("पञ्चन्", "सप्तन्", "अष्टन्", "नवन्", "दशन्", "एकादशन्", "द्वादशन्", "त्रयोदशन्", "चतुर्दशन्",
               "पञ्चदशन्", "षोडशन्", "सप्तदशन्", "अष्टादशन्")


@lru_cache(maxsize=1)
def _numeral_table() -> dict[str, tuple[Morph, ...]]:
    """Every forward-derived form of the -न् numerals (computed once, about 900 derivations)."""
    table: dict[str, list[Morph]] = {}
    for stem in _N_NUMERALS:
        for linga in ("पुंलिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग"):
            for pada, template in bridge.subanta_paradigm(stem, linga):
                if template.vacana != "बहुवचन":
                    continue
                for text in bridge.derived_texts(pada):
                    table.setdefault(text, []).append(replace(template, form=text, quality=3))
    return {k: tuple(v) for k, v in table.items()}


def numerals(form: str) -> tuple[Morph, ...]:
    return _numeral_table().get(form, ()) if form[:1] in "पसअनदएचषत्" else ()
