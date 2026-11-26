"""Choosing among readings by shabdabodha tests: akanksha, yogyata, sannidhi, frequency.

``resolve`` jointly picks one analysis per word (coordinate ascent over unary corpus
scores plus agreement bonuses) and links words to heads with karaka roles.
``rank`` orders readings by the weighted total and never drops one.
"""

from __future__ import annotations

import math
from dataclasses import replace
from typing import Optional

from mayur.anvaya import pick as _pick, quoted as _quoted, regions as _region_map
from mayur.model import Morph, Reading, Word

PRATHAMA, DVITIYA, TRITIYA = "प्रथमा", "द्वितीया", "तृतीया"
SAMBODHANA, SHASHTHI = "सम्बोधन", "षष्ठी"
KARAKA_OF_CASE = {"चतुर्थी": "सम्प्रदान", "पञ्चमी": "अपादान", "सप्तमी": "अधिकरण"}
NONFINITE = {"क्त्वा": "पूर्वकालक्रिया", "ल्यप्": "पूर्वकालक्रिया", "तुमुन्": "तुमर्थ"}
FIRST_PERSON = {"अस्मद्"}
SECOND_PERSON = {"युष्मद्"}
COPULA = {"अस्", "भू"}
FEAR = {"भी", "त्रस्", "उद्विज्"}
POSSESSIVE = ("वत्", "मत्", "इन्")
LOCAL = {"करण", "अधिकरण", "सम्प्रदान", "अपादान"}
PRONOUNS = {"किम्", "तद्", "यद्", "इदम्", "एतद्", "अदस्", "अस्मद्", "युष्मद्"}

# Weights grid-searched on gold morphology of Bala-kanda 1.21-79 (never 1-20): case+number+gender
# accuracy 0.901 vs 0.872 for unary scores alone, 0.967 oracle over the pruned candidates.
W_LEMMA = 0.3
W_PHRASE = 3.0  # same case+number+gender nominals, divided by distance
W_KARTA = 2.5  # nominative agreeing with a कर्तरि finite verb
W_KARMA = 0.6  # per accusative when a verb or verbal is present
W_STRAY = 0.5  # nominative not agreeing with any karta of a कर्तरि verb
W_LUT = 4.0  # लुट् reading where a तृच् agent noun is as likely
W_VOC = 3.0  # vocative without corpus support
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
    if any(is_finite(m) and m.lakara == "लुट्" for m in word.analyses):  # keep the तृच् rival of a लुट् form
        good += [i for i, m in enumerate(word.analyses) if m.krt == "तृच्" and i not in good]
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
    verbal = sum(1 for m in ms.values() if is_nonfinite(m)) + len(verbs)
    for v in verbs:
        kartas = [m for m in ms.values() if karta_agrees(m, v)]
        if kartas:
            total += W_KARTA
        stray = [m for m in ms.values() if is_case(m, PRATHAMA) and v.prayoga in (None, "कर्तरि")
                 and not any(agrees(m, k) for k in kartas)]
        total -= W_STRAY * len(stray)
    acc_groups = {(m.vacana, m.linga) for m in ms.values() if is_case(m, DVITIYA)}
    total += W_KARMA * min(len(acc_groups), verbal)  # at most one कर्म group per verb/verbal
    if not verbal:  # verbless sentence: one subject group; other nominatives do not connect
        noms = [(m.vacana, m.linga) for m in ms.values() if is_case(m, PRATHAMA)]
        if noms:
            total -= W_VERBLESS * (len(noms) - max(noms.count(k) for k in set(noms)))
        total -= W_VERBLESS * len(acc_groups)  # no verb to govern it
    # a vocative needs corpus support when the word has another reading
    total -= W_VOC * sum(1 for k, m in ms.items() if m.vibhakti == SAMBODHANA and len(words[k].analyses) > 1
                         and (_freq("analysis_count", m) == 0 or any(a.kind == "avyaya" for a in words[k].analyses)))
    total -= W_LUT * sum(1 for k, m in ms.items() if _agent_noun_preferred(words[k], m))
    total += W_KARTA * sum(1 for k, m in ms.items() if m.kind == "avyaya" and m.form == "इति"
                           and k - 1 in ms and is_finite(ms[k - 1]))  # quotative इति after a verb
    return total


def _agent_noun_preferred(word: Word, m: Morph) -> bool:
    """रक्षिता: a लुट् verb with a तृच् nominative alternative the corpus does not disfavour."""
    if not (is_finite(m) and m.lakara == "लुट्"):
        return False
    agents = [a for a in word.analyses if a.krt == "तृच्" and is_case(a, PRATHAMA)]
    return bool(agents) and _freq("analysis_count", m) <= 2 * max(_freq("analysis_count", a) for a in agents)


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


