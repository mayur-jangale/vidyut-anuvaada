"""Verb forms and agent nouns the kosha lacks, found by lookup of a sibling form and forward
generation; never by running a rule backward. All strings Devanagari.

* Augmentless past after मा (6.4.74 न माङ्योगे): मा भूत्. The augmented form (अभूत्) is looked up,
  and vidyut derives the same form without the augment.
* ārṣa voice endings: त्यजामहे, क्षमेत्, क्रोशमानम्. Epic Sanskrit often uses the आत्मनेपद endings on
  a परस्मैपद root and the reverse, against 1.3.12–93. vidyut will not derive these, so the form
  is related to its regular sibling (त्यजामस्) by the two sets of endings and LABELLED ārṣa: it is
  an analysis, not a proof, and the word stays unverified.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any, Callable, Sequence

from mayur import bridge, lipi
from mayur.model import Morph

Lookup = Callable[[str], Sequence[Morph]]

ARSHA = "arsha"
AUGMENT_NOTE = "without the augment, as after मा (6.4.74 न माङ्योगे)"
AUGMENT_ARSHA_NOTE = ("ārṣa: a past form without its augment after an upasarga (6.4.75 बहुलं छन्दस्यमाङ्योगेऽपि allows "
                      "it in the Veda; the classical rule 6.4.74 only after मा); epic usage, labelled and not derived")
ARSHA_NOTE = ("ārṣa: the {got} ending on a root that takes {want} by 1.3.12–93 (regular form {regular}); "
              "epic usage, labelled and not derived")
# (आत्मनेपद ending, परस्मैपद ending, person, number) as sounds, longest first. The person and number are
# those of BOTH endings: a sibling in another slot (क्रामेत 2nd plural for क्रामेत्) is not this pair.
_P1, _P2, _P3 = "प्रथमपुरुष", "मध्यमपुरुष", "उत्तमपुरुष"
_SG, _DU, _PL = "एकवचन", "द्विवचन", "बहुवचन"
_PAIRS = tuple((lipi.varnas(a), lipi.varnas(p), who, n) for a, p, who, n in (
    ("महे", "मस्", _P3, _PL), ("वहे", "वस्", _P3, _DU), ("न्ताम्", "न्तु", _P1, _PL), ("न्ते", "न्ति", _P1, _PL),
    ("ध्वम्", "त", _P2, _PL), ("ध्वे", "थ", _P2, _PL), ("न्त", "न्", _P1, _PL), ("ताम्", "तु", _P1, _SG),
    ("ते", "ति", _P1, _SG), ("से", "सि", _P2, _SG), ("एत", "एत्", _P1, _SG), ("त", "त्", _P1, _SG),
    ("ए", "आमि", _P3, _SG),
    # optative and imperative of the first person, the second singular optative, and the endings
    # without न् of the classes that have no अ before them (आश्नुवन् for आश्नुवत, प्रपद्येम for प्रपद्येमहि)
    ("एमहि", "एम", _P3, _PL), ("एवहि", "एव", _P3, _DU), ("आमहै", "आम", _P3, _PL), ("आवहै", "आव", _P3, _DU),
    ("एथास्", "एस्", _P2, _SG), ("एय", "एयम्", _P3, _SG), ("एरन्", "एयुस्", _P1, _PL),
    ("अते", "अन्ति", _P1, _PL), ("अत", "अन्", _P1, _PL), ("अताम्", "अन्तु", _P1, _PL)))
LYAP_NOTE = ("ārṣa: an absolutive in -य without a prefix (7.1.37 समासेऽनञ्पूर्वे क्त्वो ल्यप् gives ल्यप् only after a "
             "prefix; the regular form has क्त्वा); epic usage, labelled and not derived")
_SVA, _SHVA = lipi.varnas("स्व"), lipi.varnas("ष्व")
_PARTICIPLE = (lipi.varnas("अमान"), lipi.varnas("आन"))  # शानच् stems: क्रोशमान, दर्शयान


def _swap(sounds: tuple[str, ...], old: tuple[str, ...], new: tuple[str, ...]) -> str:
    return lipi.from_varnas(sounds[: len(sounds) - len(old)] + new)


def augmentless(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """भूत् of अभूत्: the augmented लुङ्/लङ् form is in the kosha; vidyut derives it without the augment."""
    from vidyut.prakriya import Pada

    sounds = lipi.varnas(form)
    if not sounds or lipi.varnas("अ")[0] == sounds[0] or len(sounds) < 3:
        return ()
    out = []
    for entry in bridge.lookup("अ" + form):
        e = entry.morph.handle
        if entry.entry != "tinanta" or entry.morph.lakara not in ("लुङ्", "लङ्"):
            continue
        pada = Pada.Tinanta(dhatu=e.dhatu_entry.dhatu, prayoga=e.prayoga, lakara=e.lakara, purusha=e.purusha,
                            vacana=e.vacana, skip_at_agama=True)
        if form in bridge.derived_texts(pada):
            out.append(replace(entry.morph, form=form, source="generated", quality=2, handle=pada))
    return tuple(dict.fromkeys(out))


def _finite(form: str) -> list[Morph]:
    """Finite analyses of ``form`` in the kosha (a dictionary probe: cheap enough for every word)."""
    return [e.morph for e in bridge.lookup(form) if e.entry == "tinanta"]


def _has_prefix(form: str) -> bool:
    from mayur.lexicon_gen import _splits

    return bool(_splits(form))


def _prefixed_finite(form: str, padas: Lookup) -> list[Morph]:
    """Finite analyses of a prefixed verb form (forward-generated with its upasargas)."""
    return [m for m in padas(form) if m.kind == "tinanta" and m.quality >= 2]


def arsha_voice(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """Finite forms and शानच् participles with the other voice's endings (see the module docstring)."""
    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for atmane, parasmai, who, number in _PAIRS:
        for old, new, got, want in ((atmane, parasmai, "आत्मनेपद", "परस्मैपद"), (parasmai, atmane, "परस्मैपद", "आत्मनेपद")):
            if len(sounds) > len(old) + 1 and sounds[-len(old):] == old:
                regular = _swap(sounds, old, new)
                siblings = _finite(regular) or (_prefixed_finite(regular, padas) if _has_prefix(form) else [])
                for m in siblings:
                    if (m.purusha, m.vacana) != (who, number):
                        continue
                    note = ARSHA_NOTE.format(got=got, want=want, regular=lipi.pausa(regular))
                    out.append(replace(m, form=form, source=ARSHA, quality=1, handle=("special", note)))
    if len(sounds) > 4 and sounds[-3:] in (_SVA, _SHVA):  # गच्छस्व, शृणुष्व: the regular imperative is गच्छ, शृणु
        regular = lipi.from_varnas(sounds[:-3])
        for m in _finite(regular) or (_prefixed_finite(regular, padas) if _has_prefix(form) else []):
            if (m.lakara, m.purusha, m.vacana) == ("लोट्", _P2, _SG):
                note = ARSHA_NOTE.format(got="आत्मनेपद", want="परस्मैपद", regular=regular)
                out.append(replace(m, form=form, source=ARSHA, quality=1, handle=("special", note)))
    if len(sounds) > 3 and sounds[-1] == "अ":  # समुत्तिष्ठ: the rule form is समुत्तिष्ठस्व (1.3.22 समवप्रविभ्यः स्थः)
        regular = form + "स्व"
        for m in _finite(regular) or (_prefixed_finite(regular, padas) if _has_prefix(form) else []):
            if (m.lakara, m.purusha, m.vacana) == ("लोट्", _P2, _SG):
                note = ARSHA_NOTE.format(got="परस्मैपद", want="आत्मनेपद", regular=regular)
                out.append(replace(m, form=form, source=ARSHA, quality=1, handle=("special", note)))
    return tuple(dict.fromkeys(out))


