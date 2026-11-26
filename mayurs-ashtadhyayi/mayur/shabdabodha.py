"""Choosing among readings by shabdabodha tests: akanksha, yogyata, sannidhi, frequency.

``resolve`` jointly picks one analysis per word (coordinate ascent over unary corpus
scores plus agreement bonuses) and links words to heads with karaka roles.
``rank`` orders readings by the weighted total and never drops one.
"""

from __future__ import annotations

import math
from dataclasses import replace
from typing import Optional

from mayur.model import Morph, Reading, Word

PRATHAMA, DVITIYA, TRITIYA = "प्रथमा", "द्वितीया", "तृतीया"
SAMBODHANA, SHASHTHI = "सम्बोधन", "षष्ठी"
KARAKA_OF_CASE = {"चतुर्थी": "सम्प्रदान", "पञ्चमी": "अपादान", "सप्तमी": "अधिकरण"}
NONFINITE = {"क्त्वा": "पूर्वकालक्रिया", "ल्यप्": "पूर्वकालक्रिया", "तुमुन्": "तुमर्थ"}
FIRST_PERSON = {"अस्मद्"}
SECOND_PERSON = {"युष्मद्"}
PRONOUNS = {"किम्", "तद्", "यद्", "इदम्", "एतद्", "अदस्", "अस्मद्", "युष्मद्"}

# Weights grid-searched on gold morphology of Bala-kanda 1.21-79 (never 1-20): case+number+gender
# accuracy 0.903 vs 0.872 for unary scores alone, 0.967 oracle over the pruned candidates.
W_LEMMA = 0.3
W_PHRASE = 2.0  # same case+number+gender nominals, divided by distance
W_KARTA = 2.5  # nominative agreeing with a कर्तरि finite verb
W_KARMA = 0.6  # per accusative when a verb or verbal is present
W_STRAY = 0.25  # nominative not agreeing with any karta of a कर्तरि verb
W_VERBLESS = 1.5  # verbless: nominative outside the subject group, or ungoverned accusative
SWEEPS = 4
# total = 0.35·akanksha + 0.2·yogyata + 0.15·sannidhi + 0.3·frequency (frequency: incoming
# score in 0..1, else the mean normalised unary score of the chosen analyses).
WEIGHTS = {"akanksha": 0.35, "yogyata": 0.2, "sannidhi": 0.15, "frequency": 0.3}


def _freq(fn: str, arg) -> float:
    try:
        from mayur import freq
        return float(getattr(freq, fn)(arg) or 0)
    except Exception:  # tables or module not available
        return 0.0


def lemma_class(lemma: str) -> str:
    try:
        from mayur import freq
        return freq.lemma_class(lemma) or ""
    except Exception:
        return ""


def unary(m: Morph) -> float:
    return math.log1p(_freq("analysis_count", m)) + W_LEMMA * math.log1p(_freq("lemma_count", m.lemma)) + m.quality


def _key(m: Morph) -> tuple:
    return (m.kind, m.vibhakti, m.vacana, m.linga, m.purusha, m.lakara, m.lemma, m.krt)


def candidates(word: Word) -> list[int]:
    """Indices into ``word.analyses`` worth considering (distinct, quality ≥ 2 if any)."""
    good = [i for i, m in enumerate(word.analyses) if m.quality >= 2] or list(range(len(word.analyses)))
    seen: set[tuple] = set()
    out = []
    for i in good:
        k = _key(word.analyses[i])
        if k not in seen:
            seen.add(k)
            out.append(i)
    return out


def nominal_person(m: Morph) -> str:
    if m.lemma in FIRST_PERSON:
        return "उत्तमपुरुष"
    if m.lemma in SECOND_PERSON:
        return "मध्यमपुरुष"
    return "प्रथमपुरुष"


def is_finite(m: Optional[Morph]) -> bool:
    return m is not None and m.kind == "tinanta"


def is_nonfinite(m: Optional[Morph]) -> bool:
    return m is not None and m.krt in NONFINITE


