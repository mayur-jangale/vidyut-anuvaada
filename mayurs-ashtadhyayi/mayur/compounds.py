"""Compound (samasa) grouping and heuristic classification.

vidyut's Python API has no samasa derivation, so every type assigned here is a
heuristic; ``Compound.basis`` always starts with "heuristic:". Sutra numbers cited in
``basis`` name the general rule the heuristic targets, not a derivation.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.model import Compound, Morph, Reading, Word

TATPURUSHA = "तत्पुरुष"
KARMADHARAYA = "कर्मधारय"
DVANDVA = "द्वन्द्व"
BAHUVRIHI = "बहुव्रीहि"
NAN_TATPURUSHA = "नञ्-तत्पुरुष"
NAN_BAHUVRIHI = "नञ्-बहुव्रीहि"
UNKNOWN = "अज्ञात"

_KTA = {"क्त", "क्तवतु"}
_AGENT_KRT = {"क", "क्विप्", "अण्", "ण्वुल्", "तृच्", "तृन्", "अच्", "ड", "खश्", "टक्", "णिनि"}
_AGENT_ENDINGS = ("ज्ञ", "विद्", "कृत्", "कर", "ग", "द", "प", "स्थ", "हन्", "जित्")
_SAMA_LIKE = {"सम", "सदृश", "प्रिय", "उपेत", "सम्पन्न", "युक्त"}
_EPITHET_PREFIX = {"सु", "दुस्", "दुर्", "महा", "महत्"}
_NAN_FORMS = {"अ", "अन्", "न", "नञ्"}
_ADJ_CLASSES = {"adjective"}
_VIRAMA = "्"
_MATRAS = set("ािीुूृॄेैोौंःँ") | {_VIRAMA}


def _lemma_class(lemma: str) -> str:
    try:
        from mayur import freq
        return freq.lemma_class(lemma)
    except Exception:  # tables or module missing: no class information
        return ""


def _lemma(word: Word) -> str:
    m = word.morph
    return (m.stem or m.lemma) if m else word.form


def _lexical_genders(lemma: str) -> set[str]:
    """Genders the lexicon gives the stem itself (empty when unknown)."""
    try:
        from mayur import lexicon
        return {m.linga for m in lexicon.stems(lemma) if m.linga}
    except Exception:  # lexicon unavailable
        return set()


def _gender_shift(word: Word) -> bool:
    """Final member used in a gender it does not have lexically (व्रत n. in दृढव्रतस् m.)."""
    m = word.morph
    genders = _lexical_genders(_lemma(word))
    return bool(m is not None and m.linga and genders and m.linga not in genders)


def _is_a_stem(stem: str) -> bool:
    return bool(stem) and stem[-1] not in _MATRAS and "क" <= stem[-1] <= "ह"


def _is_adjectival(word: Word) -> bool:
    m = word.morph
    if m is None:
        return False
    return m.krt in _KTA or _lemma_class(m.lemma) in _ADJ_CLASSES


def _final_governs(final: Optional[Morph]) -> str:
    """'kta', 'agent' or '' for a final member that can govern the preceding member."""
    if final is None:
        return ""
    if final.krt in _KTA:
        return "kta"
    lemma = final.stem or final.lemma
    if final.krt in _AGENT_KRT or lemma.endswith(_AGENT_ENDINGS):
        return "agent"
    return ""


def _external_head(reading: Reading, idx: int) -> bool:
    """Does the compound's final pada qualify another word of the reading?"""
    word = reading.words[idx]
    if word.role in ("विशेषण", "विधेय"):
        return True
    if word.role:
        return False
    m = word.morph
    if m is None or m.vibhakti is None:
        return False
    for j, other in enumerate(reading.words):
        om = other.morph
        if j == idx or other.in_compound or om is None or om.kind != "subanta":
            continue
        if (om.vibhakti, om.vacana, om.linga) == (m.vibhakti, m.vacana, m.linga):
            return True
    return False


