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
# चानश् (3.2.129 ताच्छील्यवयोवचनशक्तिषु चानश्) has the form of शानच् on any root (मार्गमाण, काङ्क्षमाण);
# the corpus tags it as the present participle
CANASH = "चानश्"
PARTICIPLE_TENSE = {"शतृ": "Pres", "शानच्": "Pres", CANASH: "Pres", "क्वसु": "Past", "कानच्": "Past"}
PAST_PARTICIPLE_KRT = frozenset({"क्त", "क्तवतु"})
GERUNDIVE_KRT = frozenset({"तव्य", "अनीयर्", "यत्", "ण्यत्", "क्यप्"})
VERBFORM_OF_NONFINITE = {"क्त्वा": "Conv", "ल्यप्": "Conv", "तुमुन्": "Inf"}

# Lemmas that vidyut and DCS write differently: vidyut -> DCS.
LEMMA_EQUIVALENCE = {"किम्": "क", "अस्मद्": "मद्", "युष्मद्": "त्वद्", "उभ": "उभ्"}  # DCS cites the dual उभ as उभ्
# DCS cites the feminine of some pronouns under its own stem (ताम्, तया -> ता)
FEMININE_PRONOUN = {"तद्": "ता", "यद्": "या", "एतद्": "एता"}
# 3.4.83 विदो लटो वा, 3.4.84 ब्रुवः पञ्चानामादित आहो ब्रुवः: present tense with perfect endings, which
# the corpus tags as Tense=Past (वेद, विदुः; आह, आत्थ)
_PERFECT_ENDING_PRESENT = (("विद्", ("वेद", "वेत्थ", "विदुस्", "विदतुस्", "विदथुस्", "विद", "विद्व", "विद्म")),
                           ("अह्", ("आह", "आहतुस्", "आहुस्", "आत्थ", "आहथुस्")))
_CLASS_NASAL = {"क": "ङ्", "ख": "ङ्", "ग": "ङ्", "घ": "ङ्", "च": "ञ्", "छ": "ञ्", "ज": "ञ्", "झ": "ञ्",
                "ट": "ण्", "ठ": "ण्", "ड": "ण्", "ढ": "ण्", "त": "न्", "थ": "न्", "द": "न्", "ध": "न्",
                "प": "म्", "फ": "म्", "ब": "म्", "भ": "म्", "म": "म्"}  # (संमन् = सम्मन्: the corpus has both)


def is_verbal_noun(m: Morph) -> bool:
    krt = m.krt or ""
    return bool(m.root) and (krt in terms.PARTICIPLE_KRT or krt in terms.NONFINITE_KRT or krt == CANASH)


# DCS word classes that are indeclinable: any case/number tag on them is ignored, and DCS often
# cites the word itself as the lemma (भृशम्, शनैस्) where grammar sees a case form of a stem.
INDECLINABLE_UPOS = frozenset({"ADV", "PART", "CCONJ", "SCONJ", "INTJ", "ADP"})


def lemma(m: Morph) -> str:
    """DCS lemma: upasargas joined to the root for verbal forms and participles, else the stem."""
    if m.kind == "tinanta" or is_verbal_noun(m):
        from mayur import lexicon  # lazy: lexicon -> freq -> ud

        return lexicon.verbal_lemma(m)
    base = m.stem or m.lemma
    return LEMMA_EQUIVALENCE.get(base, base)


def canonical_lemma(text: str) -> str:
    """One spelling for citation variants: DCS cites some -मत्/-वत्/-अत् stems in their strong
    form (हनुमन्त्, हिमवन्त्, विवस्वन्त्); a final visarga-sound is written स्."""
    if "ं" in text[:-1]:  # 8.4.59 वा पदान्तस्य: anusvara before a stop is also written as the class nasal
        text = "".join(_CLASS_NASAL.get(text[i + 1], ch) if ch == "ं" and i + 1 < len(text) else ch
                       for i, ch in enumerate(text))
    text = text.replace("ॄ", "ृ")  # the corpus cites most roots in long ॠ with the short vowel (तृ, कृ), a few not
    if text.endswith("न्त्"):
        return text[: -len("न्त्")] + "त्"
    if text.endswith("क्षण्"):  # the corpus cites क्षणु हिंसायाम् (क्षत, विक्षत) as क्षन्
        return text[: -len("ण्")] + "न्"
    if text.endswith(("ः", "र्")):
        return text[:-1 if text.endswith("ः") else -2] + "स्"
    return text


def _feminine_of(ours: str, gold: str) -> bool:
    """Our lemma is the feminine stem (सुमुखी, आत्मिका) of the stem the corpus cites (सुमुख, आत्मक)."""
    if len(ours) < 2 or ours[-1] not in ("ी", "ा"):
        return False
    base = ours[:-1]
    if ours[-1] == "ी" and gold == base + "्":  # सुदती of सुदत्, बलवती of बलवत् (4.1.5, 4.1.6)
        return True
    return gold == base or (ours[-1] == "ा" and len(base) > 2 and base[-2] == "ि" and gold == base[:-2] + base[-1])


