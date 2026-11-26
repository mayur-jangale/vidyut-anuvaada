"""Shabdabodha: choose one analysis per word and link words by karaka relations.

Search (kept tractable): each word's analyses are pruned to distinct grammatical
signatures (quality >= 2 when any exist); then every configuration of which words are
finite verbs (and which person/number each takes) is tried, and for each one the
nominal analyses are chosen by case-driven agreement scoring and roles are assigned
(see ``assign_roles``). The configuration with the best total wins.

Scores (all 0..1):
  akanksha  mean of: fraction of words connected; agreement satisfied; every verb has
            a karta (pro-drop accepted for 1st/2nd person); karma not checked because
            vidyut exposes no transitivity (karmatva) here -> never penalised.
  yogyata   1 - penalties/len: quality-0 kvip analysis chosen (1.0, 1.5 if karta),
            vocative chosen while a nominative was available (0.5), lexical gender
            mismatch (0.5). Deeper semantic compatibility is NOT implemented.
  sannidhi  mean over dependencies of 1/distance(dependent, head).
  total     0.5*akanksha + 0.2*yogyata + 0.15*sannidhi + 0.15*frequency (0 if absent).
"""

from __future__ import annotations

from dataclasses import replace
from itertools import product
from typing import Optional

from mayur import lexicon
from mayur.model import Morph, Reading, Word
from mayur.compounds import is_adjectival, PRONOUN_STEMS

PARTICLES = frozenset({"ca", "nu", "hi", "eva", "api", "tu", "vA", "iti", "Kalu", "u", "sma", "ha"})
NEGATION = frozenset({"na", "mA"})
ADVERBS = frozenset({"itas", "tatas", "atra", "tatra", "iha", "sAmpratam", "adya", "punar", "sadA",
                     "kva", "katham", "yatra", "yadA", "tadA", "sma", "evam", "tathA", "yaTA", "taTA"})
NONFINITE_KRTS = frozenset({"ktvA", "lyap", "tumu~n"})
CASE_ROLE = {"tftIyA": "karana", "caturTI": "sampradana", "paYcamI": "apadana",
             "saptamI": "adhikarana", "zazWI": "sambandha", "samboDanam": "sambodhana"}
WEIGHTS = {"akanksha": 0.5, "yogyata": 0.2, "sannidhi": 0.15, "frequency": 0.15}
MAX_CONFIGS = 256


def signature(m: Morph) -> tuple:
    return (m.kind, m.vibhakti, m.vacana, m.linga, m.purusha, m.lakara)


def prune(analyses: list[Morph]) -> list[int]:
    """Indices of analyses with distinct signatures, preferring quality >= 2."""
    good = [i for i, m in enumerate(analyses) if lexicon.quality(m) >= 2]
    pool = good or list(range(len(analyses)))
    seen: dict[tuple, int] = {}
    for i in pool:
        seen.setdefault(signature(analyses[i]), i)
    return list(seen.values())


def _verb_options(w: Word, cands: list[int]) -> list[Optional[int]]:
    """None (not a verb here) plus each tinanta candidate, root-in-form first."""
    tins = [i for i in cands if w.analyses[i].kind == "tinanta"]
    tins.sort(key=lambda i: (w.analyses[i].root or "") not in w.form)
    return [None] + tins if len(cands) > len(tins) else tins


def _configs(words: list[Word], cands: list[list[int]]) -> list[dict[int, int]]:
    slots = [(i, _verb_options(w, cands[i])) for i, w in enumerate(words)
             if not w.in_compound and any(w.analyses[j].kind == "tinanta" for j in cands[i])]
    out = []
    for combo in product(*[opts for _, opts in slots]):
        out.append({i: c for (i, _), c in zip(slots, combo) if c is not None})
        if len(out) >= MAX_CONFIGS:
            break
    return out or [{}]


def _sannidhi(words: list[Word]) -> float:
    ds = [abs(i - w.head) for i, w in enumerate(words) if w.head is not None and w.head != i]
    return sum(1.0 / d for d in ds) / len(ds) if ds else 1.0


