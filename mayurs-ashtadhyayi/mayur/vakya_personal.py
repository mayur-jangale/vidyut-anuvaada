"""Qualifiers of अस्मद् / युष्मद्: माम् अप्रतीकारम् अशस्त्रम् "me, unresisting and unarmed".

The personal pronouns have no gender of their own (the person meant supplies it), so an adjective,
a participle or a बहुव्रीहि that stands next to one of them in its case and number qualifies it
(समानाधिकरण, 2.1.57 विशेषणं विशेष्येण बहुलम् for the relation). A noun in the same case is taken only
when no verb has claimed it (त्वाम् राजानम् नमामि: an apposition); otherwise it is another argument. The nominative is left to the clause rules (त्वम् समर्थस्
असि has a predicate, not a qualifier). All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace

from mayur.model import Word
from mayur.shabdabodha import FIRST_PERSON, PRATHAMA, PRONOUNS, SAMBODHANA, SECOND_PERSON, SHASHTHI, lemma_class

QUALIFIER_KRT = {"क्त", "क्तवतु", "शतृ", "शानच्", "चानश्", "तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्"}
NEGATION_PREFIX = ("अन", "अ")


def _negated_noun(lemma: str) -> bool:
    """अशस्त्र, अप्रतीकार: नञ् + a noun, an adjective by formation (2.2.6, as a बहुव्रीहि 2.2.24)."""
    return any(lemma.startswith(p) and lemma_class(lemma[len(p):]) == "noun" for p in NEGATION_PREFIX)


def attributive(words: list[Word], i: int, qualifying: set[int]) -> bool:
    """Word ``i`` can only qualify: a participle, an adjective, a बहुव्रीहि or a negated noun."""
    m = words[i].morph
    if m.lemma in PRONOUNS | FIRST_PERSON | SECOND_PERSON:
        return False
    cls = lemma_class(m.lemma)
    return m.krt in QUALIFIER_KRT or i in qualifying or cls == "adjective" or _negated_noun(m.lemma) \
        or (cls == "" and not m.krt and i > 0 and words[i - 1].in_compound)


def qualify_personal(words: list[Word], qualifying: set[int], notes: list[str]) -> None:
    """Attach the qualifiers standing next to an oblique अस्मद् / युष्मद् to it (in place, like the caller)."""
    for p, w in enumerate(words):
        m = w.morph
        if m is None or w.in_compound or m.lemma not in FIRST_PERSON | SECOND_PERSON \
                or m.vibhakti in (None, PRATHAMA, SHASHTHI, SAMBODHANA):
            continue
        taken = []
        for step in (1, -1):
            j = p + step
            while 0 <= j < len(words) and words[j].line == w.line:
                x = words[j]
                if x.in_compound:  # a member of the qualifier's own compound
                    j += step
                    continue
                xm = x.morph
                if xm is None or xm.kind != "subanta" or (xm.vibhakti, xm.vacana) != (m.vibhakti, m.vacana):
                    break
                if not attributive(words, j, qualifying) and x.role:
                    break  # a noun with a role of its own; one left without any is the pronoun's apposition (त्वाम् राजानम्)
                words[j] = replace(x, role="विशेषण", head=p)
                taken.append(x.form)
                j += step
        if taken:
            notes.append(f"{', '.join(taken)}: in the case and number of {w.form} and next to it, so its qualifier(s)")
