"""Prose order (anvaya) built by rule from the karaka links set by ``shabdabodha.resolve``.

Order inside a clause: vocatives, particles, karta group, अधिकरण, अपादान, सम्प्रदान, करण
groups, karma group, non-finite verbals (each after its own objects), विधेय, न, verb.
A group is: genitive dependents, qualifiers, then the head. च follows the item it
joins. Compound members stay together in their original order. Clauses follow text order.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Any, Callable, Optional

from mayur.model import Reading, Word

PRIORITY = {
    "सम्बोधन": 0, "अव्यय": 1, "कर्ता": 2, "सम्बन्ध": 3, "विशेषण": 4, "अधिकरण": 5, "भावलक्षण": 5, "अपादान": 6,
    "सम्प्रदान": 7, "करण": 8, "कर्म": 9, "पूर्वकालक्रिया": 10, "तुमर्थ": 10,
}
NEGATION = "न"
CONJUNCTION = "च"
QUOTE = "इति"
_LAST = 12


# Clause segmentation, shared with shabdabodha.resolve.

def quoted(words: list[Word], v: int) -> bool:
    """A finite verb directly followed by इति is quoted speech (its own clause)."""
    nxt = v + 1
    return nxt < len(words) and words[nxt].form == "इति"


def regions(words: list[Word], verbs: list[int], agrees: Callable[[Any, Any], bool]) -> dict[int, int]:
    """line → clause region: a verbless half-verse joins a neighbouring line it agrees with."""
    lines = sorted({w.line for w in words})
    with_verb = {words[v].line for v in verbs} | _krt_clause_lines(words)
    region = {ln: ln for ln in lines}
    for ln in lines:
        if ln in with_verb:
            continue
        mine = [w.morph for w in words if w.line == ln and not w.in_compound and w.morph and w.morph.vibhakti]
        for other in (ln + 1, ln - 1, -1):
            if other == -1:  # no verb line agrees: join the preceding verbless line if it agrees
                other = ln - 1
                if other not in region or other in with_verb:
                    break
            elif other not in with_verb:
                continue
            theirs = [w.morph for w in words if w.line == other and w.morph is not None and w.morph.kind == "subanta"]
            if any(agrees(a, b) and a.vibhakti not in ("षष्ठी", "सम्बोधन") for a in mine for b in theirs) \
                    or _supplies_agent(words, mine, other, verbs):
                region[ln] = region[other]
                break
    return region


KRT_PREDICATE = ("क्त", "क्तवतु", "तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्")
OBLIQUE = ("तृतीया", "चतुर्थी", "पञ्चमी", "सप्तमी")


def _krt_clause_lines(words: list[Word]) -> set[int]:
    """Half-verses that are clauses of their own: a nominative kṛt predicate (not a compound final)
    with its own oblique kāraka in the same half-verse (सारसेन … राजा जले क्षिप्तः)."""
    out = set()
    for i, w in enumerate(words):
        m = w.morph
        if m is None or w.in_compound or m.kind != "subanta" or m.vibhakti != "प्रथमा" or m.krt not in KRT_PREDICATE \
                or (i > 0 and words[i - 1].in_compound):
            continue
        if any(o.line == w.line and not o.in_compound and o.morph is not None and o.morph.vibhakti in OBLIQUE
               for o in words):
            out.add(w.line)
    return out


def _supplies_agent(words: list[Word], mine: list[Any], line: int, verbs: list[int]) -> bool:
    """The verbless line holds the कर्ता (person/number agreement, 1.4.105–108) of a verb of ``line``
    that has no agreeing nominative in its own line."""
    from mayur.shabdabodha import karta_agrees

    own = [w.morph for w in words if w.line == line and not w.in_compound and w.morph is not None]
    for v in (v for v in verbs if words[v].line == line):
        vm = words[v].morph
        if not any(karta_agrees(m, vm) for m in own) and any(karta_agrees(m, vm) for m in mine):
            return True
    return False


def pick(cands: list[int], words: list[Word], i: int) -> Optional[int]:
    """Same half-verse first, then nearest."""
    return min(cands, key=lambda j: (words[j].line != words[i].line, abs(j - i), j < i)) if cands else None


# Shabdabodha scores (kept here for file size; used by shabdabodha.resolve).

def evaluate(words: list[Word], incoming: dict[str, float]) -> dict[str, float]:
    """akanksha, yogyata, sannidhi (0..1), frequency and weighted total (see shabdabodha.WEIGHTS)."""
    from mayur.shabdabodha import PRATHAMA, SAMBODHANA, WEIGHTS, is_case, unary

    n = len(words) or 1
    from mayur.karaka import expressed
    from mayur.karaka_links import STRUCTURAL

    roots = {i for i, w in enumerate(words) if w.role == "क्रिया"}
    # a word counts as connected when a rule licenses its link (role_sutras) or its role is structural
    connected = sum(1 for i, w in enumerate(words) if w.role_sutras or w.in_compound
                    or (w.role in STRUCTURAL and w.role and (w.head is not None or i in roots)))
    parts = [connected / n]
    for v in roots:  # the kāraka the verb expresses: found in the text 1.0, supplied (अध्याहार) 0.5
        options = {r for r, _ in expressed(words[v].morph) if r}
        if options:
            found = any(w.head == v and w.role in options and w.role_sutras for w in words)
            parts.append(1.0 if found else 0.5)
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


def _priority(word: Word) -> int:
    if word.role == "अव्यय" and word.form == NEGATION:
        return _LAST
    return PRIORITY.get(word.role, _LAST - 1)


def _members(words: list[Word], i: int) -> list[int]:
    """The word with its preceding compound members (original order)."""
    start = i
    while start > 0 and words[start - 1].in_compound:
        start -= 1
    return list(range(start, i + 1))


def _root(words: list[Word], i: int) -> int:
    seen = {i}
    while words[i].head is not None and words[i].head not in seen and 0 <= words[i].head < len(words):
        i = words[i].head
        seen.add(i)
    return i


def _emit(words: list[Word], i: int, deps: dict[int, list[int]], out: list[int], done: set[int]) -> None:
    if i in done:
        return
    done.add(i)
    children = [d for d in deps.get(i, []) if not words[d].in_compound]
    trailing = [d for d in children if words[d].role == "विधेय"
                or (words[d].role == "अव्यय" and words[d].form in (CONJUNCTION, QUOTE) and d > i)]
    before = sorted((d for d in children if d not in trailing), key=lambda d: (_priority(words[d]), d))
    for d in before:
        _emit(words, d, deps, out, done)
    for m in _members(words, i):
        if m not in out:
            out.append(m)
            done.add(m)
    for d in trailing:
        _emit(words, d, deps, out, done)


def prose_order(words: list[Word]) -> list[int]:
    deps: dict[int, list[int]] = {}
    for i, w in enumerate(words):
        if w.head is not None and w.head != i and 0 <= w.head < len(words):
            deps.setdefault(w.head, []).append(i)
    roots: list[int] = []
    for i in range(len(words)):
        r = _root(words, i)
        if r not in roots and not words[r].in_compound:
            roots.append(r)
    roots.sort(key=lambda r: min(j for j in range(len(words)) if _root(words, j) == r))
    out: list[int] = []
    done: set[int] = set()
    for r in roots:
        _emit(words, r, deps, out, done)
    out.extend(i for i in range(len(words)) if i not in out)  # safety: every index once
    return out


def order(reading: Reading) -> Reading:
    """New Reading with ``anvaya`` set."""
    return replace(reading, anvaya=prose_order(reading.words))


def head_of(words: list[Word], i: int) -> Optional[int]:
    return words[i].head