def arsha_participle(form: str, generated: Lookup, padas: Lookup) -> tuple[Morph, ...]:
    """क्रोशमानम्: a शानच् participle of a परस्मैपद root; its stem + न्ति is the regular present."""
    out: list[Morph] = []
    for g in generated(form):
        stem = lipi.varnas(g.stem or g.lemma)
        for suffix in _PARTICIPLE:
            if len(stem) > len(suffix) + 1 and stem[-len(suffix):] == suffix:
                regular = lipi.from_varnas(stem[: len(stem) - len(suffix)] + lipi.varnas("अन्ति"))
                for m in _finite(regular):
                    note = ARSHA_NOTE.format(got="आत्मनेपद (शानच्)", want="परस्मैपद (शतृ)", regular=lipi.pausa(regular))
                    out.append(replace(g, lemma=m.lemma, root=m.root, dhatu=m.dhatu, gana=m.gana, prefixes=m.prefixes,
                                       krt="शानच्", root_gloss=m.root_gloss, source=ARSHA, quality=1,
                                       handle=("special", note)))
    return tuple(dict.fromkeys(out))


# Words that join a verb as गति: प्रादुस्, आविस्, नमस् … before कृ, भू, अस् (1.4.61 ऊर्यादिच्विडाचश्च,
# 1.4.74 साक्षात्प्रभृतीनि च); तिरस्, अन्तर् also before धा (1.4.71), अस्तम् before गम्/इ (1.4.68).
GATI_ROOTS = {"प्रादुस्": ("कृ", "भू", "अस्"), "आविस्": ("कृ", "भू", "अस्"), "नमस्": ("कृ",), "अलम्": ("कृ",),
              "सत्": ("कृ",), "साक्षात्": ("कृ",), "तिरस्": ("कृ", "भू", "धा"), "अन्तर्": ("धा", "भू", "इ", "गम्"),
              "अस्तम्": ("गम्", "इ", "या"), "पुरस्": ("कृ", "धा", "गम्"), "श्रत्": ("धा",)}  # 1.4.67 पुरोऽव्ययम्