def _head_priority(words: list[Word], i: int, verbs: list[int]) -> float:
    m = words[i].morph
    if m.lemma in FIRST_PERSON | SECOND_PERSON:
        return 4.0  # अस्मद्/युष्मद् never qualify another word
    cls = lemma_class(m.lemma)
    if not verbs and m.vibhakti == PRATHAMA and (cls == "pronoun" or m.lemma in PRONOUNS):
        return 3.0  # verbless clause: the pronoun (कस्) is the subject
    score = {"noun": 2.0, "pronoun": 1.5, "": 1.0}.get(cls, 0.0)
    if m.krt:
        score -= 0.5
    if i > 0 and words[i - 1].in_compound:
        score -= 0.5
    if verbs:
        score -= 0.1 * min(abs(i - v) for v in verbs)
    return score


def _groups(words: list[Word], region: dict[int, int], governed: set[int]) -> list[list[int]]:
    """Agreement groups (same case, number, gender) per clause: the half-verse when it has a
    verb or verbal, else its region; अस्मद्/युष्मद् never group with (qualify) other words."""
    groups: dict[tuple, list[int]] = {}
    for i, w in enumerate(words):
        m = w.morph
        if not w.in_compound and not w.role and m is not None and m.kind == "subanta" and m.vibhakti:
            clause = w.line if w.line in governed else region[w.line]
            personal = m.lemma in FIRST_PERSON | SECOND_PERSON and m.vibhakti == PRATHAMA
            groups.setdefault((m.vibhakti, m.vacana, m.linga, clause, i if personal else -1), []).append(i)
    order = lambda g: (words[g[0]].morph.vibhakti != PRATHAMA, words[g[0]].morph.lemma not in FIRST_PERSON | SECOND_PERSON)
    return sorted(groups.values(), key=order)


def _set(words: list[Word], i: int, role: str, head: Optional[int]) -> None:
    words[i] = replace(words[i], role=role, head=head)


def _kta_near(words: list[Word], i: int) -> Optional[int]:
    near = [j for j in range(max(0, i - 2), min(len(words), i + 3))
            if j != i and words[j].morph is not None and words[j].morph.krt == "क्त" and words[j].morph.kind == "subanta"]
    return _pick(near, words, i)


def _adjacent_nominal(words: list[Word], g: int) -> Optional[int]:
    """Non-genitive nominal next to the genitive head (skipping particles), following first."""
    for step in (1, -1):
        j = g + step
        while 0 <= j < len(words) and words[j].line == words[g].line and words[j].morph is not None \
                and words[j].morph.kind == "avyaya":
            j += step
        if 0 <= j < len(words) and words[j].line == words[g].line and not words[j].in_compound \
                and words[j].morph is not None and words[j].morph.kind == "subanta" \
                and words[j].morph.vibhakti not in (SHASHTHI, SAMBODHANA):
            return j
    return None


def assign_roles(words_in: list[Word]) -> tuple[list[Word], list[str]]:
    """Karaka roles and heads for the chosen analyses (returns new Word objects)."""
    words = [replace(w, role="", head=None) for w in words_in]
    notes: list[str] = []
    finite = [i for i, w in enumerate(words) if is_finite(w.morph)]
    verbs = [v for v in finite if not _quoted(words, v)]
    verbals = [i for i, w in enumerate(words) if is_nonfinite(w.morph)]
    region = _region_map(words, verbs, agrees)
    in_region = {r: [v for v in verbs if region[words[v].line] == r] for r in set(region.values())}
    for v in finite:
        _set(words, v, "क्रिया", None if v in verbs else _pick(verbs, words, v))
        if v not in verbs:
            _set(words, v + 1, "अव्यय", v)
            notes.append(f"{words[v].form} इति: quoted speech, a clause of its own")
    for i in verbals:
        _set(words, i, NONFINITE[words[i].morph.krt], _pick(in_region[region[words[i].line]] or verbs, words, i))
    for i, w in enumerate(words):
        if w.in_compound:
            _set(words, i, "समासपूर्वपद", _compound_final(words, i))
        elif w.morph is None or w.morph.kind == "unknown":
            notes.append(f"{w.form}: no analysis; passed through unlinked")
    has_karma: set[int] = set()
    kartas: dict[int, int] = {}  # verb → karta head
    genitives: list[list[int]] = []
    governed = {words[v].line for v in verbs + verbals}
    for group in _groups(words, region, governed):
        case = words[group[0]].morph.vibhakti
        rverbs = in_region[region[words[group[0]].line]]
        head = max(group, key=lambda i: _head_priority(words, i, rverbs))
        verb, sub_role, role = None, "विशेषण", ""
        if case == PRATHAMA:
            agreeing = [v for v in rverbs if karta_agrees(words[head].morph, words[v].morph)]
            passive = [v for v in rverbs if words[v].morph.prayoga in ("कर्मणि", "भावे")
                       and words[v].morph.vacana == words[head].morph.vacana]
            copular = [v for v in rverbs if v in kartas and words[v].morph.root in COPULA
                       and words[v].morph.vacana == words[head].morph.vacana]
            if agreeing and _pick(agreeing, words, head) in kartas:  # second phrase of the same karta
                verb = _pick(agreeing, words, head)
                head_k = kartas[verb]
                for j in group:
                    _set(words, j, "विशेषण", head_k)
                continue
            if agreeing:
                verb, role = _pick(agreeing, words, head), "कर्ता"
                kartas[verb] = head
                if words[verb].morph.root in COPULA:
                    sub_role = "विधेय"
            elif copular:  # त्वम् समर्थस् असि: the other nominative is the predicate
                for j in group:
                    _set(words, j, "विधेय", kartas[_pick(copular, words, head)])
                continue
            elif passive:
                verb, role = _pick(passive, words, head), "कर्म"
            else:
                sub_role = "विधेय"
        elif case == DVITIYA:
            free = [v for v in rverbs + verbals if v not in has_karma]
            verb = _pick(free, words, head)
            if verb is not None:
                role = "कर्म"
                has_karma.add(verb)
            else:
                notes.append(f"{words[head].form}: accusative with no verb left to govern it")
        elif case == TRITIYA:
            kta = _kta_near(words, head)
            verb = kta if kta is not None else _pick(rverbs, words, head)
            passive = verb is not None and (kta is not None or words[verb].morph.prayoga in ("कर्मणि", "भावे"))
            role = "कर्ता" if passive else "करण"
        elif case == SAMBODHANA:
            role, verb = "सम्बोधन", _pick(rverbs or verbs, words, head)
        elif case == SHASHTHI:
            genitives.append(group)
            continue
        else:
            role, verb = KARAKA_OF_CASE.get(case, ""), _pick(rverbs, words, head)
        _set(words, head, role, verb)
        for j in group:
            if j != head:
                _set(words, j, "सम्बोधन" if case == SAMBODHANA else sub_role, head)
    for group in genitives:  # सम्बन्ध of the adjacent nominal; else an argument of the verb
        head = max(group, key=lambda i: _head_priority(words, i, []))
        target = _adjacent_nominal(words, head)
        if target is None:
            verb = _pick(in_region[region[words[head].line]] or verbs, words, head)
            fear = verb is not None and words[verb].morph.root in FEAR
            _set(words, head, "अपादान" if fear else "सम्बन्ध", verb)
        else:
            _set(words, head, "सम्बन्ध", target)
        for j in group:
            if j != head:
                _set(words, j, "विशेषण", head)
    for i, w in enumerate(words):
        if w.morph is not None and w.morph.kind == "avyaya" and not w.role:
            line_verbs = [v for v in verbs if words[v].line == w.line]
            head = i - 1 if w.form in ("च", "इव") and i > 0 else _pick(line_verbs or in_region[region[w.line]], words, i)
            _set(words, i, "अव्यय", head)
    _attach_verbless(words, region, in_region, notes)
    return words, notes