def _yogyata(words: list[Word], cands: list[list[int]]) -> float:
    pen = 0.0
    for i, w in enumerate(words):
        m = w.morph
        if m is None or w.in_compound:
            continue
        if lexicon.quality(m) == 0:
            pen += 1.5 if w.role == "karta" else 1.0
        if m.vibhakti == "samboDanam" and any(w.analyses[j].vibhakti == "praTamA" for j in cands[i]):
            pen += 0.5
        if not m.lexical_linga_ok:
            pen += 0.5
    return max(0.0, 1.0 - pen / max(1, len(words)))


NOMINAL_SENTENCE_KRIYA = 0.6  # a supplied copula is valid but weaker than an overt kriya


def is_root(w: Word) -> bool:
    return w.head is None and (w.role == "kriya" or w.role == "karta")


def connected(words: list[Word], i: int) -> bool:
    """True if the head chain from word i reaches a clause root (verb / nominal subject)."""
    seen = set()
    while i is not None and i not in seen:
        seen.add(i)
        w = words[i]
        if not w.role:
            return False
        if is_root(w):
            return True
        i = w.head
    return False


def _akanksha(words: list[Word], stats: dict) -> float:
    conn = sum(1 for i in range(len(words)) if connected(words, i)) / max(1, len(words))
    kriya = 1.0 if stats.get("finite") else NOMINAL_SENTENCE_KRIYA
    parts = [conn, stats.get("agreement", 1.0), stats.get("verbs_with_karta", 1.0), kriya]
    return sum(parts) / len(parts)


def score(words: list[Word], cands: list[list[int]], stats: dict, frequency: float) -> dict[str, float]:
    s = {"akanksha": _akanksha(words, stats), "yogyata": _yogyata(words, cands),
         "sannidhi": _sannidhi(words)}
    s["total"] = sum(WEIGHTS[k] * s[k] for k in ("akanksha", "yogyata", "sannidhi")) + \
        WEIGHTS["frequency"] * frequency
    return s


def _evaluate(words: list[Word], cands: list[list[int]], verbs: dict[int, int],
              frequency: float) -> tuple[list[Word], dict[str, float], list[str]]:
    chosen = choose_nominals(words, cands, verbs)
    picked = [replace(w, chosen=chosen[i]) for i, w in enumerate(words)]
    linked, stats, notes = assign_roles(picked, sorted(verbs))
    return linked, score(linked, cands, stats, frequency), notes


def resolve(reading: Reading) -> Reading:
    words = list(reading.words)
    cands = [prune(w.analyses) for w in words]
    freq = reading.scores.get("frequency", 0.0)
    best = None
    for verbs in _configs(words, cands):
        result = _evaluate(words, cands, verbs, freq)
        if best is None or result[1]["total"] > best[1]["total"]:
            best = result
    linked, scores, notes = best
    unanalysed = [w.form for w in linked if not w.analyses]
    if unanalysed:
        notes = notes + [f"unanalysed (kept, no role): {', '.join(unanalysed)}"]
    return replace(reading, words=linked, scores={**reading.scores, **scores},
                   notes=list(reading.notes) + notes)


def rank(readings: list[Reading]) -> list[Reading]:
    """Best first by total; ties -> fewer words. Never drops a reading."""
    return sorted(readings, key=lambda r: (-r.scores.get("total", 0.0), len(r.words)))


# ---------------------------------------------------------------- analysis choice

def _person(m: Morph) -> str:
    return {"asmad": "uttama", "yuzmad": "maDyama"}.get(m.lemma, "praTama")


def _agrees_with_verb(m: Morph, v: Morph) -> bool:
    return m.vibhakti == "praTamA" and m.vacana == v.vacana and _person(m) == v.purusha


def _nkey(m: Morph) -> tuple:
    return (m.vibhakti, m.vacana, m.linga)


def _nominal_cands(w: Word, cands: list[int]) -> list[int]:
    non = [i for i in cands if w.analyses[i].kind != "tinanta"]
    return non or cands


