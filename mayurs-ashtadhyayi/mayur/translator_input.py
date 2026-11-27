"""The simplified-Sanskrit input of the trained translator.

The rule engine undoes sandhi, splits compounds, and gives every word its stem, its grammar and
its gloss; this module writes that analysis as a flat list of tokens (words and atomic tags).
The same function builds the input when the translator is trained and when it is used.

Form "A": per word the stem (Devanagari) and a compact grammar tag, in text order.
Form "B": form A with the engine's English gloss of each word added after the tag.

A non-final compound member is the stem followed by the tag ``<C>``. A half-verse ends with
``<L>``. A tag is one token: ``N3pm`` is a noun in the instrumental (3) plural (p) masculine (m),
``V.lat.3s`` a finite verb (present, third person singular), ``<AV>`` an indeclinable, ``<UNK>``
a word the engine could not analyse; ``K.क्त`` follows the tag of a participle or other krdanta.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional

from mayur.model import Morph, Reading, Word

FORMS = ("A", "B")
LINE_END = "<L>"
MEMBER = "<C>"
CASES = {"प्रथमा": "1", "द्वितीया": "2", "तृतीया": "3", "चतुर्थी": "4", "पञ्चमी": "5", "षष्ठी": "6",
         "सप्तमी": "7", "सम्बोधन": "8"}
NUMBERS = {"एकवचन": "s", "द्विवचन": "d", "बहुवचन": "p"}
GENDERS = {"पुंलिङ्ग": "m", "स्त्रीलिङ्ग": "f", "नपुंसकलिङ्ग": "n"}
PERSONS = {"प्रथमपुरुष": "3", "मध्यमपुरुष": "2", "उत्तमपुरुष": "1"}
TENSES = {"लट्": "lat", "लिट्": "lit", "लुट्": "lut", "लृट्": "lrt", "लोट्": "lot", "लङ्": "lan",
          "विधिलिङ्": "vidhi", "आशीर्लिङ्": "ashir", "लुङ्": "lun", "लृङ्": "lrn"}
VOICES = {"कर्मणि": ".pas", "भावे": ".bha"}
_GLOSS_WORD = re.compile(r"[A-Za-zāīūṛṭḍśṣṇñṅ'\-]+")
MAX_GLOSS_WORDS = 3


def tag_of(m: Optional[Morph]) -> str:
    """The compact grammar tag (one token) of an analysis."""
    if m is None or m.kind in ("unknown", "stem"):
        return "<UNK>"
    if m.kind == "avyaya":
        return "<AV>"
    if m.kind == "tinanta":
        tense = TENSES.get(m.lakara or "", "x")
        person = PERSONS.get(m.purusha or "", "x") + NUMBERS.get(m.vacana or "", "x")
        return f"V.{tense}.{person}{VOICES.get(m.prayoga or '', '')}"
    case = CASES.get(m.vibhakti or "", "x")
    return f"N{case}{NUMBERS.get(m.vacana or '', 'x')}{GENDERS.get(m.linga or '', 'x')}"


def stem_of(w: Word) -> str:
    """The word's stem (a krdanta's own stem, else its lemma); the written form when unanalysed."""
    m = w.morph
    if m is None or m.kind in ("unknown",):
        return w.form
    if w.in_compound:
        return m.stem or m.lemma or w.form
    if m.kind in ("tinanta", "avyaya"):  # an absolutive's lemma is its root (श्रुत्वा: श्रु), not the form
        return m.lemma or w.form
    return m.stem or m.lemma or w.form


def gloss_tokens(text: str) -> list[str]:
    """The gloss as at most three lower-case words (a gloss is already cleaned by ``mayur.gloss``)."""
    return [t.lower() for t in _GLOSS_WORD.findall(text or "")][:MAX_GLOSS_WORDS]


def _krt_token(m: Optional[Morph]) -> list[str]:
    return [f"K.{m.krt}"] if m is not None and m.krt and not m.is_verb else []


def word_tokens(w: Word, form: str) -> list[str]:
    """The tokens of one word in input form ``form``."""
    m = w.morph
    if w.in_compound:
        out = [stem_of(w), MEMBER]
    else:
        out = [stem_of(w), tag_of(m), *_krt_token(m)]
    if form == "B":
        out.extend(gloss_tokens(w.gloss))
    return out


def encode_reading(reading: Reading, form: str = "B") -> list[str]:
    """The simplified input of ``reading`` as a list of tokens, in text order."""
    if form not in FORMS:
        raise ValueError(f"unknown input form {form!r}")
    out: list[str] = []
    previous: Optional[int] = None
    for w in reading.words:
        if previous is not None and w.line != previous:
            out.append(LINE_END)
        previous = w.line
        out.extend(word_tokens(w, form))
    if previous is not None:
        out.append(LINE_END)
    return out


def special_tokens() -> list[str]:
    """Every atomic token the builder can write besides words (the tokenizer keeps them whole)."""
    tags = [f"N{c}{n}{g}" for c in [*CASES.values(), "x"] for n in [*NUMBERS.values(), "x"]
            for g in [*GENDERS.values(), "x"]]
    verbs = [f"V.{t}.{p}{n}{v}" for t in [*TENSES.values(), "x"] for p in [*PERSONS.values(), "x"]
             for n in [*NUMBERS.values(), "x"] for v in ("", *VOICES.values())]
    return [LINE_END, MEMBER, "<AV>", "<UNK>", *tags, *verbs]


def plain_glosses(words: Iterable[Word]) -> list[str]:
    """The gloss of each word, for the copy-of-glosses baseline."""
    return [w.gloss for w in words if w.gloss]
