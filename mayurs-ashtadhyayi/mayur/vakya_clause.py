"""Clause predicates of half-verses without a finite verb (part of mayur.vakya).

A half-verse (or prose sentence) with no finite verb can still be a clause of its own when a
nominative kṛt (क्त, क्तवतु, कृत्य) predicates of its subject: सारसेन … राजा जले क्षिप्तः. Such a kṛt is the
governor of the absolutives and instrumentals of its half-verse, as a finite verb would be.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.karaka_rules import GATI_AKARMAKA
from mayur.model import Morph, Word
from mayur.anvaya import pick as _pick
from mayur.shabdabodha import PRATHAMA, is_case, is_finite

KRT_PREDICATE = ("क्त", "क्तवतु", "तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्")
# roots that take no object (a list, not a rule; with GATI_AKARMAKA the roots of 3.4.72)
AKARMAKA = frozenset({"भू", "अस्", "स्था", "शी", "आस्", "जन्", "वृत्", "जीव्", "मृ", "वस्", "स्वप्", "नश्", "रुह्",
                      "जॄ", "भा", "शुभ्", "राज्", "दीप्", "हस्", "रुद्", "क्रुध्", "लज्ज्", "मुद्", "सिध्", "पत्",
                      "श्वस्", "तुष्", "हृष्", "शम्"})


def _predicate_like(words: list[Word], j: int) -> bool:
    w = words[j]
    m = w.morph
    return m is not None and not w.in_compound and not (j > 0 and words[j - 1].in_compound) \
        and is_case(m, PRATHAMA) and m.krt in KRT_PREDICATE


def line_predicate(words: list[Word], i: int) -> Optional[int]:
    """The nominative kṛt predicate of word ``i``'s half-verse when that half-verse has no finite
    verb (choice among several: the last one, where the predicate of a clause usually stands)."""
    line = words[i].line
    mates = [j for j, w in enumerate(words) if w.line == line]
    if any(is_finite(words[j].morph) for j in mates):
        return None
    preds = [j for j in mates if j != i and _predicate_like(words, j)]
    return preds[-1] if preds else None


def wanting_object(words: list[Word], i: int, verbs: list[int], has_karma: set[int]) -> Optional[int]:
    """An accusative left without a governor in its own clause: the nearest active finite verb of the
    verse, in another half-verse, that has no कर्म yet and whose root is not intransitive (कर्तुरीप्सिततमं
    कर्म 1.4.49, कर्मणि द्वितीया 2.3.2): प्राविशत् … देवसद्म तत्. Nearest is a choice, not a rule."""
    free = [v for v in verbs if v not in has_karma and words[v].line != words[i].line
            and words[v].morph.prayoga in (None, "कर्तरि") and (words[v].morph.root or "") not in AKARMAKA]
    return min(free, key=lambda v: (abs(v - i), v < i)) if free else None


def agent_expressed(m: Morph) -> bool:
    """A क्त of a root of motion or an intransitive root, agreeing with a subject, is कर्तरि (3.4.72):
    the agent is expressed by the suffix (अभिहित), so a तृतीया beside it is no agent (2.3.1 अनभिहिते,
    2.3.18): सुग्रीवेण समागतः 'met with Sugrīva' is करण (or सहार्थ), not 'met by Sugrīva'. A neuter
    singular may be भावे (गतम् अनेन) and is left to the general rule."""
    root = m.root or ""
    if m.krt != "क्त" or not (root in GATI_AKARMAKA or root in AKARMAKA):
        return False
    return not (m.linga == "नपुंसकलिङ्ग" and m.vacana == "एकवचन")


def _connective_head(words: list[Word], i: int, near: list[int], verbs: list[int], verbals: list[int]) -> list[int]:
    """ततः, अथ: the next event of the narrative is the main action, not an absolutive that precedes it
    (3.4.21 पूर्वकाले) nor a participle qualifying the agent. Main action: a finite verb of the half-verse;
    a kṛt with its own agent in the तृतीया (सारसेन … क्षिप्तः, 2.3.18, 3.4.70); a finite verb of the next
    half-verse; else the nearest verbal as for other particles."""
    line = words[i].line
    finite = [j for j in near if j in verbs]
    with_agent = [j for j in near if j not in verbals and any(w.head == j and w.role == "कर्ता" for w in words)]
    later = [v for v in verbs if words[v].line == line + 1]
    return finite or with_agent or ([_pick(later, words, i)] if later else near)


def _attach_orphans(words: list[Word], orphans: list[tuple[list[int], int]], verbs: list[int], has_karma: set[int],
                    notes: list[str]) -> None:
    """Accusative phrases left without a governor in their clause: कर्म of a verb in another half-verse
    that still wants one (vakya_clause.wanting_object), else unlinked."""
    for group, head in orphans:
        verb = wanting_object(words, head, verbs, has_karma)
        if verb is None:
            notes.append(f"{words[head].form}: accusative with no verb left to govern it")
        else:
            has_karma.add(verb)
            notes.append(f"{words[head].form}: कर्म of {words[verb].form} in the other half-verse (1.4.49, 2.3.2)")
        words[head] = replace(words[head], role="कर्म" if verb is not None else "", head=verb)
        for j in group:
            if j != head:
                words[j] = replace(words[j], role="विशेषण", head=head)
