"""Kāraka engine: which case endings express a role, read off the Aṣṭādhyāyī (karaka_rules).

FORWARD  ``expected_cases(role, governor)`` — given what the governor already expresses
(3.4.67–72 for kṛt and tiṅ), the case(s) that express ``role`` with the rules that do it.
LOOKUP   ``licences(dependent, governor)`` — every role the dependent's actual case can express:
built by running ``expected_cases`` for each role and keeping those that reproduce the case.
CHECK    ``verify(reading)`` — re-runs the forward rules on every role link of a reading.
``mayur.karaka_links.license_words`` (used by shabdabodha.resolve) keeps only licensed links.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Optional

from mayur.karaka_rules import (ADHI_SHI, BHI_ARTHA, DVIKARMAKA, GATI_AKARMAKA, KALA_ADHVA, KRUDHA_ARTHA, RUCI_ARTHA,
                                RULES, SEPARATION, SIMILAR, UPAPADA_WORDS, VARANA_ARTHA, VIBHAKTI)
from mayur.model import Morph, Reading

P1, P2, P3, P4, P5, P6, P7, PS = "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
KARAKAS = ("कर्ता", "कर्म", "करण", "सम्प्रदान", "अपादान", "अधिकरण")
CASE_ROLES = KARAKAS + ("सम्बन्ध", "सम्बोधन", "विधेय", "विशेषण", "पूर्वकालक्रिया", "तुमर्थ", "भावलक्षण")
CASE_RULE = {"कर्ता": (P3, "2.3.18"), "करण": (P3, "2.3.18"), "कर्म": (P2, "2.3.2"), "सम्प्रदान": (P4, "2.3.13"),
             "अपादान": (P5, "2.3.28"), "अधिकरण": (P7, "2.3.36")}
NISHTHA = {"क्त", "क्तवतु"}
LA_ADESHA = {"शतृ", "शानच्", "क्वसु", "कानच्"}
AVYAYA_KRT = {"क्त्वा", "ल्यप्", "तुमुन्", "णमुल्"}
KRTYA = {"तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्", "केलिमर्"}
BHAVA_KRT = {"घञ्", "ल्युट्", "क्तिन्", "अ", "युच्", "अप्", "क्तिच्", "अङ्"}
NO_GENITIVE = NISHTHA | LA_ADESHA | AVYAYA_KRT | {"तृन्", "खल्"}  # 2.3.69
PARTICIPLES = NISHTHA | LA_ADESHA
VERBAL_KRT = PARTICIPLES | AVYAYA_KRT | KRTYA


@dataclass(frozen=True)
class Licence:
    role: str
    vibhakti: Optional[str]
    sutras: tuple[str, ...]
    note: str = ""
    krt: tuple[str, ...] = ()  # for verbal dependents: the kṛt the dependent must carry


def is_verbal(m: Optional[Morph]) -> bool:
    return m is not None and (m.kind == "tinanta" or (m.krt is not None and
                                                      (m.root is not None or m.krt in VERBAL_KRT)))


def _root(m: Morph) -> str:
    return m.root or m.lemma


def expressed(gov: Optional[Morph]) -> list[tuple[Optional[str], tuple[str, ...]]]:
    """Options for what the governor's suffix itself expresses: (role or None for भाव, rules)."""
    if gov is None or not is_verbal(gov):
        return []
    if gov.kind == "tinanta":
        return [({"कर्मणि": "कर्म", "भावे": None}.get(gov.prayoga or "", "कर्ता"), ("3.4.69",))]
    krt = gov.krt or ""
    if krt in AVYAYA_KRT or krt in BHAVA_KRT:
        return [(None, ())]  # agent shared with the main verb (3.4.21, 3.3.158) / action noun
    if krt == "क्त":
        out: list[tuple[Optional[str], tuple[str, ...]]] = [("कर्म", ("3.4.70",))]
        return out + [("कर्ता", ("3.4.72",))] if _root(gov) in GATI_AKARMAKA else out
    if krt in KRTYA:
        return [("कर्म", ("3.4.70",))]
    return [("कर्ता", ("3.4.67",))]


