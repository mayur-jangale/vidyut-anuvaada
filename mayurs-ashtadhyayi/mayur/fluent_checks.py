"""Pure checks that a language-model rewording keeps the verified analysis.

A rewording is accepted only if every check returns no :class:`Failure`. The checks never
call a model and never touch the network. English is compared with a crude stemmer, so the
checks are deliberately conservative: when in doubt they reject and the template English
stays.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Mapping, Sequence

from . import english, lipi, terms
from .model import Alignment, Reading, Word
from .translate_words import ADJ_SENSE

MAX_SYNONYMS = 5  # alternatives the model may offer per word
MAX_SYNONYM_WORDS = 3
MAX_SYNONYM_CHARS = 30
LENGTH_BOUNDS = (0.5, 2.2)  # reworded length / template length

FUNCTION_WORDS = frozenset("""
a an the of to in on at by with and or but for from as that which who whom whose is are was were be been
being am has have had does did do will shall it its he him his she her they them their we us our you your
i me my this these those then thus there so into upon after before when while until over under among
between through about also o if than
""".split())
NEGATION_WORDS = frozenset({"not", "no", "never", "nor", "neither", "none", "cannot", "without"})
NEGATION_FORMS = frozenset({"न", "नहि", "नो", "नैव", "नञ्"})  # Devanagari words that negate

_TOKEN = re.compile(r"[^\W\d_]+(?:['’][^\W\d_]+)?|\d+(?:[.,]\d+)*")
_IRREGULAR_PLURALS = frozenset({"men", "women", "children", "feet", "teeth", "mice", "people", "geese"})
_PAST_AUX = frozenset({"was", "were", "had", "did"})
_PRESENT_AUX = frozenset({"is", "are", "am", "does", "do", "has", "have"})
_MODALS = frozenset({"should", "may", "might", "would", "could", "can", "must"})
_PAST_LAKARA = frozenset({"लिट्", "लङ्", "लुङ्"})
_PRESENT_LAKARA = frozenset({"लट्"})
_FUTURE_LAKARA = frozenset({"लृट्", "लुट्"})


@dataclass(frozen=True)
class Failure:
    code: str  # alignment | substring | overlap | synonyms | content | vocabulary | number | tense | negation | order | length | malformed
    message: str

    def __str__(self) -> str:
        return f"{self.code}: {self.message}"


@dataclass(frozen=True)
class Rendering:
    """The substring of the rewording that renders Reading.words[word]."""

    word: int
    text: str


# ---------------------------------------------------------------- tokens and stems

def tokens(text: str) -> list[str]:
    """Lower-cased alphabetic and numeric tokens; brackets and punctuation are ignored."""
    return [t.lower() for t in _TOKEN.findall(re.sub(r"['\u2019]s\b", "", text))]


def stem(token: str) -> str:
    t = token.lower().replace("’", "'")
    for _ in range(3):
        for suf, rep in (("ies", "y"), ("ied", "y"), ("ity", ""), ("ing", ""), ("ed", ""), ("es", ""),
                         ("ly", ""), ("er", ""), ("s", "")):
            if t.endswith(suf) and len(t) - len(suf) + len(rep) >= 3 and not t.endswith(("ss", "us")):
                t = t[: -len(suf)] + rep
                break
        else:
            break
    return t[:-1] if t.endswith("e") and len(t) > 3 else t


def shares_stem(a: str, b: str) -> bool:
    sa, sb = stem(a), stem(b)
    if sa == sb:
        return True
    p = 0
    while p < min(len(sa), len(sb)) and sa[p] == sb[p]:
        p += 1
    return (p == min(len(sa), len(sb)) and p >= 3) or p >= 5


_UNMARKED_PLURALS = frozenset({"fish", "sheep", "deer", "cattle", "folk"})


def is_plural_token(token: str, unmarked: bool = True) -> bool:
    t = token.lower()
    return (unmarked and t in _UNMARKED_PLURALS) or t in _IRREGULAR_PLURALS or t.endswith("ren") or (len(t) > 3 and t.endswith("s") and not t.endswith(("ss", "us", "is")))


# ---------------------------------------------------------------- facts read from the reading

def _display(w: Word) -> str:
    return lipi.pausa(w.form)


def template_spans(reading: Reading) -> dict[int, str]:
    return {a.word: reading.translation[a.start:a.end] for a in reading.alignment}


def is_proper_name(w: Word) -> bool:
    return bool(w.gloss) and w.gloss[0].isupper()


def content_words(reading: Reading) -> list[int]:
    """Nouns, verbs, adjectives (and compound members) that carry a gloss; pronouns excluded."""
    out = []
    for i, w in enumerate(reading.words):
        m = w.morph
        if m is None or not w.gloss or m.kind not in ("subanta", "tinanta", "stem"):
            continue
        if english.is_pronoun(m.lemma):
            continue
        out.append(i)
    return out


def allowed_vocabulary(reading: Reading) -> set[str]:
    """Stems of every word the analysis itself supplies: glosses, derived meanings, the template."""
    words: list[str] = tokens(reading.translation)
    for w in reading.words:
        words += tokens(w.gloss) + tokens(w.derived_meaning)
    for c in reading.compounds:
        words += tokens(c.note)
    return {stem(t) for t in words} | {stem(t) for t in FUNCTION_WORDS | NEGATION_WORDS}


def analysis_negated(reading: Reading) -> bool:
    if any(t in NEGATION_WORDS for t in tokens(reading.translation)):
        return True
    return any(_display(w) in NEGATION_FORMS or (w.morph is not None and w.morph.lemma in NEGATION_FORMS)
               for w in reading.words)


# ---------------------------------------------------------------- the checks

def check_alignment_complete(reading: Reading, renderings: Sequence[Rendering]) -> list[Failure]:
    """Every word aligned in the template is aligned in the rewording, once, and no unknown word."""
    have = [r.word for r in renderings]
    want = {a.word for a in reading.alignment}
    out = [Failure("alignment", f"word {i} is aligned in the template but not in the rewording")
           for i in sorted(want - set(have))]
    out += [Failure("alignment", f"word {i} is not a word of the analysis") for i in sorted(set(have) - want)]
    out += [Failure("alignment", f"word {i} is aligned twice") for i in sorted({i for i in have if have.count(i) > 1})]
    out += [Failure("alignment", f"word {r.word} has an empty rendering") for r in renderings if not r.text.strip()]
    return out


def _boundary_ok(text: str, start: int, end: int) -> bool:
    before = text[start - 1] if start else " "
    after = text[end] if end < len(text) else " "
    return not (text[start].isalnum() and before.isalnum()) and not (text[end - 1].isalnum() and after.isalnum())


def _occurrences(text: str, sub: str) -> list[tuple[int, int]]:
    out, pos = [], text.find(sub)
    while pos != -1:
        if _boundary_ok(text, pos, pos + len(sub)):
            out.append((pos, pos + len(sub)))
        pos = text.find(sub, pos + 1)
    return out


def locate(reworded: str, renderings: Sequence[Rendering]) -> tuple[list[Alignment], list[Failure]]:
    """Non-overlapping character spans of the renderings in ``reworded`` (whole-word matches)."""
    options: list[tuple[int, list[tuple[int, int]]]] = []
    for r in renderings:
        occ = _occurrences(reworded, r.text) if r.text.strip() else []
        if not occ:
            return [], [Failure("substring", f"rendering of word {r.word} {r.text!r} does not occur in the rewording")]
        options.append((r.word, occ))
    chosen: list[tuple[int, int, int]] = []
    budget = [20000]  # backtracking is bounded: a pathological verse is rejected, never hangs

    def place(k: int) -> bool:
        budget[0] -= 1
        if k == len(options) or budget[0] < 0:
            return budget[0] >= 0
        word, occ = options[k]
        for s, e in occ:
            if all(e <= s2 or s >= e2 for _, s2, e2 in chosen):
                chosen.append((word, s, e))
                if place(k + 1):
                    return True
                chosen.pop()
        return False

    if not place(0):
        return [], [Failure("overlap", "the renderings cannot be placed as non-overlapping spans of the rewording")]
    return sorted((Alignment(w, s, e) for w, s, e in chosen), key=lambda a: a.start), []


def check_synonyms(synonyms: Mapping[int, Sequence[str]]) -> list[Failure]:
    out = []
    for i, alts in synonyms.items():
        if len(alts) > MAX_SYNONYMS:
            out.append(Failure("synonyms", f"word {i}: more than {MAX_SYNONYMS} alternatives"))
        for a in alts:
            toks = tokens(a)
            if not toks or len(toks) > MAX_SYNONYM_WORDS or len(a) > MAX_SYNONYM_CHARS:
                out.append(Failure("synonyms", f"word {i}: alternative {a!r} is empty or too long"))
    return out


def _used_synonyms(synonyms: Mapping[int, Sequence[str]], spans: Mapping[int, str]) -> dict[int, list[str]]:
    """Only alternatives that actually occur inside the word's own rendering count."""
    out: dict[int, list[str]] = {}
    for i, alts in synonyms.items():
        mine = set(tokens(spans.get(i, "")))
        out[i] = [a for a in alts if tokens(a) and set(tokens(a)) <= mine]
    return out