def _bahuvrihi_vigraha(members: list[Word]) -> str:
    """'दृढं व्रतं यस्य सः' when both members are अ-stems and the final's gender is known."""
    if len(members) != 2:
        return ""
    first, last = _lemma(members[0]), _lemma(members[1])
    stem_gender = next((a.linga for a in members[1].analyses if a.kind == "stem" and a.linga), None)
    if not (_is_a_stem(first) and _is_a_stem(last)) or stem_gender is None:
        return ""
    if stem_gender == "नपुंसकलिङ्ग":
        return f"{first}ं {last}ं यस्य सः"
    if stem_gender == "पुंलिङ्ग":
        return f"{first}ः {last}ः यस्य सः"
    return ""


_KTA_RELATION = {"रत": "सप्तमी", "निरत": "सप्तमी", "युक्त": "तृतीया", "उपेत": "तृतीया", "सम्पन्न": "तृतीया",
                 "गत": "द्वितीया", "प्राप्त": "द्वितीया", "आपन्न": "द्वितीया", "सदृश": "तृतीया", "सम": "तृतीया"}
_UPAPADA = ("ज्ञ", "विद्", "कृत्", "हन्", "द", "ग", "स्थ", "धर", "कर", "हर", "भृत्", "जित्")


def relation(final_stem: str) -> str:
    """Vibhakti of the first member as decided by the final member (षष्ठी by default)."""
    for key, rel in _KTA_RELATION.items():
        if final_stem == key or final_stem.endswith(key) and len(key) > 1:
            return rel
    return "षष्ठी"


def samasa_key(samasa: str, basis: str) -> str:
    """Key into ``samasa.TYPE_RULE`` for a (samasa, basis) pair."""
    if samasa in (NAN_TATPURUSHA, NAN_BAHUVRIHI):
        return "नञ्" if samasa == NAN_TATPURUSHA else BAHUVRIHI
    if samasa == TATPURUSHA and "उपपद" in basis:
        return "उपपद"
    return samasa


def derivation(reading: Reading, comp: Compound) -> "samasa.SamasaDerivation":
    """Forward rule chain (mayur.samasa) for ``comp``; inner द्वन्द्व is noted in basis."""
    from mayur import samasa
    words = [reading.words[i] for i in comp.members]
    morphs = [w.morph or Morph(form=w.form, lemma=w.form, kind="stem") for w in words]
    final = morphs[-1]
    rel = relation(_lemma(words[-1])) if comp.samasa == TATPURUSHA and "उपपद" not in comp.basis else ""
    return samasa.derive(morphs, final, samasa_key(comp.samasa, comp.basis), relation=rel,
                         surface=comp.stem, forms=[w.form for w in words])


