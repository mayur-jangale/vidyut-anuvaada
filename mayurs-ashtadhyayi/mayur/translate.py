"""Literal English by template from a resolved, ordered Reading. No free paraphrase.

Per clause: [O vocative,] karta phrase, verb (tense/person/number from the morphology),
karma phrase, then prepositional phrases (by/with, to/for, from, in), adverbs.
Nominal sentences get a supplied copula written "[is]". Every content word is aligned
to the exact span of its English rendering; particles align to their own word.
All English wording tables below are our own.
"""

from __future__ import annotations

import re
from dataclasses import replace
from typing import Optional

from mayur.anvaya import clauses
from mayur.model import Alignment, Compound, Reading, Word
from mayur.translit import to_iast

REL_PREP = {"saptamI": "to", "tftIyA": "by", "zazWI": "of", "dvitIyA": "of"}


class Tok:
    """An English token; ``parts`` maps word index -> (offset, length) inside ``text``."""

    def __init__(self, text: str, word: Optional[int] = None,
                 parts: Optional[list[tuple[int, int, int]]] = None):
        self.text = text
        self.parts = parts if parts is not None else ([(word, 0, len(text))] if word is not None else [])

    def spans(self, start: int) -> list[tuple[int, int, int]]:
        return [(w, start + off, start + off + ln) for w, off, ln in self.parts]


def pluralize(noun: str) -> str:
    if re.search(r"(s|sh|ch|x|z)$", noun):
        return noun + "es"
    if re.search(r"[^aeiou]y$", noun):
        return noun[:-1] + "ies"
    return noun + "s"


def _join(pieces: list[tuple[Optional[int], str]]) -> Tok:
    text, parts = "", []
    for word, piece in pieces:
        if word is not None:
            parts.append((word, len(text), len(piece)))
        text += piece
    return Tok(text, parts=parts)


def compound_tokens(c: Compound, glosses: list[str], plural: bool) -> list[Tok]:
    """Hyphenated English for a compound, each member's gloss separately aligned."""
    g = [x.replace(" ", "-") for x in glosses]
    if "agent" in c.basis and not re.search(r"(er|or|ant|ent|ing)$", g[-1]):
        g[-1] = g[-1] + ("r" if g[-1].endswith("e") else "er")  # know -> knower
    if plural:
        g[-1] = pluralize(g[-1])
    if "best-of" in c.basis and g:
        g[-2] = pluralize(g[-2])  # munInAm puMgavaH: bull of sages
    first = [(m, x) for m, x in zip(c.members[:-1], g[:-1])]
    final = (c.members[-1], g[-1])
    firsts: list[tuple[Optional[int], str]] = []
    for n, (m, x) in enumerate(first):
        firsts += ([(None, "-and-")] if n else []) + [(m, x)]
    if c.samasa == "tatpurusha":
        rel = re.search(r"in (\w+)", c.basis)
        prep = REL_PREP.get(rel.group(1) if rel else "zazWI", "of")
        if len(first) == 1 and "agent" not in c.basis and "best-of" not in c.basis and "kta" not in c.basis:
            prep = "of"
        return [_join([final, (None, f"-{prep}-")] + firsts)]
    if c.samasa == "bahuvrihi":
        return [_join([(None, "having-")] + firsts + [(None, "-"), final])]
    if c.samasa == "dvandva":
        return [_join(firsts + [(None, "-and-"), final])]
    return [_join(firsts + [(None, "-"), final])]


PRONOUNS = {"kim": "who", "ka": "who", "idam": "this", "etad": "this", "tad": "that",
            "yad": "who", "adas": "that", "asmad": "I", "yuzmad": "you", "sarva": "all"}
PARTICLES = {"ca": "and", "nu": "indeed", "hi": "for", "eva": "only", "api": "also",
             "tu": "but", "vA": "or", "na": "not", "mA": "not", "iti": "thus"}
CASE_PREP = {"karana": "by", "sampradana": "for", "apadana": "from", "adhikarana": "in"}
IRREGULAR_PAST = {"run": "ran", "go": "went", "say": "said", "see": "saw", "speak": "spoke",
                  "give": "gave", "take": "took", "know": "knew", "come": "came", "be": "was",
                  "do": "did", "make": "made", "tell": "told", "hear": "heard", "stand": "stood"}