def _cand_score(m: Morph, support: float, vmorphs: list[Morph]) -> float:
    s = float(lexicon.quality(m)) - (0.0 if m.lexical_linga_ok else 0.5)
    if m.kind == "avyaya":
        return s + (2.5 if m.lemma in PARTICLES | NEGATION | ADVERBS else 0.5)
    s += 0.8 * min(support, 4)
    kartari = [v for v in vmorphs if v.prayoga != "karmaRi"]
    vib = m.vibhakti
    if vib == "praTamA":
        s += 2.0 if any(_agrees_with_verb(m, v) for v in kartari) else (1.5 if not vmorphs else 0.0)
    elif vib == "dvitIyA":
        s += 1.0 if kartari else 0.0
    elif vib == "tftIyA":
        s += 1.5 if len(kartari) < len(vmorphs) else 0.3
    elif vib == "samboDanam":
        s -= 1.5
    elif vib in ("zazWI", "saptamI"):
        s += 0.5
    else:
        s += 0.3
    return s


def _key_weights(w: Word, nc: list[int]) -> dict[tuple, float]:
    """Agreement keys this word could take, weighted by its best analysis quality / 3."""
    out: dict[tuple, float] = {}
    for j in nc:
        m = w.analyses[j]
        if m.kind == "subanta":
            out[_nkey(m)] = max(out.get(_nkey(m), 0.0), lexicon.quality(m) / 3)
    return out


def choose_nominals(words: list[Word], cands: list[list[int]], verbs: dict[int, int]) -> list[int]:
    vmorphs = [words[i].analyses[j] for i, j in verbs.items()]
    ncands = [_nominal_cands(w, c) for w, c in zip(words, cands)]
    keys: list[dict] = [{} if w.in_compound else _key_weights(w, nc) for w, nc in zip(words, ncands)]
    chosen = []
    for i, w in enumerate(words):
        if i in verbs:
            chosen.append(verbs[i])
            continue
        if not w.analyses or w.in_compound:
            chosen.append(0)
            continue

        def total(j: int) -> float:
            m = w.analyses[j]
            sup = sum(ks.get(_nkey(m), 0.0) for k, ks in enumerate(keys) if k != i and k not in verbs)
            return _cand_score(m, sup if m.kind == "subanta" else 0, vmorphs)
        chosen.append(max(ncands[i], key=total))
    return chosen


# ---------------------------------------------------------------- role assignment

def _final(words: list[Word], i: int) -> int:
    while i < len(words) - 1 and words[i].in_compound:
        i += 1
    return i


def _nearest(i: int, pool: list[int]) -> Optional[int]:
    pool = [p for p in pool if p != i]
    return min(pool, key=lambda p: (abs(p - i), p < i)) if pool else None


def _pick_head(words: list[Word], members: list[int], verbs: list[int]) -> int:
    def key(i: int) -> tuple:
        m = words[i].morph
        near = min((abs(i - v) for v in verbs), default=i)
        return (is_adjectival(m), words[i].compound is not None or words[i - 1].in_compound if i else False, near)
    return min(members, key=key)


def _groups(words: list[Word], nominals: list[int]) -> dict[tuple, list[int]]:
    out: dict[tuple, list[int]] = {}
    for i in nominals:
        out.setdefault(_nkey(words[i].morph), []).append(i)
    return out


def _set(words: list[Word], i: int, role: str, head: Optional[int]) -> None:
    words[i] = replace(words[i], role=role, head=head)


def _link_group(words, members, verbs, finite, subjects_out, nominal_sentence) -> None:
    m0 = words[members[0]].morph
    vib = m0.vibhakti
    vm = {v: words[v].morph for v in finite}
    if vib == "praTamA" and nominal_sentence:
        subs = [i for i in members if words[i].morph.lemma in PRONOUN_STEMS] or \
               [_pick_head(words, members, verbs)]
        for i in members:
            if i in subs:
                _set(words, i, "karta", None)
                subjects_out.append(i)
            else:
                prev = [s for s in subs if s < i]
                _set(words, i, "visheshana", max(prev) if prev else _nearest(i, subs))
        return
    head = _pick_head(words, members, verbs)
    role, hv = "", None
    if vib == "praTamA":
        agree = [v for v in finite if vm[v].prayoga != "karmaRi" and _agrees_with_verb(m0, vm[v])]
        pas = [v for v in finite if vm[v].prayoga == "karmaRi" and m0.vacana == vm[v].vacana]
        if agree:
            role, hv = "karta", _nearest(head, agree)
        elif pas:
            role, hv = "karma", _nearest(head, pas)
    elif vib == "dvitIyA":
        role, hv = "karma", _nearest(head, verbs)
    elif vib == "tftIyA":
        pas = [v for v in finite if vm[v].prayoga == "karmaRi"]
        role, hv = ("karta", _nearest(head, pas)) if pas else ("karana", _nearest(head, verbs))
    elif vib == "zazWI":
        role, hv = "sambandha", None  # attached per word below
    else:
        role = CASE_ROLE.get(vib, "")
        hv = _nearest(head, finite[:1] if vib == "samboDanam" else verbs)
    for i in members:
        if role == "sambandha":
            _set(words, i, role, _genitive_head(words, i))
        elif i == head:
            _set(words, i, role, hv)
        else:
            _set(words, i, "visheshana", head)


