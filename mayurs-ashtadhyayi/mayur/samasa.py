"""Forward समास derivation: an explicit rule chain for a compound, each step citing its सूत्र.

vidyut's Python API has no समास derivation. This module builds the chain itself:
the alaukika-vigraha and the type rule (the TYPE is a heuristic choice and says so),
1.2.46 / 2.4.71 / upasarjana placement, member-form rules, then it RUNS the forward
compound-internal sandhi (``sandhi.outcomes(..., samasa=True)``) member by member and
RUNS vidyut (through ``mayur.bridge``) on the whole compound stem in the final word's
gender, case and number. ``derivable`` is True only when both run steps reproduced the
surface. Nothing is run backward.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence

from mayur import bridge, sandhi
from mayur.model import Morph, SutraStep

SRC = "अष्टाध्यायी"
HEUR = "(heuristic choice of type)"

TYPE_RULE: dict[str, tuple[str, str]] = {
    "षष्ठी": ("2.2.8", "षष्ठी"),
    "द्वितीया": ("2.1.24", "द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः"),
    "तृतीया": ("2.1.30", "तृतीया तत्कृतार्थेन गुणवचनेन"),
    "चतुर्थी": ("2.1.36", "चतुर्थी तदर्थार्थबलिहितसुखरक्षितैः"),
    "पञ्चमी": ("2.1.37", "पञ्चमी भयेन"),
    "सप्तमी": ("2.1.40", "सप्तमी शौण्डैः"),
    "कर्मधारय": ("2.1.57", "विशेषणं विशेष्येण बहुलम्"),
    "नञ्": ("2.2.6", "नञ्"),
    "उपपद": ("2.2.19", "उपपदमतिङ्"),
    "द्वन्द्व": ("2.2.29", "चार्थे द्वन्द्वः"),
    "बहुव्रीहि": ("2.2.24", "अनेकमन्यपदार्थे"),
    "अव्ययीभाव": ("2.1.6", "अव्ययं विभक्तिसमीप..."),
    "प्रादि": ("2.2.18", "कुगतिप्रादयः"),
    "सह": ("2.2.28", "तेन सहेति तुल्ययोगे"),
    "द्विगु": ("2.1.52", "संख्यापूर्वो द्विगुः"),
    "उपमान": ("2.1.55", "उपमानानि सामान्यवचनैः"),
    "उपमान-बहुव्रीहि": ("2.2.24", "अनेकमन्यपदार्थे"),
    "तुं-काम": ("2.2.24", "अनेकमन्यपदार्थे"),
    "संख्या": ("2.1.57", "विशेषणं विशेष्येण बहुलम्"),
}
# 2.1.32 कर्तृकरणे कृता बहुलम् for तृतीया with a कृदन्त final member
TRITIYA_KRT = ("2.1.32", "कर्तृकरणे कृता बहुलम्")

SUP_EKA = {"प्रथमा": "सु", "द्वितीया": "अम्", "तृतीया": "टा", "चतुर्थी": "ङे", "पञ्चमी": "ङसि",
           "षष्ठी": "ङस्", "सप्तमी": "ङि"}
NAN = {"अ", "अन्", "न", "नञ्"}
_DEVA_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
_VOWEL_START = set("अआइईउऊऋॠऌएऐओऔ")


@dataclass(frozen=True)
class SamasaDerivation:
    stem: str
    trace: tuple[SutraStep, ...]
    derivable: bool
    note: str
    final_form: str = ""


def _step(code: str, result: str) -> SutraStep:
    return SutraStep(SRC, code.translate(_DEVA_DIGITS), result)


def _stem_of(m: Morph) -> str:
    return m.stem or m.lemma


def _member_cases(samasa: str, relation: str, n: int) -> list[str]:
    """Case ending of each member in the alaukika-vigraha."""
    if samasa in ("द्वन्द्व", "बहुव्रीहि", "कर्मधारय", "नञ्", "प्रादि", "सह", "द्विगु", "उपमान",
                  "उपमान-बहुव्रीहि", "तुं-काम", "संख्या", "अव्ययीभाव"):
        return ["सु"] * n
    first = SUP_EKA.get(relation, "ङस्")
    return [first] * (n - 1) + ["सु"]


def _type_step(samasa: str, relation: str, final: Morph, rule_code: str = "", rule_note: str = "") -> SutraStep:
    if rule_code:
        return _step(rule_code, f"{rule_note} {HEUR}")
    key = relation if samasa == "तत्पुरुष" else samasa
    code, name = TYPE_RULE.get(key, TYPE_RULE["षष्ठी"])
    if key == "तृतीया" and final.krt:
        code, name = TRITIYA_KRT
    return _step(code, f"{name}: {samasa}{' (' + relation + ')' if relation else ''} {HEUR}")


def _member_form(stem: str, nxt: str, surface: str) -> tuple[str, Optional[SutraStep]]:
    """Forms that a non-final member takes before sandhi (only where the surface shows it)."""
    if stem == "महत्" and surface.startswith("महा"):
        return "महा", _step("6.3.46", "आन्महतः समानाधिकरणजातीययोः: महत् → महा")
    if stem in NAN:
        if nxt[:1] in _VOWEL_START:
            return "अन्", _step("6.3.74", "तस्मान्नुडचि: न → अन्")
        return "अ", _step("6.3.73", "नलोपो नञः: न → अ")
    if stem.endswith("न्") and len(stem) > 2:
        return stem[:-2], _step("8.2.7", f"नलोपः प्रातिपदिकान्तस्य: {stem} → {stem[:-2]}")
    return stem, None


def _join(parts: Sequence[str], forms: Sequence[str], surface: str) -> tuple[str, list[SutraStep], bool]:
    """RUN compound-internal sandhi left to right, keeping the outcome that the surface shows."""
    target = sandhi.canon(surface)
    acc, steps, ok = parts[0], [], True
    for k in range(1, len(parts)):
        cands = [acc] if k > 1 else list(dict.fromkeys([acc, forms[0]]))
        chosen = None
        for left in cands:
            for o in sandhi.outcomes(left, parts[k], samasa=True):
                if target.startswith(sandhi.canon(o.text)) or k == len(parts) - 1 and sandhi.canon(o.text) == target:
                    chosen = (left, o)
                    break
            if chosen:
                break
        if chosen is None:
            outs = sandhi.outcomes(acc, parts[k], samasa=True)
            ok = False
            if not outs:
                return acc + parts[k], steps + [_step("—", f"{acc} + {parts[k]}: sandhi gave no outcome")], False
            chosen = (acc, outs[0])
        left, o = chosen
        via = "" if left == acc else f" (member taken in its pada form {left})"
        steps.append(_step(", ".join(o.sutras) or "—", f"{left} + {parts[k]} → {o.text}{via}"))
        acc = o.text
    return acc, steps, ok and sandhi.canon(acc) == target


def _expected(stem: str, final: Morph) -> str:
    """The whole compound pada as the text shows it: the final member's ending put on the
    compound stem (the part of the final stem the pada keeps is replaced by the pada)."""
    fs = _stem_of(final)
    common = 0
    while common < min(len(fs), len(final.form)) and fs[common] == final.form[common]:
        common += 1
    cut = len(fs) - common
    return (stem[: len(stem) - cut] if cut else stem) + final.form[common:]


def _inflect(stem: str, final: Morph) -> tuple[str, list[SutraStep], bool, str]:
    """RUN vidyut on the compound stem in the final word's gender/case/number."""
    if not (final.linga and final.vibhakti and final.vacana):
        return "", [], False, "final word has no gender/case/number: step d not run"
    try:
        paradigm = bridge.subanta_paradigm(stem, final.linga)
    except Exception as e:  # noqa: BLE001 - vidyut rejected the stem
        return "", [], False, f"bridge.subanta_paradigm failed: {e}; step d not run"
    match = [h for h, m in paradigm if (m.vibhakti, m.vacana) == (final.vibhakti, final.vacana)]
    ders = bridge.derive(match[0]) if match else ()
    if not ders:
        return "", [], False, "vidyut derived nothing for the compound stem; step d not run"
    from mayur.lexicon import nasal_variants
    expected = _expected(stem, final)
    targets = {sandhi.canon(v) for v in nasal_variants(expected)} if expected else set()
    for d in ders:
        if sandhi.canon(d.text) in targets:
            return d.text, list(d.trace), True, ""
    return ders[0].text, list(ders[0].trace), False, f"vidyut derived {ders[0].text}, not {expected or final.form}"


