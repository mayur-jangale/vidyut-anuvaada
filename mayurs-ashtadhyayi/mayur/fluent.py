"""Rule-based fluent English: smooths the literal template without changing the analysis.

Offline and deterministic. The template (``Reading.translation`` + ``Reading.alignment``) is cut
into tokens; an aligned word is one token that carries its word index, everything else
(function words, punctuation, bracketed supplied words) has ``word=None``. Each rule is a small
pure function ``(tokens, reading) -> tokens`` that may insert, drop or move unaligned tokens,
re-order an aligned word with its neighbours, or re-word an aligned token, but never drops an aligned
word. The result is accepted only if every check in ``fluent_checks`` passes on it, beyond
what already failed on the template itself.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, replace
from typing import Callable, Optional

from . import english
from .fluent_checks import Failure, Rendering, run_checks
from .model import Alignment, Reading, Word

NOTE_OK = "rule-based; checks passed"
PUNCT = {",", ";", ".", "?", "!", ":"}
_PIECE = re.compile(r"\[[^\]]*\]|[^\s,;.?!:\-\[\]]+|[,;.?!:\-]")
_AUX = {"is", "are", "am", "was", "were", "will", "shall", "do", "did", "does", "has", "have"}
_DET = {"such", "other", "same", "the", "a", "an", "this", "that", "these", "those", "my", "your", "his", "her", "its", "our", "their",
        "all", "some", "no", "each", "every", "whose", "which"}
_DANGLING = {"and", "or", "but", "of", "to", "in", "by", "with", "from", "as", "for", "at", "on", "who", "which"}
_WH = {"who", "what", "whom", "whose", "which"}
_MASS = {"water", "fire", "speech", "dharma", "truth", "joy", "anger", "grief", "affection", "valour", "virtue",
         "knowledge", "austerity", "study", "patience", "battle", "fortune", "happiness", "wealth", "time"}
_NOUN_SKIP = {"विशेषण", "समासपूर्वपद", "सम्बोधन", "क्रिया", "अव्यय", "सम्बन्ध"}
_ADJ = {"विशेषण", "विधेय"}
_AGENT_END = ("er", "or", "ist")
_ADJ_WORDS = {"like", "equal", "good", "best", "great", "other", "dear", "fine", "firm", "such", "same", "all", "only",
              "noble", "wise", "high", "low", "steadfast", "clean", "well", "mahat", "large", "small", "many", "much"}
_PREP_START = ("of", "in", "by", "to", "from", "with", "for", "on", "at", "like", "as")


@dataclass(frozen=True)
class Tok:
    text: str
    word: Optional[int] = None


Rule = Callable[[list[Tok], Reading], list[Tok]]


# ---------------------------------------------------------------- tokens <-> text

def tokenize(reading: Reading) -> list[Tok]:
    """Template -> tokens; aligned spans stay whole, gaps are cut into words and punctuation."""
    text, out, pos = reading.translation, [], 0
    for a in sorted(reading.alignment, key=lambda x: x.start):
        out += [Tok(m) for m in _PIECE.findall(text[pos:a.start])]
        span = text[a.start:a.end]
        if span[:1].isupper() and not reading.words[a.word].gloss[:1].isupper() and (pos or a.start == 0):
            span = span[0].lower() + span[1:]  # a capital that only marks the sentence start
        out.append(Tok(span, a.word))
        pos = a.end
    return out + [Tok(m) for m in _PIECE.findall(text[pos:])]


def render(toks: list[Tok]) -> tuple[str, list[Alignment]]:
    """Text and exact spans of the aligned tokens."""
    out, spans = "", []
    for i, t in enumerate(toks):
        glued = i == 0 or t.text in PUNCT or t.text == "-" or toks[i - 1].text == "-"
        out += ("" if glued else " ")
        if t.word is not None:
            spans.append(Alignment(t.word, len(out), len(out) + len(t.text)))
        out += t.text
    return out, spans


def _w(reading: Reading, t: Tok) -> Optional[Word]:
    return reading.words[t.word] if t.word is not None else None


def _is_name(w: Optional[Word]) -> bool:
    return bool(w and w.gloss and w.gloss[0].isupper())


def _pronoun(w: Optional[Word]) -> bool:
    return bool(w and w.morph and english.is_pronoun(w.morph.lemma))


def _sentence_start(toks: list[Tok], i: int) -> int:
    k = i
    while k > 0 and toks[k - 1].text not in (".", "?", "!", ";"):
        k -= 1
    return k


# ---------------------------------------------------------------- rules

def unbracket(toks, reading):
    """Supplied words lose their brackets ('[is]' -> 'is'); a supplied 'He is' stays lower case mid-sentence."""
    out = []
    for t in toks:
        if t.word is None and t.text.startswith("["):
            inner = t.text.strip("[]")
            first = inner.split()[0] if inner.split() else ""
            if first in ("He", "She", "They", "It", "We"):
                inner = inner[0].lower() + inner[1:]
            out += [Tok(p) for p in inner.split()]
        else:
            out.append(t)
    return out


def smooth_compounds(toks, reading):
    """Two-member compounds: dvandva 'a-b' -> 'a and b'; tatpurusha with an agent noun last -> 'b of a'."""
    toks = list(toks)
    for c in reading.compounds:
        if len(c.members) != 2:
            continue
        a, b = c.members
        pos = {t.word: i for i, t in enumerate(toks) if t.word is not None}
        if a not in pos or b not in pos or pos[b] != pos[a] + 2 or toks[pos[a] + 1].text != "-":
            continue
        i = pos[a]
        if c.samasa == "द्वन्द्व":
            toks[i + 1] = Tok("and")
        elif c.samasa == "तत्पुरुष" and reading.words[b].gloss.lower().endswith(_AGENT_END) \
                and toks[i + 2].text.lower().endswith(("er", "ers", "or", "ors", "ist", "ists")):
            toks[i:i + 3] = [toks[i + 2], Tok("of"), toks[i]]
    return toks


def possessive_names(toks, reading):
    """'<head phrase> of <Name>' -> '<Name>'s <head phrase>' for a one-word proper-name possessor."""
    toks = list(toks)
    i = 1
    while i < len(toks) - 1:
        t, w = toks[i + 1], _w(reading, toks[i + 1])
        if toks[i].text == "of" and toks[i].word is None and _is_name(w) and w.role == "सम्बन्ध" and w.head is not None:
            if toks[i - 1].word != w.head or (i > 1 and toks[i - 2].text == "-") or _is_name(_w(reading, toks[i - 1])):
                i += 1
                continue
            j = i - 1
            while j > 0 and toks[j - 1].word is not None and reading.words[toks[j - 1].word].role == "विशेषण" \
                    and reading.words[toks[j - 1].word].head == w.head and toks[j - 1].text != "-" \
                    and not (j > 1 and toks[j - 2].text == "-"):
                j -= 1
            toks[j:i + 2] = [Tok(t.text + "'s", t.word)] + toks[j:i]
        i += 1
    return toks


