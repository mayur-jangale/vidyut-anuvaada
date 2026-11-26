"""Mapping of ``model.Morph`` to the conventions of the Digital Corpus of Sanskrit (UD-style).

The lakara table and the VerbForm values below were read off the DCS Ramayana files:
Pres+Ind = लट्, Impf+Ind = लङ्, Pres+Imp = लोट्, Pres+Opt = विधिलिङ्, Fut+Ind = लृट् (and the
periphrastic लुट्, marked there only by Formation=peri), Fut+Cond = लृङ्, Past+Ind = लिट् and लुङ् (told
apart only by Formation=...), Past+Jus = the injunctive, Past+Prec = आशीर्लिङ्, Pres+Sub = लेट्.
Participles carry VerbForm=Part (Tense=Pres for शतृ/शानच्; क्त/क्तवतु no Tense), gerundives
VerbForm=Gdv, absolutives VerbForm=Conv, infinitives VerbForm=Inf. DCS lemmatises participles and
the other verbal nouns under upasarga + root, e.g. निरतम् -> निरम्.
"""

from __future__ import annotations

from mayur import terms
from mayur.model import Morph

TAG_FEATS = ("Case", "Gender", "Number", "Person", "Tense", "Mood", "VerbForm")

LAKARA_TENSE_MOOD = {
    "लट्": ("Pres", "Ind"), "लङ्": ("Impf", "Ind"), "लोट्": ("Pres", "Imp"), "विधिलिङ्": ("Pres", "Opt"),
    "लृट्": ("Fut", "Ind"), "लुट्": ("Fut", "Ind"), "लिट्": ("Past", "Ind"), "लुङ्": ("Past", "Ind"),
    "लृङ्": ("Fut", "Cond"), "आशीर्लिङ्": ("Past", "Prec"), "लेट्": ("Pres", "Sub"),
}
PARTICIPLE_TENSE = {"शतृ": "Pres", "शानच्": "Pres", "क्वसु": "Past", "कानच्": "Past"}
GERUNDIVE_KRT = frozenset({"तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्"})
VERBFORM_OF_NONFINITE = {"क्त्वा": "Conv", "ल्यप्": "Conv", "तुमुन्": "Inf"}

# Lemmas that vidyut and DCS write differently: vidyut -> DCS.
LEMMA_EQUIVALENCE = {"किम्": "क", "अस्मद्": "मद्", "युष्मद्": "त्वद्"}


def is_verbal_noun(m: Morph) -> bool:
    krt = m.krt or ""
    return bool(m.root) and (krt in terms.PARTICIPLE_KRT or krt in terms.NONFINITE_KRT)


def lemma(m: Morph) -> str:
    """DCS lemma: upasargas + root for verbal forms and participles, else the stem."""
    if m.kind == "tinanta" or is_verbal_noun(m):
        base = "".join(m.prefixes) + (m.root or m.lemma)
        return base
    base = m.stem or m.lemma
    return LEMMA_EQUIVALENCE.get(base, base)


def feats(m: Morph) -> dict[str, str]:
    """DCS features of ``m`` (only those that apply)."""
    out: dict[str, str] = {}
    if m.kind == "stem":
        return {"Case": "Cpd"}
    krt = m.krt or ""
    if m.kind == "tinanta" and m.lakara in LAKARA_TENSE_MOOD:
        out["Tense"], out["Mood"] = LAKARA_TENSE_MOOD[m.lakara]
        if m.purusha in terms.UD_PERSON:
            out["Person"] = terms.UD_PERSON[m.purusha]
        if m.vacana in terms.UD_NUMBER:
            out["Number"] = terms.UD_NUMBER[m.vacana]
        return out
    if m.root and krt in VERBFORM_OF_NONFINITE:
        return {"VerbForm": VERBFORM_OF_NONFINITE[krt]}
    if m.root and krt in terms.PARTICIPLE_KRT:
        if krt in GERUNDIVE_KRT:
            out["VerbForm"] = "Gdv"
        else:
            out["VerbForm"] = "Part"
            if krt in PARTICIPLE_TENSE:
                out["Tense"] = PARTICIPLE_TENSE[krt]
    for key, value, table in (("Case", m.vibhakti, terms.UD_CASE), ("Gender", m.linga, terms.UD_GENDER),
                              ("Number", m.vacana, terms.UD_NUMBER)):
        if value in table:
            out[key] = table[value]
    return out


def upos(m: Morph) -> str:
    if m.kind == "tinanta" or is_verbal_noun(m):
        return "VERB"
    return {"avyaya": "ADV", "stem": "NOUN"}.get(m.kind, "NOUN")


def tag_key(lemma_: str, upos_: str, feats_: dict[str, str]) -> str:
    """Key of mayur's form_tags table: ``lemma|UPOS|Case=..|Gender=..`` with sorted features."""
    parts = [f"{k}={feats_[k]}" for k in sorted(TAG_FEATS) if feats_.get(k)]
    return "|".join([lemma_, upos_, *parts])


def parse_tag_key(key: str) -> tuple[str, str, dict[str, str]]:
    lemma_, upos_, *rest = key.split("|")
    return lemma_, upos_, dict(p.split("=", 1) for p in rest)


def feats_agree(ours: dict[str, str], theirs: dict[str, str]) -> bool:
    """Every feature we assert is the corpus value (features we do not assert are ignored)."""
    return all(theirs.get(k) == v for k, v in ours.items() if k in TAG_FEATS)
