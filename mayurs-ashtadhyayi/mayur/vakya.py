"""Sentence structure: kāraka roles and heads for the chosen analyses (used by shabdabodha.resolve).

Links proposed here are kept only if ``mayur.karaka_links.license_words`` finds a rule that licenses them.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.karaka_rules import DVIKARMAKA, GATI_AKARMAKA
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


_QUALIFYING: set[int] = set()  # set per call of assign_roles


def _head_priority(words: list[Word], i: int, verbs: list[int]) -> float:
    m = words[i].morph
    if i in _QUALIFYING:
        return 0.2  # दृढव्रतस्, पापात्मानस्: an adjective by formation, whatever its last member is
    if m.lemma in FIRST_PERSON | SECOND_PERSON:
        return 4.0  # अस्मद्/युष्मद् never qualify another word
    cls = lemma_class(m.lemma)
    nxt = words[i + 1] if i + 1 < len(words) else None
    points = m.lemma in DEMONSTRATIVE and nxt is not None and nxt.line == words[i].line and nxt.morph is not None \
        and not nxt.in_compound and agrees(m, nxt.morph) and nxt.morph.lemma not in PRONOUNS
    to_noun = points and not any(
        agrees(m, w.morph) for w in words[i + 2:] if w.line == words[i].line and w.morph is not None
        and not w.in_compound)  # (इदम् पवित्रम् पापघ्नम् पुण्यम्: a list of predicates; इदम् is the subject)
    if not verbs and m.vibhakti == PRATHAMA and m.lemma in PRONOUNS and not to_noun:
        return 3.0  # verbless clause: the pronoun (कस्) is the subject (not कश्चित्, अन्य: they delimit a noun;
        # not अयम् आत्मा: right before the noun it points at, it is that noun's determiner)
    score = {"noun": 2.0, "pronoun": 1.5, "": 1.0, "adjective": 0.8}.get(cls, 0.0)  # सा प्रिया: the adjective heads
    if m.lemma in DEMONSTRATIVE:
        score = 0.1 if points else 0.5  # तत् सर्वम्, सस् कपिस्: the demonstrative qualifies the other word;
        # सा प्रिया: right before the word it points at, it is that word's determiner
    if m.lemma in NUMERAL:
        score = min(score, 0.3)  # पञ्च बालकाः: a संख्या (1.1.23) counts the noun it stands with
    if m.lemma in OWN:
        score = 0.05  # तत् स्वम्: "that, his own"
    if m.krt and cls != "noun":  # (वित्तम्, a noun in its own right, heads यत् वित्तम्); below a demonstrative:
        score -= 0.6  # चङ्क्रम्यमाणौ तौ, the participle says something of the one तौ points at
    if i > 0 and words[i - 1].in_compound:
        score -= 0.5
    if verbs:
        same = [abs(v - i) for v in verbs if words[v].line == words[i].line]  # tie-breaks only: nearest the
        score -= 0.001 * min(same) if same else 0.01 + 0.0001 * i  # verb in its half-verse, else the first noun
    return score


def _segment(words: list[Word], i: int) -> Optional[int]:
    """Clause of word ``i`` inside its line when the line has two or more finite verbs: the clause
    runs up to and including each finite verb (यस् पठति | सस् सुखम् लभते); words after the last verb
    belong to it. None when the line has one finite verb or none (then the line is the clause)."""
    line = [j for j, w in enumerate(words) if w.line == words[i].line and is_finite(w.morph)]
    if len(line) < 2:
        return None
    nxt = next((j for j in line if j >= i), line[-1])
    before = [j for j in line if j < i]
    m = words[i].morph
    if before and m is not None and is_case(m, PRATHAMA) and not karta_agrees(m, words[nxt].morph) \
            and karta_agrees(m, words[before[-1]].morph):
        return before[-1]  # वक्ष्यामि अहम्: the subject stands after its verb, as verse allows
    return nxt


def _next_governor(words: list[Word], i: int) -> Optional[int]:
    """The absolutive, infinitive or motion participle (गत, प्राप्त: 3.4.72) standing right after word ``i``
    (particles skipped): वनम् गते. An accusative there is its कर्म, not part of a later phrase."""
    j = i + 1
    while j < len(words) and words[j].line == words[i].line and words[j].form in ENCLITIC:
        j += 1
    if j >= len(words) or words[j].line != words[i].line or words[j].morph is None or words[j].in_compound:
        return None
    m = words[j].morph
    return j if m.krt in ("क्त", "क्तवतु") and (m.root or "") in GATI_AKARMAKA else None


def _before_verbal(words: list[Word], i: int) -> bool:
    """Word ``i`` stands right before a finite verb, absolutive or infinitive (particles skipped)."""
    j = i + 1
    while j < len(words) and words[j].line == words[i].line and words[j].form in ENCLITIC:
        j += 1
    return j < len(words) and words[j].line == words[i].line and (is_finite(words[j].morph) or is_nonfinite(words[j].morph))


def _split_at_absolutive(words: list[Word], group: list[int]) -> list[list[int]]:
    """वनम् गत्वा फलम् खादति: two object nouns with an absolutive between them are two phrases, the
    first governed by the absolutive. An adjective and its noun are not parted this way."""
    def noun(j: int) -> bool:
        m = words[j].morph
        return not m.krt and lemma_class(m.lemma) == "noun"
    for k in range(1, len(group)):
        between = [j for j in range(group[k - 1] + 1, group[k]) if words[j].morph is not None
                   and words[j].morph.krt in ("क्त्वा", "ल्यप्")]
        if between and any(noun(j) for j in group[:k]) and any(noun(j) for j in group[k:]) \
                and _before_verbal(words, group[-1]):  # (गृध्रम् हत्वा जटायुषम् stays one phrase: an apposition)
            return [group[:k]] + _split_at_absolutive(words, group[k:])
    return [group]


def _apart_from_personal(words: list[Word], group: list[int]) -> list[list[int]]:
    """मम मित्रस्य: a noun does not qualify अस्मद्/युष्मद् (they name the speaker and the one addressed);
    in an oblique case it is a phrase of its own. (A participle or adjective may: मम भोक्तुकामस्य.)"""
    if words[group[0]].morph.vibhakti == PRATHAMA or not any(words[j].morph.lemma in FIRST_PERSON | SECOND_PERSON
                                                             for j in group):
        return [group]
    nouns = [j for j in group if not words[j].morph.krt and j not in _QUALIFYING
             and lemma_class(words[j].morph.lemma) == "noun"]
    rest = [j for j in group if j not in nouns]
    return [g for g in (rest, nouns) if g]


def _joined_segment(words: list[Word], line: int, anchor: int) -> Optional[int]:
    """A verbless half-verse joined to one with two finite verbs belongs to the nearer clause of that line:
    शस्त्रपाणयस् | धार्तराष्ट्रास् रणे हन्युस् तत् … भवेत् goes with हन्युस्, the first verb after it."""
    finite = [j for j, w in enumerate(words) if w.line == anchor and is_finite(w.morph)]
    if anchor == line or len(finite) < 2:
        return None
    return finite[0] if line < anchor else finite[-1]


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
            segment = _segment(words, i)
            if segment is None and w.line not in governed:
                segment = _joined_segment(words, w.line, region[w.line])
            clause = (clause, segment, _next_governor(words, i) if m.vibhakti == DVITIYA else None)
            own = i if personal or relative else -1
            prev = words[i - 1].morph if i > 0 and words[i - 1].line == w.line else None
            if own == -1 and prev is not None and prev.lemma == "यद्" and agrees(prev, m) \
                    and sum(is_finite(x.morph) for x in words if x.line == w.line) > 1:
                own = i - 1  # यम् ग्रामम् त्वम् गच्छसि: the relative and the noun it qualifies are one phrase
            groups.setdefault((m.vibhakti, m.vacana, m.linga, clause, own), []).append(i)
    order = lambda g: (words[g[0]].morph.vibhakti != PRATHAMA, words[g[0]].morph.lemma not in FIRST_PERSON | SECOND_PERSON)
    parts = [part for g in groups.values() for part in _apart_from_personal(words, g)]
    parts = [part for g in parts
             for part in (_split_at_absolutive(words, g) if words[g[0]].morph.vibhakti == DVITIYA else [g])]
    return sorted(parts, key=order)


def _set(words: list[Word], i: int, role: str, head: Optional[int]) -> None:
    words[i] = replace(words[i], role=role, head=head)


def _kta_near(words: list[Word], i: int) -> Optional[int]:
    near = [j for j in range(max(0, i - 2), min(len(words), i + 3))
            if j != i and words[j].morph is not None and words[j].morph.krt == "क्त" and words[j].morph.kind == "subanta"]
    return _pick(near, words, i)


DEMONSTRATIVE = {"तद्", "एतद्", "इदम्", "अदस्"}
from mayur.vakya_nominal import NUMERAL  # noqa: E402
OWN = {"स्व", "स्वक", "स्वीय", "निज"}
# क्त forms that take a तृतीया of what one is furnished with or parted from, not of an agent (2.3.18 करण)
FURNISHED = ("युक्त", "संयुक्त", "समायुक्त", "अन्वित", "समन्वित", "उपेत", "समेत", "सहित", "हीन", "विहीन", "रहित", "वर्जित")
NEGATION = {"न", "मा"}
CONNECTIVE = {"ततः", "ततस्", "अथ", "तदा", "पश्चात्", "अनन्तरम्"}  # sentence connectives (nipāta, 1.4.57)
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
    if words[i].form == "तु" and i > 0:  # सौमित्रिः तु, राघवः … तु: तु sets its topic, the agent, against what
        agent = [j for j, w in enumerate(words) if w.line == words[i].line and w.role == "कर्ता"]  # went before;
        return _pick(agent, words, i) if agent else i - 1  # (nipāta 1.4.57; choice by position) else its word
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
        nxt = i + 1  # न संशयस्: with no verb in its half-verse it denies the noun right after it (न अतः पुण्यतरम्:
        while nxt < len(words) and words[nxt].line == line and words[nxt].morph is not None \
                and words[nxt].morph.kind == "avyaya":  # particles between are skipped)
            nxt += 1
        if nxt < len(words) and words[nxt].line == line and not any(j in verbs for j in range(len(words)) if words[j].line == line) \
                and words[nxt].morph is not None and words[nxt].morph.kind == "subanta" and words[nxt].morph.vibhakti == PRATHAMA:
            return nxt
    if _segment(words, i) is not None:
        return _segment(words, i)
    verbal_in_line = any(words[j].line == line for j in verbs + verbals)
    near = [j for j, w in enumerate(words) if j != i and w.line == line and not w.in_compound
            and (j in verbs or j in verbals or (w.morph is not None and w.morph.kind == "subanta" and w.morph.krt in PREDICATE_KRT
                                                and not (verbal_in_line and lemma_class(w.morph.lemma) == "noun")))]
    # (ददौ नित्यम् वित्तम्: beside a verb, a participle that has become a noun is no predicate)
    if words[i].form in CONNECTIVE:
        near = _connective_head(words, i, near, verbs, verbals)
    if near:
        return min(near, key=lambda j: (abs(j - i), j < i))
    pool = [v for v in verbs if region[words[v].line] == region[line]]
    return _pick(pool, words, i) if pool else None  # verbless: attached to the subject by _attach_verbless


def _conjuncts(words: list[Word], group: list[int], head: int) -> list[int]:
    """Members of an agreement group joined to its head by च/वा (A B च, A च B च): nouns or pronouns
    followed by the particle, or preceding a head that is followed by it. Qualifiers are not conjuncts."""
    def marked(j: int) -> bool:
        return j + 1 < len(words) and words[j + 1].form in CONJUNCTION
    def nounlike(j: int) -> bool:  # a noun or अस्मद्/युष्मद्: एक, अन्य, सर्व, तद् qualify, they are not conjuncts
        m = words[j].morph
        return not m.krt and (lemma_class(m.lemma) == "noun" or m.lemma in FIRST_PERSON | SECOND_PERSON)
    others = [j for j in group if j != head and nounlike(j)]
    if not nounlike(head):
        return []
    out = [j for j in others if marked(j)]
    if marked(head):  # A B च with B chosen as head: the other nouns are its conjuncts
        pair = [j for j in group if j != head and not words[j].morph.krt] if len(group) == 2 else []
        out = others or pair  # मामकास् पाण्डवास् च: the only other word of the phrase
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


def _qualifies(words: list[Word], i: int, adjectives: bool = False) -> bool:
    """A participle or a बहुव्रीहि: a word that says something of another, named or not. A plain adjective
    counts only with ``adjectives``: beside a third-person verb it may itself name the agent (श्वेतस् धावति)."""
    m = words[i].morph
    return m.krt in PREDICATE_KRT or i in _QUALIFYING or \
        (adjectives and lemma_class(m.lemma) == "adjective" and m.lemma not in PRONOUNS)


def _adverbial(word: Word) -> bool:
    """A neuter accusative singular that the corpus knows mainly as an adverb (शीघ्रम्, सुखम्, चिरम्)."""
    m = word.morph
    if m.krt or m.vacana != "एकवचन" or m.linga != "नपुंसकलिङ्ग":
        return False
    from mayur import freq

    tags = freq._parsed(word.form)
    adverb = sum(n for _, upos, _, n in tags if upos in ("ADV", "PART"))
    return adverb > 0 and adverb >= sum(n for _, upos, _, n in tags if upos not in ("ADV", "PART"))


def assign_roles(words_in: list[Word], qualifying: frozenset = frozenset()) -> tuple[list[Word], list[str]]:
    """Karaka roles and heads for the chosen analyses (returns new Word objects). ``qualifying``:
    indices of words known to qualify another (the final of a बहुव्रीहि)."""
    words = [replace(w, role="", head=None) for w in words_in]
    _QUALIFYING.clear()
    _QUALIFYING.update(qualifying)
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
    for i in verbals:  # the absolutive or infinitive depends on the main action of its clause (3.4.21, 3.3.10):
        own = line_predicate(words, i)  # in a half-verse with no finite verb, its kṛt predicate
        _set(words, i, NONFINITE[words[i].morph.krt],
             own if own is not None else _pick(in_region[region[words[i].line]] or verbs, words, i))
    for i, w in enumerate(words):
        if w.in_compound:
            _set(words, i, "समासपूर्वपद", _compound_final(words, i))
        elif w.morph is None or w.morph.kind == "unknown":
            notes.append(f"{w.form}: no analysis; passed through unlinked")
    has_karma: set[int] = set()
    kartas: dict[int, int] = {}  # verb → karta head
    genitives: list[list[int]] = []
    orphans: list[tuple[list[int], int]] = []  # accusative phrases with no governor in their clause
    governed = {words[v].line for v in verbs + verbals}
    for group in _groups(words, region, governed):
        case = words[group[0]].morph.vibhakti
        rverbs = in_region[region[words[group[0]].line]]
        if _segment(words, group[0]) is not None:
            rverbs = [_segment(words, group[0])]  # the finite verb that closes this word's clause
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
            shared = [v for v in agreeing if v in kartas and agrees(words[kartas[v]].morph, words[head].morph)
                      and words[v].line != words[head].line]  # प्रानृत्यन् व्यनदन् च … जनप्रियाः: co-ordinate verbs
            if agreeing and (_pick(agreeing, words, head) in kartas or shared):  # share one agent; this is a
                verb = _pick(agreeing, words, head) if _pick(agreeing, words, head) in kartas else shared[0]
                # second phrase of the same karta (समानाधिकरण), in the other half-verse
                head_k = kartas[verb]
                joined = any(j + 1 < len(words) and words[j + 1].form in CONJUNCTION for j in group)
                for j in group:  # … पाण्डवास् च: a second agent joined by च, else an apposition of the first
                    _set(words, j, "कर्ता" if joined and j == head else "विशेषण", verb if joined and j == head else
                         head if joined else head_k)
                if joined:
                    notes.append(f"{words[head_k].form} and {words[head].form}: joined by च/वा, both कर्ता of {words[verb].form}")
                continue
            if not agreeing and not copular and all(_qualifies(words, j, adjectives=True) for j in group):
                # विप्रमोहिता … बिभेषि: it qualifies the त्वम् / अहम् that the verb ending expresses (1.4.105–108)
                agreeing = [v for v in rverbs if words[v].morph.purusha in ("मध्यमपुरुष", "उत्तमपुरुष")
                            and words[v].morph.vacana == words[head].morph.vacana and v not in kartas
                            and words[v].morph.prayoga in (None, "कर्तरि") and words[v].morph.root not in COPULA]
            if agreeing and all(_qualifies(words, j) for j in group) or \
                    (agreeing and words[agreeing[0]].morph.purusha != "प्रथमपुरुष"
                     and all(_qualifies(words, j, adjectives=True) for j in group)):
                verb = _pick(agreeing, words, head)  # मार्गमाणस् संददर्श, दक्षिणामुखस् प्रययौ: no noun names the agent
                for j in group:
                    _set(words, j, "विशेषण", verb)
                notes.append(f"{words[head].form}: qualifies the unexpressed agent of {words[verb].form} (अध्याहार)")
                continue
            if agreeing:
                verb, role = _pick(agreeing, words, head), "कर्ता"
                if words[verb].morph.root in COPULA:
                    sub_role = "विधेय"
                    pronouns = [j for j in group if words[j].morph.lemma in PRONOUNS | FIRST_PERSON | SECOND_PERSON]
                    nouns = [j for j in group if not words[j].morph.krt and lemma_class(words[j].morph.lemma) == "noun"]
                    if pronouns and head not in pronouns:
                        head = pronouns[0]  # सस् राजा अस्ति: "he is a king"
                    elif not pronouns and len(nouns) > 1:
                        plain = [j for j in nouns if not (j > 0 and words[j - 1].in_compound) and j not in _QUALIFYING]
                        head = (plain or nouns)[0]  # रामस् वीरस् अस्ति: what is named first is what is spoken of;
                        # नित्योदकस् ब्राह्मणस् स्यात्: a compound says something of the plain noun
                kartas[verb] = head  # रामस् वीरस् अस्ति; a qualifier standing right before its noun stays विशेषण
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
        elif case == DVITIYA and _next_governor(words, group[-1]) is not None:
            verb, role = _next_governor(words, group[-1]), "कर्म"  # the object stands right before its governor
            has_karma.add(verb)
        elif case == DVITIYA:
            governors = rverbs + [g for g in verbals + participles if region[words[g].line] == region[words[head].line]
                                  and g not in group]
            free = [v for v in governors if v not in has_karma]
            verb = _pick(free, words, head)
            coordinated = any(k + 1 < len(words) and words[k + 1].form in ("च", "वा") for k in group)
            if verb is None and governors:
                near = _pick(governors, words, head)
                verb = near if coordinated or words[near].morph.root in DVIKARMAKA else None
            if verb is None:  # decided after every phrase of the verse has taken its governor
                orphans.append((group, head))
                continue
            if verb in has_karma:  # A च B च / द्विकर्मक: the governor takes another कर्म
                notes.append(f"{words[head].form}: further कर्म of {words[verb].form} (choice: nearest governor)")
            role = "कर्म"
            has_karma.add(verb)
        elif case == TRITIYA:
            kta = _kta_near(words, head)
            own = line_predicate(words, head)  # सारसेन … क्षिप्तः: the क्त predicate of a half-verse with no
            kta = kta if kta is not None or own is None or words[own].morph.krt != "क्त" else own  # finite verb
            near = _line_verbal(words, head, verbs, verbals + participles)
            verb = kta if kta is not None else near if near is not None else _pick(rverbs, words, head)
            passive = verb is not None and (kta is not None or words[verb].morph.prayoga in ("कर्मणि", "भावे"))
            furnished = kta is not None and ((words[kta].morph.stem or words[kta].form).startswith(FURNISHED)
                                             or agent_expressed(words[kta].morph))  # 3.4.72: समागतः कर्तरि
            role = "कर्ता" if passive and not furnished else "करण"  # मुदा युक्तास्: joy is no agent
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
            elif sub_role == "विधेय" and _determiner(words, j):  # भयम् किंचित्: a pronoun delimits, not predicates
                _set(words, j, "विशेषण", head)
            else:
                _set(words, j, "सम्बोधन" if case == SAMBODHANA else sub_role, head)
        if conjuncts and role:
            notes.append(f"{words[head].form} and {', '.join(words[j].form for j in conjuncts)}: joined by च/वा, "
                         f"the same {role}")
    _attach_orphans(words, orphans, verbs, has_karma, notes)
    for group in genitives:  # सम्बन्ध of the adjacent nominal; else an argument of the verb
        head = max(group, key=lambda i: _head_priority(words, i, []))
        inside = range(min(group), max(group) + 1)  # one unbroken phrase (compound members and particles apart)
        solid = all(j in group or words[j].in_compound or (words[j].morph is not None and words[j].morph.kind == "avyaya")
                    for j in inside)
        target = enclitic_owner(words, head)  # अधिकारः ते; मम मित्रस्य (vakya_genitive)
        target = target if target is not None else genitive_after(words, head, group)
        target = target if target is not None else \
            _adjacent_nominal(words, head, span=(min(group), max(group)) if solid else None)
        verb = _pick(in_region[region[words[head].line]] or verbs, words, head)
        fear = verb is not None and words[verb].morph.root in FEAR
        if target is None and not fear:
            target = _adjacent_nominal(words, head, over_verb=True)
        if target is None:
            _set(words, head, "अपादान" if fear else "सम्बन्ध", verb)
        else:
            owner = words[target].head  # तस्य सा प्रिया: the genitive belongs to the noun that सा qualifies
            if words[target].role == "विशेषण" and words[target].morph.lemma in DEMONSTRATIVE and owner is not None \
                    and words[owner].line == words[target].line \
                    and words[owner].morph is not None and words[owner].morph.kind == "subanta" and owner not in group:
                target = owner
            _set(words, head, "सम्बन्ध", target)
        for j in group:
            if j != head:
                _set(words, j, "विशेषण", head)
    for i, w in enumerate(words):
        if w.morph is not None and w.morph.kind == "avyaya" and not w.role:
            _set(words, i, "अव्यय", _particle_head(words, i, verbs, verbals, region))
    _attach_verbless(words, region, in_region, notes)
    from mayur.vakya_personal import qualify_personal

    qualify_personal(words, _QUALIFYING, notes)
    for i in range(1, len(words)):  # मासि मासि: a word said twice is one phrase (8.1.4 नित्यवीप्सयोः)
        a, b = words[i - 1], words[i]
        if a.form == b.form and a.line == b.line and not a.in_compound and not b.in_compound and a.role \
                and b.morph is not None and b.morph.kind == "subanta" and a.head != i \
                and a.morph is not None and a.morph.lemma == b.morph.lemma:  # (मा मा हिंसीः is two words)
            _set(words, i, a.role, a.head)
    return words, notes


from mayur.vakya_nominal import _attach_verbless, _determiner, can_be_subject  # noqa: E402,F401
from mayur.vakya_clause import _attach_orphans, _connective_head, agent_expressed, line_predicate  # noqa: E402
from mayur.vakya_genitive import _adjacent_nominal, enclitic_owner, genitive_after  # noqa: E402