def is_case(m: Optional[Morph], case: str) -> bool:
    return m is not None and m.kind == "subanta" and m.vibhakti == case


def agrees(a: Morph, b: Morph) -> bool:
    return a.kind == b.kind == "subanta" and (a.vibhakti, a.vacana, a.linga) == (b.vibhakti, b.vacana, b.linga)


def karta_agrees(n: Morph, v: Morph) -> bool:
    return (is_case(n, PRATHAMA) and is_finite(v) and v.prayoga in (None, "कर्तरि")
            and n.vacana == v.vacana and nominal_person(n) == (v.purusha or "प्रथमपुरुष"))


def pair_bonus(a: Morph, b: Morph, dist: int) -> float:
    """Phrase bonus: nominals in the same case+number+gender, weaker with distance."""
    if agrees(a, b) and a.vibhakti != SAMBODHANA:
        return W_PHRASE / max(dist, 1)
    return 0.0


def objective(words: list[Word], chosen: list[int], active: list[int]) -> float:
    """Joint score: unary + phrase bonuses + saturating karta bonus per verb + karma bonus."""
    ms = {k: words[k].analyses[chosen[k]] for k in active}
    total = sum(unary(m) for m in ms.values())
    keys = sorted(ms)
    for x, i in enumerate(keys):
        for j in keys[x + 1:]:
            total += pair_bonus(ms[i], ms[j], j - i)
    verbs = [m for m in ms.values() if is_finite(m)]
    verbal = bool(verbs) or any(is_nonfinite(m) for m in ms.values())
    for v in verbs:
        kartas = [m for m in ms.values() if karta_agrees(m, v)]
        if kartas:
            total += W_KARTA
        stray = [m for m in ms.values() if is_case(m, PRATHAMA) and v.prayoga in (None, "कर्तरि")
                 and not any(agrees(m, k) for k in kartas)]
        total -= W_STRAY * len(stray)
    if verbal:
        total += W_KARMA * sum(1 for m in ms.values() if is_case(m, DVITIYA))
    else:  # verbless sentence: one subject group; other nominatives do not connect
        noms = [(m.vacana, m.linga) for m in ms.values() if is_case(m, PRATHAMA)]
        if noms:
            total -= W_VERBLESS * (len(noms) - max(noms.count(k) for k in set(noms)))
        total -= W_VERBLESS * sum(1 for m in ms.values() if is_case(m, DVITIYA))  # no verb to govern it
    return total


def choose(words: list[Word]) -> list[int]:
    """Coordinate ascent from the best unary choice; returns chosen analysis indices."""
    cands = [candidates(w) if not w.in_compound else [] for w in words]
    chosen = [max(c, key=lambda i, w=w: unary(w.analyses[i])) if c else w.chosen for c, w in zip(cands, words)]
    active = [k for k, c in enumerate(cands) if c]
    for _ in range(SWEEPS):
        changed = False
        for k in active:
            if len(cands[k]) < 2:
                continue
            best = max(cands[k], key=lambda i: objective(words, chosen[:k] + [i] + chosen[k + 1:], active))
            if best != chosen[k]:
                chosen[k], changed = best, True
        if not changed:
            break
    return chosen


def _compound_final(words: list[Word], i: int) -> Optional[int]:
    for j in range(i + 1, len(words)):
        if not words[j].in_compound:
            return j
    return None


def _nearest(cands: list[int], i: int) -> Optional[int]:
    return min(cands, key=lambda j: (abs(j - i), j < i)) if cands else None


def _head_priority(words: list[Word], i: int, verbs: list[int]) -> float:
    m = words[i].morph
    cls = lemma_class(m.lemma)
    if not verbs and m.vibhakti == PRATHAMA and (cls == "pronoun" or m.lemma in PRONOUNS):
        return 3.0  # verbless sentence: the pronoun (कस्) is the subject
    score = {"noun": 2.0, "pronoun": 1.5, "": 1.0}.get(cls, 0.0)
    if m.krt:
        score -= 0.5
    if i > 0 and words[i - 1].in_compound:
        score -= 0.5
    if verbs:
        score -= 0.1 * min(abs(i - v) for v in verbs)
    return score


