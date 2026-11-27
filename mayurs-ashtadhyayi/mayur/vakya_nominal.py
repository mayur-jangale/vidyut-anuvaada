"""Nominal clauses (no finite verb): subject, kṛt predicates, epithets. Part of mayur.vakya."""

from __future__ import annotations

from typing import Optional

from mayur.anvaya import pick as _pick
from mayur.model import Word
from mayur.shabdabodha import (DVITIYA, LOCAL, POSSESSIVE, PRATHAMA, PRONOUNS, agrees, is_case, lemma_class)


def _set(words: list[Word], i: int, role: str, head: Optional[int]) -> None:
    from dataclasses import replace

    words[i] = replace(words[i], role=role, head=head)


def _head_priority(words: list[Word], i: int, verbs: list[int]) -> float:
    from mayur import vakya

    return vakya._head_priority(words, i, verbs)


def can_be_subject(words: list[Word], i: int, compound: bool = False) -> bool:
    """Pronoun, or a noun that is not a participle, possessive (-वत्/-मत्/-इन्) or compound final (with
    ``compound``: a compound final that is not a बहुव्रीहि)."""
    m = words[i].morph
    same = [a for a in words[i].analyses if (a.vibhakti, a.vacana, a.linga) == (m.vibhakti, m.vacana, m.linga)]
    if any(a.lemma in PRONOUNS for a in same):
        return True  # also when the chosen lemma is a variant stem (क for किम्)
    from mayur import vakya

    if m.krt or m.lemma.endswith(POSSESSIVE) or i in vakya._QUALIFYING or (i > 0 and words[i - 1].in_compound
                                                                          and not compound):
        return False  # a बहुव्रीहि final qualifies (2.2.24 अनेकमन्यपदार्थे); a द्वन्द्व or तत्पुरुष final
    return lemma_class(m.lemma) == "noun" or m.lemma in HONORIFIC  # names its own referent (रामलक्ष्मणौ)


HONORIFIC = {"भवत्"}  # भवान्: the second person spoken of in the third (a pronoun the corpus calls a noun)


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


def _determiner(words: list[Word], i: int) -> bool:
    """A pronoun (सर्वनाम, 1.1.27: किंचित्, अन्य, सस्) agreeing with the subject delimits it — वातजम् भयम्
    किंचित् 'any fear' — it does not say something of it, so it is its विशेषण, not a predicate."""
    m = words[i].morph
    return not m.krt and (m.lemma in PRONOUNS or m.lemma in NUMERAL or lemma_class(m.lemma) == "pronoun")


# संख्या (1.1.23 बहुगणवतुडति संख्या, and the numerals proper): a number counts the noun it stands with
NUMERAL = {"एक", "द्वि", "त्रि", "चतुर्", "पञ्चन्", "षष्", "सप्तन्", "अष्टन्", "नवन्", "दशन्", "विंशति", "त्रिंशत्"}


def _predicate_noun_after(words: list[Word], i: int, main: Optional[int]) -> Optional[int]:
    """आचारः परमः धर्मः: an adjective standing right before an agreeing noun that is not the subject
    qualifies that noun (समानाधिकरण), and the noun is the predicate; it is not a second predicate."""
    j = i + 1
    while j < len(words) and words[j].morph is not None and words[j].morph.kind == "avyaya":
        j += 1
    if main is None or j >= len(words) or j == main or words[j].line != words[i].line or words[j].in_compound \
            or words[j].morph is None or not _qualifier(words, i) or _qualifier(words, j):
        return None
    return j if agrees(words[i].morph, words[j].morph) and can_be_subject(words, j) else None


def _attach_verbless(words: list[Word], region: dict[int, int], in_region: dict[int, list[int]],
                     notes: list[str]) -> None:
    """Nominal clauses: one expressed subject or none; dependents attach to the nearest predicate."""
    for r, rverbs in in_region.items():
        idx = [i for i, w in enumerate(words) if region[w.line] == r]
        subjects = [i for i in idx if words[i].role == "" and is_case(words[i].morph, PRATHAMA)]
        if not subjects:
            continue
        if not rverbs:
            noms = [i for i in idx if is_case(words[i].morph, PRATHAMA) and not words[i].in_compound]
            able = [i for i in subjects if can_be_subject(words, i)] or \
                [i for i in subjects if len(noms) == 2 and can_be_subject(words, i, compound=True)
                 and _krt_predicates(words, idx, i)]
            # (रामलक्ष्मणौ वनम् गतौ: a compound and its kṛt predicate alone; the compound names the subject; in
            # a list of epithets a compound final stays an epithet)
            main = max(able, key=lambda i: (_head_priority(words, i, []), -i)) if able else None
            preds = _krt_predicates(words, idx, main)
            for i in idx:  # nominatives: kṛt predicates are क्रिया; qualifiers of the subject विशेषण; others विधेय
                if not (is_case(words[i].morph, PRATHAMA) and i != main and (i in subjects or words[i].role == "विधेय")):
                    continue
                if i in preds:
                    _set(words, i, "क्रिया", None)
                elif main is not None and agrees(words[i].morph, words[main].morph) \
                        and (preds or _determiner(words, i)):
                    _set(words, i, "विशेषण", main)
                elif _predicate_noun_after(words, i, main) is not None:
                    _set(words, i, "विशेषण", _predicate_noun_after(words, i, main))
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