PAST = frozenset({"li~w", "la~N", "lu~N"})
FUTURE = frozenset({"lf~w", "lu~w", "lf~N"})
DROPPED_SUBJECT = {("praTama", "eka"): "he", ("praTama", "dvi"): "the two", ("praTama", "bahu"): "they",
                   ("maDyama", "eka"): "you", ("maDyama", "dvi"): "you two", ("maDyama", "bahu"): "you",
                   ("uttama", "eka"): "I", ("uttama", "dvi"): "we two", ("uttama", "bahu"): "we"}


def first_sense(gloss: str) -> str:
    g = re.sub(r"\([^)]*\)", "", gloss or "")
    g = re.split(r"[;,/]", g)[0].strip()
    return re.sub(r"^to\s+", "", g)


def lemma_english(w: Word) -> str:
    m = w.morph
    if m is not None and m.kind == "subanta" and m.lemma in PRONOUNS:
        return "what" if (m.lemma == "kim" and m.linga == "napuMsaka") else PRONOUNS[m.lemma]
    if m is not None and m.kind == "avyaya" and not w.gloss and m.lemma in PARTICLES:
        return PARTICLES[m.lemma]
    return first_sense(w.gloss) or to_iast(m.lemma if m else w.form)


def verb_phrase(base: str, m) -> str:
    third_sg = m.purusha == "praTama" and m.vacana == "eka"
    if m.lakara in PAST:
        if base in IRREGULAR_PAST:
            return IRREGULAR_PAST[base]
        return base + ("d" if base.endswith("e") else "ed")
    if m.lakara in FUTURE:
        return "will " + base
    if m.lakara == "lo~w":
        return base if m.purusha == "maDyama" else "let " + base
    if m.lakara == "viDili~N":
        return "should " + base
    if m.lakara == "ASIrli~N":
        return "may " + base
    if third_sg:
        return base + ("es" if re.search(r"(s|sh|ch|x|o)$", base) else "s")
    return base


