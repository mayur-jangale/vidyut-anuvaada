"""Choosing among readings by shabdabodha tests: akanksha, yogyata, sannidhi, frequency.

``resolve`` jointly picks one analysis per word (coordinate ascent over unary corpus
scores plus agreement bonuses) and links words to heads with karaka roles.
``rank`` orders readings by the weighted total and never drops one.
"""

from __future__ import annotations

import math
from dataclasses import replace
from typing import Optional

from mayur import karaka_links
from mayur.anvaya import evaluate
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
    """Chosen analysis indices: the learned tagger when its model is present, else the rules."""
    from mayur import tagger
    learned = tagger.choose(words, lambda w: candidates(w) if w.analyses else [])
    return tagger.enforce(words, learned) if learned is not None else choose_rules(words)


def choose_rules(words: list[Word]) -> list[int]:
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


def resolve(reading: Reading) -> Reading:
    """New Reading with ``chosen``, ``role`` and ``head`` set and shabdabodha scores."""
    from mayur import particle_ma

    chosen, ma_notes = particle_ma.apply(reading.words, choose(reading.words))
    words = [replace(w, chosen=c) if w.analyses else w for w, c in zip(reading.words, chosen)]
    from mayur.vakya import assign_roles
    from mayur.vakya_case import ablative, syncretic

    words, case_notes = syncretic(words)  # प्रथमा/द्वितीया only where the kāraka rules decide it
    words, ablative_notes = ablative(words)  # पञ्चमी/षष्ठी with a verb of moving
    case_notes = case_notes + ablative_notes
    qualifying = frozenset(c.members[-1] for c in reading.compounds if "बहुव्रीहि" in c.samasa and c.members)
    words, notes = assign_roles(words, qualifying)  # a बहुव्रीहि qualifies another word: it does not head a phrase
    notes = ma_notes + case_notes + notes
    words, licence_notes = karaka_links.license_words(words)  # a link stays only if a rule licenses it
    scores = evaluate(words, reading.scores)
    out = replace(reading, words=words, scores=scores, notes=list(reading.notes) + notes + licence_notes)
    verified, extra = karaka_links.check(out)
    return replace(out, scores={**scores, "karaka_verified": verified}, notes=out.notes + extra)


def rank(readings: list[Reading]) -> list[Reading]:
    """All readings, best first by ``scores['total']``; ties → fewer words."""
    return sorted(readings, key=lambda r: (-r.scores.get("total", 0.0), len(r.words)))
