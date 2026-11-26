"""Licensing the role links of a reading (used by shabdabodha.resolve): a link stays only if the
forward rules of ``mayur.karaka`` license it; the rules are stored in ``Word.role_sutras``."""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.karaka import (KARAKAS, CASE_ROLES, KRTYA, NISHTHA, P1, P2, P6, P7, PARTICIPLES, Licence, case_rules,
                          expressed, is_verbal, licences, matches, upapada, verify, _root)
from mayur.karaka_rules import DVIKARMAKA
from mayur.model import Morph, Reading, Word


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
    # षष्ठी चानादरे (2.3.38) needs an action going on in disregard of someone: only a present
    # participle shows that (पश्यतस् तस्य); सुप्तस्य सिंहस्य is an ordinary genitive phrase.
    allowed = PARTICIPLES if m.vibhakti != P6 else PARTICIPLES & {"शतृ", "शानच्", "चानश्"}
    for j, w in enumerate(words):
        o = w.morph
        if j != i and o is not None and (w.head == i or i == j + 1 or i == j - 1) and o.krt in allowed \
                and (o.vibhakti, o.vacana) == (m.vibhakti, m.vacana) and o.kind == "subanta":
            return True
    return m.krt in allowed and any(words[j].head == i for j in range(len(words)))


def _verbal_head(words: list[Word], i: int) -> Optional[int]:
    """Nearest verbal word (same half-verse first) whose forward rules license this word's role."""
    w = words[i]
    near = sorted((j for j, o in enumerate(words) if j != i and not o.in_compound and is_verbal(o.morph) and o.head != i),
                  key=lambda j: (words[j].line != w.line, abs(j - i)))
    return next((j for j in near if any(lic.role == w.role for lic in licences(w.morph, words[j].morph))), None)


def _choose(words: list[Word], i: int, role: str, lics: list[Licence]) -> Licence:
    mine = [lic for lic in lics if lic.role == role]
    if role == "कर्म" and any("1.4.51" in lic.sutras for lic in mine) and any(
            k != i and o.head == words[i].head and o.role == "कर्म" and "1.4.49" in o.role_sutras for k, o in enumerate(words)):
        mine = [lic for lic in mine if "1.4.51" in lic.sutras]  # the verb's other कर्म is already 1.4.49
    return mine[0]


def _promote_predicates(words: list[Word], notes: list[str]) -> list[Word]:
    """रावणस् हतस्: a predicate kṛt that expresses a kāraka (3.4.67/3.4.70/3.4.72) governs its subject."""
    out = list(words)
    for i, w in enumerate(out):
        if w.role not in ("", "कर्ता") or w.head is not None or w.morph is None or w.morph.vibhakti != P1 \
                or w.in_compound:
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
        if w.role in ("", "कर्ता") and w.head is None and w.morph is not None and w.morph.vibhakti == P1 \
                and not w.in_compound:  # subject of a nominal clause: agent of the understood अस्ति (अध्याहार)
            words[i] = replace(w, role="कर्ता", role_sutras=("1.4.54", "2.3.46"))
            continue
        if w.role in STRUCTURAL or w.role not in CASE_ROLES or w.morph is None or w.in_compound:
            continue
        if w.role in ("अधिकरण", "सम्बन्ध") and w.morph.vibhakti in (P7, P6) and _bhavalakshana(words, i):
            gov = w.head if w.head is not None and is_verbal(_gov(words, w.head)) else None
            near = [j for j, o in enumerate(words) if o.role == "क्रिया" and j != i]
            gov = gov if gov is not None else (min(near, key=lambda j: abs(j - i)) if near else None)
            lic = [x for x in licences(w.morph, _gov(words, gov)) if x.role == "भावलक्षण"] if gov is not None else []
            if lic:
                words[i] = replace(w, role="भावलक्षण", head=gov, role_sutras=lic[0].sutras)
                notes.append(f"{w.form}: {w.morph.vibhakti} with an agreeing participle: भावलक्षण "
                             f"({', '.join(lic[0].sutras)}) chosen over {w.role} (evidence: the participle)")
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
