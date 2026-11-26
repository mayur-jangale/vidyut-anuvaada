"""Kāraka engine: which case endings express a role, read off the Aṣṭādhyāyī (karaka_rules).

FORWARD  ``expected_cases(role, governor)`` — given what the governor already expresses
(3.4.67–72 for kṛt and tiṅ), the case(s) that express ``role`` with the rules that do it.
LOOKUP   ``licences(dependent, governor)`` — every role the dependent's actual case can express:
built by running ``expected_cases`` for each role and keeping those that reproduce the case.
CHECK    ``verify(reading)`` — re-runs the forward rules on every role link of a reading.
``license_words`` (used by shabdabodha.resolve) keeps only licensed links and records the rules.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Optional

from mayur.karaka_rules import (ADHI_SHI, BHI_ARTHA, DVIKARMAKA, GATI_AKARMAKA, KALA_ADHVA, KRUDHA_ARTHA, RUCI_ARTHA,
                                RULES, SEPARATION, SIMILAR, UPAPADA_WORDS, VARANA_ARTHA, VIBHAKTI)
from mayur.model import Morph, Reading, Word

P1, P2, P3, P4, P5, P6, P7, PS = "प्रथमा", "द्वितीया", "तृतीया", "चतुर्थी", "पञ्चमी", "षष्ठी", "सप्तमी", "सम्बोधन"
KARAKAS = ("कर्ता", "कर्म", "करण", "सम्प्रदान", "अपादान", "अधिकरण")
CASE_ROLES = KARAKAS + ("सम्बन्ध", "सम्बोधन", "विधेय", "विशेषण", "पूर्वकालक्रिया", "तुमर्थ")
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
        out.append(Licence(role, P7, ("2.3.37",), "भावलक्षण सप्तमी (कारकं न)"))
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
    if role == "सम्बोधन":
        return [Licence(role, PS, ("2.3.47",))]
    if role == "विधेय":
        return [Licence(role, P1, ("2.3.46",), "प्रातिपदिकार्थमात्रे")]
    if role == "विशेषण":
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


# Licensing the links of a reading (used by shabdabodha.resolve).

STRUCTURAL = {"क्रिया", "समासपूर्वपद", "अव्यय", ""}
UPAPADA_REACH = 2


def _gov(words: list[Word], h: Optional[int]) -> Optional[Morph]:
    return words[h].morph if h is not None and 0 <= h < len(words) else None


def _upapada_head(words: list[Word], i: int) -> Optional[tuple[int, Licence]]:
    """An upapada word (सह, नमस्, विना …) within reach in the same line that assigns this case."""
    dep = words[i].morph
    near = sorted((j for j in range(max(0, i - UPAPADA_REACH), min(len(words), i + UPAPADA_REACH + 1))
                   if j != i and words[j].line == words[i].line and not words[j].in_compound),
                  key=lambda j: (abs(j - i), j != words[i].head, j < i))
    for j in near:
        for lic in upapada(words[j].morph):
            if matches(lic, dep):
                return j, lic
    return None


def _bhavalakshana(words: list[Word], i: int) -> bool:
    """Evidence for 2.3.37: a locative participle in the same case/number qualifies the word."""
    m = words[i].morph
    for j, w in enumerate(words):
        o = w.morph
        if j != i and o is not None and (w.head == i or i == j + 1 or i == j - 1) and o.krt in PARTICIPLES \
                and (o.vibhakti, o.vacana) == (m.vibhakti, m.vacana) and o.kind == "subanta":
            return True
    return m.krt in PARTICIPLES and any(words[j].head == i for j in range(len(words)))


def _verbal_head(words: list[Word], i: int) -> Optional[int]:
    """Nearest verbal word (same half-verse first) whose forward rules license this word's role."""
    w = words[i]
    near = sorted((j for j, o in enumerate(words) if j != i and not o.in_compound and is_verbal(o.morph) and o.head != i),
                  key=lambda j: (words[j].line != w.line, abs(j - i)))
    return next((j for j in near if any(lic.role == w.role for lic in licences(w.morph, words[j].morph))), None)