def definitions(role: str, gov: Optional[Morph]) -> list[tuple[str, ...]]:
    """Rules that give the dependent the kāraka name ``role`` with this governor (alternatives)."""
    root = _root(gov) if gov is not None else ""
    pre = gov.prefixes if gov is not None else ()
    base = {"कर्ता": "1.4.54", "कर्म": "1.4.49", "करण": "1.4.42", "सम्प्रदान": "1.4.32", "अपादान": "1.4.24",
            "अधिकरण": "1.4.45"}[role]
    out = [(base,)]
    special = {"कर्म": [("1.4.51", root in DVIKARMAKA), ("1.4.46", root in ADHI_SHI and "अधि" in pre)],
               "सम्प्रदान": [("1.4.33", root in RUCI_ARTHA), ("1.4.37", root in KRUDHA_ARTHA)],
               "अपादान": [("1.4.25", root in BHI_ARTHA), ("1.4.27", root in VARANA_ARTHA)]}
    return out + [(r,) for r, ok in special.get(role, []) if ok]


def _number_rule(m: Optional[Morph]) -> tuple[str, ...]:
    if m is None or not m.vacana:
        return ()
    return ("1.4.21",) if m.vacana == "बहुवचन" else ("1.4.22",)


def _karaka_cases(role: str, gov: Morph, dep: Optional[Morph]) -> list[Licence]:
    out: list[Licence] = []
    for exp_role, exp_rules in expressed(gov):
        for d in definitions(role, gov):
            if role == exp_role:
                out.append(Licence(role, P1, d + exp_rules + ("2.3.46",), "अभिहित: प्रथमा"))
                continue
            if "1.4.46" in d:
                out.append(Licence(role, P2, d + ("2.3.2",), "अधि+शीङ्स्थास्: आधारः कर्म"))
                continue
            case, rule = CASE_RULE[role]
            out.append(Licence(role, case, d + (rule,), "अनभिहिते (2.3.1)"))
            if gov.kind != "tinanta" and role in ("कर्ता", "कर्म"):
                if (gov.krt or "") not in NO_GENITIVE:
                    out.append(Licence(role, P6, d + ("2.3.65",), "कृद्योगे षष्ठी"))
                elif gov.krt == "क्त" and role == "कर्ता":
                    out.append(Licence(role, P6, d + ("2.3.67",), "वर्तमाने क्त एव"))
    if role == "अधिकरण":
        if dep is not None and dep.lemma in KALA_ADHVA:
            out.append(Licence(role, P2, ("2.3.5",), "कालाध्वनोरत्यन्तसंयोगे"))
    if role == "कर्म" and gov.kind == "tinanta" and gov.prayoga == "कर्मणि" and _root(gov) in DVIKARMAKA:
        out.append(Licence(role, P2, ("1.4.51", "2.3.2"), "द्विकर्मके अप्रधानं कर्म"))
    return _dedupe(out)


def _dedupe(lics: list[Licence]) -> list[Licence]:
    seen: set[tuple] = set()
    out = []
    for lic in lics:
        k = (lic.role, lic.vibhakti, lic.sutras)
        if k not in seen:
            seen.add(k)
            out.append(lic)
    return out


def upapada(gov: Optional[Morph]) -> list[Licence]:
    """Cases an indeclinable/adjectival governor (नमस्, सह, विना, तुल्य …) assigns (role सम्बन्ध)."""
    if gov is None:
        return []
    names = {gov.lemma, gov.form, gov.stem}
    out = [Licence("सम्बन्ध", UPAPADA_WORDS[n][0], UPAPADA_WORDS[n][1], "उपपदविभक्ति") for n in names
           if n in UPAPADA_WORDS]
    if names & SEPARATION:
        out += [Licence("सम्बन्ध", P3, ("2.3.32",), "उपपदविभक्ति"), Licence("सम्बन्ध", P5, ("2.3.32",), "पक्षे पञ्चमी")]
    if names & SIMILAR:
        out += [Licence("सम्बन्ध", P3, ("2.3.72",), "उपपदविभक्ति"), Licence("सम्बन्ध", P6, ("2.3.72",), "पक्षे षष्ठी")]
    return _dedupe(out)


