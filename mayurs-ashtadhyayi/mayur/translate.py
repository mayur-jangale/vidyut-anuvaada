"""Literal English built by template from the grammatical analysis; every content word is aligned."""

from __future__ import annotations

from dataclasses import replace

from . import english
from .model import Alignment, Reading
from .translate_core import _CONNECTIVES, _PREP, Piece, _p, _Renderer

_KIM = {"किम्", "क", "कः", "कस्"}


def _compose(pieces: list[Piece]) -> tuple[str, list[Alignment]]:
    out = ""
    spans: dict[int, Alignment] = {}
    for text, idx, sep in pieces:
        text = " ".join(text.split()) if text else ""
        if not text or (idx is not None and idx in spans):
            continue
        if text in (",", ";") and out.endswith((",", ";")):
            continue  # a participial phrase closes with a comma that another comma already supplies
        if out:
            out += sep
        start = len(out)
        out += text
        if idx is not None and idx not in spans:
            spans[idx] = Alignment(idx, start, len(out))
    return out.rstrip(",; "), sorted(spans.values(), key=lambda a: a.start)


def _copular(r: "_Renderer", top) -> list[Piece]:
    """A verbless sentence: subject, supplied copula, predicates (X च Y -> 'X, and Y')."""
    n = len(r.words)
    for ch in r.children.values():
        ch.sort(key=lambda k: r.pos[k])
    roots = [i for i in r.order if top(i) and not r.words[i].in_compound
             and (r.words[i].head is None or not 0 <= r.words[i].head < n)]
    subj = [i for i in roots if r.role(i) == "कर्ता"] or [i for i in roots if r.role(i) not in ("विधेय", "सम्बोधन")][:1]
    pred = [i for i in roots if r.role(i) == "विधेय"]
    out: list[Piece] = []
    for i in roots:
        if r.role(i) == "सम्बोधन":
            out += [_p("O")] + r.np(i) + [_p(",", None, "")]
    mods = ("विशेषण", "सम्बन्ध")
    for s in subj:
        kids = r.children.get(s, [])
        pred += [k for k in kids if r.role(k) == "विधेय"]
        out += r.np(s, [k for k in kids if r.role(k) in mods])
        for k in kids:
            if r.role(k) in mods or r.role(k) == "विधेय":
                continue
            sm_ = r.words[s].morph
            if r.role(k) == "कर्ता" and sm_ is not None and sm_.krt in ("क्त", "क्तवतु"):
                out += [_p("by")] + r.np(k)
            else:
                out += r.case_phrase(k) if r.role(k) in _PREP else r.np(k)
    sm = r.words[subj[0]].morph if subj else None
    if pred:
        pl = bool(sm and sm.vacana in ("बहुवचन", "द्विवचन"))
        if not subj:
            out.append(_p("[They are]" if any(r.words[k].morph and r.words[k].morph.vacana == "बहुवचन"
                                              for k in pred) else "[He is]"))
        else:
            out.append(_p("[are]" if pl or (sm and sm.purusha == "मध्यमपुरुष") else "[am]"
                      if sm and sm.lemma == "अस्मद्" else "[is]"))
    pred.sort(key=lambda k: r.pos[k])
    prev_pron = True
    for n_, k in enumerate(pred):
        pm = r.words[k].morph
        piece = r.np(k)
        has_conn = any(r.role(c) == "अव्यय" and r.text(c) in _CONNECTIVES for c in r.children.get(k, []))
        if piece and n_ and (has_conn or not prev_pron):
            piece[0] = (piece[0][0], piece[0][1], ", ")
            if piece[0][1] is None:
                piece[0] = (piece[0][0], None, ", ")
        out += piece
        prev_pron = bool(pm and english.is_pronoun(pm.lemma))
    for i in roots:
        if i not in subj and i not in pred and r.role(i) != "सम्बोधन":
            out += r.case_phrase(i) if r.role(i) in _PREP else r.np(i)
    return out


def render(reading: Reading) -> Reading:
    """A copy of ``reading`` with ``translation`` and ``alignment`` filled in."""
    if not reading.words:
        return replace(reading, translation="", alignment=[])
    r = _Renderer(reading)
    verbs = [i for i in r.order if r.role(i) == "क्रिया" and not r.words[i].in_compound]
    pieces: list[Piece] = []

    def top(i: int) -> bool:
        w = r.words[i]
        return not w.in_compound and r.role(i) not in ("विशेषण", "सम्बन्ध", "समासपूर्वपद")

    if verbs:
        first = verbs[0]
        for i in r.order:  # orphans attach to the first verb
            w = r.words[i]
            unattached = w.head is None or not 0 <= w.head < len(r.words)
            if top(i) and i not in verbs and unattached and r.role(i) not in ("", "पूर्वकालक्रिया"):
                r.children.setdefault(first, []).append(i)
        for ch in r.children.values():
            ch.sort(key=lambda k: r.pos[k])
        for n, v in enumerate(sorted(verbs, key=lambda k: r.pos[k])):
            pieces += ([_p(";", None, "")] if n else []) + r.clause(v, keep_conn=n > 0)
    else:
        pieces += _copular(r, top)
    for i in r.order:  # anything not yet consumed still appears, in prose order
        w = r.words[i]
        if i not in r.used and not w.in_compound:
            pieces += r.case_phrase(i) if r.role(i) in _PREP else r.np(i)
    for i in r.order:
        w = r.words[i]
        if w.in_compound and i not in r.used:
            r.used.add(i)
            pieces.append(_p(r.text(i), i))
    while pieces and (pieces[0][0] in _CONNECTIVES or not pieces[0][0]) and pieces[0][1] is not None:
        pieces = pieces[1:]  # never open a sentence with a dangling conjunction
    text, alignment = _compose(pieces)
    if text:
        k = next((n for n, ch in enumerate(text) if ch.isalpha()), 0)
        text = text[:k] + text[k].upper() + text[k + 1:]
        asks = any(w.morph is not None and not w.in_compound and w.morph.lemma in _KIM for w in reading.words)
        text += "" if text.endswith((".", "?", "!")) else ("?" if asks else ".")
    return replace(reading, translation=text, alignment=alignment)