def _choose(words: list[Word], i: int, role: str, lics: list[Licence]) -> Licence:
    mine = [lic for lic in lics if lic.role == role]
    if role == "अधिकरण" and len(mine) > 1:
        want = "2.3.37" if _bhavalakshana(words, i) else "1.4.45"
        mine = [lic for lic in mine if want in lic.sutras] or mine
    return mine[0]


def _promote_predicates(words: list[Word], notes: list[str]) -> list[Word]:
    """रावणस् हतस्: a predicate kṛt that expresses a kāraka (3.4.67/3.4.70/3.4.72) governs its subject."""
    out = list(words)
    for i, w in enumerate(out):
        if w.role or w.head is not None or w.morph is None or w.morph.vibhakti != P1 or w.in_compound:
            continue
        preds = [j for j, p in enumerate(out) if p.head == i and p.role == "विधेय" and is_verbal(p.morph)
                 and p.morph.krt in NISHTHA | KRTYA]
        for j in preds:
            lics = [lic for lic in licences(w.morph, out[j].morph) if lic.role in ("कर्ता", "कर्म")]
            if lics:
                out[j] = replace(out[j], role="क्रिया", head=None)
                for k, o in enumerate(out):  # dependents of the subject that belong to the action
                    if o.head == i and k != j and o.role in KARAKAS:
                        out[k] = replace(o, head=j)
                out[i] = replace(w, role=lics[0].role, head=j)
                notes.append(f"{out[j].form}: कृदन्त predicate; {w.form} is its {lics[0].role} "
                             f"({', '.join(lics[0].sutras)}); copula अस्ति supplied (अध्याहार)")
                break
    return out


def license_words(words_in: list[Word]) -> tuple[list[Word], list[str]]:
    """New words where each case-role link is licensed (``role_sutras`` set) or removed."""
    notes: list[str] = []
    words = _promote_predicates([replace(w, role_sutras=()) for w in words_in], notes)
    order = sorted(range(len(words)), key=lambda k: words[k].role == "विशेषण")
    for i in order:
        w = words[i]
        if w.role == "" and w.head is None and w.morph is not None and w.morph.vibhakti == P1 and not w.in_compound:
            words[i] = replace(w, role_sutras=("2.3.46",))  # subject of a nominal clause
            continue
        if w.role in STRUCTURAL or w.role not in CASE_ROLES or w.morph is None or w.in_compound:
            continue
        hit = _upapada_head(words, i) if w.role in ("करण", "सम्प्रदान", "अपादान", "सम्बन्ध") else None
        if hit is None and w.head is None and w.role not in ("विधेय", "सम्बोधन"):
            continue
        if hit is not None and (hit[0] != w.head or w.role != "सम्बन्ध"):
            j, lic = hit
            notes.append(f"{w.form}: {w.morph.vibhakti} with {words[j].form} ({', '.join(lic.sutras)}) chosen "
                         f"over {w.role} (choice: adjacent उपपद)")
            words[i] = replace(w, role="सम्बन्ध", head=j, role_sutras=lic.sutras)
            continue
        gov = _gov(words, w.head)
        lics = licences(w.morph, gov)
        roles = sorted({lic.role for lic in lics if lic.role in KARAKAS + ("सम्बन्ध",)})
        if any(lic.role == w.role for lic in lics):
            lic = _choose(words, i, w.role, lics)
            sutras = lic.sutras
            if w.role == "विशेषण":
                sutras = sutras + case_rules(words[w.head].role_sutras)
            words[i] = replace(w, role_sutras=sutras)
            if len(roles) > 1:
                notes.append(f"{w.form}: {w.morph.vibhakti} can be {' / '.join(roles)}; {w.role} chosen by evidence")
            continue
        alt = [lic for lic in lics if lic.role in KARAKAS + ("सम्बन्ध",)]
        if alt:
            words[i] = replace(w, role=alt[0].role, role_sutras=alt[0].sutras)
            notes.append(f"{w.form}: {w.role} not licensed with {words[w.head].form}; {alt[0].role} "
                         f"({', '.join(alt[0].sutras)}) is (choice among licensed roles)")
        elif (j := _verbal_head(words, i)) is not None:
            lic = _choose(words, i, w.role, licences(w.morph, words[j].morph))
            words[i] = replace(w, head=j, role_sutras=lic.sutras)
            notes.append(f"{w.form}: {w.role} re-attached to the nearest verbal {words[j].form} "
                         f"({', '.join(lic.sutras)}); {words[w.head].form if w.head is not None else '—'} "
                         f"cannot govern it (choice: nearest licensed governor)")
        else:
            words[i] = replace(w, head=None)
            notes.append(f"{w.form}: no rule licenses {w.role} with "
                         f"{words[w.head].form if w.head is not None else '—'}; left unlinked")
    return _second_objects(words, notes), notes + _expressed_notes(words)


