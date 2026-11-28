"""Proofs that need the sentence: three word forms a rule gives only in a context.

vidyut's Python API derives one word at a time, so it cannot give these; each is proved here in two
steps: vidyut derives the full form, and one rule, whose condition is CHECKED on the reading,
gives the form of the text. Where the condition does not hold the word stays unverified.

* मे, ते, नौ, वाम्, नस्, वस्, मा, त्वा for the full forms of अस्मद् / युष्मद् (8.1.20–23): only after another
  word, never first (8.1.17 पदात्, 8.1.18 अनुदात्तं सर्वमपादादौ). Checked: the word is not the first of its
  half-verse. (The start of the second quarter inside a half-verse is not known here and is not checked.)
* स, एष for सस्, एषस्: before a consonant by 6.1.132 एतत्तदोः सुलोपोऽकोरनञ्समासे हलि, before a vowel other
  than अ by the ordinary 8.3.17 and 8.3.19. Checked: the next word of the half-verse begins so.
* महा- for महत्- as a compound member (6.3.46 आन्महतः समानाधिकरणजातीययोः): only before a final member it
  is co-referent with. Checked: the compound is typed कर्मधारय or बहुव्रीहि.

All strings Devanagari.
"""

from __future__ import annotations

from typing import Optional, Sequence

from mayur import lipi, sandhi
from mayur.model import Compound, SutraStep, Word, WordProof

SOURCE = "अष्टाध्यायी"
# enclitic -> (rule, {(lemma, vibhakti): full form})
_FULL = {
    "मे": ("8.1.22", {("अस्मद्", "षष्ठी"): "मम", ("अस्मद्", "चतुर्थी"): "मह्यम्"}),
    "ते": ("8.1.22", {("युष्मद्", "षष्ठी"): "तव", ("युष्मद्", "चतुर्थी"): "तुभ्यम्"}),
    "मा": ("8.1.23", {("अस्मद्", "द्वितीया"): "माम्"}),
    "त्वा": ("8.1.23", {("युष्मद्", "द्वितीया"): "त्वाम्"}),
    "नौ": ("8.1.20", {("अस्मद्", "षष्ठी"): "आवयोस्", ("अस्मद्", "चतुर्थी"): "आवाभ्याम्", ("अस्मद्", "द्वितीया"): "आवाम्"}),
    "वाम्": ("8.1.20", {("युष्मद्", "षष्ठी"): "युवयोस्", ("युष्मद्", "चतुर्थी"): "युवाभ्याम्", ("युष्मद्", "द्वितीया"): "युवाम्"}),
    "नस्": ("8.1.21", {("अस्मद्", "षष्ठी"): "अस्माकम्", ("अस्मद्", "चतुर्थी"): "अस्मभ्यम्", ("अस्मद्", "द्वितीया"): "अस्मान्"}),
    "वस्": ("8.1.21", {("युष्मद्", "षष्ठी"): "युष्माकम्", ("युष्मद्", "चतुर्थी"): "युष्मभ्यम्", ("युष्मद्", "द्वितीया"): "युष्मान्"}),
}
_SU_LOPA = {"स": "सस्", "एष": "एषस्"}
_COREFERENT = ("कर्मधारय", "बहुव्रीहि")


def _full_form_proof(full: str, lemma: str, vibhakti: Optional[str], vacana: Optional[str]) -> Optional[WordProof]:
    """vidyut's proof of the full pada ``full`` in the same case and number."""
    from mayur import lexicon

    for m in lexicon.padas(full):
        if m.lemma == lemma and m.vibhakti == vibhakti and (vacana is None or m.vacana == vacana) and m.source == "kosha":
            proof = lexicon.prove(m)
            if proof.derivable:
                return proof
    return None


def _enclitic(words: Sequence[Word], i: int) -> Optional[WordProof]:
    w = words[i]
    m = w.morph
    rule, table = _FULL[w.form]
    full = table.get((m.lemma, m.vibhakti))
    first = i == 0 or words[i - 1].line != w.line
    if full is None or first:
        return None  # another case than the rule allows, or at the start of the half-verse (8.1.18)
    inner = _full_form_proof(full, m.lemma, m.vibhakti, m.vacana)
    if inner is None:
        return None
    step = SutraStep(SOURCE, rule, w.form)
    return WordProof(derivable=True, method=f"vidyut-prakriya (full form) + {rule}", derived_form=w.form,
                     trace=[*inner.trace, step],
                     note=f"vidyut derives {lipi.pausa(full)}; after another word and not at the start of the "
                          f"half-verse (8.1.17, 8.1.18), {rule} puts {lipi.pausa(w.form)} in its place")


def _su_lopa(words: Sequence[Word], i: int) -> Optional[WordProof]:
    w = words[i]
    nxt = words[i + 1] if i + 1 < len(words) and words[i + 1].line == w.line else None
    if nxt is None or not nxt.form:
        return None  # in pausa the text has सः
    first = lipi.varnas(nxt.form)[0]
    if first == "अ":
        return None  # before अ the text has सो ऽ (6.1.113, 6.1.109)
    full = _SU_LOPA[w.form]
    inner = _full_form_proof(full, w.morph.lemma, "प्रथमा", "एकवचन")
    if inner is None:
        return None
    if sandhi.is_vowel(first):  # स इच्छति: the ordinary loss of the visarga before a vowel
        rule, why = "8.3.17, 8.3.19", "its final is elided (8.3.17 भोभगोअघोअपूर्वस्य योऽशि, 8.3.19 लोपः शाकल्यस्य)"
    else:
        rule, why = "6.1.132", "its सु is elided (6.1.132 एतत्तदोः सुलोपोऽकोरनञ्समासे हलि)"
    steps = [SutraStep(SOURCE, code.strip(), w.form) for code in rule.split(",")]
    return WordProof(derivable=True, method=f"vidyut-prakriya (full form) + {rule}", derived_form=w.form,
                     trace=[*inner.trace, *steps],
                     note=f"vidyut derives {lipi.pausa(full)}; before {lipi.pausa(nxt.form)} {why}")


def _maha(words: Sequence[Word], i: int, compounds: Sequence[Compound], stem_proof: WordProof) -> Optional[WordProof]:
    w = words[i]
    comp = next((c for c in compounds if i in c.members), None)
    if comp is None or not any(t in comp.samasa for t in _COREFERENT) or not stem_proof.trace:
        return None  # 6.3.46 needs a final member महत् is co-referent with
    step = SutraStep(SOURCE, "6.3.46", w.form)
    return WordProof(derivable=True, method="vidyut-prakriya (stem) + 6.3.46", derived_form=w.form,
                     trace=[*stem_proof.trace, step],
                     note=f"vidyut derives the stem महत्; in this {comp.samasa} compound आ takes the place of its "
                          f"final (6.3.46 आन्महतः समानाधिकरणजातीययोः)")


def prove(words: Sequence[Word], i: int, compounds: Sequence[Compound], plain: WordProof) -> Optional[WordProof]:
    """The contextual proof of word ``i`` whose one-word proof ``plain`` failed; None when no rule here applies."""
    w = words[i]
    if w.morph is None:
        return None
    if w.form in _FULL and w.morph.lemma in ("अस्मद्", "युष्मद्") and not w.in_compound:
        return _enclitic(words, i)
    if w.form in _SU_LOPA and w.morph.lemma in ("तद्", "एतद्") and not w.in_compound:
        return _su_lopa(words, i)
    if w.form == "महा" and w.in_compound and w.morph.lemma == "महत्":
        return _maha(words, i, compounds, plain)
    return None