def verb_agreement(toks, reading):
    """be-forms agree with the preceding subject; present 3rd singular verbs take -s."""
    toks = list(toks)
    for i, t in enumerate(toks):
        if t.word is None and t.text in ("is", "are", "am"):
            subj = next((x for x in reversed(toks[_sentence_start(toks, i):i]) if x.word is not None
                         and (reading.words[x.word].role == "कर्ता" or _pronoun(reading.words[x.word]))), None)
            m = reading.words[subj.word].morph if subj else None
            if m is not None and m.kind == "subanta":
                if english.is_pronoun(m.lemma) and subj.text.lower() == "i":
                    toks[i] = Tok("am")
                else:
                    toks[i] = Tok("are" if m.vacana in ("बहुवचन", "द्विवचन") or subj.text.lower() in ("you", "we", "they")
                                  else "is")
        w = _w(reading, t)
        m = w.morph if w else None
        if m and m.kind == "tinanta" and m.lakara == "लट्" and m.purusha == "प्रथमपुरुष" and m.vacana == "एकवचन" \
                and w.gloss and t.text.lower() == english.base(w.gloss.split()[0]):
            toks[i] = Tok(english.third_singular(t.text.lower()), t.word)
    return toks


def relative_clauses(toks, reading):
    """A relative pronoun (यद्) after a noun opens a clause set off by a comma."""
    out = []
    for i, t in enumerate(toks):
        w = _w(reading, t)
        if w and w.morph and w.morph.lemma == "यद्" and out and out[-1].text not in PUNCT | {"and", "or", "O"} \
                and out[-1].text.lower() not in ("by", "to", "in", "with", "from", "of"):
            out.append(Tok(","))
        out.append(t)
    return out


def vocatives(toks, reading):
    """'O sage' is set off by commas."""
    out = []
    for i, t in enumerate(toks):
        w = _w(reading, t)
        glued = (i + 1 < len(toks) and toks[i + 1].text == "-") or (i and toks[i - 1].text == "-")
        if w and w.role == "सम्बोधन" and not w.in_compound and not glued:
            mod = bool(out) and out[-1].word is not None and reading.words[out[-1].word].head == t.word
            if out and out[-1].text not in PUNCT and out[-1].text != "O" and not mod:
                out.append(Tok(","))
            out.append(t)
            nxt = toks[i + 1] if i + 1 < len(toks) else None
            if nxt and nxt.text not in PUNCT and not (nxt.word is not None and _w(reading, nxt).role == "सम्बोधन"):
                out.append(Tok(","))
            continue
        out.append(t)
    return out


