"""Linking the clauses of a verse (part of mayur.vakya; run last by karaka_links.license_words).

After the kāraka links are set and licensed, each clause is a tree whose root is its predicate: a
finite verb, a kṛt predicate (क्रिया) or the subject of a nominal clause. Two kinds of clause depend
on another one, and their root gets a head:

* a relative clause (a form of यद्, or यदा/यदि/यत्र/यथा/चेत्) — its verb is subordinate, as 8.1.66
  यद्वृत्तान्नित्यम् says for its accent. The pronoun यद् is in constant relation to its correlative
  तद् (यत्तदोर्नित्यसम्बन्धः): यः … विमुञ्चेत … सः गच्छति, the root विमुञ्चेत goes to सः; with no तद् to the
  noun of the main clause that agrees with it (यत् … गतम् … सर्वम्), else to the main predicate. A
  relative adverb links its clause to the main predicate (यदा … संसृजेत … कार्या), यथा to its
  correlative तथा/एवम्.
* the content of speech, which is the कर्म of the verb of saying (1.4.49): after a frame
  'X उवाच ।' every following clause; after any other verb of saying, a following clause whose verb is
  in the first or second person or the imperative (the speaker's own words, 1.4.105–108).

Which candidate is taken when several are allowed (nearest, agreeing first) is a choice, not a rule.
"""

from __future__ import annotations

from dataclasses import replace
from typing import Optional

from mayur.model import Word

RELATIVE_ADVERB = {"यदा", "यदि", "यत्र", "चेत्", "यथा", "यत्"}
CORRELATIVE_ADVERB = {"यदा": {"तदा"}, "यदि": {"तर्हि", "तदा"}, "यत्र": {"तत्र"}, "यथा": {"तथा", "एवम्"},
                      "चेत्": {"तर्हि"}, "यत्": {"तत्"}}
CORRELATIVE = {"तद्", "एतद्"}
SPEECH = {"वच्", "ब्रू", "अह्", "आह्", "भाष्", "वद्", "कथ्", "कथि", "शंस्", "प्रच्छ्"}  # verbs of saying (a list)
JOINED = {"च", "वा"}


def _root_of(words: list[Word], k: int) -> int:
    seen = {k}
    while words[k].head is not None and 0 <= words[k].head < len(words) and words[k].head not in seen:
        k = words[k].head
        seen.add(k)
    return k


def _roots(words: list[Word]) -> list[int]:
    """Clause roots: predicates (क्रिया) and nominal-clause subjects (कर्ता) with no head."""
    return [i for i, w in enumerate(words) if w.head is None and not w.in_compound and w.morph is not None
            and w.role in ("क्रिया", "कर्ता")]


def _relative(words: list[Word], members: list[int]) -> Optional[int]:
    """The relative word of a clause; one followed by च/वा is an elliptic co-ordinate (यावत् च यत् च), not
    a clause marker."""
    for k in members:
        w = words[k]
        joined = k + 1 < len(words) and words[k + 1].form in JOINED
        pronoun = w.morph.kind == "subanta" and w.morph.lemma == "यद्"
        if (pronoun or (w.morph.kind == "avyaya" and w.form in RELATIVE_ADVERB)) and not joined:
            return k
    return None


def _agreeing(words: list[Word], rel: int, cands: list[int], lemmas: Optional[set[str]]) -> list[int]:
    r = words[rel].morph
    return [k for k in cands if words[k].morph.kind == "subanta" and not words[k].in_compound
            and (lemmas is None or words[k].morph.lemma in lemmas)
            and (words[k].morph.vacana, words[k].morph.linga) == (r.vacana, r.linga)]


def _nearest(cands: list[int], i: int) -> Optional[int]:
    return min(cands, key=lambda k: (abs(k - i), k < i)) if cands else None