def check_content_words(reading: Reading, renderings: Sequence[Rendering],
                        synonyms: Mapping[int, Sequence[str]]) -> list[Failure]:
    """Each content word's rendering shares a stem with its gloss, template span or an allowed synonym;
    a proper name is kept verbatim."""
    mine = {r.word: r.text for r in renderings}
    spans = template_spans(reading)
    syn = _used_synonyms(synonyms, mine)
    out = []
    for i in content_words(reading):
        if i not in mine:
            continue
        w, text = reading.words[i], mine[i]
        if is_proper_name(w):
            if ADJ_SENSE.get(w.gloss) in tokens(text):
                continue  # a name-gloss that is a colour as a predicate: "black"
            if w.gloss not in text:
                out.append(Failure("content", f"name {w.gloss!r} (word {i}) is not kept verbatim in {text!r}"))
            continue
        ref_all = tokens(w.gloss) + tokens(spans.get(i, "")) + [t for a in syn.get(i, []) for t in tokens(a)]
        ref = [t for t in ref_all if t not in FUNCTION_WORDS] or ref_all  # "do" may be the content word
        got = [t for t in tokens(text) if t not in FUNCTION_WORDS] or tokens(text)
        if not any(shares_stem(g, r) for g in got for r in ref):
            out.append(Failure("content", f"{text!r} does not render {w.gloss!r} (word {i})"))
    return out