def classify(reading: Reading, members: list[int]) -> tuple[str, str, str]:
    """(samasa, vigraha, basis) for the compound made of ``members``."""
    words = [reading.words[i] for i in members]
    hyphen = "-".join(w.form if w.in_compound else _lemma(w) for w in words)
    final = words[-1].morph
    first = words[0]
    if first.form in _NAN_FORMS:
        if _external_head(reading, members[-1]):
            return NAN_BAHUVRIHI, hyphen, "heuristic: नञ् first member; whole qualifies an external head (2.2.24, 2.2.6)"
        return NAN_TATPURUSHA, hyphen, "heuristic: नञ् first member (2.2.6)"
    final_stem = _lemma(words[-1])
    if final_stem in _SAMA_LIKE:
        rel = "षष्ठी" if final_stem == "प्रिय" else "तृतीया"
        return TATPURUSHA, hyphen, f"heuristic: noun + {final_stem}, {rel} relation (2.1.31 / 2.2.8)"
    classes = [_lemma_class(_lemma(w)) for w in words]
    if first.form in _EPITHET_PREFIX and classes[-1] in ("noun", "") and _external_head(reading, members[-1]):
        vig = _bahuvrihi_vigraha(words) or hyphen
        return BAHUVRIHI, vig, "heuristic: सु/दुस्/महा + noun used as an epithet of an external head (2.2.24)"
    governs = _final_governs(final)
    if final_stem in _UPAPADA or (len(words) == 2 and final_stem.endswith(("ज्ञ", "विद्", "कृत्", "हन्", "भृत्"))):
        return TATPURUSHA, hyphen, "heuristic: root-noun/kṛt agent final governs the first member, उपपद (2.2.19)"
    if governs == "kta" and final_stem in _KTA_RELATION:
        rel = relation(final_stem)
        inner = " [inner द्वन्द्व of the non-final members, 2.2.29]" if len(words) > 2 else ""
        return TATPURUSHA, hyphen, f"heuristic: क्त final {final_stem} takes {rel} (table){inner}"
    if governs == "kta":
        rel = "सप्तमी or तृतीया" if len(words) > 2 else "तृतीया/सप्तमी"
        note = " (non-final members coordinated: द्वन्द्व inside)" if len(words) > 2 else ""
        return TATPURUSHA, hyphen, f"heuristic: क्त final member governs the noun before it, {rel} relation (2.1.40, 2.1.32){note}"
    if governs == "agent":
        return TATPURUSHA, hyphen, "heuristic: agent-noun final member governs the first member, उपपद/षष्ठी relation (2.2.19, 2.2.8)"
    if _is_adjectival(first) or _lemma_class(_lemma(first)) in _ADJ_CLASSES:
        if _external_head(reading, members[-1]):
            vig = _bahuvrihi_vigraha(words) or hyphen
            return BAHUVRIHI, vig, "heuristic: adjective + noun whose whole qualifies an external head (2.2.24)"
        return KARMADHARAYA, hyphen, "heuristic: adjective + noun, same referent (2.1.57)"
    if len(words) >= 2 and all(c == "noun" for c in classes) and final is not None and final.vacana in ("द्विवचन", "बहुवचन"):
        return DVANDVA, " ".join(f"{_lemma(w)} च" for w in words), "heuristic: coordinated nouns, non-singular final (2.2.29)"
    if classes[-1] == "noun" and classes[0] not in ("noun", "") and _external_head(reading, members[-1]):
        return BAHUVRIHI, hyphen, "heuristic: noun-final compound qualifying an external head (2.2.24)"
    if _gender_shift(words[-1]) and _external_head(reading, members[-1]):
        return BAHUVRIHI, hyphen, "heuristic: final noun in a gender not its own, agreeing with an external head (2.2.24)"
    if all(c in ("noun", "") for c in classes) and "noun" in classes and final is not None \
            and final.vacana in (None, "एकवचन"):
        return TATPURUSHA, hyphen, "heuristic: chain of nouns ending in a singular, each qualifying the next (षष्ठी, 2.2.8)"
    return UNKNOWN, hyphen, "heuristic: no pattern matched"


def _runs(words: list[Word]) -> list[list[int]]:
    runs: list[list[int]] = []
    current: list[int] = []
    for i, w in enumerate(words):
        if w.in_compound:
            current.append(i)
            continue
        if current:
            runs.append(current + [i])
            current = []
    if current:  # a dangling run with no final pada: keep it as a compound anyway
        runs.append(current)
    return runs


def annotate(reading: Reading) -> Reading:
    """New Reading with ``compounds`` built and ``Word.compound`` set."""
    runs = _runs(reading.words)
    words = list(reading.words)
    for cid, members in enumerate(runs):
        for i in members:
            words[i] = replace(words[i], compound=cid)
    base = replace(reading, words=words)
    compounds = []
    for cid, members in enumerate(runs):
        samasa, vigraha, basis = classify(base, members)
        stem = _surface_stem(base, members)
        compounds.append(Compound(id=cid, members=list(members), stem=stem, samasa=samasa, vigraha=vigraha, basis=basis))
    return replace(base, compounds=[_with_chain(base, c) for c in compounds])


def _surface_stem(reading: Reading, members: list[int]) -> str:
    """The compound stem as written: member forms re-joined by the sandhi outcome whose
    sūtras the segmenter recorded for each junction (that choice reproduced the text)."""
    from mayur import sandhi
    parts = [reading.words[i].form if reading.words[i].in_compound else _lemma(reading.words[i]) for i in members]
    recorded = {j.left: j.sutras for j in reading.junctions}
    acc = parts[0]
    for k, nxt in enumerate(parts[1:]):
        outs = sandhi.outcomes(acc, nxt, samasa=True)
        want = recorded.get(members[k])
        plain = next((o for o in outs if o.text == acc + nxt), outs[0] if outs else None)
        pick = next((o for o in outs if want and set(want) <= set(o.sutras)), plain)
        acc = pick.text if pick else acc + nxt
    return acc