def instrument_with(toks, reading):
    """An instrument of an active verb is "with" (with an arrow); "by" stays for agents and causes of participles."""
    out = list(toks)
    for i, t in enumerate(out[1:], 1):
        w = _w(reading, t)
        prev = out[i - 1]
        if w and w.role == "करण" and prev.word is None and prev.text == "by" and w.head is not None \
                and 0 <= w.head < len(reading.words):
            h = reading.words[w.head].morph
            if h is not None and h.kind == "tinanta" and (h.prayoga or "") not in ("कर्मणि", "भावे"):
                out[i - 1] = Tok("with")
    return out


def apposition(toks, reading):
    """Qualifiers that follow a proper name are set off by commas."""
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        out.append(t)
        if _is_name(_w(reading, t)) and i + 1 < len(toks):
            j = i + 1
            while j < len(toks) and toks[j].word is not None and reading.words[toks[j].word].role == "विशेषण" \
                    and reading.words[toks[j].word].head == t.word:
                j += 1
            if j > i + 1:
                out += [Tok(",")] + toks[i + 1:j]
                if j < len(toks) and toks[j].text not in PUNCT:
                    out.append(Tok(","))
                i = j
                continue
        i += 1
    return out


def coordination(toks, reading):
    """'a, b, c, d' / ', and b, and c' of three or more predicates or qualifiers -> 'a, b, c and d'."""
    items, cur = [], []
    for t in toks:
        if t.text == ",":
            items.append(cur)
            cur = []
        else:
            cur.append(t)
    items.append(cur)

    def adjectival(it: list[Tok], first: bool = False) -> bool:
        body = [t for t in it if not (t.word is None and t.text in ("and", "also", ".", "?", "!"))]
        ok = [t for t in body if t.word is not None and reading.words[t.word].role in _ADJ]
        return bool(body) and (all(t.word is not None and reading.words[t.word].role in _ADJ for t in body)
                               if not first else bool(ok) and body[-1] in ok)

    k, nocomma = 0, set()
    while k < len(items):
        if not adjectival(items[k], True):
            k += 1
            continue
        e = k + 1
        while e < len(items) and adjectival(items[e]):
            e += 1
        if e - k >= 3 and e == len(items):
            for n in range(k + 1, e):
                items[n] = [t for t in items[n] if not (t.word is None and t.text == "and")]
            items[e - 1] = [Tok("and")] + items[e - 1]
            nocomma.add(e - 1)
        k = max(e, k + 1)
    out: list[Tok] = []
    for n, it in enumerate(items):
        if n and n not in nocomma:
            out.append(Tok(","))
        out += it
    return out


def questions(toks, reading):
    """Sentence-initial question word that is not the subject: move the auxiliary up (inversion)."""
    if not toks or toks[0].word is None or toks[0].text.lower() not in _WH or "?" not in [t.text for t in toks]:
        return toks
    w = reading.words[toks[0].word]
    if w.role == "कर्ता":
        return toks
    k = next((i for i, t in enumerate(toks) if i > 1 and t.word is None and t.text in _AUX), None)
    if k is None or any(t.text in PUNCT for t in toks[:k]):
        return toks
    return [toks[0], toks[k]] + toks[1:k] + toks[k + 1:]


def _phrase_start(toks, i, t, reading) -> int:
    j = i
    while j > 0 and toks[j - 1].word is not None and reading.words[toks[j - 1].word].head == t.word \
            and (reading.words[toks[j - 1].word].role == "विशेषण" or reading.words[toks[j - 1].word].in_compound) \
            and toks[j - 1].text.lower() not in ("with", "without"):
        j -= 1
    return j


