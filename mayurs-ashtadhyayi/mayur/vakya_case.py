"""Syncretic nominative/accusative (वनम्, फले, फलानि) decided by the clause's kāraka structure."""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.karaka_rules import DVIKARMAKA
from mayur.model import Word
from mayur.shabdabodha import DVITIYA, PRATHAMA, PRONOUNS, is_case, is_finite, karta_agrees

AKARMAKA = {"भू", "अस्", "स्था", "शी", "आस्", "जन्", "वृत्", "जीव्", "मृ", "वस्", "स्वप्", "नश्", "रुह्", "जॄ", "विद्",
            "भा", "शुभ्", "राज्", "दीप्", "हस्", "रुद्", "क्रुध्", "लज्ज्", "मुद्", "सिध्", "पत्"}  # list, not a rule


def _alt(word: Word, case: str) -> Optional[int]:
    m = word.morph
    for k, a in enumerate(word.analyses):
        if a.kind == "subanta" and a.vibhakti == case and (a.lemma, a.vacana, a.linga) == (m.lemma, m.vacana, m.linga):
            return k
    return None


def syncretic(words_in: list[Word]) -> tuple[list[Word], list[str]]:
    """Re-choose प्रथमा/द्वितीया for a form that is both, only where the rules decide it: an active
    transitive verb whose agent is already an agreeing nominative takes it as कर्म (1.4.49, 2.3.2); a
    passive verb with no other subject expresses it as कर्म in प्रथमा (3.4.69, 2.3.46)."""
    words, notes = list(words_in), []
    for i, w in enumerate(words):
        m = w.morph
        if w.in_compound or m is None or m.vibhakti not in (PRATHAMA, DVITIYA):
            continue
        other = DVITIYA if m.vibhakti == PRATHAMA else PRATHAMA
        k = _alt(w, other)
        if k is None:
            continue
        line = [j for j, o in enumerate(words) if o.line == w.line and j != i and not o.in_compound and o.morph]
        if m.krt or m.lemma in PRONOUNS - {"तद्", "एतद्", "इदम्"} or any(
                words[j].form == "इति" or words[j].morph.lemma in ("यद्", "किम्") for j in line):
            continue  # a kṛt (शक्यम्) or a subordinate/quoted clause (किम्, यद्, इति): not decisive
        verbs = [j for j in line if is_finite(words[j].morph)]
        if len(verbs) != 1:
            continue  # decisive only with one finite verb in the half-verse
        v = words[verbs[0]].morph
        firm = [j for j in line if is_case(words[j].morph, PRATHAMA) and _alt(words[j], DVITIYA) is None]
        agent = [j for j in firm if karta_agrees(words[j].morph, v)]
        same_phrase = any((words[j].morph.vacana, words[j].morph.linga) == (m.vacana, m.linga) for j in agent)
        if v.prayoga in (None, "कर्तरि") and agent and not same_phrase and (v.root or "") not in AKARMAKA \
                and m.vibhakti == PRATHAMA:
            words[i] = replace(w, chosen=k)
            notes.append(f"{w.form}: द्वितीया, not प्रथमा: {words[verbs[0]].form} already has its agreeing कर्ता "
                         f"{words[agent[0]].form} (3.4.69, 2.3.46), so this is its कर्म (1.4.49, 2.3.2)")
        elif v.prayoga == "कर्मणि" and m.vibhakti == DVITIYA and not firm and m.vacana == v.vacana \
                and (v.root or "") not in DVIKARMAKA:
            words[i] = replace(w, chosen=k)
            notes.append(f"{w.form}: प्रथमा, not द्वितीया: the कर्मणि verb {words[verbs[0]].form} expresses its "
                         f"कर्म (1.4.49, 3.4.69, 2.3.46)")
    return words, notes
