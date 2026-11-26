"""Coordination and question rules of the fluent layer (see ``fluent`` for the driver)."""

from __future__ import annotations

from .fluent_checks import unrendered
from .fluent_tok import PUNCT, Tok, _w

_ADJ = {"विशेषण", "विधेय"}
_AUX = {"is", "are", "am", "was", "were", "will", "shall", "do", "did", "does", "has", "have"}
_WH = {"who", "what", "whom", "whose", "which"}


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


def drop_particles(toks, reading):
    """Emphatic particles (fluent_checks.UNRENDERED_PARTICLES: एव, हि, वै ...) are left out of the fluent line."""
    return [t for t in toks if t.word is None or not unrendered(reading, t.word)]


_NOMINAL_ROLES = {"कर्ता", "कर्म", "करण", "सम्प्रदान", "अपादान", "अधिकरण", "सम्बोधन", "सम्बन्ध"}


def unglossed(toks, reading):
    """A word the glossary lacks stays as its IAST: without angle brackets, capitalised as a name when it
    stands as a noun (कर्ता, कर्म, ...)."""
    out = []
    for t in toks:
        w = _w(reading, t)
        if w is not None and not w.gloss and t.text:
            text = t.text.strip("⟨⟩")
            if w.role in _NOMINAL_ROLES and (w.morph is None or w.morph.kind == "subanta") and text[:1].islower():
                text = text[0].upper() + text[1:]
            t = Tok(text, t.word, t.glue)
        out.append(t)
    return out