def articles(toks, reading):
    """'the' / 'a' before singular common-noun phrases; never before names, pronouns, plurals or mass nouns."""
    ins: dict[int, str] = {}
    for i, t in enumerate(toks):
        w = _w(reading, t)
        m = w.morph if w else None
        if not (m and m.kind == "subanta" and w.gloss and not w.in_compound) or _pronoun(w):
            continue
        if _is_name(w) and not (m.vacana == "बहुवचन" and t.text.endswith("s") and " " not in t.text):
            continue  # a plural name takes "the" (the Pāṇḍavas); a single name never does
        g = w.gloss.lower().split()[0]
        if m.krt or g in _ADJ_WORDS:
            continue
        if w.role == "विधेय" and not t.text.lower().endswith(_AGENT_END):
            continue
        plural_name = _is_name(w) and m.vacana == "बहुवचन"
        if plural_name:
            ins[_phrase_start(toks, i, t, reading)] = "the"
            continue
        if w.role in _NOUN_SKIP or m.vacana != "एकवचन" or w.gloss.lower() in _MASS or m.vibhakti == "सम्बोधन":
            continue
        if t.text.lower().split()[0] in _MASS | {"this", "that"} or t.text.endswith(("ing",)) and w.role == "विधेय":
            continue
        j = i
        while j > 0 and toks[j - 1].word is not None and reading.words[toks[j - 1].word].head == t.word \
                and (reading.words[toks[j - 1].word].role == "विशेषण" or reading.words[toks[j - 1].word].in_compound) \
            and toks[j - 1].text.lower() not in ("with", "without"):
            j -= 1
        prev = toks[j - 1].text.lower() if j else ""
        if prev in _DET or prev.endswith("'s") or prev in ("of", "-") or toks[j].text.lower() in _DET:
            continue
        if j and toks[j - 1].word is not None and (toks[j - 1].text.lower().split()[0] in _PREP_START
                                                   or _is_name(_w(reading, toks[j - 1]))):
            continue
        if any(_is_name(_w(reading, x)) or (x.word is not None and reading.words[x.word].role == "सम्बन्ध")
               for x in toks[j:i]):
            continue
        first = toks[j].text.lstrip("[").lower()
        ins[j] = ("an" if first[:1] in "aeiou" else "a") if w.role == "विधेय" else "the"
    out: list[Tok] = []
    for i, t in enumerate(toks):
        if i in ins:
            out.append(Tok(ins[i]))
        out.append(t)
    return out


def tidy(toks, reading):
    """No dangling conjunctions or prepositions, no doubled commas, final punctuation, capitals."""
    ts = [t for t in toks if t.text]
    ends = {".", "?", "!"}
    asks = bool(ts) and ts[-1].text == "?"
    while ts and ts[-1].text in ends | {",", ";"}:
        ts.pop()
    while ts and ts[-1].word is None and ts[-1].text.lower() in _DANGLING | {"O"}:
        ts.pop()
    while ts and ts[0].word is None and ts[0].text.lower() in {"and", "or", "but", ",", ";"}:
        ts.pop(0)
    out: list[Tok] = []
    for t in ts:
        if t.text in {",", ";"} and out and out[-1].text in {",", ";"}:
            continue
        if t.text == "," and out and out[-1].word is None and out[-1].text in ("of", "to", "by", "in") and False:
            continue
        out.append(t)
    if out:
        out.append(Tok("?" if asks else "."))
    cap = True
    for i, t in enumerate(out):
        if cap and t.text[:1].isalpha():
            out[i] = replace(t, text=t.text[0].upper() + t.text[1:])
        cap = t.text in ends if t.text in PUNCT else (cap and not t.text[:1].isalpha())
    return out


RULES: tuple[Rule, ...] = (unbracket, instrument_with, smooth_compounds, possessive_names, verb_agreement, relative_clauses,
                           vocatives, apposition, coordination, questions, articles, tidy)


# ---------------------------------------------------------------- driver

def _renderings(toks: list[Tok]) -> list[Rendering]:
    return [Rendering(t.word, t.text) for t in toks if t.word is not None]


def _failures(reading: Reading, text: str, toks: list[Tok], exact=None) -> list[Failure]:
    return run_checks(reading, text, _renderings(toks), {}, exact)[1]


def rewrite(reading: Reading) -> tuple[Reading, list[Alignment]]:
    """A copy of ``reading`` with ``reworded`` filled, and the exact spans of the aligned words in it.

    ``translation`` and ``alignment`` are untouched. If a check fails that the template itself passes,
    ``reworded`` stays empty and ``reworded_note`` names the check.
    """
    if not reading.translation or not reading.alignment:
        return reading, []
    base = tokenize(reading)
    toks = base
    for rule in RULES:
        toks = rule(toks, reading)
    text, spans = render(toks)
    aligned = sorted(t.word for t in toks if t.word is not None)
    if aligned != sorted(a.word for a in reading.alignment):
        return replace(reading, reworded="", reworded_note="rule-based; check failed: alignment: an aligned word was lost"), []
    already = {str(f) for f in _failures(reading, reading.translation, base, reading.alignment)}
    new = [f for f in _failures(reading, text, toks, spans) if str(f) not in already]
    if new:
        return replace(reading, reworded="", reworded_note=f"rule-based; check failed: {new[0]}"), []
    return replace(reading, reworded=text, reworded_note=NOTE_OK), spans
