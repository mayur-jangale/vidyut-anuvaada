"""Shared data model.

Every Sanskrit string in these objects is Devanagari. A pada is kept in its grammatical
(padapatha) form with the final स् / र् / म् written as such: रामस्, पुनर्, निरतम्;
``mayur.lipi.pausa`` gives the form with visarga for display. Category values are the
traditional terms in Devanagari (प्रथमा, पुंलिङ्ग, एकवचन, लट्, कर्तरि ...); ``mayur.labels``
gives their English names.
"""

from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any, Optional

VERIFIED = "verified"
UNVERIFIED = "unverified"


@dataclass(frozen=True)
class SutraStep:
    source: str  # which text the rule is from: अष्टाध्यायी, वार्त्तिक, धातुपाठ ...
    code: str  # e.g. "6.1.87"
    result: str  # state of the derivation after the rule, terms joined by " + "


@dataclass(frozen=True)
class Morph:
    """One grammatical analysis of one word form."""

    form: str
    lemma: str  # pratipadika; for verbal forms the dhatu with its upasargas
    kind: str  # "subanta" | "tinanta" | "avyaya" | "stem" | "unknown"
    stem: str = ""  # pratipadika text when it differs from the lemma (krdanta stems)
    linga: Optional[str] = None
    vibhakti: Optional[str] = None
    vacana: Optional[str] = None
    purusha: Optional[str] = None
    lakara: Optional[str] = None
    prayoga: Optional[str] = None
    root: Optional[str] = None  # dhatu without upasargas, if the form is verbal
    dhatu: Optional[str] = None  # dhatu as taught in the Dhatupatha (aupadeshika)
    gana: Optional[str] = None
    prefixes: tuple[str, ...] = ()
    krt: Optional[str] = None  # krt pratyaya if the stem is a krdanta
    root_gloss: Optional[str] = None  # vidyut's English meaning of the dhatu
    source: str = "kosha"  # "kosha" | "generated" (forward-derived, not listed) | "special" | "none"
    quality: int = 3  # 3 ordinary ... 0 kosha over-generation
    handle: Any = field(default=None, compare=False, repr=False)  # vidyut arguments for derivation

    @property
    def is_verb(self) -> bool:
        return self.kind == "tinanta"

    @property
    def is_nominal(self) -> bool:
        return self.kind == "subanta"

    @property
    def is_verbal(self) -> bool:
        return self.root is not None


@dataclass
class WordProof:
    derivable: bool
    method: str = ""
    derived_form: str = ""
    trace: list[SutraStep] = field(default_factory=list)
    note: str = ""


@dataclass
class Word:
    """A word of a reading: a pada, or a non-final compound member (stem form)."""

    form: str
    line: int  # index of the half-verse
    start: int  # span [start, end) in the line's varna sequence, spaces not counted
    end: int
    in_compound: bool = False  # True => non-final member of a compound
    compound: Optional[int] = None  # id of the Compound this word belongs to, if any
    analyses: list[Morph] = field(default_factory=list)
    chosen: int = 0
    proof: Optional[WordProof] = None
    role: str = ""  # see mayur.labels.ROLES
    head: Optional[int] = None  # index (in Reading.words) of the word this one depends on
    gloss: str = ""
    gloss_source: str = ""
    arsha: bool = False  # not derivable by Panini's rules as implemented; labelled, never forced

    @property
    def morph(self) -> Optional[Morph]:
        return self.analyses[self.chosen] if self.analyses else None


@dataclass
class Junction:
    """The sandhi between word ``left`` and the next word, with the rules that license it."""

    left: int
    sutras: tuple[str, ...] = ()
    in_compound: bool = False
    surface: str = ""  # what the two edges became in the text


@dataclass
class Compound:
    id: int
    members: list[int]  # indices into Reading.words, in order
    stem: str = ""
    samasa: str = ""  # tatpurusha | karmadharaya | dvandva | bahuvrihi | avyayibhava | unknown
    vigraha: str = ""  # dissolved paraphrase
    basis: str = ""  # how the type was decided; always says when it is a heuristic


@dataclass
class Alignment:
    word: int  # index into Reading.words
    start: int  # span [start, end) in Reading.translation
    end: int


@dataclass
class Reading:
    words: list[Word]
    junctions: list[Junction] = field(default_factory=list)
    compounds: list[Compound] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)
    sandhi_ok: bool = False  # the words re-joined by sandhi reproduce the input exactly
    rejoined: list[str] = field(default_factory=list)  # per line
    status: str = UNVERIFIED
    notes: list[str] = field(default_factory=list)
    anvaya: list[int] = field(default_factory=list)  # word indices in prose order
    translation: str = ""
    alignment: list[Alignment] = field(default_factory=list)


@dataclass
class VerseAnalysis:
    id: str
    input: str  # exactly as given
    lines: list[str] = field(default_factory=list)  # half-verses in Devanagari
    metre: dict[str, Any] = field(default_factory=dict)
    split_counts: list[int] = field(default_factory=list)  # number of valid splits per line
    readings: list[Reading] = field(default_factory=list)  # ranked; [0] is the chosen one
    status: str = UNVERIFIED
    notes: list[str] = field(default_factory=list)


def to_plain(obj: Any) -> Any:
    """Model objects as plain JSON types (drops the opaque ``handle``)."""
    if is_dataclass(obj) and not isinstance(obj, type):
        return {f.name: to_plain(getattr(obj, f.name)) for f in fields(obj) if f.name != "handle"}
    if isinstance(obj, (list, tuple)):
        return [to_plain(x) for x in obj]
    if isinstance(obj, dict):
        return {k: to_plain(v) for k, v in obj.items()}
    return obj
