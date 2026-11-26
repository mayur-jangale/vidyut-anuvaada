"""Word lookup and forward proof. All arguments and results are Devanagari.

A form is accepted only when vidyut-kosha lists it or a FORWARD vidyut-prakriya derivation
reproduces it exactly; nothing is ever run backward.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge, lipi
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


def _kosha_morphs(form: str) -> list[Morph]:
    out = []
    for variant in spelling_variants(form):
        for entry in bridge.lookup(variant):
            m = replace(entry.morph, form=form, quality=_quality(entry))
            out.append(m)
            if m.krt in _ADJECTIVAL_KRT and m.stem and m.kind == "subanta":
                out.append(_as_adjective(m))
    return out


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
    from mayur.lexicon_gen import anvadesha, avyaya_compound, indefinite, looks_verbal, prefixed, sa_esha

    found = _kosha_morphs(form) + list(anvadesha(form)) + list(sa_esha(form)) + list(indefinite(form, padas))
    if not any(m.kind == "avyaya" and m.quality >= 2 for m in found):
        found.extend(avyaya_compound(form, _kosha_ranked, stems))
    if not any(m.quality >= 2 for m in found) or looks_verbal(form):
        # prefixed participles/absolutives sit next to the kosha's adjective (सम्पन्नस्, विचिन्त्य)
        known = set(found)
        found.extend(m for m in prefixed(form) if m not in known)
    return _rank(found)


def is_pada(form: str, min_quality: int = 0) -> bool:
    return any(m.quality >= min_quality for m in padas(form))


_SPECIAL_STEMS = {
    "अ": ("नञ्", "निषेध"), "अन्": ("नञ्", "निषेध"), "महा": ("महत्", "6.3.46"),
    "मद्": ("अस्मद्", ""), "त्वद्": ("युष्मद्", ""), "तद्": ("तद्", ""), "यद्": ("यद्", ""), "एतद्": ("एतद्", ""),
    "मत्": ("अस्मद्", ""), "त्वत्": ("युष्मद्", ""), "अस्मत्": ("अस्मद्", ""), "युष्मत्": ("युष्मद्", ""),
    "तत्": ("तद्", ""), "यत्": ("यद्", ""), "एतत्": ("एतद्", ""), "किम्": ("किम्", ""),
    "दुस्": ("दुस्", ""), "कु": ("कु", ""),
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
    return Morph(form=form, lemma=lemma, kind="stem", stem=m.stem or lemma, root=m.root, dhatu=m.dhatu,
                 gana=m.gana, prefixes=m.prefixes, krt=m.krt, root_gloss=m.root_gloss,
                 quality=q, handle=("stem", bridge.stem_handle(entry)))


@lru_cache(maxsize=200_000)
def stems(form: str) -> tuple[Morph, ...]:
    """Analyses of ``form`` as a non-final compound member (kind "stem"), best first."""
    out: list[Morph] = []
    for variant in nasal_variants(form):
        for entry in bridge.lookup(variant):
            if _stem_entry_ok(entry, variant):
                out.append(_as_stem(entry, form))
        # a stem cited as such: वाच् (pada वाक्), वधू (pada वधूस्)
        for key in final_variants(variant)[1:] + (variant + "स्",):
            for entry in bridge.lookup(key):
                if entry.entry == "basic" and entry.pratipadika == variant:
                    out.append(_as_stem(entry, form))
    known = set(out)
    out.extend(m for m in _prefixed_stems(form) if m not in known)
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
    targets = set(nasal_variants(target))
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


def prove(m: Morph) -> WordProof:
    """Forward derivation of ``m``; derivable only if vidyut yields exactly the expected text."""
    h = m.handle
    if h is None:
        return WordProof(derivable=False, method="none", note="no vidyut arguments for this analysis")
    if isinstance(h, tuple) and h and h[0] == "special":
        return WordProof(derivable=False, method="special", note=h[1])
    if isinstance(h, tuple) and h and h[0] == "particle":
        return _prove_with_particle(m, h[1], h[2])
    if isinstance(h, tuple) and h and h[0] == "stem":
        if h[1] is None:
            return WordProof(derivable=False, method="stem", note="no stem derivation available")
        target = m.stem or m.lemma
        ok, text, trace = _matching(h[1], target)
        if not ok and m.source == "special":
            ok, text, trace = _matching(h[1], m.lemma)
        note = _NOTE_2471
        if ok and text != m.form:
            note += f"; the stem {text} appears as {m.form} by pada-final rules (1.4.14 with 8.2.x)"
        return WordProof(derivable=ok, method="vidyut-prakriya (stem)", derived_form=text, trace=trace,
                         note=note if ok else "the stem derivation did not yield " + target + "; " + note)
    ok, text, trace = _matching(h, m.form)
    note = ""
    if ok and text != m.form:
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


_R_PREFIX = ("प्र", "परा", "परि", "निर्", "निस्", "दुर्")


def _join(left: str, right: str) -> str:
    from mayur import sandhi

    if left == "पुरस्":  # 8.3.40 नमस्पुरसोर्गत्योः
        return left + right
    if left[-1:] in ("ि", "ु") and right.startswith(_SHATVA_ROOTS):  # 8.3.65-8.3.70, 8.4.41
        right = "ष" + right[1:]
        right = right.replace("ष्था", "ष्ठा", 1).replace("ष्तु", "ष्टु", 1).replace("ष्तम्भ्", "ष्टम्भ्", 1)
        return left + right
    if left == "उद्" and right.startswith(("स्था", "स्तम्भ्")):  # 8.4.61 उदः स्थास्तम्भोः पूर्वस्य
        return "उत्" + right[2:]
    if left == "उद्" and right[:1] in ("न", "म"):  # 8.4.45 यरोऽनुनासिकेऽनुनासिको वा (the usual spelling)
        return "उन्" + right
    if left in ("निर्", "दुर्"):  # the upasarga is निस् / दुस् (र् is its sandhi form)
        left = left[:-2] + "स्"
    if left in ("निस्", "दुस्") and right[:1] in _VOWEL_INITIAL:
        return lipi.from_varnas(lipi.varnas(left[:-2] + "र्") + lipi.varnas(right))
    outs = sandhi.outcomes(left, right)
    # within a word the samhita rules are obligatory (1.4.109 with 6.1.72): prefer an outcome that applied one
    applied = [o for o in outs if o.sutras and "पादान्त-विराम" not in o.sutras]
    text = (applied or list(outs))[0].text if outs else left + right
    if "ः" in text and right[:1] not in _VOWEL_INITIAL:  # निस्/दुस् before a voiced sound: निर्, दुर्
        if right[:1] in _VOICED:
            sub = "र्"
        elif right[:1] in "कखपफ" and left[-3:-2] in ("ि", "ु"):  # 8.3.41 इदुदुपधस्य चाप्रत्ययस्य
            sub = "ष्"
        elif right[:1] in "तथ":
            sub = "स्"
        elif right[:1] in "चछ":
            sub = "श्"
        else:
            sub = "ः"
        text = text.replace("ः", sub, 1)
    if left in _R_PREFIX and text[len(left):].startswith("न"):  # 8.4.14 उपसर्गादसमासेऽपि णोपदेशस्य
        text = text[: len(left)] + "ण" + text[len(left) + 1:]
    return text


_VOWEL_INITIAL = frozenset("अआइईउऊऋॠऌएऐओऔ")
_VOICED = frozenset("गघङजझञडढणदधनबभमयरलवह")
_SHATVA_ROOTS = ("स्था", "सद्", "सिच्", "सिध्", "सञ्ज्", "स्तु", "स्तम्भ्", "सेव्", "सो", "स्वप्", "सह्",
                 "सिव्", "सु", "सू", "स्यन्द्", "स्वञ्ज्")


def _dcs_root(m: Morph) -> str:
    """A ṇic / curādi stem as the corpus cites it: कथि -> कथय्, कारि -> कारय् (vidyut ends it in इ)."""
    root = m.root or m.lemma
    taught = "".join(ch for ch in (m.dhatu or "") if ch not in "॒॑ँ")
    if root.endswith("ि") and not taught.startswith(root):
        short = root.replace("ा", "", 1)
        if short != root and short[:-1] in m.form and root[:-1] not in m.form:  # 6.4.92 मितां ह्रस्वः
            root = short
        return root[:-1] + "य्"
    return _CITED_ROOT.get(root, root)


# How the corpus cites roots that vidyut names by their Dhatupatha form (ध्यै -> ध्या, 6.1.45)
_CITED_ROOT = {"ध्यै": "ध्या", "गै": "गा", "ह्वे": "ह्वा", "म्लै": "म्ला", "ग्लै": "ग्ला", "त्रै": "त्रा",
               "दै": "दा", "वे": "वा", "व्ये": "व्या", "शो": "शा", "सो": "सा", "छो": "छा", "दो": "दा"}
# Present-system suppletion (7.3.78 पाघ्राध्मास्थाम्नादाण्दृश्यर्तिसर्तिशदसदां पिबजिघ्र...): दृश् -> पश्य
_PRESENT = frozenset({"लट्", "लोट्", "लङ्", "विधिलिङ्"})


def _suppletive_root(m: Morph, root: str) -> str:
    if root == "दृश्" and "पश्य" in m.form and (m.lakara in _PRESENT or m.krt in ("शतृ", "शानच्")):
        return "पश्"
    if root == "इ" and m.lakara == "लुङ्" and "गा" in m.form:  # 2.4.45 इणो गा लुङि
        return "गा"
    if root == "ब्रू" and any(x in m.form for x in ("आह", "ाह", "आत्थ", "ात्थ")):  # 3.4.84 ब्रुवः पञ्चानाम् ... आहः
        return "अह्"
    return root


@lru_cache(maxsize=100_000)
def _verbal_lemma(prefixes: tuple[str, ...], root: str) -> str:
    out = root
    for p in reversed(prefixes):
        out = _join(p, out)
    return out


def _labial_m(text: str) -> str:
    """The corpus writes म् before a labial (सम्पद्, सम्भू) and ं elsewhere (संगम्, संयम्)."""
    for lab in "पफबभम":
        text = text.replace("ं" + lab, "म्" + lab)
    return text


def verbal_lemma(m: Morph) -> str:
    """The upasargas joined to the root by sandhi, in the corpus' citation form: प्र+आप् -> प्राप्,
    प्र+नम् -> प्रणम्, आ+इ -> ए, आ+सादि -> आसादय्. For ``mayur.ud.lemma``."""
    return _labial_m(_verbal_lemma(tuple(m.prefixes), _suppletive_root(m, _dcs_root(m))))