def _groups(words: list[Word]) -> list[list[int]]:
    """Agreement groups of case-bearing nominals (same case, number, gender)."""
    groups: dict[tuple, list[int]] = {}
    for i, w in enumerate(words):
        m = w.morph
        if not w.in_compound and m is not None and m.kind == "subanta" and m.vibhakti:
            groups.setdefault((m.vibhakti, m.vacana, m.linga), []).append(i)
    return list(groups.values())


def _set(words: list[Word], i: int, role: str, head: Optional[int]) -> None:
    words[i] = replace(words[i], role=role, head=head)


def assign_roles(words_in: list[Word]) -> tuple[list[Word], list[str]]:
    """Karaka roles and heads for the chosen analyses (returns new Word objects)."""
    words = [replace(w, role="", head=None) for w in words_in]
    notes: list[str] = []
    verbs = [i for i, w in enumerate(words) if is_finite(w.morph)]
    verbals = [i for i, w in enumerate(words) if is_nonfinite(w.morph)]
    for v in verbs:
        _set(words, v, "क्रिया", None)
    for i in verbals:
        _set(words, i, NONFINITE[words[i].morph.krt], _nearest(verbs, i))
    for i, w in enumerate(words):
        if w.in_compound:
            _set(words, i, "समासपूर्वपद", _compound_final(words, i))
        elif w.morph is None or w.morph.kind == "unknown":
            notes.append(f"{w.form}: no analysis; passed through unlinked")
    genitives: list[int] = []
    for group in _groups(words):
        case = words[group[0]].morph.vibhakti
        head = max(group, key=lambda i: _head_priority(words, i, verbs))
        verb = _nearest(verbs, head)
        vm = words[verb].morph if verb is not None else None
        passive = vm is not None and vm.prayoga in ("कर्मणि", "भावे")
        sub_role = "विशेषण"
        if case == PRATHAMA:
            if vm is not None and (karta_agrees(words[head].morph, vm) or not passive):
                role = "कर्म" if passive else "कर्ता"
                if not karta_agrees(words[head].morph, vm) and not passive:
                    notes.append(f"{words[head].form}: कर्ता without number/person agreement with {words[verb].form}")
            elif vm is None:
                role, verb, sub_role = "", None, "विधेय"
                notes.append(f"verbless nominal sentence: {words[head].form} is the subject, agreeing nominatives are विधेय")
            else:
                role = "कर्म"
        elif case == DVITIYA:
            verb = _nearest(verbs + verbals, head)
            role = "कर्म" if verb is not None else ""
        elif case == TRITIYA:
            kta_pred = not verbs and any(words[j].morph.krt == "क्त" and is_case(words[j].morph, PRATHAMA)
                                         for j in range(len(words)) if words[j].morph)
            role = "कर्ता" if passive or kta_pred else "करण"
            if kta_pred:
                verb = next(j for j in range(len(words)) if words[j].morph and words[j].morph.krt == "क्त"
                            and is_case(words[j].morph, PRATHAMA))
        elif case == SAMBODHANA:
            role = "सम्बोधन"
        elif case == SHASHTHI:
            genitives.extend(group)
            continue
        else:
            role = KARAKA_OF_CASE.get(case, "")
        _set(words, head, role, verb)
        for j in group:
            if j != head:
                _set(words, j, "सम्बोधन" if case == SAMBODHANA else sub_role, head)
    for g in genitives:  # सम्बन्ध: attach to the adjacent nominal, the following one preferred
        nxt = [j for j in (g + 1, g - 1) if 0 <= j < len(words) and not words[j].in_compound
               and words[j].morph is not None and words[j].morph.kind == "subanta"
               and words[j].morph.vibhakti != SHASHTHI]
        _set(words, g, "सम्बन्ध", nxt[0] if nxt else _nearest(verbs, g))
    for i, w in enumerate(words):
        if w.morph is not None and w.morph.kind == "avyaya" and not w.role:
            if w.form == "च" and i > 0:
                head = i - 1  # च joins the item it follows
            else:
                head = _nearest(verbs, i)  # verbless: attached to the subject below
            _set(words, i, "अव्यय", head)
    subjects = [i for i, w in enumerate(words) if w.role == "" and is_case(w.morph, PRATHAMA)]
    if not verbs and subjects:  # verbless sentence: other karakas attach to its subject
        main = max(subjects, key=lambda i: (_head_priority(words, i, verbs), -i))
        for i in subjects:
            if i != main:
                _set(words, i, "विधेय", main)
        subjects = [main]
        for i, w in enumerate(words):
            if w.role and w.head is None and i not in subjects:
                _set(words, i, w.role, _nearest(subjects, i))
    return words, notes


