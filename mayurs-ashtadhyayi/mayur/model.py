"""Shared data model. Every module exchanges these objects; all text is SLP1.

Conventions
-----------
* A *pada* is written in its unsandhied padapatha form with final ``s``/``r``/``m``
  kept as such (``rAmas``, ``punar``, ``niratam``) -- the same keys vidyut-kosha uses.
* Paninian category values are the vidyut strings (``praTamA``, ``puM``, ``eka``,
  ``la~w``, ``kartari`` ...). ``mayur.labels`` maps them to English.
"""

from __future__ import annotations

from dataclasses import dataclass, field, fields, is_dataclass
from typing import Any, Optional

VERIFIED = "verified"
UNVERIFIED = "unverified"


@dataclass(frozen=True)
class SutraStep:
    source: str  # "ashtadhyayi", "varttika", "dhatupatha", ...
    code: str  # e.g. "6.1.87"
    result: str  # state of the derivation after the rule, terms joined by " + "


@dataclass(frozen=True)
class Morph:
    """One grammatical analysis of one word form."""

    form: str
    lemma: str  # pratipadika, or dhatu (with upasargas prefixed) for tinantas
    kind: str  # "subanta" | "tinanta" | "avyaya" | "stem" | "unknown"
    linga: Optional[str] = None
    vibhakti: Optional[str] = None
    vacana: Optional[str] = None
    purusha: Optional[str] = None
    lakara: Optional[str] = None
    prayoga: Optional[str] = None
    root: Optional[str] = None  # clean dhatu text if verbal (tinanta or krdanta)
    dhatu: Optional[str] = None  # aupadeshika dhatu
    gana: Optional[str] = None
    prefixes: tuple[str, ...] = ()
    krt: Optional[str] = None  # krt pratyaya if the stem is a krdanta
    root_gloss: Optional[str] = None  # vidyut dhatupatha English meaning
    source: str = "kosha"  # "kosha" | "generated" (forward-generated, stem not in kosha) | "none"
    lexical_linga_ok: bool = True  # False if kosha lists the stem only in other genders
    handle: Any = field(default=None, compare=False, repr=False)  # vidyut object for derivation

    @property
    def is_verb(self) -> bool:
        return self.kind == "tinanta"

    @property
    def is_nominal(self) -> bool:
        return self.kind == "subanta"


@dataclass
class WordProof:
    derivable: bool
    method: str = ""  # "vidyut-prakriya" | "" when not derivable
    derived_form: str = ""
    trace: list[SutraStep] = field(default_factory=list)
    note: str = ""


@dataclass
class Word:
    """A word of a reading: a pada, or a non-final compound member (stem form)."""

    form: str
    line: int  # index of the input line (half-verse)
    start: int  # span [start, end) in that line's SLP1 surface text
    end: int
    in_compound: bool = False  # True => non-final member of a compound (stem form)
    compound: Optional[int] = None  # id of the Compound this word belongs to, if any
    analyses: list[Morph] = field(default_factory=list)
    chosen: int = 0
    proof: Optional[WordProof] = None
    role: str = ""  # karta | karma | karana | sampradana | apadana | adhikarana | sambandha |
    #                 kriya | visheshana | sambodhana | avyaya | samasa-purvapada | ""
    head: Optional[int] = None  # index (in Reading.words) of the word this one depends on
    gloss: str = ""
    gloss_source: str = ""
    arsha: bool = False  # labelled non-Paninian; not forced into a parse

    @property
    def morph(self) -> Optional[Morph]:
        return self.analyses[self.chosen] if self.analyses else None


@dataclass
class Compound:
    id: int
    members: list[int]  # indices into Reading.words, in order
    stem: str = ""  # compound stem as joined
    samasa: str = ""  # tatpurusha | karmadharaya | dvandva | bahuvrihi | avyayibhava | unknown
    vigraha: str = ""  # dissolved paraphrase in SLP1
    basis: str = ""  # how the type was decided ("heuristic: ...")


@dataclass
class Alignment:
    word: int  # index into Reading.words
    start: int  # span [start, end) in Reading.translation
    end: int


@dataclass
class Reading:
    words: list[Word]
    compounds: list[Compound] = field(default_factory=list)
    scores: dict[str, float] = field(default_factory=dict)  # frequency, akanksha, yogyata, sannidhi, total
    sandhi_ok: bool = False  # re-joined words reproduce the input exactly
    rejoined: list[str] = field(default_factory=list)  # per line, what the words re-join to
    status: str = UNVERIFIED
    notes: list[str] = field(default_factory=list)
    anvaya: list[int] = field(default_factory=list)  # word indices in prose order
    translation: str = ""
    alignment: list[Alignment] = field(default_factory=list)


@dataclass
class VerseAnalysis:
    id: str
    input: str  # as given (any script)
    lines: list[str] = field(default_factory=list)  # SLP1 surface per half-verse
    metre: dict[str, Any] = field(default_factory=dict)
    split_counts: list[int] = field(default_factory=list)  # number of valid splits per line
    readings: list[Reading] = field(default_factory=list)  # ranked, [0] is the chosen one
    status: str = UNVERIFIED
    notes: list[str] = field(default_factory=list)


def to_jsonable(obj: Any) -> Any:
    """Convert model objects to plain JSON types (drops opaque ``handle`` fields)."""
    if is_dataclass(obj) and not isinstance(obj, type):
        return {f.name: to_jsonable(getattr(obj, f.name)) for f in fields(obj) if f.name != "handle"}
    if isinstance(obj, (list, tuple)):
        return [to_jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {k: to_jsonable(v) for k, v in obj.items()}
    return obj