def same_lemma(m: Morph, gold_lemma: str, gold_upos: str = "") -> bool:
    """Our analysis names the same lexeme as the gold lemma, under the conventions above."""
    want, ours = canonical_lemma(gold_lemma), canonical_lemma(lemma(m))
    if ours == want or _feminine_of(ours, want) or _citation_variant(m, ours, want) or _causative_citation(ours, want):
        return True
    if (m.kind == "tinanta" or is_verbal_noun(m)) and _causative_citation(want, ours):
        return True  # the other way round: गुम्फित under गुम्फ्, नीनशस् under नश्, where we name the stem in -अय्
    if gold_upos in INDECLINABLE_UPOS:
        word = canonical_lemma(m.form)
        return word == want or (word.endswith("त्") and word[:-2] + "द्" == want)  # 8.2.39: चेत् = चेद्
    return False


def _causative_citation(ours: str, gold: str) -> bool:
    """The corpus cites a causative by its stem in -अय् (निशामय्, पीडय्) where the form at hand is
    built on the root (the absolutives निशम्य, पीड्य): the same lexeme for scoring."""
    if not gold.endswith("य्") or len(gold) < 4:
        return False
    base = gold[:-2]  # without य्: the consonant before अय् now ends the string
    short = base[::-1].replace("ा", "", 1)[::-1]  # निशाम -> निशम (the root's own vowel)
    return ours in (base + "्", short + "्", base + "ि")


def _citation_variant(m: Morph, ours: str, want: str) -> bool:
    """Citation conventions where the corpus names the same lexeme by another stem."""
    if m.linga == "स्त्रीलिङ्ग" and (FEMININE_PRONOUN.get(ours) == want or FEMININE_PRONOUN.get(want) == ours):
        return True  # ताम् under ता or under तद्
    # 1.2.48 गोस्त्रियोरुपसर्जनस्य: a feminine in -आ shortened as the final of a bahuvrīhi (शुभ्र-प्रभम्)
    if m.kind == "subanta" and m.linga != "स्त्रीलिङ्ग" and want == ours + "ा":
        return True
    if m.krt == "शतृ" and ours == "अस्" and want == "सत्":
        return True  # सन्, सन्तः: the participle of अस्, which the corpus also cites as the adjective सत्
    if (m.kind == "tinanta" or m.root) and ours.endswith("धु") and want == ours[:-1] + "ू":
        return True  # धुञ् / धूञ् कम्पने: one root with a short and a long vowel (धुनोति, धूनोति)
    # 7.3.78: पश्य is the present-system substitute of दृश्; the corpus cites it under either root
    return (m.kind == "tinanta" or is_verbal_noun(m)) and ours.endswith("पश्") and want == ours[:-3] + "दृश्"


def compared_features(gold_upos: str, gold_feats: dict[str, str]) -> tuple[str, ...]:
    """The gold features that are scored for a word of this class (none for indeclinables)."""
    if gold_upos in INDECLINABLE_UPOS:
        return ()
    return tuple(k for k in TAG_FEATS if k in gold_feats)


def same_feats(m: Morph, gold_upos: str, gold_feats: dict[str, str]) -> bool:
    """Every feature the gold annotates for this word agrees with ours.

    Features the gold leaves out cannot be scored (it gives the personal pronouns no gender);
    for indeclinable gold words there is nothing to score.
    """
    if gold_upos in INDECLINABLE_UPOS:
        return True
    ours = feats(m)
    if gold_feats.get("VerbForm") == "Part" and gold_feats.get("Tense") == "Past" and m.krt in PAST_PARTICIPLE_KRT:
        ours = {**ours, "Tense": "Past"}  # the corpus marks the tense of क्त only now and then
    if gold_feats.get("Tense") == "Past" and ours.get("Tense") == "Pres" and perfect_ending_present(m):
        ours = {**ours, "Tense": "Past"}
    if gold_feats.get("Mood") == "Jus" and m.kind == "tinanta" and m.lakara in ("लुङ्", "लङ्") and m.form[:1] != "अ":
        ours = {**ours, "Mood": "Jus"}  # the injunctive: an aorist or imperfect without its augment (मा भूत्, 6.4.74)
    return all(ours.get(k) == v for k, v in gold_feats.items() if k in TAG_FEATS)


def perfect_ending_present(m: Morph) -> bool:
    """A लट् form of विद् or ब्रू with perfect endings (3.4.83, 3.4.84)."""
    if m.kind != "tinanta" or m.lakara != "लट्":
        return False
    root = lemma(m)
    form = m.form.replace("आ", "ा") if m.form[:1] != "आ" else m.form  # प्राह: the आ after an upasarga
    return any((root.endswith(r) or root.endswith(r.replace("अ", "ा"))) and
               (m.form.endswith(ends) or form.endswith(tuple(e.replace("आ", "ा") for e in ends)))
               for r, ends in _PERFECT_ENDING_PRESENT)


def _future_participle(m: Morph) -> bool:
    """भविष्यत्, करिष्यमाण: शतृ / शानच् in place of लृट् (3.3.14 लृटः सद्वा), as the kosha entry records it."""
    entry = getattr(m.handle, "pratipadika_entry", None)
    return str(getattr(entry, "lakara", "")) == "lf~w"


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
    if m.root and (krt in terms.PARTICIPLE_KRT or krt == CANASH):
        if krt in GERUNDIVE_KRT:
            out["VerbForm"] = "Gdv"
        else:
            out["VerbForm"] = "Part"
            if krt in PARTICIPLE_TENSE:
                out["Tense"] = "Fut" if _future_participle(m) else PARTICIPLE_TENSE[krt]
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
    """Every feature we assert is the corpus value.

    Features we do not assert are ignored, and so are features the corpus leaves out
    (it tags the personal pronouns without gender).
    """
    return all(theirs.get(k, v) == v for k, v in ours.items() if k in TAG_FEATS)