CVI_ROOTS = ("कृ", "भू", "अस्")
GATI_NOTE = "{gati} is a गति ({rule}) joined to the verb form {verb} by sandhi; the verb form is derived by vidyut"


def _verbal(form: str, roots: Sequence[str], padas: Lookup) -> list[Morph]:
    found = [m for m in padas(form) if m.root in roots and m.quality >= 2 and (m.kind == "tinanta" or m.krt)]
    if form.endswith("य") and not any(m.krt == "ल्यप्" for m in found):
        # पुरोधाय, नमस्कृत्य: after a गति the absolutive takes ल्यप् (7.1.37), which vidyut derives after an
        # upasarga; प्र + the same remainder is that sibling (प्रधाय, प्रकृत्य)
        found += [replace(m, form=form, lemma=m.root or m.lemma, prefixes=tuple(m.prefixes[1:]))
                  for m in padas("प्र" + form) if m.krt == "ल्यप्" and m.root in roots and m.prefixes[:1] == ("प्र",)]
    return found


def gati_verbs(form: str, padas: Lookup, is_stem: Callable[[str], bool]) -> tuple[Morph, ...]:
    """प्रादुरासीत्, नमश्चकार, आविर्भूत; च्वि: वशीकृत, शुक्लीभवति (5.4.50, 7.4.32 अस्य च्वौ)."""
    from mayur import sandhi

    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for gati, roots in GATI_ROOTS.items():
        gv = lipi.varnas(gati)
        if sounds[: len(gv) - 1] != gv[:-1]:
            continue
        for n in (len(gv) - 1, len(gv), len(gv) + 1):
            rest = lipi.from_varnas(sounds[n:]) if 1 < n < len(sounds) - 1 else ""
            if rest and (sandhi.rejoin_matching([gati, rest], [True], form) is not None
                         or sandhi.rejoin_matching([gati, rest], [True], lipi.pausa(form)) is not None):
                for m in _verbal(rest, roots, padas):
                    note = GATI_NOTE.format(gati=gati, rule="1.4.61, 1.4.74", verb=rest)
                    out.append(replace(m, form=form, prefixes=(gati,) + tuple(m.prefixes), source="generated",
                                       quality=2, handle=("gati", note, m)))
    for i, v in enumerate(sounds):
        if v != "ई" or i < 2 or i > len(sounds) - 3:
            continue
        rest = lipi.from_varnas(sounds[i + 1:])
        verbal = _verbal(rest, CVI_ROOTS, padas)
        base = [lipi.from_varnas(sounds[:i] + (end,)) for end in ("अ", "आ", "इ", "ई")] if verbal else []
        stem = next((b for b in base if is_stem(b)), None)
        if stem is None:
            continue
        for m in verbal:
            cvi = lipi.from_varnas(sounds[: i + 1])
            note = GATI_NOTE.format(gati=f"{cvi} ({stem} + च्वि, 5.4.50, 7.4.32)", rule="1.4.61", verb=rest)
            out.append(replace(m, form=form, prefixes=(cvi,) + tuple(m.prefixes), source="generated", quality=2,
                               handle=("gati", note, m)))
    return tuple(dict.fromkeys(out))


