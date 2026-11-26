"""Readings for syntax tests: from the lexicon, or hand-made Morphs (no vidyut needed)."""

from __future__ import annotations

from typing import Optional

from mayur.model import Morph, Reading, Word

M, F, N = "पुंलिङ्ग", "स्त्रीलिङ्ग", "नपुंसकलिङ्ग"
SG = "एकवचन"


def reading(items: list[tuple[str, bool]]) -> Reading:
    """Words analysed by ``mayur.lexicon`` (stems for non-final compound members)."""
    from mayur import lexicon

    words = []
    for k, (form, in_compound) in enumerate(items):
        analyses = list(lexicon.stems(form) if in_compound else lexicon.padas(form))
        words.append(Word(form=form, line=0, start=k, end=k + 1, in_compound=in_compound, analyses=analyses))
    return Reading(words=words)


def nom(form: str, lemma: str, case: str, linga: Optional[str] = M, vacana: str = SG, krt: Optional[str] = None,
        quality: int = 3, stem: str = "") -> Morph:
    return Morph(form=form, lemma=lemma, kind="subanta", vibhakti=case, linga=linga, vacana=vacana, krt=krt, stem=stem,
                 quality=quality)


def verb(form: str, lemma: str, lakara: str = "लिट्", prayoga: str = "कर्तरि") -> Morph:
    return Morph(form=form, lemma=lemma, kind="tinanta", purusha="प्रथमपुरुष", vacana=SG, lakara=lakara,
                 prayoga=prayoga, root=lemma)


def avyaya(form: str, krt: Optional[str] = None) -> Morph:
    return Morph(form=form, lemma=form, kind="avyaya", krt=krt)


def stem(form: str, linga: Optional[str] = None) -> Morph:
    return Morph(form=form, lemma=form, kind="stem", linga=linga)


def hand(items: list[tuple[str, bool, list[Morph]]]) -> Reading:
    words = [Word(form=f, line=0, start=k, end=k + 1, in_compound=c, analyses=list(a))
             for k, (f, c, a) in enumerate(items)]
    return Reading(words=words)


def verse1() -> Reading:
    """तपस्-स्वाध्याय-निरतम् तपस्वी वाक्-विदाम् वरम् / नारदम् परिपप्रच्छ वाल्मीकिस् मुनि-पुंगवम्"""
    acc, nom1 = "द्वितीया", "प्रथमा"
    return hand([
        ("तपस्", True, [stem("तपस्", N)]),
        ("स्वाध्याय", True, [stem("स्वाध्याय", M)]),
        ("निरतम्", False, [nom("निरतम्", "निरम्", nom1, N, krt="क्त", stem="निरत"), nom("निरतम्", "निरम्", acc, M, krt="क्त", stem="निरत")]),
        ("तपस्वी", False, [nom("तपस्वी", "तपस्विन्", nom1)]),
        ("वाक्", True, [stem("वाच्", F)]),
        ("विदाम्", False, [nom("विदाम्", "विद्", "षष्ठी", M, "बहुवचन")]),
        ("वरम्", False, [nom("वरम्", "वर", nom1, N), nom("वरम्", "वर", acc, M)]),
        ("नारदम्", False, [nom("नारदम्", "नारद", acc)]),
        ("परिपप्रच्छ", False, [verb("परिपप्रच्छ", "परि-प्रच्छ्")]),
        ("वाल्मीकिस्", False, [nom("वाल्मीकिस्", "वाल्मीकि", nom1)]),
        ("मुनि", True, [stem("मुनि", M)]),
        ("पुंगवम्", False, [nom("पुंगवम्", "पुंगव", nom1, N), nom("पुंगवम्", "पुंगव", acc, M)]),
    ])


def verse2() -> Reading:
    """कस् नु अस्मिन् साम्प्रतम् लोके गुणवान् कस् च वीर्यवान् / धर्म-ज्ञस् च कृतज्ञस् च सत्य-वाक्यस् दृढ-व्रतस्"""
    p, loc = "प्रथमा", "सप्तमी"
    return hand([
        ("कस्", False, [nom("कस्", "किम्", p)]),
        ("नु", False, [avyaya("नु")]),
        ("अस्मिन्", False, [nom("अस्मिन्", "इदम्", loc), nom("अस्मिन्", "इदम्", loc, N)]),
        ("साम्प्रतम्", False, [avyaya("साम्प्रतम्")]),
        ("लोके", False, [nom("लोके", "लोक", loc)]),
        ("गुणवान्", False, [nom("गुणवान्", "गुणवत्", p)]),
        ("कस्", False, [nom("कस्", "किम्", p)]),
        ("च", False, [avyaya("च")]),
        ("वीर्यवान्", False, [nom("वीर्यवान्", "वीर्यवत्", p)]),
        ("धर्म", True, [stem("धर्म", M)]),
        ("ज्ञस्", False, [nom("ज्ञस्", "ज्ञ", p)]),
        ("च", False, [avyaya("च")]),
        ("कृतज्ञस्", False, [nom("कृतज्ञस्", "कृतज्ञ", p)]),
        ("च", False, [avyaya("च")]),
        ("सत्य", True, [stem("सत्य", N)]),
        ("वाक्यस्", False, [nom("वाक्यस्", "वाक्य", p)]),
        ("दृढ", True, [stem("दृढ")]),
        ("व्रतस्", False, [nom("व्रतस्", "व्रत", p)]),
    ])


def shveta() -> tuple[Reading, Reading]:
    """श्वेतस् धावति  vs  श्वा इतस् धावति"""
    dhav = verb("धावति", "धाव्", "लट्")
    a = hand([("श्वेतस्", False, [nom("श्वेतस्", "श्वेत", "प्रथमा")]), ("धावति", False, [dhav])])
    b = hand([("श्वा", False, [nom("श्वा", "श्वन्", "प्रथमा")]), ("इतस्", False, [avyaya("इतस्")]),
              ("धावति", False, [dhav])])
    return a, b


def gold_reading(number: int) -> Reading:
    """Verse ``number`` of the sarga split as in the gold file, analysed by the lexicon."""
    from mayur import gold, lexicon

    words = []
    for li, line in enumerate(gold.load()["verses"][number - 1]["lines"]):
        for k, g in enumerate(line["words"]):
            c = g["compound_member"]
            words.append(Word(form=g["form"], line=li, start=k, end=k + 1, in_compound=c,
                              analyses=list(lexicon.stems(g["form"]) if c else lexicon.padas(g["form"]))))
    return Reading(words=words)