def can_be_subject(words: list[Word], i: int) -> bool:
    """Pronoun, or a noun that is not a participle, possessive (-वत्/-मत्/-इन्) or compound final."""
    m = words[i].morph
    same = [a for a in words[i].analyses if (a.vibhakti, a.vacana, a.linga) == (m.vibhakti, m.vacana, m.linga)]
    if any(a.lemma in PRONOUNS or lemma_class(a.lemma) == "pronoun" for a in same):
        return True  # also when the chosen lemma is a variant stem (क for किम्)
    if m.krt or m.lemma.endswith(POSSESSIVE) or (i > 0 and words[i - 1].in_compound):
        return False
    return lemma_class(m.lemma) == "noun"


def _attach_verbless(words: list[Word], region: dict[int, int], in_region: dict[int, list[int]],
                     notes: list[str]) -> None:
    """Nominal clauses: one expressed subject or none; dependents attach to the nearest predicate."""
    for r, rverbs in in_region.items():
        idx = [i for i, w in enumerate(words) if region[w.line] == r]
        subjects = [i for i in idx if words[i].role == "" and is_case(words[i].morph, PRATHAMA)]
        if not subjects:
            continue
        if not rverbs:
            able = [i for i in subjects if can_be_subject(words, i)]
            main = max(able, key=lambda i: (_head_priority(words, i, []), -i)) if able else None
            for i in idx:  # every nominative, including qualifiers of a non-subject, is विधेय
                if is_case(words[i].morph, PRATHAMA) and i != main and (i in subjects or words[i].role == "विधेय"):
                    _set(words, i, "विधेय", main)
            notes.append("nominal clause: subject not expressed; all nominatives are विधेय" if main is None
                         else f"nominal clause: {words[main].form} is the subject, agreeing nominatives are विधेय")
            predicates = [i for i in idx if is_case(words[i].morph, PRATHAMA) and not words[i].in_compound]
            for i in idx:  # epithet lists: local attachment to the nearest predicate in the line
                if words[i].role in LOCAL and words[i].role != "सम्बन्ध" or (words[i].role == "सम्बन्ध" and
                                                                           words[i].head is None):
                    same = [j for j in predicates if words[j].line == words[i].line] or predicates
                    _set(words, i, words[i].role, _pick(same, words, i))
            subjects = [main] if main is not None else []
        if not subjects:
            continue
        for i in idx:
            if words[i].role and words[i].head is None and i not in subjects and words[i].role != "क्रिया":
                _set(words, i, words[i].role, _pick(subjects, words, i))


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