def expected_cases(role: str, governor: Optional[Morph], dependent: Optional[Morph] = None) -> list[Licence]:
    """FORWARD: the case endings (with rules) that express ``role`` with this governor."""
    if role in KARAKAS:
        if is_verbal(governor):
            return _karaka_cases(role, governor, dependent)
        if role == "अधिकरण" and governor is not None and governor.kind == "subanta":  # वीर्ये सदृशस्
            return [Licence(role, P7, ("1.4.45", "2.3.36"), "आधारः of the understood अस्ति (अध्याहार)")]
        return []
    if role == "सम्बन्ध":
        return upapada(governor) + [Licence(role, P6, ("2.3.50",), "शेषे षष्ठी")]
    if role == "भावलक्षण":  # गते रामे: the action of one marks the time of another (not a kāraka)
        if not is_verbal(governor):
            return []
        return [Licence(role, P7, ("2.3.37",), "भावलक्षण सप्तमी"), Licence(role, P6, ("2.3.38",), "अनादरे षष्ठी")]
    if role == "सम्बोधन":
        return [Licence(role, PS, ("2.3.47",))]
    if role == "विधेय":
        return [Licence(role, P1, ("2.3.46",), "प्रातिपदिकार्थमात्रे")]
    if role == "विशेषण":
        if is_verbal(governor) and governor.kind == "tinanta":  # qualifies the expressed, unstated kāraka
            return [Licence(role, P1, rules + ("2.3.46",) + _number_rule(governor), "qualifies the unexpressed "
                            f"{r} (अध्याहार)") for r, rules in expressed(governor) if r]
        if governor is None or governor.kind != "subanta":
            return []
        return [Licence(role, governor.vibhakti, _number_rule(governor), "समानाधिकरणम्: विशेष्यस्य विभक्तिः")]
    if role == "पूर्वकालक्रिया" and is_verbal(governor):
        return [Licence(role, None, ("3.4.21",), "समानकर्तृकयोः", ("क्त्वा", "ल्यप्"))]
    if role == "तुमर्थ" and is_verbal(governor):
        return [Licence(role, None, ("3.3.10", "3.3.158"), "क्रियार्थायाम्", ("तुमुन्",))]
    return []


def nominal_person(m: Morph) -> tuple[str, str]:
    if m.lemma == "अस्मद्":
        return "उत्तमपुरुष", "1.4.107"
    if m.lemma == "युष्मद्":
        return "मध्यमपुरुष", "1.4.105"
    return "प्रथमपुरुष", "1.4.108"


def agreement(dep: Morph, gov: Morph) -> Optional[tuple[str, ...]]:
    """Rules by which the governor agrees with the kāraka it expresses; None if it does not."""
    if gov.kind == "tinanta":
        person, rule = nominal_person(dep)
        ok = dep.vacana == gov.vacana and person == (gov.purusha or "प्रथमपुरुष")
        return (rule,) + _number_rule(gov) if ok else None
    ok = (dep.vacana, dep.linga) == (gov.vacana, gov.linga) or not gov.vacana
    return _number_rule(gov) if ok else None


def matches(lic: Licence, dep: Morph) -> bool:
    if lic.krt:
        return dep.krt in lic.krt
    return dep.kind == "subanta" and dep.vibhakti == lic.vibhakti


def licences(dependent: Morph, governor: Optional[Morph]) -> list[Licence]:
    """LOOKUP: every role the dependent's case can express with this governor (from the forward rules)."""
    out = []
    for role in CASE_ROLES:
        for lic in expected_cases(role, governor, dependent):
            if not matches(lic, dependent):
                continue
            if lic.vibhakti == P1 and role in KARAKAS:  # the governor expresses it: it must agree
                rules = agreement(dependent, governor)
                if rules is None:
                    continue
                lic = replace(lic, sutras=lic.sutras + rules)
            if role == "विशेषण" and dependent.vacana != governor.vacana:
                continue
            out.append(lic)
    return out


def text(number: str) -> str:
    return RULES[number].text if number in RULES else ""


def case_rules(sutras: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(s for s in sutras if s in RULES and RULES[s].kind == VIBHAKTI)


def verify(reading: Reading) -> list[str]:
    """Violations: role links whose case the forward rules do not produce (empty = derivable)."""
    words = reading.words
    bad = []
    for i, w in enumerate(words):
        if w.role not in CASE_ROLES or w.in_compound or w.morph is None:
            continue
        gov = words[w.head].morph if w.head is not None and 0 <= w.head < len(words) else None
        if w.head is None and w.role not in ("विधेय", "सम्बोधन"):
            continue  # unlinked: listed by license_words, not a case violation
        exp = expected_cases(w.role, gov, w.morph)
        if not any(matches(lic, w.morph) for lic in exp):
            got = w.morph.vibhakti or w.morph.krt or w.morph.kind
            want = ", ".join(sorted({lic.vibhakti or "/".join(lic.krt) for lic in exp})) or "—"
            bad.append(f"{w.form}: {w.role} of {words[w.head].form if w.head is not None else '—'} "
                       f"needs {want}, has {got}")
    return bad
