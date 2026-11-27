"""मा: the prohibitive particle, or the enclitic that stands for माम् (8.1.23 त्वामौ द्वितीयायाः).

The two are the same letters; the rules that tell them apart are checked on the reading:

* First in its half-verse it is the particle: an enclitic never stands first (8.1.18 अनुदात्तं सर्वमपादादौ).
* With the augmentless aorist it is the particle (3.3.175 माङि लुङ्); of two (मा मा हिंसीः) the second is
  the pronoun.
* With a verb that is neither aorist, imperative nor optative (स मा पश्यति) a prohibition is not
  formed, so it is the pronoun.
* With an imperative or optative both are in use (मा गच्छ; असतो मा सद् गमय). The pronoun is taken only
  where मा stands after another word and is parted from the verb by an inflected word, and the verb
  can take it as its object: a causative (1.4.52: the one made to go is कर्म), or a verb with no
  other accusative in the half-verse. Elsewhere the tagger's choice stands.

Each change is noted with the other reading; nothing is dropped. All strings Devanagari.
"""

from __future__ import annotations

from typing import Optional, Sequence

from mayur import bridge
from mayur.model import Morph, Word

FORM = "मा"
AORIST = "लुङ्"
MODAL = ("लोट्", "विधिलिङ्", "आशीर्लिङ्")
NOTE_PRONOUN = ("मा is read as the enclitic of माम् (8.1.23): {why}. As the prohibitive particle the line would "
                "mean a prohibition; that reading is not chosen")
NOTE_PARTICLE = "मा is read as the prohibitive particle: {why}"


def _index(word: Word, pronoun: bool) -> Optional[int]:
    for i, m in enumerate(word.analyses):
        if pronoun and m.lemma == "अस्मद्" and m.vibhakti == "द्वितीया":
            return i
        if not pronoun and m.kind == "avyaya" and m.lemma == FORM:
            return i
    return None


def _morph(words: Sequence[Word], chosen: Sequence[int], i: int) -> Optional[Morph]:
    return words[i].analyses[chosen[i]] if words[i].analyses else None


def _decide(words: Sequence[Word], chosen: Sequence[int], i: int, line: list[int]) -> tuple[Optional[bool], str]:
    """(pronoun?, reason); (None, '') where no rule decides."""
    at = line.index(i)
    if at == 0:
        return False, "it stands first in its half-verse, where an enclitic cannot (8.1.18)"
    verb = next((j for j in line[at + 1:] if (_morph(words, chosen, j) or Morph("", "", "")).kind == "tinanta"), None)
    if verb is None:
        return None, ""
    vm = _morph(words, chosen, verb)
    if vm.lakara == AORIST:
        earlier = any(words[j].form == FORM for j in line[:at])
        if earlier:
            return True, "a prohibitive मा already stands before it"
        return False, "the verb is an aorist (3.3.175 माङि लुङ्)"
    if vm.lakara not in MODAL:
        return True, f"a prohibition is not formed with {vm.lakara}"
    between = [j for j in line[at + 1:verb] if (_morph(words, chosen, j) or Morph("", "", "")).kind == "subanta"]
    if not between:
        return None, ""
    accusatives = [j for j in line if j != i and (_morph(words, chosen, j) or Morph("", "", "")).vibhakti == "द्वितीया"]
    if bridge.is_causative(vm):
        return True, "it stands second, apart from the verb, and the causative takes the one made to act as कर्म (1.4.52)"
    if not accusatives:
        return True, "it stands second, apart from the verb, which has no other object"
    return None, ""


def apply(words: Sequence[Word], chosen: Sequence[int]) -> tuple[list[int], list[str]]:
    """``chosen`` with every मा set by the rules above, and a note for each one changed."""
    out, notes = list(chosen), []
    for i, w in enumerate(words):
        if w.form != FORM or w.in_compound or not w.analyses:
            continue
        pronoun, particle = _index(w, True), _index(w, False)
        if pronoun is None or particle is None:
            continue
        line = [j for j, x in enumerate(words) if x.line == w.line and not x.in_compound]
        verdict, why = _decide(words, out, i, line)
        if verdict is None:
            continue
        want = pronoun if verdict else particle
        if out[i] != want:
            out[i] = want
            notes.append((NOTE_PRONOUN if verdict else NOTE_PARTICLE).format(why=why))
    return out, notes
