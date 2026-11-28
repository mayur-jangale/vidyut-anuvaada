"""One finite verb to a sentence: किम् अकुर्वत सञ्जय.

A half-verse with two finite verbs and nothing that joins two clauses (वा, इति, a relative, च after a verb)
is one sentence with one verb too many (एकतिङ् वाक्यम्, the vārttika on 2.1.1). Where one of the two
is also the vocative of a listed stem (सञ्जय: the name, or the imperative of सम् + जि), the vocative
is taken: an address needs no place in the syntax. The verb standing later is tried first. The
vocative must be one the corpus knows (not पश्य "O seeing" in एहि पश्य).

The other way round, a half-verse without a finite verb: a word read as an oblique participle (जयते "to the
conquering one") that is also a labelled finite form of the same root, agreeing with a nominative, is that
verb (सत्यम् एव जयते). The reading not taken is named in the notes; nothing is dropped. All strings Devanagari.
"""

from __future__ import annotations

from typing import Optional, Sequence

from mayur.model import Word

JOINERS = frozenset({"वा", "इति", "यदि", "चेद्", "चेत्", "यदा", "यावत्", "यथा", "यत्र", "अथवा", "किंवा"})
AFTER_VERB = frozenset({"च", "अपि", "तु"})  # गच्छति पश्यति च: joins two verbs only when it stands right after one
RELATIVE = "यद्"
VOCATIVE_MIN = 5  # occurrences of the stem in the corpus
DATIVE_WORDS = frozenset({"नमस्", "स्वस्ति", "स्वाहा", "स्वधा", "अलम्", "वषट्"})
NOTE = ("{form} is read as a vocative: its half-verse already has the finite verb {verb} and nothing joins two "
        "clauses. As a verb form it would be {lemma} ({lakara}); that reading is not chosen")
VERB_NOTE = ("{form} is read as the finite verb of {subject} ({lakara}, labelled ārṣa: see its proof), not as a case "
             "form of the participle of the same root: the half-verse has no other verb")


def _vocative(word: Word) -> Optional[int]:
    """A vocative singular of a listed stem that the corpus knows as a noun (सञ्जय; not पश्य "O seeing")."""
    from mayur import freq

    for i, m in enumerate(word.analyses):
        if m.kind == "subanta" and m.vibhakti == "सम्बोधन" and m.vacana == "एकवचन" and m.quality >= 2 and not m.krt \
                and freq.lemma_class(m.lemma) == "noun" and (freq.lemma_count(m.lemma) or 0) >= VOCATIVE_MIN:
            return i
    return None


def _joined(words: Sequence[Word], chosen: Sequence[int], line: list[int], finite: list[int]) -> bool:
    for at, j in enumerate(line):
        m = words[j].analyses[chosen[j]] if words[j].analyses else None
        if words[j].form in JOINERS or (m is not None and m.lemma == RELATIVE):
            return True
        if words[j].form in AFTER_VERB and at > 0 and line[at - 1] in finite:
            return True
    return False


def _labelled_verb(words: Sequence[Word], chosen: Sequence[int], line: list[int]) -> Optional[tuple[int, int, int]]:
    """(word, analysis, subject): a word read as an oblique participle that is also a labelled finite form of
    the same root agreeing with a nominative of the half-verse (सत्यम् एव जयते)."""
    from mayur.shabdabodha import karta_agrees

    if any(words[i].form in DATIVE_WORDS for i in line):
        return None  # गच्छते नमस्: the dative has its governor (2.3.16 नमःस्वस्तिस्वाहास्वधालंवषड्योगाच्च)
    for j in line:
        now = words[j].analyses[chosen[j]]
        if now.krt not in ("शतृ", "शानच्") or now.vibhakti in (None, "प्रथमा"):
            continue
        if any(i != j and words[i].analyses[chosen[i]].vibhakti == now.vibhakti for i in line):
            continue  # रामाय जयते: the participle has a noun in its own case
        for k, m in enumerate(words[j].analyses):
            if m.kind != "tinanta" or m.source != "arsha" or m.root != now.root:
                continue
            subject = next((i for i in line if i != j and karta_agrees(words[i].analyses[chosen[i]], m)), None)
            if subject is not None:
                return j, k, subject
    return None


def apply(words: Sequence[Word], chosen: Sequence[int]) -> tuple[list[int], list[str]]:
    """``chosen`` with a second finite verb of an unjoined half-verse turned into its vocative reading."""
    out, notes = list(chosen), []
    for line_no in sorted({w.line for w in words}):
        line = [j for j, w in enumerate(words) if w.line == line_no and not w.in_compound and w.analyses]
        finite = [j for j in line if words[j].analyses[out[j]].kind == "tinanta"]
        if not finite:
            found = _labelled_verb(words, out, line)
            if found is not None:
                j, k, subject = found
                out[j] = k
                notes.append(VERB_NOTE.format(form=words[j].form, subject=words[subject].form,
                                              lakara=words[j].analyses[k].lakara))
            continue
        if len(finite) != 2 or words[finite[0]].form == words[finite[1]].form or _joined(words, out, line, finite):
            continue
        for j in reversed(finite):
            k = _vocative(words[j])
            at = line.index(j)
            object_before = at > 0 and words[line[at - 1]].analyses[out[line[at - 1]]].vibhakti == "द्वितीया"
            if k is None or j not in (line[0], line[-1]) or object_before:
                continue  # an address stands at the edge of the half-verse; शत्रून् जय keeps its verb
            other = next(v for v in finite if v != j)
            old = words[j].analyses[out[j]]
            out[j] = k
            notes.append(NOTE.format(form=words[j].form, verb=words[other].form, lemma=old.lemma, lakara=old.lakara))
            break
    return out, notes