def _with_chain(reading: Reading, comp: Compound) -> Compound:
    try:
        d = derivation(reading, comp)
    except Exception as e:  # noqa: BLE001 - derivation unavailable: keep the heuristic only
        return replace(comp, basis=f"{comp.basis}; rule chain failed ({e})")
    codes = ", ".join(dict.fromkeys(t.code for t in d.trace if t.source == "अष्टाध्यायी"))[:200]
    status = "derivable" if d.derivable else "not derivable: " + d.note
    vig = vigraha(reading, comp) or comp.vigraha
    return replace(comp, vigraha=vig, basis=f"{comp.basis}; rule chain {codes} ({status})")


def _inflected(stem: str, linga: Optional[str], vibhakti: str, vacana: str) -> str:
    """A form generated FORWARD by vidyut through the bridge ("" if none)."""
    from mayur import bridge
    genders = [linga] if linga else sorted(_lexical_genders(stem)) or ["पुंलिङ्ग"]
    for g in genders:
        try:
            paradigm = bridge.subanta_paradigm(stem, g)
        except Exception:  # noqa: BLE001 - vidyut rejected the stem
            continue
        for h, m in paradigm:
            if (m.vibhakti, m.vacana) == (vibhakti, vacana):
                ders = bridge.derive(h)
                texts = [d.text for d in ders if d.text != stem]  # a bare stem is no inflected form
                if texts:
                    return texts[0]
    return ""


def _own_gender(word: Word) -> Optional[str]:
    m = word.morph
    if m is not None and m.kind == "avyaya":
        return None
    genders = _lexical_genders(_lemma(word))
    if "स्त्रीलिङ्ग" in genders and _lemma(word).endswith(("ा", "ी")):
        return "स्त्रीलिङ्ग"
    return sorted(genders)[0] if genders else None


def vigraha(reading: Reading, comp: Compound) -> str:
    """Laukika-vigraha with every member generated by vidyut; "" if any form is missing."""
    words = [reading.words[i] for i in comp.members]
    final = words[-1].morph
    if final is None or not final.vibhakti or len(words) != 2:
        return ""
    first, last = _lemma(words[0]), _lemma(words[1])
    if words[0].morph is not None and words[0].morph.kind == "avyaya" or first in _EPITHET_PREFIX - {"महा", "महत्"}:
        return ""  # indeclinable first member: no forward-generated vigraha
    if comp.samasa == TATPURUSHA:
        rel = relation(last)
        a = _inflected(first, _own_gender(words[0]), rel, "बहुवचन" if last == "पुंगव" else "एकवचन")
        b = _inflected(last, final.linga, "प्रथमा", "एकवचन")
        return f"{a} {b}" if a and b else ""
    if comp.samasa == KARMADHARAYA:
        g = _own_gender(words[1])
        a, b = _inflected(first, g, "प्रथमा", "एकवचन"), _inflected(last, g, "प्रथमा", "एकवचन")
        return f"{a} {b}" if a and b else ""
    if comp.samasa == BAHUVRIHI:
        g = _own_gender(words[1])
        vac = final.vacana if last in ("बाहु", "अक्ष", "नेत्र") else "एकवचन"
        vac = "द्विवचन" if last == "बाहु" else vac
        a, b = _inflected(first, g, "प्रथमा", vac), _inflected(last, g, "प्रथमा", vac)
        return f"{a} {b} यस्य सः" if a and b else ""
    if comp.samasa == DVANDVA:
        a, b = _inflected(first, _own_gender(words[0]), "प्रथमा", "एकवचन"), _inflected(last, _own_gender(words[1]), "प्रथमा", "एकवचन")
        return f"{a} च {b} च" if a and b else ""
    return ""