def arsha_shatr(form: str) -> tuple[Morph, ...]:
    """स्मयन्: the परस्मैपद participle (शतृ) of a root that takes आत्मनेपद; its regular present is स्मयन्ते."""
    sounds = lipi.varnas(form)
    if len(sounds) < 4 or sounds[-2:] != ("अ", "न्"):
        return ()
    regular = lipi.from_varnas(sounds + ("त्", "ए"))
    out = []
    for m in _finite(regular):
        note = ARSHA_NOTE.format(got="परस्मैपद (शतृ)", want="आत्मनेपद (शानच्)", regular=lipi.pausa(regular))
        out.append(replace(m, form=form, kind="subanta", krt="शतृ", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन",
                           purusha=None, lakara=None, prayoga=None, source=ARSHA, quality=1, handle=("special", note)))
    return tuple(dict.fromkeys(out))


KRAM_NOTE = ("ārṣa: क्रम् without the long vowel that 7.3.76 क्रमः परस्मैपदेषु gives before the परस्मैपद endings "
             "(regular form {regular}); epic usage, labelled and not derived")
KRAM_SHATR_NOTE = ("शतृ of क्रम् with the long vowel of 7.3.76 क्रमः परस्मैपदेषु (शतृ is a परस्मैपद suffix, 1.4.99); "
                   "vidyut derives the stem with the short vowel ({short}), so this form is labelled, not proved")
_KRAM, _KRAAM = lipi.varnas("क्रम"), lipi.varnas("क्राम")


def kram_participle(form: str) -> tuple[Morph, ...]:
    """क्रामन्, क्रामन्तम्: the participle vidyut derives as क्रमन्, क्रमन्तम्."""
    sounds = lipi.varnas(form)
    if sounds[: len(_KRAAM)] != _KRAAM:
        return ()
    short = lipi.from_varnas(_KRAM + sounds[len(_KRAAM):])
    note = KRAM_SHATR_NOTE.format(short=lipi.pausa(short))
    return tuple(dict.fromkeys(
        replace(e.morph, form=form, source="generated", quality=2, handle=("special", note))
        for e in bridge.lookup(short) if e.entry == "krdanta" and e.morph.krt == "शतृ" and e.morph.root == "क्रम्"))


def kram_short(form: str) -> tuple[Morph, ...]:
    """क्रमेत्, क्रमति: epic forms of क्रम् with the short vowel; the regular sibling has क्राम्."""
    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for i in (0, 1):  # क्रमेत्, अक्रमत्
        if sounds[i: i + len(_KRAM)] == _KRAM:
            regular = lipi.from_varnas(sounds[:i] + _KRAAM + sounds[i + len(_KRAM):])
            note = KRAM_NOTE.format(regular=lipi.pausa(regular))
            out += [replace(m, form=form, source=ARSHA, quality=1, handle=("special", note))
                    for m in _finite(regular) if m.root == "क्रम्"]
    return tuple(dict.fromkeys(out))


def _labelled(form: str, padas: Lookup, generated: Lookup) -> list[Morph]:
    """The labelled (not derived) verbal analyses of an unprefixed form."""
    found = padas(form)
    regular = {(m.lemma, m.lakara, m.purusha, m.vacana) for m in found if m.kind == "tinanta" and m.quality >= 2}
    voice = [m for m in arsha_voice(form, padas) if (m.lemma, m.lakara, m.purusha, m.vacana) not in regular]
    out = [*kram_participle(form), *kram_short(form), *voice]  # (गमय is a rule form: no label for it)
    if not any(m.quality >= 2 for m in found):
        out += [*arsha_participle(form, generated, padas), *arsha_shatr(form), *arsha_shatr_oblique(form)]
    if not any(m.kind == "tinanta" for m in found):
        from mayur.lexicon_guna import epic_imperative, first_imperative

        out += [*arsha_thematic(form), *first_imperative(form, padas), *epic_imperative(form, padas)]
    if not any(m.kind == "tinanta" for m in found):  # प्रजायन्त: the past without its augment after an upasarga
        out += [replace(m, source=ARSHA, quality=1, handle=("special", AUGMENT_ARSHA_NOTE))
                for m in augmentless(form, padas)]
    return out