def check_vocabulary(reading: Reading, reworded: str, renderings: Sequence[Rendering],
                     synonyms: Mapping[int, Sequence[str]]) -> list[Failure]:
    """No numeral, name or content word that the analysis does not supply."""
    allowed = allowed_vocabulary(reading)
    for alts in _used_synonyms(synonyms, {r.word: r.text for r in renderings}).values():
        allowed |= {stem(t) for a in alts for t in tokens(a)}
    seen: list[str] = []
    for t in tokens(reworded):
        if stem(t) not in allowed and t not in seen:
            seen.append(t)
    return [Failure("vocabulary", f"{t!r} is not supplied by the analysis") for t in seen]


def _head_token(text: str, w: Word, ref: Sequence[str]) -> str | None:
    for t in reversed(tokens(text)):
        if t not in FUNCTION_WORDS and any(shares_stem(t, r) for r in ref):
            return t
    return None


def check_number(reading: Reading, renderings: Sequence[Rendering]) -> list[Failure]:
    """Plural and dual nouns are rendered plural; singular nouns are not."""
    mine = {r.word: r.text for r in renderings}
    spans = template_spans(reading)
    out = []
    for i in content_words(reading):
        w, m = reading.words[i], reading.words[i].morph
        if i not in mine or m is None or m.kind != "subanta" or w.role == "विशेषण" or is_proper_name(w) or w.in_compound:
            continue
        ref = tokens(w.gloss) + tokens(spans.get(i, ""))
        head = _head_token(mine[i], w, [t for t in ref if t not in FUNCTION_WORDS])
        if head is None:
            continue
        gloss_plural = any(is_plural_token(t) for t in tokens(w.gloss))
        if m.vacana in ("बहुवचन", "द्विवचन") and not is_plural_token(head):
            out.append(Failure("number", f"word {i} is {terms.english(m.vacana)} but rendered {head!r}"))
        elif m.vacana == "एकवचन" and is_plural_token(head, False) and not gloss_plural:
            out.append(Failure("number", f"word {i} is singular but rendered {head!r}"))
    return out


def tense_classes(text: str, gloss: str) -> set[str]:
    g = gloss.lower().split()[0] if gloss.split() else ""
    base, past, third = (english.base(g), english.past(g), english.third_singular(g)) if g else ("", "", "")
    found: set[str] = set()
    prev = ""
    for t in tokens(text):
        passive_participle = prev in _PAST_AUX | _PRESENT_AUX | {"be", "been"} and t.endswith("ed")
        prev = t
        if passive_participle:
            continue  # "is conveyed": the participle is not a second tense marker
        if t in _PAST_AUX or t == past or (t.endswith("ed") and len(t) > 3):
            found.add("past")
        elif t in ("will", "shall") or t.endswith("'ll"):
            found.add("future")
        elif t in _PRESENT_AUX or t in (base, third) or (t.endswith("s") and len(t) > 3 and not t.endswith(("ss", "us", "is"))):
            found.add("present")
    return found


