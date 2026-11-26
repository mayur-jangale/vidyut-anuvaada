"""Sentence structure: kāraka roles and heads for the chosen analyses (used by shabdabodha.resolve).

Links proposed here are kept only if ``mayur.karaka_links.license_words`` finds a rule that licenses them.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.karaka_rules import DVIKARMAKA
from mayur.anvaya import pick as _pick, quoted as _quoted, regions as _region_map
from mayur.model import Word
from mayur.shabdabodha import (COPULA, DVITIYA, FEAR, FIRST_PERSON, KARAKA_OF_CASE, LOCAL, NONFINITE, POSSESSIVE,
                               PRATHAMA, PRONOUNS, SAMBODHANA, SECOND_PERSON, SHASHTHI, TRITIYA, agrees, is_case,
                               is_finite, is_nonfinite, karta_agrees, lemma_class)


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
    score = {"noun": 2.0, "pronoun": 1.5, "": 1.0, "adjective": 0.8}.get(cls, 0.0)  # सा प्रिया: the adjective heads
    if m.lemma in DEMONSTRATIVE:
        score = 0.5  # तत् सर्वम्, सस् कपिस्: the demonstrative qualifies the other word
    if m.krt:
        score -= 0.5
    if i > 0 and words[i - 1].in_compound:
        score -= 0.5
    if verbs:
        same = [abs(v - i) for v in verbs if words[v].line == words[i].line]  # tie-breaks only: nearest the
        score -= 0.001 * min(same) if same else 0.01 + 0.0001 * i  # verb in its half-verse, else the first noun
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
            relative = m.lemma == "यद्" and sum(is_finite(x.morph) for x in words if x.line == w.line) > 1
            if m.vibhakti not in (PRATHAMA, DVITIYA):  # oblique phrases do not run across half-verses
                clause = (clause, w.line)
            groups.setdefault((m.vibhakti, m.vacana, m.linga, clause, i if personal or relative else -1), []).append(i)
    order = lambda g: (words[g[0]].morph.vibhakti != PRATHAMA, words[g[0]].morph.lemma not in FIRST_PERSON | SECOND_PERSON)
    return sorted(groups.values(), key=order)


def _set(words: list[Word], i: int, role: str, head: Optional[int]) -> None:
    words[i] = replace(words[i], role=role, head=head)


def _kta_near(words: list[Word], i: int) -> Optional[int]:
    near = [j for j in range(max(0, i - 2), min(len(words), i + 3))
            if j != i and words[j].morph is not None and words[j].morph.krt == "क्त" and words[j].morph.kind == "subanta"]
    return _pick(near, words, i)


def _adjacent_nominal(words: list[Word], g: int, over_verb: bool = False) -> Optional[int]:
    """Non-genitive nominal next to the genitive head (skipping particles), following first; with
    ``over_verb`` an oblique noun standing after the verb counts too (सिंहस्य प्रविशन्ति मुखे)."""
    for step in (1, -1):
        j = g + step
        crossed = False
        while 0 <= j < len(words) and words[j].line == words[g].line and words[j].morph is not None \
                and (words[j].morph.kind == "avyaya" or (over_verb and step == 1 and is_finite(words[j].morph))):
            crossed = crossed or is_finite(words[j].morph)
            j += step
        if crossed and 0 <= j < len(words) and words[j].morph is not None and words[j].morph.vibhakti == PRATHAMA:
            continue  # कस्य बिभ्यति देवास्: the nominative after the verb is its subject, not the genitive's noun
        if 0 <= j < len(words) and words[j].line == words[g].line and not words[j].in_compound \
                and words[j].morph is not None and words[j].morph.kind == "subanta" \
                and words[j].morph.vibhakti not in (SHASHTHI, SAMBODHANA):
            return j
    return None


DEMONSTRATIVE = {"तद्", "एतद्", "इदम्", "अदस्"}
NEGATION = {"न", "मा"}
CONJUNCTION = {"च", "वा"}
NUMBER_OF = {2: "द्विवचन"}
ENCLITIC = {"च", "वा", "एव", "अपि", "इव", "नाम", "वै", "उ", "चैव"}
PREDICATE_KRT = {"क्त", "क्तवतु", "शतृ", "शानच्", "चानश्", "तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्"}
OBJECT_TAKING = {"शतृ", "शानच्", "चानश्", "क्तवतु", "क्वसु", "कानच्", "तृच्", "णिनि"}  # kṛt with a कर्म (3.4.67)


def _line_verbal(words: list[Word], i: int, verbs: list[int], others: list[int]) -> Optional[int]:
    """Nearest verbal governor (finite verb, absolutive, participle) in the word's own half-verse
    (choice: nearest governor; karaka_links.license_words keeps it only if a rule licenses the link)."""
    near = [j for j in verbs + others if j != i and words[j].line == words[i].line]
    return min(near, key=lambda j: (abs(j - i), j < i)) if near else None


def _particle_head(words: list[Word], i: int, verbs: list[int], verbals: list[int], region: dict[int, int]) -> Optional[int]:
    """च/वा/एव/अपि … join the word they follow (skipping other enclitics); other particles the nearest
    verbal form of their half-verse (finite, absolutive or participle), else a verb of their clause."""
    if words[i].form in ENCLITIC and i > 0:
        j = i - 1
        while j > 0 and words[j].form in ENCLITIC and words[j].line == words[i].line:
            j -= 1
        return j
    line = words[i].line
    if words[i].form in NEGATION:  # न negates what follows it: the finite verb of its half-verse, else a predicate
        after = [j for j in verbs if j > i and words[j].line == line] or \
                [j for j, w in enumerate(words) if j > i and w.line == line and not w.in_compound and w.morph is not None
                 and w.morph.kind == "subanta" and w.morph.krt in PREDICATE_KRT and w.morph.vibhakti == PRATHAMA]
        if after:
            return after[0]
    near = [j for j, w in enumerate(words) if j != i and w.line == line and not w.in_compound
            and (j in verbs or j in verbals or (w.morph is not None and w.morph.kind == "subanta" and w.morph.krt in PREDICATE_KRT))]
    if near:
        return min(near, key=lambda j: (abs(j - i), j < i))
    pool = [v for v in verbs if region[words[v].line] == region[line]]
    return _pick(pool, words, i) if pool else None  # verbless: attached to the subject by _attach_verbless


def _conjuncts(words: list[Word], group: list[int], head: int) -> list[int]:
    """Members of an agreement group joined to its head by च/वा (A B च, A च B च): nouns or pronouns
    followed by the particle, or preceding a head that is followed by it. Qualifiers are not conjuncts."""
    def marked(j: int) -> bool:
        return j + 1 < len(words) and words[j + 1].form in CONJUNCTION
    def nounlike(j: int) -> bool:
        m = words[j].morph
        return not m.krt and (lemma_class(m.lemma) in ("noun", "pronoun", "") or m.lemma in PRONOUNS)
    others = [j for j in group if j != head and nounlike(j)]
    if not nounlike(head):
        return []
    out = [j for j in others if marked(j)]
    if marked(head):  # A B च with B chosen as head: the other nouns are its conjuncts
        out = others or [j for j in group if j != head and not words[j].morph.krt]  # मामकास् पाण्डवास् च
    return out


def _joint_agreement(words: list[Word], subjects: list[int], v: int) -> bool:
    """Two singular subjects joined by च take a dual verb, more (or any plural) a plural one."""
    if len(subjects) < 2:
        return False
    m, verb = words[subjects[0]].morph, words[v].morph
    if not (is_case(m, PRATHAMA) and is_finite(verb) and verb.prayoga in (None, "कर्तरि")):
        return False
    singular = all(words[j].morph.vacana == "एकवचन" for j in subjects)
    want = "द्विवचन" if singular and len(subjects) == 2 else "बहुवचन"
    return verb.vacana == want


def _adverbial(word: Word) -> bool:
    """A neuter accusative singular that the corpus knows mainly as an adverb (शीघ्रम्, सुखम्, चिरम्)."""
    m = word.morph
    if m.krt or m.vacana != "एकवचन" or m.linga != "नपुंसकलिङ्ग":
        return False
    from mayur import freq

    tags = freq._parsed(word.form)
    adverb = sum(n for _, upos, _, n in tags if upos in ("ADV", "PART"))
    return adverb > 0 and adverb >= sum(n for _, upos, _, n in tags if upos not in ("ADV", "PART"))


def assign_roles(words_in: list[Word]) -> tuple[list[Word], list[str]]:
    """Karaka roles and heads for the chosen analyses (returns new Word objects)."""
    words = [replace(w, role="", head=None) for w in words_in]
    notes: list[str] = []
    finite = [i for i, w in enumerate(words) if is_finite(w.morph)]
    verbs = [v for v in finite if not _quoted(words, v)]
    verbals = [i for i, w in enumerate(words) if is_nonfinite(w.morph)]
    participles = [i for i, w in enumerate(words) if not w.in_compound and w.morph is not None
                   and w.morph.kind == "subanta" and w.morph.krt in OBJECT_TAKING]
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
        conjuncts = _conjuncts(words, group, head)
        if case == PRATHAMA:
            agreeing = [v for v in rverbs if karta_agrees(words[head].morph, words[v].morph)
                        or _joint_agreement(words, [head] + conjuncts, v)]
            passive = [v for v in rverbs if words[v].morph.prayoga in ("कर्मणि", "भावे")
                       and words[v].morph.vacana == words[head].morph.vacana]
            copular = [v for v in rverbs if v in kartas and words[v].morph.root in COPULA
                       and words[v].morph.vacana == words[head].morph.vacana]
            if agreeing and _pick(agreeing, words, head) in kartas:  # second phrase of the same karta
                verb = _pick(agreeing, words, head)
                head_k = kartas[verb]
                joined = any(j + 1 < len(words) and words[j + 1].form in CONJUNCTION for j in group)
                for j in group:  # … पाण्डवास् च: a second agent joined by च, else an apposition of the first
                    _set(words, j, "कर्ता" if joined and j == head else "विशेषण", verb if joined and j == head else
                         head if joined else head_k)
                if joined:
                    notes.append(f"{words[head_k].form} and {words[head].form}: joined by च/वा, both कर्ता of {words[verb].form}")
                continue
            if agreeing and all(words[j].morph.krt in PREDICATE_KRT for j in group):
                verb = _pick(agreeing, words, head)  # मार्गमाणस् संददर्श: no noun names the agent
                for j in group:
                    _set(words, j, "विशेषण", verb)
                notes.append(f"{words[head].form}: qualifies the unexpressed agent of {words[verb].form} (अध्याहार)")
                continue
            if agreeing:
                verb, role = _pick(agreeing, words, head), "कर्ता"
                kartas[verb] = head
                if words[verb].morph.root in COPULA:
                    sub_role = "विधेय"  # रामस् वीरस् अस्ति; a qualifier standing right before its noun stays विशेषण
            elif copular:  # त्वम् समर्थस् असि: the other nominative is the predicate
                for j in group:
                    _set(words, j, "विधेय", kartas[_pick(copular, words, head)])
                continue
            elif passive:
                verb, role = _pick(passive, words, head), "कर्म"
            else:
                sub_role = "विधेय"
        elif case == DVITIYA and len(group) == 1 and _adverbial(words[head]):
            verb = _line_verbal(words, head, verbs, verbals + participles)
            verb = verb if verb is not None else _pick(rverbs, words, head)
            _set(words, head, "अव्यय", verb)
            notes.append(f"{words[head].form}: क्रियाविशेषण, the neuter accusative used as an adverb "
                         f"(the corpus tags this form as an adverb)")
            continue
        elif case == DVITIYA:
            governors = rverbs + [g for g in verbals + participles if region[words[g].line] == region[words[head].line]
                                  and g not in group]
            free = [v for v in governors if v not in has_karma]
            verb = _pick(free, words, head)
            coordinated = any(k + 1 < len(words) and words[k + 1].form in ("च", "वा") for k in group)
            if verb is None and governors:
                near = _pick(governors, words, head)
                verb = near if coordinated or words[near].morph.root in DVIKARMAKA else None
            if verb is not None and verb in has_karma:  # A च B च / द्विकर्मक: the governor takes another कर्म
                notes.append(f"{words[head].form}: further कर्म of {words[verb].form} (choice: nearest governor)")
            if verb is not None:
                role = "कर्म"
                has_karma.add(verb)
            else:
                notes.append(f"{words[head].form}: accusative with no verb left to govern it")
        elif case == TRITIYA:
            kta = _kta_near(words, head)
            near = _line_verbal(words, head, verbs, verbals + participles)
            verb = kta if kta is not None else near if near is not None else _pick(rverbs, words, head)
            passive = verb is not None and (kta is not None or words[verb].morph.prayoga in ("कर्मणि", "भावे"))
            role = "कर्ता" if passive else "करण"
        elif case == SAMBODHANA:
            role, verb = "सम्बोधन", _pick(rverbs or verbs, words, head)
        elif case == SHASHTHI:
            genitives.append(group)
            continue
        else:
            near = _line_verbal(words, head, verbs, verbals + participles)
            role, verb = KARAKA_OF_CASE.get(case, ""), near if near is not None else _pick(rverbs, words, head)
        _set(words, head, role, verb)
        for j in group:
            if j == head:
                continue
            if j in conjuncts and role:  # रामस् लक्ष्मणस् च: a conjunct shares the role and the governor
                _set(words, j, role, verb)
            elif sub_role == "विधेय" and verb is not None and j < head and _compound_final(words, j) == head:
                _set(words, j, "विशेषण", head)
            else:
                _set(words, j, "सम्बोधन" if case == SAMBODHANA else sub_role, head)
        if conjuncts and role:
            notes.append(f"{words[head].form} and {', '.join(words[j].form for j in conjuncts)}: joined by च/वा, "
                         f"the same {role}")
    for group in genitives:  # सम्बन्ध of the adjacent nominal; else an argument of the verb
        head = max(group, key=lambda i: _head_priority(words, i, []))
        target = _adjacent_nominal(words, head)
        verb = _pick(in_region[region[words[head].line]] or verbs, words, head)
        fear = verb is not None and words[verb].morph.root in FEAR
        if target is None and not fear:
            target = _adjacent_nominal(words, head, over_verb=True)
        if target is None:
            _set(words, head, "अपादान" if fear else "सम्बन्ध", verb)
        else:
            _set(words, head, "सम्बन्ध", target)
        for j in group:
            if j != head:
                _set(words, j, "विशेषण", head)
    for i, w in enumerate(words):
        if w.morph is not None and w.morph.kind == "avyaya" and not w.role:
            _set(words, i, "अव्यय", _particle_head(words, i, verbs, verbals, region))
    _attach_verbless(words, region, in_region, notes)
    return words, notes


def can_be_subject(words: list[Word], i: int) -> bool:
    """Pronoun, or a noun that is not a participle, possessive (-वत्/-मत्/-इन्) or compound final."""
    m = words[i].morph
    same = [a for a in words[i].analyses if (a.vibhakti, a.vacana, a.linga) == (m.vibhakti, m.vacana, m.linga)]
    if any(a.lemma in PRONOUNS for a in same):
        return True  # also when the chosen lemma is a variant stem (क for किम्)
    if m.krt or m.lemma.endswith(POSSESSIVE) or (i > 0 and words[i - 1].in_compound):
        return False
    return lemma_class(m.lemma) == "noun"


def _krt_predicates(words: list[Word], idx: list[int], main: Optional[int]) -> list[int]:
    """Nominative kṛt (क्त, क्तवतु, कृत्य) agreeing with the subject: the predicates of a verbless clause."""
    krt = [i for i in idx if i != main and not words[i].in_compound and not (i > 0 and words[i - 1].in_compound)
           and words[i].morph is not None and words[i].morph.krt in ("क्त", "क्तवतु", "तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्")
           and is_case(words[i].morph, PRATHAMA) and (main is None or agrees(words[i].morph, words[main].morph))]
    oblique = ("तृतीया", "चतुर्थी", "पञ्चमी", "सप्तमी", DVITIYA)
    with_deps = [i for i in krt if any(w.line == words[i].line and not w.in_compound and w.morph is not None
                                       and w.morph.vibhakti in oblique for w in words)]
    if main is None:  # हनुमता संगतस्: the one nominative of its half-verse, with its own kārakas, predicates
        alone = lambda i: not any(j != i and w.line == words[i].line and not w.in_compound  # noqa: E731
                                  and is_case(w.morph, PRATHAMA) for j, w in enumerate(words))
        return [i for i in with_deps if alone(i)]  # of the earlier subject; in a list of epithets it is one more
    return with_deps or krt[-1:]  # choice: the kṛt with its own kārakas, else the last one


def _qualifier(words: list[Word], i: int) -> bool:
    """Adjective, participle or pronoun: a word that qualifies rather than predicates (by lemma class)."""
    m = words[i].morph
    return bool(m.krt) or lemma_class(m.lemma) in ("adjective", "pronoun") or m.lemma in PRONOUNS


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
            preds = _krt_predicates(words, idx, main)
            for i in idx:  # nominatives: kṛt predicates are क्रिया; qualifiers of the subject विशेषण; others विधेय
                if not (is_case(words[i].morph, PRATHAMA) and i != main and (i in subjects or words[i].role == "विधेय")):
                    continue
                if i in preds:
                    _set(words, i, "क्रिया", None)
                elif main is not None and preds and agrees(words[i].morph, words[main].morph):
                    _set(words, i, "विशेषण", main)
                else:
                    _set(words, i, "विधेय", main)
            if preds and main is not None:
                _set(words, main, "कर्ता", _pick(preds, words, main))  # karaka_links.license_words fixes कर्ता/कर्म (3.4.70)
                notes.append(f"nominal clause: {', '.join(words[p].form for p in preds)} kṛt predicate(s) of "
                             f"{words[main].form}; copula अस्ति supplied (अध्याहार)")
            if preds and main is None:
                notes.append(f"{', '.join(words[p].form for p in preds)}: kṛt predicate(s); the subject is not "
                             f"expressed here (carried over, अनुवृत्ति)")
            notes.append("nominal clause: subject not expressed; all nominatives are विधेय" if main is None
                         else f"nominal clause: {words[main].form} is the subject (कर्ता of the understood अस्ति, "
                              f"अध्याहार), agreeing nominatives are विधेय")
            predicates = preds or [i for i in idx if is_case(words[i].morph, PRATHAMA) and not words[i].in_compound]
            for i in idx:  # epithet lists: local attachment to the nearest predicate in the line
                if words[i].role in LOCAL and words[i].role != "सम्बन्ध" or (words[i].role == "सम्बन्ध" and
                                                                           words[i].head is None):
                    same = [j for j in predicates if words[j].line == words[i].line] or predicates
                    _set(words, i, words[i].role, _pick(same, words, i))
            subjects = preds or ([main] if main is not None else [])
        if not subjects:
            continue
        for i in idx:
            if words[i].role and words[i].head is None and i not in subjects and words[i].role != "क्रिया":
                _set(words, i, words[i].role, _pick(subjects, words, i))
        if not rverbs and main is not None and words[main].head is None:
            _set(words, main, "कर्ता", None)