def _relative_head(words: list[Word], rel: int, root: int, clauses: dict[int, list[int]]) -> Optional[int]:
    """Where a relative clause attaches: correlative, agreeing noun, or main predicate (see module doc)."""
    others = [r for r in clauses if r != root and _relative(words, clauses[r]) is None]
    form = words[rel].form
    if not others or any(words[k].form in CORRELATIVE_ADVERB.get(form, ()) for k in clauses[root]):
        return None  # यथा कृते युगे तथा: relative and correlative in one clause, an elliptic comparison
    outside = [k for r in others for k in clauses[r]]
    if words[rel].morph.kind == "subanta":
        tad = [k for k in outside if words[k].morph.kind == "subanta" and words[k].morph.lemma in CORRELATIVE]
        pick = _nearest(_agreeing(words, rel, tad, None), rel) or _nearest(tad, rel)
        pick = pick if pick is not None else _nearest(_agreeing(words, rel, outside, None), rel)
        if pick is not None:
            return pick
    elif form == "यथा":
        pick = _nearest([k for k in outside if words[k].form in CORRELATIVE_ADVERB[form]], rel)
        if pick is not None:
            return pick
    marked = [r for r in others if any(words[k].form in CORRELATIVE_ADVERB.get(form, ()) for k in clauses[r])]
    return _nearest(marked or others, root)


def _frame(words: list[Word], v: int) -> bool:
    """'महादेवः उवाच ।': the verb of saying with nothing in its half-verse but its agent and particles."""
    line = [k for k, w in enumerate(words) if w.line == words[v].line and k != v and not w.in_compound]
    return all(words[k].morph is not None and (words[k].head == v and words[k].role == "कर्ता"
                                                 or words[k].morph.kind == "avyaya") for k in line)


def _own_words(words: list[Word], root: int) -> bool:
    m = words[root].morph
    return m.kind == "tinanta" and (m.purusha in ("उत्तमपुरुष", "मध्यमपुरुष") or m.lakara == "लोट्")


def _speech_head(words: list[Word], root: int, speech: list[int]) -> Optional[int]:
    before = [s for s in speech if s < root and words[s].line <= words[root].line and s != root]
    if not before:
        return None
    s = before[-1]
    if _frame(words, s) and words[root].line > words[s].line:
        return s
    third = words[s].morph.purusha in (None, "प्रथमपुरुष")
    return s if third and _own_words(words, root) else None


def _quoted_links(words: list[Word], speech: list[int]) -> dict[int, int]:
    """'अभिगच्छ' इति … कथयामास: words closed by इति are the कर्म (1.4.49) of the verb of saying when the
    verse has one; the nearest verb is only the fallback chosen earlier (vakya.assign_roles)."""
    out = {}
    for v, w in enumerate(words):
        if w.role == "क्रिया" and w.head is not None and v + 1 < len(words) and words[v + 1].form == "इति":
            say = [s for s in speech if s != v]
            if say and w.head not in say:
                out[v] = _nearest(say, v)
    return out


def link_clauses(words_in: list[Word]) -> tuple[list[Word], list[str]]:
    """New words with relative and speech clauses attached (see module doc)."""
    words, notes = list(words_in), []
    roots = _roots(words)
    clauses = {r: [k for k in range(len(words)) if words[k].morph is not None and _root_of(words, k) == r]
               for r in roots}  # (unanalysed words take no part)
    links: dict[int, int] = {}
    for r in roots:
        rel = _relative(words, clauses[r])
        if rel is not None and words[r].role == "क्रिया":
            head = _relative_head(words, rel, r, clauses)
            if head is not None:
                links[r] = head
                notes.append(f"{words[r].form}: verb of the relative clause of {words[rel].form} (8.1.66), "
                             f"attached to {words[head].form}")
    speech = [r for r in roots if words[r].role == "क्रिया" and words[r].morph.kind == "tinanta"
              and (words[r].morph.root or "") in SPEECH]
    for r in roots:
        if r in links or words[r].role != "क्रिया":
            continue
        s = _speech_head(words, r, speech)
        if s is not None and _root_of(words, s) != r:
            links[r] = s
            notes.append(f"{words[r].form}: the words spoken, कर्म of {words[s].form} (1.4.49)")
    links.update(_quoted_links(words, speech))
    for r, h in links.items():
        if _root_of(words, h) != r:  # never a cycle
            words[r] = replace(words[r], head=h)
    return words, notes
