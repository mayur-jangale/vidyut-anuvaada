"""Word lookup and forward proof. All arguments and results are Devanagari.

A form is accepted only when vidyut-kosha lists it or a FORWARD vidyut-prakriya derivation
reproduces it exactly; nothing is ever run backward.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge
from mayur.model import Morph, SutraStep, WordProof
from mayur.terms import NONFINITE_KRT, PARTICIPLE_KRT

_GOOD_KRT = frozenset(PARTICIPLE_KRT) | frozenset(NONFINITE_KRT)
_JUNK_KRT = frozenset({"क्विप्", "क्विन्", "विच्", "विट्"})
_NOTE_2471 = ("compound-internal elision of the case ending (2.4.71, with 1.4.14 for pada status) "
              "is not derivable through vidyut's Python API; the trace is the stem's own derivation")

_NASAL = {"क": "ङ्", "ख": "ङ्", "ग": "ङ्", "घ": "ङ्", "च": "ञ्", "छ": "ञ्", "ज": "ञ्", "झ": "ञ्",
          "ट": "ण्", "ठ": "ण्", "ड": "ण्", "ढ": "ण्", "त": "न्", "थ": "न्", "द": "न्", "ध": "न्",
          "प": "म्", "फ": "म्", "ब": "म्", "भ": "म्", "न": "न्", "म": "म्"}
# pada-final spellings (8.2.30, 8.2.39, 8.4.56): a stem's final consonant as it stands at a pada end
_FINAL = {"द्": ("त्",), "ग्": ("क्",), "ड्": ("ट्",), "ब्": ("प्",), "च्": ("क्",), "ज्": ("क्", "ट्"),
          "श्": ("ट्", "क्"), "ष्": ("ट्",), "ह्": ("ट्", "क्"), "ध्": ("त्",), "भ्": ("प्",)}


def _quality(entry: bridge.Entry) -> int:
    m = entry.morph
    if entry.entry == "tinanta" or entry.is_avyaya:
        return 3
    if entry.entry == "krdanta":
        if m.krt in _JUNK_KRT:
            return 0
        return 3 if m.krt in _GOOD_KRT else 1
    if not entry.lingas or m.linga in entry.lingas:
        return 3
    return 2


_ENCLITIC = frozenset({"मे", "ते", "नौ", "वाम्", "नस्", "वस्", "मा", "त्वा"})
_FREQ_ALIAS = {"अस्मद्": "मद्", "युष्मद्": "त्वद्"}  # the corpus cites these pronouns by these stems


def _freq(lemma: str) -> int:
    try:
        from mayur.freq import lemma_count

        return int(lemma_count(_FREQ_ALIAS.get(lemma, lemma)))
    except Exception:  # noqa: BLE001 - freq is optional and written elsewhere
        return 0


def _rank(morphs: list[Morph]) -> tuple[Morph, ...]:
    seen: list[Morph] = []
    for m in morphs:
        if m not in seen:
            seen.append(m)
    return tuple(sorted(seen, key=lambda m: (-m.quality, -_freq(m.lemma), _KIND_ORDER.get(_kind_key(m), 3))))


_KIND_ORDER = {"tinanta": 0, "avyaya": 1, "basic": 1, "krdanta": 2}


def _kind_key(m: Morph) -> str:
    if m.kind in ("tinanta", "avyaya"):
        return m.kind
    return "krdanta" if m.krt else "basic"


def nasal_variants(form: str) -> tuple[str, ...]:
    """``form`` with anusvara before a stop written as the class nasal, and vice versa."""
    out = [form]
    chars = list(form)
    alt = []
    for i, ch in enumerate(chars):
        nxt = chars[i + 1] if i + 1 < len(chars) else ""
        if ch == "ं" and nxt in _NASAL:
            alt.append(_NASAL[nxt])
        else:
            alt.append(ch)
    out.append("".join(alt))
    back = form
    for nasal in set(_NASAL.values()):
        for cons, n in _NASAL.items():
            if n == nasal:
                back = back.replace(nasal + cons, "ं" + cons)
    out.append(back)
    return tuple(dict.fromkeys(x for x in out if x))


def final_variants(form: str) -> tuple[str, ...]:
    """``form`` and its spellings with the final consonant as at a pada end (केचिद् -> केचित्)."""
    for cons, alts in _FINAL.items():
        if form.endswith(cons) and len(form) > len(cons):
            return (form,) + tuple(form[: -len(cons)] + a for a in alts)
    return (form,)


def spelling_variants(form: str) -> tuple[str, ...]:
    return tuple(dict.fromkeys(n for f in final_variants(form) for n in nasal_variants(f)))


_STOPS = frozenset("कखगघचछजझटठडढतथदधपफबभ")
_AFTER_GEMINATE = frozenset("यरलव")
GEMINATE_NOTE = ("the text writes {form}; the derived form is {derived}, with the doubled consonant that is "
                 "commonly written single (पत्र for पत्त्र, तत्व for तत्त्व)")


def geminate_variants(form: str) -> tuple[str, ...]:
    """Spellings of ``form`` with one stop doubled before a semivowel: पत्रम् -> पत्त्रम्, छात्र ->
    छात्त्र, तत्वम् -> तत्त्वम्, उज्वल -> उज्ज्वल. Derivation gives the doubled form (पत् + त्र);
    manuscripts and print usually write one consonant. Used only when the written form is unknown."""
    out = []
    for i in range(len(form) - 2):
        c = form[i]
        if c in _STOPS and form[i + 1] == "्" and form[i + 2] in _AFTER_GEMINATE and (i == 0 or form[i - 1] != "्"):
            out.append(form[:i] + c + "्" + form[i:])
    return tuple(out)


def _kosha_morphs(form: str) -> list[Morph]:
    out = _kosha_morphs_of(form, spelling_variants(form))
    if not any(m.quality >= 2 for m in out):  # unknown as written: the spelling with a doubled stop
        out += _kosha_morphs_of(form, geminate_variants(form))
    return out


def _kosha_morphs_of(form: str, variants: tuple[str, ...]) -> list[Morph]:
    out = []
    for variant in variants:
        for entry in bridge.lookup(variant):
            m = replace(entry.morph, form=form, quality=_quality(entry))
            if entry.entry == "basic" and m.lemma in _LEMMA_ALIAS:
                m = replace(m, lemma=_LEMMA_ALIAS[m.lemma])
            elif entry.entry == "basic" and m.linga == "स्त्रीलिङ्ग":
                m = replace(m, lemma=feminine_stem(m.lemma, form))
            out.append(m)
            if m.krt in _ADJECTIVAL_KRT and m.stem and m.kind == "subanta":
                out.append(_as_adjective(m))
    return out


def feminine_stem(stem: str, form: str) -> str:
    """The feminine stem of an a-stem that ``form`` (a feminine pada of it) shows: सुमुख -> सुमुखी
    (ङीष्, 4.1.41ff.: सुमुखी, सुमुख्या) or शिष्य -> शिष्या (टाप्, 4.1.4: शिष्या, शिष्यया)."""
    if not stem or not "क" <= stem[-1] <= "ह" or not form.startswith(stem):
        return stem
    return stem + ("ी" if form[len(stem):len(stem) + 1] in ("ी", "्") else "ा")


# stems the corpus cites under another name (it has 593 अहर्, no अहन्); the handle is unchanged
_LEMMA_ALIAS = {"अहन्": "अहर्", "ओम्": "ॐ"}


# participles the corpus also cites as adjectives under their own stem (समन्वित, शक्य, उचित)
_ADJECTIVAL_KRT = frozenset({"क्त", "क्तवतु", "यत्", "ण्यत्", "क्यप्", "तव्य", "अनीयर्"})


def _as_adjective(m: Morph) -> Morph:
    """The same derived pada, analysed as a subanta of the kṛdanta stem (same vidyut handle)."""
    return replace(m, lemma=m.stem, stem="", root=None, dhatu=None, gana=None, prefixes=(), krt=None,
                   root_gloss=m.root_gloss, quality=min(m.quality, 2))


@lru_cache(maxsize=100_000)
def _kosha_ranked(form: str) -> tuple[Morph, ...]:
    """Kosha analyses only (no generation): the members of generated compounds."""
    return tuple(_kosha_morphs(form))


@lru_cache(maxsize=200_000)
def padas(form: str) -> tuple[Morph, ...]:
    """All analyses of ``form`` as a complete pada, best first; () if none."""
    from mayur.lexicon_iyan import iyan_uvan
    from mayur.lexicon_paradigm import closed_paradigms
    from mayur.lexicon_gen import (anvadesha, avyaya_compound, indefinite, looks_verbal, prefixed, sa_esha,
                                   numerals, tasi_forms)

    found = _kosha_morphs(form) + list(anvadesha(form)) + list(sa_esha(form)) + list(indefinite(form, padas))
    if not any(m.kind == "avyaya" and m.quality >= 2 for m in found):
        found.extend(avyaya_compound(form, _kosha_ranked, stems))
    found.extend(tasi_forms(form, stems))
    found.extend(numerals(form))
    found.extend(iyan_uvan(form))
    found.extend(closed_paradigms(form))
    from mayur.lexicon_fem import feminine_padas

    have = {m.lemma for m in found if m.linga == "स्त्रीलिङ्ग"}
    found.extend(m for m in feminine_padas(form) if m.lemma not in have and m.lemma[:-1] not in have)
    if not any(m.krt == "क्त" for m in found):
        from mayur.lexicon_kta import kta_padas

        found.extend(kta_padas(form, bridge.lookup(form)))
    if not any(m.quality >= 2 for m in found) or looks_verbal(form):
        # prefixed participles/absolutives sit next to the kosha's adjective (सम्पन्नस्, विचिन्त्य)
        known = set(found)
        found.extend(m for m in prefixed(form) if m not in known)
    return _rank(found)


def is_pada(form: str, min_quality: int = 0) -> bool:
    return any(m.quality >= min_quality for m in padas(form))


_SPECIAL_STEMS = {
    "अ": ("नञ्", "निषेध"), "अन्": ("नञ्", "निषेध"), "महा": ("महत्", "6.3.46"),
    "पञ्च": ("पञ्चन्", ""), "सप्त": ("सप्तन्", ""), "अष्ट": ("अष्टन्", ""), "नव": ("नवन्", ""),
    "दश": ("दशन्", ""), "द्वादश": ("द्वादशन्", ""), "एकादश": ("एकादशन्", ""),
    "मद्": ("अस्मद्", ""), "त्वद्": ("युष्मद्", ""), "तद्": ("तद्", ""), "यद्": ("यद्", ""), "एतद्": ("एतद्", ""),
    "मत्": ("अस्मद्", ""), "त्वत्": ("युष्मद्", ""), "अस्मत्": ("अस्मद्", ""), "युष्मत्": ("युष्मद्", ""),
    "तत्": ("तद्", ""), "यत्": ("यद्", ""), "एतत्": ("एतद्", ""), "किम्": ("किम्", ""),
    "दुस्": ("दुस्", ""), "कु": ("कु", ""),
    # अञ्च् stems (3.2.59 ऋत्विग्...अञ्चु...; weak stem by 6.4.30 नाञ्चेः पूजायाम्, 6.4.138 अचः, 6.3.138 चौ)
    "प्राञ्च्": ("प्राञ्च्", ""), "प्राच्": ("प्राञ्च्", ""), "प्राक्": ("प्राञ्च्", ""),
    "तिर्यञ्च्": ("तिर्यञ्च्", ""), "तिरश्च्": ("तिर्यञ्च्", ""), "तिर्यक्": ("तिर्यञ्च्", ""),
    "प्रत्यञ्च्": ("प्रत्यञ्च्", ""), "प्रतीच्": ("प्रत्यञ्च्", ""), "प्रत्यक्": ("प्रत्यञ्च्", ""),
    "उदञ्च्": ("उदञ्च्", ""), "उदीच्": ("उदञ्च्", ""), "उदक्": ("उदञ्च्", ""),
    "अवाञ्च्": ("अवाञ्च्", ""), "अवाच्": ("अवाञ्च्", ""), "अवाक्": ("अवाञ्च्", ""),
    "सम्यञ्च्": ("सम्यञ्च्", ""), "सम्यच्": ("सम्यञ्च्", ""), "सम्यक्": ("सम्यञ्च्", ""),
}


def _stem_entry_ok(entry: bridge.Entry, form: str) -> bool:
    m = entry.morph
    if entry.is_avyaya:
        return entry.entry == "basic"
    neuter_nom = m.linga == "नपुंसकलिङ्ग" and m.vibhakti == "प्रथमा" and m.vacana == "एकवचन"
    if entry.entry == "basic":
        return entry.pratipadika == form or (neuter_nom and entry.pratipadika.endswith("्"))
    if entry.entry == "krdanta" and m.krt not in _JUNK_KRT and m.kind != "avyaya":
        return m.stem == form or (neuter_nom and m.stem.endswith("्"))
    return False


def _as_stem(entry: bridge.Entry, form: str) -> Morph:
    m = entry.morph
    lemma = entry.pratipadika if entry.entry == "basic" else m.lemma
    q = _quality(entry)
    if entry.entry == "basic":
        q = 3 if entry.lingas or entry.is_avyaya else max(q, 2)
    return Morph(form=form, lemma=_LEMMA_ALIAS.get(lemma, lemma), kind="stem", stem=m.stem or lemma, root=m.root, dhatu=m.dhatu,
                 gana=m.gana, prefixes=m.prefixes, krt=m.krt, root_gloss=m.root_gloss,
                 quality=q, handle=("stem", bridge.stem_handle(entry)))


@lru_cache(maxsize=200_000)
def stems(form: str) -> tuple[Morph, ...]:
    """Analyses of ``form`` as a non-final compound member (kind "stem"), best first."""
    out: list[Morph] = []
    spellings = set(nasal_variants(form))  # the kosha may spell the stem with ं (भुजंग for भुजङ्ग)
    for variant in nasal_variants(form):
        for entry in bridge.lookup(variant):
            if _stem_entry_ok(entry, variant):
                out.append(_as_stem(entry, form))
        # a stem cited as such: वाच् (pada वाक्), वधू (pada वधूस्)
        for key in final_variants(variant)[1:] + (variant + "स्",):
            for entry in bridge.lookup(key):
                if entry.entry == "basic" and entry.pratipadika in spellings:
                    out.append(_as_stem(entry, form))
    known = set(out)
    out.extend(m for m in _prefixed_stems(form) if m not in known)
    if out and not any(m.krt == "क्त" for m in out):  # a basic stem the kosha does not see as क्त
        from mayur.lexicon_kta import kta_stems

        out.extend(kta_stems(form))
    if not out:
        for variant in geminate_variants(form):  # पत्र- for पत्त्र-
            out.extend(_as_stem(entry, form) for entry in bridge.lookup(variant) if _stem_entry_ok(entry, variant))
    if not out:
        from mayur.lexicon_gen import nanj_stems

        out.extend(nanj_stems(form, stems))
    if form in _SPECIAL_STEMS:
        lemma, _ = _SPECIAL_STEMS[form]
        out.append(Morph(form=form, lemma=lemma, kind="stem", source="special", quality=3,
                         handle=("stem", bridge.basic_pratipadika_handle(lemma))))
    return _rank(out)


def _prefixed_stems(form: str) -> list[Morph]:
    """उन्नत, प्रदीप्त: a prefixed kṛdanta stem the kosha lacks, forward-derived (stem = form)."""
    from mayur.lexicon_gen import looks_verbal, prefixed

    if not looks_verbal(form + "स्"):
        return []
    out = []
    for m in prefixed(form):
        stem_handle = bridge.pratipadika_of(m.handle) if m.kind == "subanta" else None
        if stem_handle is None or m.krt not in _GOOD_KRT:
            continue
        if any(t == form for t in bridge.derived_texts(stem_handle)):
            out.append(Morph(form=form, lemma=m.lemma, kind="stem", stem=form, root=m.root, dhatu=m.dhatu,
                             gana=m.gana, prefixes=m.prefixes, krt=m.krt, root_gloss=m.root_gloss,
                             source="generated", quality=3, handle=("stem", stem_handle)))
    return list(dict.fromkeys(out))


def is_stem(form: str) -> bool:
    return bool(stems(form))


@lru_cache(maxsize=50_000)
def generated(form: str) -> tuple[Morph, ...]:
    """Slow fallback: nominal forms not in the kosha, forward-derived from guessed stems."""
    from mayur.lexicon_gen import generated_nominals

    return _rank(list(generated_nominals(form)))


def _matching(handle, target: str) -> tuple[bool, str, list[SutraStep]]:
    ders = bridge.derive(handle)
    targets = set(nasal_variants(target)) | set(geminate_variants(target))
    if not any(d.text in targets for d in ders):
        alt = bridge.matup_subanta(handle)
        if alt is not None:
            ders = bridge.derive(alt) + ders
    for d in ders:
        if d.text in targets:
            return True, d.text, list(d.trace)
    if ders:
        return False, ders[0].text, list(ders[0].trace)
    return False, "", []


def _prove_with_particle(m: Morph, base: Morph, particle: str) -> WordProof:
    """किम्-form + चित्/चन: the base is derived by vidyut and the junction is re-run forward."""
    from mayur import sandhi

    proof = prove(base)
    wanted = {sandhi.canon(m.form), sandhi.canon(m.form[:-2] + "त्") if m.form.endswith("द्") else ""}
    joined = [o for o in sandhi.outcomes(base.form, "चन" if particle == "चन" else "चित्")
              if sandhi.canon(o.text) in wanted]
    if not proof.derivable or not joined:
        return WordProof(derivable=False, method="vidyut-prakriya + sandhi", trace=proof.trace,
                         note=f"{base.form} + {particle} does not re-join to {m.form} by the sandhi rules")
    junction = SutraStep("अष्टाध्यायी", ", ".join(joined[0].sutras) or "—", f"{base.form} + {particle} → {m.form}")
    return WordProof(derivable=True, method="vidyut-prakriya + sandhi", derived_form=m.form,
                     trace=[*proof.trace, junction],
                     note=f"{base.form} is derived by vidyut; {particle} is a particle (अव्यय) joined by sandhi")


def _prove_member(m: Morph, stem_handle) -> WordProof:
    """Proof of a non-final compound member. ``derivable`` only if a vidyut derivation yields
    exactly the member's form: the stem itself, or a pada of that stem with the same sounds
    (वाक् of वाच्). A form that exists only by a substitution made in compound formation
    (महा for महत्, मत् for अस्मद्) is reported as NOT derived."""
    target = m.stem or m.lemma
    ok, text, trace = _matching(stem_handle, target)
    if not ok and m.source == "special":
        ok, text, trace = _matching(stem_handle, m.lemma)
    if not ok:
        return WordProof(derivable=False, method="vidyut-prakriya (stem)", derived_form=text, trace=trace,
                         note="the stem derivation did not yield " + target + "; " + _NOTE_2471)
    if m.form in nasal_variants(text):
        return WordProof(derivable=True, method="vidyut-prakriya (stem)", derived_form=text, trace=trace,
                         note=_NOTE_2471)
    for pada in padas(m.form):
        if (pada.stem or pada.lemma) == text and pada.source == "kosha" and not isinstance(pada.handle, tuple):
            same, pada_text, pada_trace = _matching(pada.handle, m.form)
            if same:
                return WordProof(derivable=True, method="vidyut-prakriya (pada form of the stem)",
                                 derived_form=pada_text, trace=pada_trace,
                                 note=f"{m.form} is derived here as a pada of {text}; in the compound the same "
                                      f"pada-final form arises (1.4.14). " + _NOTE_2471)
    return WordProof(derivable=False, method="vidyut-prakriya (stem only)", derived_form=text, trace=trace,
                     note=f"vidyut derives the stem {text}, not the in-compound form {m.form}: that form is a "
                          f"substitution made in compound formation, which vidyut's Python API cannot derive")


def prove(m: Morph) -> WordProof:
    """Proof of one analysis; says so when the derived form differs from the text by a doubled stop."""
    proof = _prove(m)
    if proof.derivable and m.source == "generated" and m.quality <= 1 and m.kind == "subanta":
        # an ending fitted to a stem no dictionary lists: the inflection is regular, the word is not known
        return replace(proof, derivable=False, method="inflection of an unlisted stem",
                       note=f"the stem {m.stem or m.lemma} is not in the dictionary; only its inflection follows the rules")
    derived = proof.derived_form
    if proof.derivable and derived and derived != m.form and derived in geminate_variants(m.form):
        note = GEMINATE_NOTE.format(form=m.form, derived=derived)
        return replace(proof, note=f"{proof.note}; {note}" if proof.note else note)
    return proof


def _prove(m: Morph) -> WordProof:
    """Forward derivation of ``m``; derivable only if vidyut yields exactly the expected text."""
    h = m.handle
    if h is None:
        return WordProof(derivable=False, method="none", note="no vidyut arguments for this analysis")
    if isinstance(h, tuple) and h and h[0] == "special":
        return WordProof(derivable=False, method="special", note=h[1])
    if isinstance(h, tuple) and h and h[0] == "particle":
        return _prove_with_particle(m, h[1], h[2])
    if isinstance(h, tuple) and h and h[0] == "nanj":
        inner = prove(replace(m, handle=("stem", h[1]), stem="", lemma=m.lemma[1:] if m.lemma[1:2] != "न" else m.lemma[2:]))
        return WordProof(derivable=False, method="नञ्-समास (member derived)", derived_form=inner.derived_form,
                         trace=inner.trace, note=h[2])
    if isinstance(h, tuple) and h and h[0] == "stem":
        if h[1] is None:
            return WordProof(derivable=False, method="stem", note="no stem derivation available")
        return _prove_member(m, h[1])
    ok, text, trace = _matching(h, m.form)
    note = ""
    if ok and text != m.form and text in nasal_variants(m.form):
        note = f"derived spelling {text}; {m.form} differs only in writing the nasal"
    method = "vidyut-prakriya"
    if not ok:
        note = f"vidyut derived {text or 'nothing'}, not {m.form}"
        if m.source == "kosha":
            method = "kosha-listed"
            if m.lemma in ("अस्मद्", "युष्मद्") and m.form in _ENCLITIC:
                note = "listed in vidyut-kosha; enclitic by 8.1.20–23, which vidyut's Python API does not derive"
            else:
                note = (f"listed in vidyut-kosha; not reproduced by vidyut's derivation "
                        f"(it derived {text or 'nothing'})")
    return WordProof(derivable=ok, method=method, derived_form=text, trace=trace, note=note)


from mayur.lexicon_cite import _join, verbal_lemma  # noqa: E402,F401  (re-exported)
