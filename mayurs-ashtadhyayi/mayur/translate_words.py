"""Small word-level facts used by the template renderer (pure, English side only)."""

from __future__ import annotations

import re

MOTION = frozenset({"go", "come", "return", "travel", "walk", "run", "flee", "hasten", "proceed", "fly", "march",
                    "depart", "wander", "roam", "set out", "retire", "enter into"})
WITH_WORDS = frozenset({"with", "without", "together with", "along with", "except", "besides", "beyond"})
_LATIN = re.compile(r"^[A-Z][a-z]+(?:a|us|um|is|ia|ium|ea|ex|on|ii|ae) [A-Za-z]+(?: [A-Z][\w.]*)?$")
_LATIN_MARKS = ("Linn", "Roxb", "Willd", "Hemandifolia", "Sp.", "L.)")
_QUESTION = frozenset({"किम्", "क", "कः", "कस्"})

ADJ_FIRST = {"great", "good", "firm", "long", "big", "small", "excellent", "best", "white", "black",
              "red", "very", "many", "beautiful", "noble", "mighty", "strong", "high", "broad", "large"}
# final member of a compound -> (English head placed before its members, joiner, plural members)
FINAL = {
    "निरत": ("devoted to", " and ", False), "रत": ("delighted in", " and ", False),
    "वर": ("best of", " and ", True), "पुंगव": ("best of", " and ", True), "श्रेष्ठ": ("best of", " and ", True),
    "उत्तम": ("best of", " and ", True), "सम्पन्न": ("endowed with", " and ", False),
    "संपन्न": ("endowed with", " and ", False), "युक्त": ("endowed with", " and ", False),
    "उपेत": ("endowed with", " and ", False), "वर्धन": ("increaser of", " and ", False),
    "सदृश": ("like", " and ", False), "सम": ("equal to", " and ", False),
    "प्रभव": ("born of", "-", False), "तुल्य": ("equal to", " and ", False),
}
PAIRED = {"arm", "eye", "hand", "shoulder", "ear", "foot", "tooth", "leg", "thigh", "cheek"}



ADJ_ENDINGS = ("ed", "ful", "ous", "ive", "less", "ish", "like")

TIME_PHRASES = {"morning": "in the morning", "evening": "in the evening", "night": "at night", "noon": "at noon",
                "dawn": "at dawn", "midday": "at midday", "midnight": "at midnight"}
TO_OBJECT = frozenset({"say", "speak", "bow", "talk"})  # take their person with "to" in English
WITH_LEMMAS = frozenset({"सह", "सार्धम्", "साकम्", "विना", "समम्"})
ADJ_SENSE = {"Krishna": "black", "Kṛṣṇa": "black"}  # a name-gloss that is the colour when it is a predicate of a common noun

ON_NOUNS = frozenset({"bank", "shore", "top", "surface", "peak", "summit", "ground", "roof", "hill", "mountain"})
NOMINAL_SUFFIXES = {"ness": "ness", "hood": "hood", "ship": "ship"}  # तद्धित -ता / -त्व / -त्वम्


def adverb(adjective: str) -> str:
    """quick -> quickly, happy -> happily, gentle -> gently; a word already in -ly stays."""
    if adjective.endswith("ly") or " " in adjective:
        return adjective
    if adjective.endswith("y"):
        return adjective[:-1] + "ily"
    return adjective[:-1] + "y" if adjective.endswith("le") else adjective + "ly"


def is_latin_binomial(gloss: str) -> bool:
    """A botanical or zoological name ("Bombax ceiba Linn") is not an English meaning."""
    return bool(gloss) and (any(m in gloss for m in _LATIN_MARKS) or bool(_LATIN.match(gloss)))


def is_motion(verb_gloss: str) -> bool:
    words = verb_gloss.lower().split()
    return bool(words) and (words[0] in MOTION or " ".join(words[:2]) in MOTION)


def is_question_lemma(lemma: str) -> bool:
    return lemma in _QUESTION


def name_plural(gloss: str) -> str:
    """Plural of a capitalised name or people-name: Pāṇḍava -> Pāṇḍavas (never doubled)."""
    return gloss if gloss.endswith("s") else gloss + "s"