def prefixed_labelled(form: str, padas: Lookup, generated: Lookup) -> tuple[Morph, ...]:
    """अतिक्रमेत्, अतिक्रामन्: one or two upasargas before a verb form that is itself only labelled."""
    from mayur.lexicon_gen import _GATI_WITH_KR, _splits
    from mayur.lexicon_usage import _joins

    out: list[Morph] = []
    for u1, rest in _splits(form):
        inner = [((u1,), rest), *(((u1, u2), rest2) for u2, rest2 in _splits(rest))]
        for prefixes, base in inner:
            if any(u in _GATI_WITH_KR for u in prefixes) or not _joins(prefixes, base, form):
                continue  # (the upasarga must give this very form by sandhi: सम् + गमय is संगमय, not सद्गमय)
            for m in _labelled(base, padas, generated):
                if m.root and (m.kind == "tinanta" or m.krt in ("शतृ", "शानच्")):
                    out.append(replace(m, form=form, lemma="".join(prefixes) + m.lemma,
                                       prefixes=prefixes + tuple(m.prefixes)))
    return tuple(dict.fromkeys(out))


def prefixed_augmentless(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """अवशातयत्, व्यपरोपयत्: upasarga + a past form without its augment (regular अवाशातयत्)."""
    from mayur.lexicon_usage import prefix_splits

    from mayur.lexicon_usage import _joins

    out: list[Morph] = []
    for prefixes, rest in prefix_splits(form):
        if not _joins(prefixes, rest, form):
            continue
        out += [replace(m, form=form, lemma="".join(prefixes) + m.lemma, prefixes=prefixes + tuple(m.prefixes),
                        source=ARSHA, quality=1, handle=("special", AUGMENT_ARSHA_NOTE))
                for m in augmentless(rest, padas)]
    return tuple(dict.fromkeys(out))


FEM_NOTE = ("ārṣa: the feminine participle without the न् that 7.1.81 शप्श्यनोर्नित्यम् requires for this class "
            "(regular form {regular}); epic usage, labelled and not derived")
_ATI = lipi.varnas("अती")


def arsha_feminine(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """आक्रन्दतीम्, अनुशोचती: -अती for -अन्ती in the feminine of a present participle."""
    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for i in range(len(sounds) - 3, 1, -1):
        if sounds[i: i + 2] == ("अ", "त्") and sounds[i + 2] in ("ई", "य्", "इ"):
            regular = lipi.from_varnas(sounds[: i + 1] + ("न्",) + sounds[i + 1:])
            note = FEM_NOTE.format(regular=lipi.pausa(regular))
            out += [replace(m, form=form, source=ARSHA, quality=1, handle=("special", note))
                    for m in padas(regular) if m.krt == "शतृ" and m.linga == "स्त्रीलिङ्ग"]
            break
    return tuple(dict.fromkeys(out))


OBLIQUE_NOTE = ("ārṣa: the परस्मैपद participle (शतृ) of a root that takes आत्मनेपद by 1.3.12–93 (its present is {present}); "
                "epic usage, labelled and not derived")
_SHATR_WEAK = tuple(lipi.varnas(e) for e in ("अतस्", "अता", "अते", "अति", "अतोस्", "अताम्", "अद्भिस्", "अद्भ्यस्",
                                              "अद्भ्याम्", "अत्सु"))
LYAP_SIBLING_NOTE = ("ārṣa: an absolutive in -य without an upasarga (7.1.37 gives ल्यप् only after one; the regular "
                     "form has क्त्वा). With प्र the same form is the regular {sibling}; epic usage, labelled and not derived")


def arsha_thematic(form: str) -> tuple[Morph, ...]:
    """अहनत्, अशासत्: a second-class root conjugated in the first class (``mayur.lexicon_thematic``)."""
    from mayur.lexicon_thematic import thematic

    return thematic(form)


def arsha_shatr_oblique(form: str) -> tuple[Morph, ...]:
    """युध्यतोस्, काशद्भिस्: a weak case of the शतृ participle of an आत्मनेपद root. The stem in -अत् is
    inflected by vidyut as a plain stem; that the root has this present is a dictionary probe (युध्यते)."""
    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for ending in _SHATR_WEAK:
        if len(sounds) <= len(ending) + 1 or sounds[-len(ending):] != ending:
            continue
        head = sounds[: -len(ending)]
        present = lipi.from_varnas(head + lipi.varnas("अते"))
        roots = [m for m in _finite(present) if (m.lakara, m.purusha, m.vacana, m.prayoga) == ("लट्", _P1, _SG, "कर्तरि")]
        if not roots:
            continue
        stem = lipi.from_varnas(head + lipi.varnas("अत्"))
        note = OBLIQUE_NOTE.format(present=present)
        for linga in ("पुंलिङ्ग", "नपुंसकलिङ्ग"):
            for pada, template in bridge.subanta_paradigm(stem, linga):
                if form in bridge.derived_texts(pada):
                    out += [replace(template, form=form, lemma=r.lemma, stem=stem, root=r.root, dhatu=r.dhatu, gana=r.gana,
                                    prefixes=r.prefixes, krt="शतृ", root_gloss=r.root_gloss, source=ARSHA, quality=1,
                                    handle=("special", note)) for r in roots]
    return tuple(dict.fromkeys(out))


def arsha_lyap(form: str, padas: Lookup) -> tuple[Morph, ...]:
    """गृह्य, उष्य: प्र + the same form is a regular ल्यप् (प्रगृह्य), so this is that absolutive without its upasarga."""
    if not form.endswith("य") or len(form) < 3:
        return ()
    sibling = "प्र" + form
    note = LYAP_SIBLING_NOTE.format(sibling=sibling)
    return tuple(dict.fromkeys(
        replace(m, form=form, lemma=m.root or m.lemma, prefixes=tuple(m.prefixes[1:]), source=ARSHA, quality=1,
                handle=("special", note))
        for m in padas(sibling) if m.krt == "ल्यप्" and m.prefixes == ("प्र",) and m.quality >= 2))


def more(form: str, found: Sequence[Morph], padas: Lookup, generated: Lookup) -> tuple[Morph, ...]:
    """Extra analyses for ``form`` given what the lexicon already ``found``."""
    out: list[Any] = []
    if not any(m.kind == "tinanta" for m in found):
        out += augmentless(form, padas)
    if not any(m.krt == "शतृ" for m in found):
        out += kram_participle(form)
    out += kram_short(form)
    have = {(m.lemma, m.lakara, m.purusha, m.vacana, m.prayoga) for m in [*found, *out] if m.kind == "tinanta"}
    out += [m for m in arsha_voice(form, padas) if (m.lemma, m.lakara, m.purusha, m.vacana, m.prayoga) not in have]
    if not found and not out:
        out += prefixed_labelled(form, padas, generated)
    elif not any(m.kind == "tinanta" or (not m.root and m.quality >= 2) for m in [*found, *out]):
        # अवशातयत् beside the participle; never beside a listed noun (प्रभवस् is प्रभव, not प्र + भवस्)
        out += prefixed_augmentless(form, padas)
    if not any(m.quality >= 2 for m in found):
        out += arsha_participle(form, generated, padas)
        out += arsha_shatr(form)
        out += arsha_shatr_oblique(form)
    elif not any(m.root for m in found):  # कामयानस्य: the kosha lists कामयान as an adjective only
        out += arsha_participle(form, lambda _f: [m for m in found if m.kind == "subanta" and m.quality >= 2], padas)
    if not any(m.root and m.quality >= 2 for m in found):
        out += arsha_feminine(form, padas)
    if not any(m.kind == "tinanta" for m in found):
        from mayur.lexicon_guna import epic_imperative, first_imperative

        out += [*arsha_thematic(form), *first_imperative(form, padas), *epic_imperative(form, padas)]
    if not any(m.kind == "avyaya" and m.krt in ("ल्यप्", "क्त्वा") for m in found):
        out += arsha_lyap(form, padas)  # गृह्य, by its sibling प्रगृह्य
    if not any(m.kind == "avyaya" and m.krt in ("ल्यप्", "क्त्वा") for m in [*found, *out]):  # पीड्य "having pressed"
        out += [replace(m, kind="avyaya", krt="ल्यप्", linga=None, vibhakti=None, vacana=None, source=ARSHA, quality=1,
                        handle=("special", LYAP_NOTE))
                for m in found if m.krt in ("यत्", "ण्यत्", "क्यप्") and m.vibhakti == "सम्बोधन" and not m.prefixes][:1]
    from mayur import lexicon
    from mayur.lexicon_usage import usage_forms

    out += gati_verbs(form, padas, lexicon.listed_stem)
    if not any(m.kind == "tinanta" and m.quality >= 2 for m in [*found, *out]):
        from mayur.lexicon_denom import denominatives

        out += denominatives(form, lambda stem: bool(lexicon.listed_stem(stem)))  # नमस्यति, पुत्रीयति
    out += usage_forms(form, [*found, *out], padas)
    return tuple(out)
