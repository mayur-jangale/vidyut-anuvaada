"""A Reading built from a reference file's own words (gold split, lemma, feats), for evaluating the
sentence layer alone: each word gets the one lexicon analysis that matches the gold feats, or a Morph
built from the feats when the lexicon has none."""

from __future__ import annotations

from typing import Any, Optional

from mayur.model import Morph, Reading, Word
from mayur.terms import UD_CASE, UD_GENDER, UD_NUMBER, UD_PERSON

_REV = {name: {v: k for k, v in table.items()} for name, table in
        (("Case", UD_CASE), ("Gender", UD_GENDER), ("Number", UD_NUMBER), ("Person", UD_PERSON))}
_ATTR = {"Case": "vibhakti", "Gender": "linga", "Number": "vacana", "Person": "purusha"}
INDECLINABLE = {"ADV", "PART", "CONJ", "CCONJ", "SCONJ", "ADP", "INTJ"}
LAKARA = {"Pres": "लट्", "Impf": "लङ्", "Past": "लिट्", "Fut": "लृट्", "Aor": "लुङ्"}
MOOD = {"Imp": "लोट्", "Opt": "विधिलिङ्", "Cond": "लृङ्"}


def _want(feats: dict[str, str]) -> dict[str, str]:
    return {_ATTR[k]: _REV[k][v] for k, v in feats.items() if k in _ATTR and v in _REV[k]}


def _form_kind(word: dict[str, Any]) -> str:
    vf, upos = word["feats"].get("VerbForm"), word.get("upos", "")
    if word.get("compound_member"):
        return "stem"
    if vf in ("Conv", "Inf") or upos in INDECLINABLE:
        return "avyaya"
    if upos == "VERB" and vf is None and "Person" in word["feats"]:
        return "tinanta"
    return "subanta"


def _fits(m: Morph, word: dict[str, Any]) -> bool:
    kind = _form_kind(word)
    if m.kind != kind and not (kind == "stem" and m.kind in ("stem", "subanta")):
        return False
    feats = word["feats"]
    if any(getattr(m, attr) != val for attr, val in _want(feats).items()):
        return False
    vf = feats.get("VerbForm")
    if vf == "Conv" and m.krt not in ("क्त्वा", "ल्यप्"):
        return False
    if vf == "Inf" and m.krt != "तुमुन्":
        return False
    if vf in ("Part", "Gdv") and not m.krt:
        return False
    if feats.get("Voice") == "Pass" and kind == "tinanta" and m.prayoga != "कर्मणि":
        return False
    return True


def _lemma_score(m: Morph, lemma: str) -> int:
    names = {m.lemma, m.root or "", m.stem, (m.lemma or "").split("-")[-1]}
    return int(lemma in names or lemma.endswith(m.root or "\0"))


def from_feats(word: dict[str, Any]) -> Morph:
    """A Morph from the gold feats alone (used when no lexicon analysis matches)."""
    feats, lemma, form, kind = word["feats"], word.get("lemma", ""), word["form"], _form_kind(word)
    want = _want(feats)
    vf = feats.get("VerbForm")
    if kind == "tinanta":
        return Morph(form=form, lemma=lemma, kind=kind, root=lemma, purusha=want.get("purusha"),
                     vacana=want.get("vacana"), lakara=MOOD.get(feats.get("Mood", "")) or LAKARA.get(feats.get("Tense", "")),
                     prayoga="कर्मणि" if feats.get("Voice") == "Pass" else "कर्तरि", source="none")
    if kind == "avyaya":
        krt = {"Conv": "ल्यप्" if "-" in lemma else "क्त्वा", "Inf": "तुमुन्"}.get(vf or "")
        return Morph(form=form, lemma=lemma, kind=kind, krt=krt, root=lemma if krt else None, source="none")
    if kind == "stem":
        return Morph(form=form, lemma=lemma or form, kind="stem", source="none")
    krt = None
    if vf == "Part":
        past = feats.get("Tense") == "Past"
        krt = ("क्तवतु" if "वत्" in form or "वन्" in form or "वान्" in form else "क्त") if past else "शतृ"
    elif vf == "Gdv":
        krt = "तव्य"
    return Morph(form=form, lemma=lemma, kind="subanta", vibhakti=want.get("vibhakti"), linga=want.get("linga"),
                 vacana=want.get("vacana"), krt=krt, root=lemma if krt else None, source="none")


def gold_morph(word: dict[str, Any], analyses: list[Morph]) -> tuple[Morph, bool]:
    """(the analysis matching the gold feats, True) or (a Morph built from the feats, False)."""
    fits = [m for m in analyses if _fits(m, word)]
    if not fits:
        return from_feats(word), False
    return max(fits, key=lambda m: (_lemma_score(m, word.get("lemma", "")), m.quality)), True


def reading_of(verse: dict[str, Any], lexicon: Optional[Any] = None) -> tuple[Reading, int]:
    """(Reading of the verse's gold words, number of words that needed a Morph built from feats)."""
    if lexicon is None:
        from mayur import lexicon as lex
        lexicon = lex
    words, built = [], 0
    for k, w in enumerate(sorted(verse["words"], key=lambda x: x["index"])):
        form, member = w["form"], bool(w.get("compound_member"))
        try:
            analyses = list(lexicon.stems(form) if member else lexicon.padas(form))
        except Exception:  # an unanalysable form: fall back to the feats
            analyses = []
        m, found = gold_morph(w, analyses)
        built += not found
        words.append(Word(form=form, line=w.get("line", 0), start=k, end=k + 1, in_compound=member, analyses=[m]))
    return Reading(words=words), built