def evaluate(words: list[Word], incoming: dict[str, float]) -> dict[str, float]:
    """akanksha, yogyata, sannidhi (0..1), frequency and weighted total."""
    n = len(words) or 1
    roots = {i for i, w in enumerate(words) if w.role == "क्रिया"}
    connected = sum(1 for i, w in enumerate(words) if w.role and (w.head is not None or i in roots or w.role == ""))
    nominatives_roots = sum(1 for w in words if w.role == "" and w.morph is not None and is_case(w.morph, PRATHAMA))
    parts = [(connected + min(nominatives_roots, 1)) / n]
    for v in roots:
        vm = words[v].morph
        kartas = [w for w in words if w.head == v and w.role == "कर्ता"]
        parts.append(1.0 if any(karta_agrees(w.morph, vm) for w in kartas) else (0.5 if kartas else 0.0))
    akanksha = min(1.0, sum(parts) / len(parts))
    # yogyata: only formal penalties; deeper semantic compatibility is not implemented.
    penalty = 0.0
    has_verb = bool(roots)
    for w in words:
        m = w.morph
        if m is None:
            continue
        if w.role in ("कर्ता", "कर्म") and m.quality <= 1:
            penalty += 0.3
        if m.vibhakti == SAMBODHANA and has_verb and any(is_case(a, PRATHAMA) for a in w.analyses):
            penalty += 0.2
        if w.role == "विशेषण" and w.head is not None and words[w.head].morph is not None \
                and m.linga != words[w.head].morph.linga:
            penalty += 0.2
    yogyata = max(0.0, 1.0 - penalty)
    dists = [abs(i - w.head) for i, w in enumerate(words) if w.head is not None]
    sannidhi = sum(1.0 / (1.0 + 0.25 * (d - 1)) for d in dists) / len(dists) if dists else 1.0
    if "frequency" in incoming:
        frequency = incoming["frequency"]
    else:
        us = [unary(w.morph) for w in words if w.morph is not None]
        frequency = (sum(min(u, 10.0) for u in us) / (10.0 * len(us))) if us else 0.0
    scores = {**incoming, "akanksha": akanksha, "yogyata": yogyata, "sannidhi": sannidhi, "frequency": frequency}
    scores["total"] = sum(WEIGHTS[k] * scores[k] for k in WEIGHTS)
    return scores


def resolve(reading: Reading) -> Reading:
    """New Reading with ``chosen``, ``role`` and ``head`` set and shabdabodha scores."""
    chosen = choose(reading.words)
    words = [replace(w, chosen=c) if w.analyses else w for w, c in zip(reading.words, chosen)]
    words, notes = assign_roles(words)
    scores = evaluate(words, reading.scores)
    return replace(reading, words=words, scores=scores, notes=list(reading.notes) + notes)


def rank(readings: list[Reading]) -> list[Reading]:
    """All readings, best first by ``scores['total']``; ties → fewer words."""
    return sorted(readings, key=lambda r: (-r.scores.get("total", 0.0), len(r.words)))