def _genitive_head(words: list[Word], i: int) -> Optional[int]:
    noms = [j for j, w in enumerate(words) if w.morph and w.morph.kind == "subanta"
            and not w.in_compound and w.morph.vibhakti != "zazWI"]
    after = [j for j in noms if i < j <= i + 3]
    if after:
        return min(after)
    before = [j for j in noms if j < i]
    return max(before) if before else (min(noms) if noms else None)


def _link_avyaya(words, i, verbs, subjects) -> None:
    m = words[i].morph
    lemma = m.lemma
    content = [j for j, w in enumerate(words) if j != i and not w.in_compound
               and (w.morph is None or w.morph.kind != "avyaya")]
    if m.krt in NONFINITE_KRTS:
        _set(words, i, "kriya", _nearest(i, [v for v in verbs if words[v].morph.kind == "tinanta"]))
    elif lemma in NEGATION:
        nxt = [v for v in verbs if v > i] or [j for j in content if j > i]
        _set(words, i, "avyaya", min(nxt) if nxt else _nearest(i, content))
    elif lemma in PARTICLES:
        prev = [j for j in content if j < i]
        _set(words, i, "avyaya", max(prev) if prev else _nearest(i, content))
    else:
        _set(words, i, "avyaya", _nearest(i, verbs) if verbs else _nearest(i, subjects or content))


def assign_roles(words: list[Word], finite: list[int]) -> tuple[list[Word], dict, list[str]]:
    words = [replace(w, role="", head=None) for w in words]
    notes: list[str] = []
    nonfinite = [i for i, w in enumerate(words) if w.morph and w.morph.kind == "avyaya"
                 and w.morph.krt in NONFINITE_KRTS]
    verbs = sorted(finite + nonfinite)
    for i, w in enumerate(words):
        if w.in_compound:
            _set(words, i, "samasa-purvapada", _final(words, i))
    for v in finite:
        _set(words, v, "kriya", None)
    nominal_sentence = not finite
    if nominal_sentence:
        notes.append("nominal sentence: no finite verb; copula supplied in translation")
    nominals = [i for i, w in enumerate(words) if not w.in_compound and w.morph and w.morph.kind == "subanta"]
    subjects: list[int] = []
    groups = _groups(words, nominals)
    order = sorted(groups, key=lambda k: k[0] != "praTamA")  # subjects first
    for k in order:
        _link_group(words, groups[k], verbs, finite, subjects, nominal_sentence)
    if nominal_sentence:  # clause-level dependents attach to the nearest subject
        for i, w in enumerate(words):
            if w.role in CASE_ROLE.values() and w.role != "sambandha" and w.head is None or \
                    (w.role == "karma" and w.head is None):
                _set(words, i, w.role, _nearest(i, subjects))
    for i, w in enumerate(words):
        if not w.in_compound and w.morph and w.morph.kind == "avyaya":
            _link_avyaya(words, i, verbs, subjects)
    return words, _stats(words, finite, subjects), notes


def _stats(words: list[Word], finite: list[int], subjects: list[int]) -> dict:
    vis = [(i, w.head) for i, w in enumerate(words) if w.role == "visheshana" and w.head is not None]
    agree = [_nkey(words[i].morph) == _nkey(words[h].morph) for i, h in vis]
    karta_heads = {w.head for w in words if w.role == "karta"}
    if finite:
        vals = [1.0 if v in karta_heads else (0.75 if words[v].morph.purusha != "praTama" else 0.0)
                for v in finite]
    else:
        vals = [1.0 if subjects else 0.5]
    return {"agreement": sum(agree) / len(agree) if agree else 1.0,
            "verbs_with_karta": sum(vals) / len(vals), "finite": float(bool(finite))}