def _second_objects(words_in: list[Word], notes: list[str]) -> list[Word]:
    """गाम् दोग्धि पयस्: an ungoverned accusative of a द्विकर्मक verb is its अकथित कर्म (1.4.51)."""
    words = list(words_in)
    for i, w in enumerate(words):
        if w.role or w.head is not None or w.in_compound or w.morph is None or w.morph.vibhakti != P2:
            continue
        verbs = [v for v, o in enumerate(words) if o.role == "क्रिया" and o.line == w.line and is_verbal(o.morph)
                 and _root(o.morph) in DVIKARMAKA and any(d.head == v and d.role == "कर्म" for d in words)]
        if verbs:
            v = min(verbs, key=lambda v: abs(v - i))
            words[i] = replace(w, role="कर्म", head=v, role_sutras=("1.4.51", "2.3.2"))
            notes.append(f"{w.form}: second कर्म of द्विकर्मक {words[v].form} (1.4.51, 2.3.2); which of the two "
                         f"is अकथित is a choice (text order), not decided by rule")
    return words


def _expressed_notes(words: list[Word]) -> list[str]:
    """Each finite verb / kṛt predicate: its expressed kāraka found in the text or supplied (अध्याहार)."""
    out = []
    for v, w in enumerate(words):
        if w.role != "क्रिया" or not is_verbal(w.morph):
            continue
        options = [role for role, _ in expressed(w.morph) if role]
        if options and not any(d.head == v and d.role in options and d.role_sutras for d in words):
            who = {"उत्तमपुरुष": "अहम्", "मध्यमपुरुष": "त्वम्"}.get(w.morph.purusha or "", "सस्")
            by = f" ({who} by 1.4.105–108)" if w.morph.kind == "tinanta" and options[0] == "कर्ता" else ""
            out.append(f"{w.form}: {options[0]} not in the text; supplied by अध्याहार{by}")
    return out


def unlinked(words: list[Word]) -> list[int]:
    """Words with neither a licensed link nor a structural role."""
    return [i for i, w in enumerate(words) if not w.in_compound and w.morph is not None and w.morph.kind != "unknown"
            and not w.role_sutras and not (w.role in STRUCTURAL and w.role and (w.head is not None or w.role == "क्रिया"))]


def check(reading: Reading) -> tuple[float, list[str]]:
    """(1.0 if ``verify`` is clean else 0.0, notes listing violations and unlinked words)."""
    bad = verify(reading)
    lone = [reading.words[i].form for i in unlinked(reading.words)]
    notes = [f"कारक check: {v}" for v in bad] or ["कारक check: every case follows from its role (forward rules)"]
    return (0.0 if bad else 1.0), notes + ([f"unlinked: {' '.join(lone)}"] if lone else [])