def check_tense(reading: Reading, renderings: Sequence[Rendering]) -> list[Failure]:
    """Past / present / future class of each finite verb matches its lakara."""
    mine = {r.word: r.text for r in renderings}
    out = []
    for i, w in enumerate(reading.words):
        m = w.morph
        if m is None or m.kind != "tinanta" or i not in mine:
            continue
        want = ("past" if m.lakara in _PAST_LAKARA else "present" if m.lakara in _PRESENT_LAKARA
                else "future" if m.lakara in _FUTURE_LAKARA else "")
        if m.lakara == "विधिलिङ्":
            if not set(tokens(mine[i])) & _MODALS:
                out.append(Failure("tense", f"optative verb (word {i}) lacks a modal: {mine[i]!r}"))
        elif want and tense_classes(mine[i], w.gloss) != {want}:
            out.append(Failure("tense", f"verb (word {i}) is {terms.english(m.lakara)} ({want}) but rendered {mine[i]!r}"))
    return out


def check_negation(reading: Reading, reworded: str) -> list[Failure]:
    want = analysis_negated(reading)
    toks = tokens(reworded)
    got = any(t in NEGATION_WORDS or t.endswith("n't") for t in toks)
    if want and not got:
        return [Failure("negation", "the analysis negates (न) but the rewording does not")]
    if got and not want:
        return [Failure("negation", "the rewording negates but the analysis does not")]
    return []


def check_voice_order(reading: Reading, reworded: str, spans: Sequence[Alignment]) -> list[Failure]:
    """The agent precedes an active verb, or follows 'by' after a passive one."""
    at = {a.word: a for a in spans}
    out = []
    for v, vw in enumerate(reading.words):
        m = vw.morph
        if m is None or m.kind != "tinanta" or v not in at:
            continue
        for a, aw in enumerate(reading.words):
            if aw.head != v or aw.role != "कर्ता" or aw.in_compound or a not in at:
                continue
            if m.prayoga == "कर्मणि":
                before = tokens(reworded[: at[a].start])[-4:]
                if at[a].start < at[v].end or "by" not in before:
                    out.append(Failure("order", f"passive agent (word {a}) must follow the verb and 'by'"))
            elif at[a].start > at[v].start:
                out.append(Failure("order", f"agent (word {a}) must precede the active verb (word {v})"))
    return out


def check_length(template: str, reworded: str) -> list[Failure]:
    if not reworded.strip():
        return [Failure("length", "empty rewording")]
    ratio = len(reworded) / max(1, len(template))
    lo, hi = LENGTH_BOUNDS
    return [] if lo <= ratio <= hi else [Failure("length", f"length ratio {ratio:.2f} outside {lo}-{hi}")]


# ---------------------------------------------------------------- all checks

def run_checks(reading: Reading, reworded: str, renderings: Sequence[Rendering],
               synonyms: Mapping[int, Sequence[str]],
               exact: Sequence[Alignment] | None = None) -> tuple[list[Alignment], list[Failure]]:
    """(alignment of the rewording, failures). The rewording may be used only if there are no failures.
    ``exact`` are spans the caller knows (a rewriter that builds the text from tokens); they are verified
    instead of searched for."""
    fails = check_alignment_complete(reading, renderings) + check_synonyms(synonyms)
    if exact is not None and not fails:
        by = {r.word: r.text for r in renderings}
        bad = [a for a in exact if reworded[a.start:a.end] != by.get(a.word)]
        spans, loc = ([], [Failure("substring", f"span of word {bad[0].word} is not its rendering")]) if bad else (list(exact), [])
        spans = sorted(spans, key=lambda a: a.start)
        if any(x.end > y.start for x, y in zip(spans, spans[1:])):
            spans, loc = [], [Failure("overlap", "spans overlap")]
    else:
        spans, loc = locate(reworded, renderings) if not fails else ([], [])
    fails += loc
    fails += check_length(reading.translation, reworded)
    if not fails:
        fails += check_content_words(reading, renderings, synonyms)
        fails += check_vocabulary(reading, reworded, renderings, synonyms)
        fails += check_number(reading, renderings) + check_tense(reading, renderings)
        fails += check_negation(reading, reworded) + check_voice_order(reading, reworded, spans)
    return (spans if not fails else []), fails