def derive(members: Sequence[Morph], final: Morph, samasa: str, relation: str = "",
           surface: str = "", forms: Sequence[str] = (), rule_code: str = "", rule_note: str = "",
           inner: str = "") -> SamasaDerivation:
    """Forward derivation of a compound of ``members`` (all members, the last being
    ``final``'s stem) of type ``samasa`` (relation = vibhakti for a विभक्ति-तत्पुरुष).
    ``surface`` is the expected compound stem; ``forms`` the members' written forms.
    ``rule_code``/``rule_note``: the type rule as decided (mayur.samasa_type); ``inner``: the
    type of the non-final members when they form a compound first (द्वन्द्व)."""
    stems = [_stem_of(m) for m in members]
    surface = surface or "".join(stems)
    forms = list(forms) or stems
    cases = _member_cases(samasa, relation, len(stems))
    vig = " + ".join(f"{s} + {c}" for s, c in zip(stems, cases))
    inner_steps = [_step("2.2.29", f"चार्थे द्वन्द्वः: [{' + '.join(stems[:-1])}] first, as one member "
                                   f"(bracketing) {HEUR}")] if inner == "द्वन्द्व" and len(stems) > 2 else []
    trace = [_step("2.1.3", f"प्राक्कडारात्समासः: {vig}"),
             _step("2.1.4", f"सह सुपा: {vig}"),
             *inner_steps,
             _type_step(samasa, relation, final, rule_code, rule_note),
             _step("1.2.43", f"प्रथमानिर्दिष्टं समास उपसर्जनम्: {stems[0]} उपसर्जन"),
             _step("2.2.30", f"उपसर्जनं पूर्वम्: {' + '.join(f'{s} + {c}' for s, c in zip(stems, cases))}"),
             _step("1.2.46", f"कृत्तद्धितसमासाश्च: प्रातिपदिक {' + '.join(stems)}"),
             _step("2.4.71", f"सुपो धातुप्रातिपदिकयोः: {' + '.join(stems)}")]
    parts = []
    for k, s in enumerate(stems):
        if k < len(stems) - 1:
            form, member_step = _member_form(s, stems[k + 1], surface if k == 0 else "")
            if member_step:
                trace.append(member_step)
            parts.append(form)
        else:
            parts.append(s)
    notes = ["समासान्त (5.4.x) and पुंवद्भाव (6.3.34) not applied"]
    stem, sandhi_steps, ok_c = _join(parts, forms, surface) if len(parts) > 1 else (parts[0], [], True)
    trace += sandhi_steps
    if not ok_c:
        notes.append(f"sandhi gave {stem}, not {surface}")
    word, inflect_steps, ok_d, note_d = _inflect(surface if ok_c else stem, final)
    trace += inflect_steps
    if note_d:
        notes.append(note_d)
    return SamasaDerivation(stem=stem, trace=tuple(trace), derivable=ok_c and ok_d,
                            note="; ".join(notes), final_form=word)