class _Renderer:
    def __init__(self, reading: Reading):
        self.r = reading
        self.words = reading.words
        self.kids: dict[int, list[int]] = {i: [] for i in range(len(self.words))}
        for i, w in enumerate(self.words):
            if w.head is not None and w.head != i:
                self.kids[w.head].append(i)
        self.cpd = {c.id: c for c in reading.compounds}
        self.used: set[int] = set()

    def _deps(self, i: int, *roles: str) -> list[int]:
        return [k for k in self.kids[i] if self.words[k].role in roles and k not in self.used]

    def word(self, i: int) -> list[Tok]:
        """Tokens for word i (whole compound if it is a compound's final member)."""
        w = self.words[i]
        c: Optional[Compound] = self.cpd.get(w.compound) if w.compound is not None else None
        plural = w.morph is not None and w.morph.vacana == "bahu" and not _adjectival(w)
        if c is not None:
            self.used.update(c.members)
            return compound_tokens(c, [lemma_english(self.words[j]) for j in c.members], plural)
        self.used.add(i)
        text = lemma_english(w)
        return [Tok(pluralize(text) if plural else text, i)]

    def np(self, i: int) -> list[Tok]:
        """Noun phrase: simple adjectives, noun, then appositive complex adjectives, of-genitives."""
        self.used.add(i)
        simple, complex_ = [], []
        for k in self._deps(i, "visheshana"):
            w = self.words[k]
            (complex_ if (w.compound is not None or self.kids[k]) else simple).append(k)
        toks: list[Tok] = []
        for k in simple:
            toks += self.np(k)
        toks += self.word(i)
        if self.words[i].role in ("karta", "karma") and _bare_adjective(self.words[i]) and not simple:
            toks.append(Tok("[one]", None))
        for k in complex_:
            toks += [Tok(",", None)] + self.np(k)
        for k in self._deps(i, "sambandha"):
            toks += [Tok("of", None)] + self.np(k)
        for k in self._deps(i, "avyaya"):
            toks += self.particle(k)
        return toks

    def particle(self, k: int) -> list[Tok]:
        self.used.add(k)
        return [Tok(lemma_english(self.words[k]), k)]

    def with_and(self, i: int) -> list[Tok]:
        """Phrase for i, with a joining `ca` rendered as a leading "and"."""
        cas = [k for k in self._deps(i, "avyaya") if (self.words[k].morph and self.words[k].morph.lemma == "ca")]
        lead = []
        for k in cas:
            lead += self.particle(k)
        return lead + self.np(i)

    def obliques(self, root: int) -> list[Tok]:
        toks: list[Tok] = []
        for role, prep in CASE_PREP.items():
            for k in self._deps(root, role):
                toks += [Tok(prep, None)] + self.np(k)
        for k in self._deps(root, "avyaya", "kriya"):
            toks += self.np(k)
        return toks

    def verbal_clause(self, v: int) -> list[Tok]:
        m = self.words[v].morph
        toks: list[Tok] = []
        for k in self._deps(v, "sambodhana"):
            toks += [Tok("O", None)] + self.np(k) + [Tok(",", None)]
        kartas = self._deps(v, "karta")
        karmas = self._deps(v, "karma")
        passive = m.prayoga == "karmaRi"
        subj, obj = (karmas, kartas) if passive else (kartas, karmas)
        for n, k in enumerate(subj):
            toks += ([Tok("and", None)] if n else []) + self.np(k)
        if not subj:
            toks.append(Tok(DROPPED_SUBJECT.get((m.purusha, m.vacana), "he"), None))
        self.used.add(v)
        base = lemma_english(self.words[v])
        verb = (("was " if m.lakara in PAST else "is ") + base + "ed") if passive else verb_phrase(base, m)
        toks.append(Tok(verb, v))
        for n, k in enumerate(obj):
            toks += ([Tok("by", None)] if passive and not n else []) + self.np(k)
        return toks + self.obliques(v)

    def nominal_clause(self, s: int) -> list[Tok]:
        toks: list[Tok] = []
        for k in self._deps(s, "avyaya"):
            if self.words[k].morph and self.words[k].morph.lemma == "ca":
                toks += self.particle(k)
        toks += self.word(s)
        toks += [t for k in self._deps(s, "sambandha") for t in [Tok("of", None)] + self.np(k)]
        toks += self.obliques(s)
        toks.append(Tok("[is]", None))
        preds = self._deps(s, "visheshana")
        for n, k in enumerate(preds):
            toks += ([Tok(",", None)] if n else []) + self.with_and(k)
        return toks

    def leftovers(self) -> list[Tok]:
        return [t for i in range(len(self.words)) if i not in self.used for t in self.word(i)]


def _bare_adjective(w: Word) -> bool:
    from mayur.compounds import stem_lingas
    m = w.morph
    return m is not None and m.kind == "subanta" and w.compound is None and m.lemma not in PRONOUNS \
        and (m.krt is not None or len(stem_lingas(m)) == 3)


def _adjectival(w: Word) -> bool:
    from mayur.compounds import is_adjectival
    return w.role == "visheshana" or is_adjectival(w.morph)


def _assemble(sentences: list[list[Tok]]) -> tuple[str, list[Alignment]]:
    text, align = "", []
    for toks in sentences:
        if not toks:
            continue
        sent_start = len(text) + (1 if text else 0)
        text += " " if text else ""
        for n, t in enumerate(toks):
            if t.text == ",":
                text += ","
                continue
            if n and not text.endswith(" "):
                text += " "
            piece = t.text
            if len(text) == sent_start and piece:
                piece = piece[0].upper() + piece[1:]
            start = len(text)
            text += piece
            for word, a, b in t.spans(start):
                align.append(Alignment(word, a, b))
        text += "."
    return text, align


def render(reading: Reading) -> Reading:
    rd = _Renderer(reading)
    sentences = []
    for root, _ in clauses(reading.words):
        if root < 0:
            continue
        w = reading.words[root]
        sentences.append(rd.verbal_clause(root) if w.role == "kriya" else rd.nominal_clause(root))
    rest = rd.leftovers()
    if rest:
        sentences.append(rest)
    text, align = _assemble(sentences)
    return replace(reading, translation=text, alignment=align)
