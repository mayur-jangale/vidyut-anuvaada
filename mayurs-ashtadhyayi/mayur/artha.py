"""The meaning a derived word has by virtue of its derivation (प्रत्ययार्थ), read off its rule trace.

In the Ashtadhyayi the rule that introduces a suffix also states the sense in which it is
introduced: 3.2.123 वर्तमाने लट्, 5.2.94 तदस्यास्त्यस्मिन्निति मतुप्, 3.1.26 हेतुमति च ... The table
``annotations/suffix_senses.json`` (our own annotation, CC BY-SA 4.0) gives, for each such rule,
the suffix, the sense in Sanskrit and an English template. A sense is stated only when its rule
occurs in the word's trace; without a trace, only when the Morph's own fields name the suffix
(``krt``, ``lakara``, ``prayoga``), and the rule cited is then the one that introduces that suffix.
"""

from __future__ import annotations

import dataclasses
import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any

from . import english, gloss
from .model import Morph, Reading, SutraStep, Word, WordProof

_TABLE = Path(__file__).parent / "annotations" / "suffix_senses.json"
_NASAL = "ँ"
LABEL_KINDS = ("lakara", "prayoga", "stri", "vibhakti", "samasanta")


@dataclass(frozen=True)
class Part:
    sutra: str  # rule number, e.g. "5.2.94"
    pratyaya: str  # the suffix (or voice) the rule introduces, Devanagari
    sense_sa: str  # the sense, as the rule (or its adhikara) states it
    english: str  # English name of the sense


@dataclass(frozen=True)
class DerivedMeaning:
    parts: tuple[Part, ...] = ()
    sanskrit: str = ""  # e.g. "गुण + मतुप् — तदस्यास्त्यस्मिन् (5.2.94)"
    english: str = ""  # e.g. "possessing virtue [5.2.94]"


EMPTY = DerivedMeaning()


@lru_cache(maxsize=1)
def table() -> dict[str, dict[str, Any]]:
    """Rule number -> entry of the suffix-sense table (keys starting with "_" are metadata)."""
    try:
        raw = json.loads(_TABLE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return {k: v for k, v in raw.items() if not k.startswith("_")}


def _terms(state: str) -> list[str]:
    return [t.strip() for t in state.split(" + ")]


def _added(before: str, after: str) -> str:
    """The term present in ``after`` but not in ``before`` (anubandha nasal removed), or ""."""
    rest = _terms(before)
    for t in _terms(after):
        if t in rest:
            rest.remove(t)
        elif t:
            return t.replace(_NASAL, "")
    return ""


def _pratyayas(entry: dict[str, Any]) -> list[str]:
    return [p.strip() for p in str(entry.get("pratyaya", "")).split(",")]


# --- English rendering -------------------------------------------------------------------------

def _on_first(phrase: str, fn: Any) -> str:
    first, _, rest = phrase.partition(" ")
    return fn(first) + (" " + rest if rest else "")


def _third(m: Morph) -> bool:
    return (m.purusha in (None, "प्रथमपुरुष")) and (m.vacana in (None, "एकवचन"))


def _imperative(v: str, m: Morph) -> str:
    if m.purusha == "मध्यमपुरुष":
        return v + "!"
    if m.purusha == "उत्तमपुरुष":
        return f"let {'me' if m.vacana in (None, 'एकवचन') else 'us'} {v}"
    return f"let {'him' if m.vacana in (None, 'एकवचन') else 'them'} {v}"


# English forms the helpers in ``english`` do not get right: (3sg present, past, participle, -ing)
_FORMS = {"be": ("is", "was", "been", "being"), "flee": ("flees", "fled", "fled", "fleeing"),
          "shoot": ("shoots", "shot", "shot", "shooting"), "born": ("is born", "was born", "born", "being born"),
          "see": ("sees", "saw", "seen", "seeing"), "lie": ("lies", "lay", "lain", "lying"),
          "slay": ("slays", "slew", "slain", "slaying"), "strike": ("strikes", "struck", "struck", "striking")}
_PARTICIPLES = {"born", "gone", "known", "fallen", "given", "taken", "bought", "fought", "sought", "slain", "risen"}


def _form(word: str, i: int) -> str:
    if word in _FORMS:
        return _FORMS[word][i]
    if i == 2 and (word in _PARTICIPLES or (word.endswith("ed") and len(word) > 4)):
        return word  # the gloss is already a participle
    fn = (english.third_singular, english.past, lambda w: english.krt_form("क्त", w),
          english.present_participle)[i]
    return fn(word)


def _present(v: str, m: Morph) -> str:
    first, _, rest = v.partition(" ")
    if first == "be" and not _third(m):
        word = "am" if m.purusha == "उत्तमपुरुष" and m.vacana in (None, "एकवचन") else "are"
        return word + (" " + rest if rest else "")
    return _on_first(v, lambda w: _form(w, 0)) if _third(m) else v


def _past(v: str, m: Morph) -> str:
    first, _, rest = v.partition(" ")
    if first == "be" and (m.vacana not in (None, "एकवचन") or m.purusha == "मध्यमपुरुष"):
        return "were" + (" " + rest if rest else "")
    return _on_first(v, lambda w: _form(w, 1))


def _slots(v: str, noun: str, m: Morph) -> dict[str, str]:
    pres3 = _on_first(v, lambda w: _form(w, 0)) if v else ""
    return {
        "base": v, "noun": noun, "pres3": pres3, "pres": _present(v, m) if v else "",
        "past": _past(v, m) if v else "",
        "pp": _on_first(v, lambda w: _form(w, 2)) if v else "",
        "ing": _on_first(v, lambda w: _form(w, 3)) if v else "",
        "agent": english.agent(v) if v and " " not in v else ("one who " + pres3 if v else ""),
        "imp": _imperative(v, m) if v else "", "is": "is" if _third(m) else "are",
    }


def _fill(template: str, v: str, noun: str, m: Morph) -> str:
    try:
        return template.format(**_slots(v, noun, m)).strip()
    except (KeyError, IndexError, ValueError):
        return ""


# dictionary glosses of roots that are agent nouns: the verb is wanted
_AGENT_GLOSS = {"slayer": "slay", "killer": "kill", "knower": "know", "doer": "do", "maker": "make", "ruler": "rule"}


def _verb_gloss(root: str, m: Morph) -> str:
    probe = Morph(form=root, lemma="".join(m.prefixes) + root, kind="tinanta", root=root,
                  prefixes=m.prefixes, root_gloss=None)
    g, _ = gloss.lookup(probe)
    if not g and root == m.root:
        g, _ = gloss.lookup(dataclasses.replace(m, stem="", krt=None, handle=None))
    g = english.base(g) if g else ""
    return _AGENT_GLOSS.get(g, g)


def _noun_gloss(stem: str) -> str:
    g, _ = gloss.lookup(Morph(form=stem, lemma=stem, kind="stem"))
    return g


# --- walking the trace ---------------------------------------------------------------------------

@dataclass(frozen=True)
class _Hit:
    step: SutraStep
    before: str
    entry: dict[str, Any]
    pratyaya: str


def _hits(trace: list[SutraStep]) -> list[_Hit]:
    rules, seen, out, before = table(), set(), [], ""
    for step in trace:
        entry = rules.get(step.code)
        if entry and step.code not in seen:
            seen.add(step.code)
            added = _added(before, step.result)
            names = _pratyayas(entry)
            pratyaya = added if added in names else names[0]
            out.append(_Hit(step, before, entry, pratyaya))
        before = step.result
    return out


_MARKS = str.maketrans("", "", "॒॑" + _NASAL)


def _base_terms(state: str, m: Morph, prefixes: bool = False) -> list[str]:
    terms = [t.translate(_MARKS) for t in _terms(state) if t]
    return terms if prefixes else ([t for t in terms if t not in m.prefixes] or terms)


def _compose(hits: list[_Hit], m: Morph) -> tuple[str, list[str], list[tuple[str, str]]]:
    """(English phrase, codes that shape the phrase, labels "sense [code]")."""
    first = hits[0]
    base = _base_terms(first.before, m)
    sanadi = any(h.entry["kind"] == "sanadi" for h in hits)
    nominal_base = first.entry["kind"] == "taddhita" or (sanadi and first.step.code in ("3.1.8", "3.1.11"))
    verb = ""
    if not nominal_base:
        root = base[-1] if (sanadi and base) else (m.root or (base[-1] if base else ""))
        verb = _verb_gloss(root, m)
    noun = _noun_gloss("".join(base)) if nominal_base else ""
    phrase, codes, labels, lakara, passive = "", [], [], None, False
    for h in hits:
        kind, entry, code = h.entry["kind"], h.entry, h.step.code
        template = entry.get("variants", {}).get(h.pratyaya, entry.get("template_en", ""))
        if kind == "sanadi" and (verb or noun or phrase):
            verb = _fill(template, verb, noun or phrase, m) or verb
            codes.append(code)
        elif kind in ("sanadi", "krt", "taddhita") and not (verb or noun or phrase):
            labels.append((entry["sense_en"], code))  # no English for the base: name the sense only
        elif kind == "krt" and template:
            phrase = _fill(template, verb, noun, m)
            verb, lakara = "", None
            codes.append(code)
        elif kind == "taddhita":
            phrase = _fill(template, verb, phrase or noun, m)
            codes.append(code)
        elif kind == "lakara":
            lakara = entry
        if kind == "prayoga" and entry.get("passive"):
            passive = True
        if kind in LABEL_KINDS or (kind == "krt" and not template):
            labels.append((entry["sense_en"], code))
    if lakara is not None and verb:
        phrase = _fill(lakara.get("template_passive_en", "") if passive else lakara["template_en"], verb, noun, m)
    elif not phrase:
        phrase = verb if sanadi else ""
    return phrase, codes, labels


def _english(phrase: str, codes: list[str], labels: list[tuple[str, str]]) -> str:
    head = f"{phrase} [{', '.join(codes)}]" if phrase and codes else phrase
    merged: dict[str, list[str]] = {}
    for sense, code in labels:
        merged.setdefault(sense, []).append(code)
    tail = "; ".join(f"{sense} [{', '.join(cs)}]" for sense, cs in merged.items())
    if head and tail:
        return f"{head}: {tail}"
    return head or tail


def _sanskrit(base: list[str], parts: tuple[Part, ...]) -> str:
    rules = table()
    suffixes = [p.pratyaya for p in parts if rules.get(p.sutra, {}).get("kind") != "prayoga"]
    chain = " + ".join(base + suffixes)
    senses = "; ".join(f"{p.sense_sa} ({p.sutra})" for p in parts)
    return f"{chain} — {senses}"


def _from_trace(m: Morph, trace: list[SutraStep]) -> DerivedMeaning:
    hits = _hits(trace)
    if not hits:
        return EMPTY
    parts = tuple(Part(h.step.code, h.pratyaya, h.entry["sense_sa"], h.entry["sense_en"]) for h in hits)
    phrase, codes, labels = _compose(hits, m)
    return DerivedMeaning(parts, _sanskrit(_base_terms(hits[0].before, m, prefixes=True), parts), _english(phrase, codes, labels))


# --- without a trace: the Morph's own fields ---------------------------------------------------

_LAKARA_RULE = {"लट्": "3.2.123", "लङ्": "3.2.111", "लिट्": "3.2.115", "लुङ्": "3.2.110", "लृट्": "3.3.13",
                "लुट्": "3.3.15", "विधिलिङ्": "3.3.161", "लोट्": "3.3.162", "आशीर्लिङ्": "3.3.173", "लृङ्": "3.3.139"}
_KRT_RULE = {"क्त": "3.2.102", "क्तवतु": "3.2.102", "शतृ": "3.2.124", "शानच्": "3.2.124", "तव्य": "3.1.96",
             "तव्यत्": "3.1.96", "अनीयर्": "3.1.96", "यत्": "3.1.97", "ण्यत्": "3.1.124", "क्यप्": "3.1.109",
             "तृच्": "3.1.133", "ण्वुल्": "3.1.133", "तुमुन्": "3.3.10", "क्त्वा": "3.4.21", "ल्यप्": "7.1.37",
             "घञ्": "3.3.18", "ल्युट्": "3.3.115", "क्तिन्": "3.3.94", "क्वसु": "3.2.107", "कानच्": "3.2.106",
             "णमुल्": "3.4.22", "तृन्": "3.2.135", "क्विप्": "3.2.76"}


def _from_fields(m: Morph) -> DerivedMeaning:
    rules, steps, root = table(), [], m.root or m.lemma
    state = " + ".join(list(m.prefixes) + [root])
    picks = []
    if m.krt and m.krt in _KRT_RULE:
        if m.krt == "ल्यप्":
            picks.append(("3.4.21", "क्त्वा"))
        picks.append((_KRT_RULE[m.krt], m.krt))
    elif m.lakara in _LAKARA_RULE:
        picks.append((_LAKARA_RULE[m.lakara], ""))
        if m.prayoga in ("कर्मणि", "भावे"):
            picks.append(("1.3.13", ""))
    for code, pratyaya in picks:
        if code not in rules:
            continue
        nxt = state + (" + " + pratyaya if pratyaya else "")
        steps.append(SutraStep("अष्टाध्यायी", code, nxt))
        state = nxt
    return _from_trace(m, steps) if steps and m.root else EMPTY


def derived_meaning(m: Morph | None, proof: WordProof | None) -> DerivedMeaning:
    """The sense ``m`` has by its derivation; ``EMPTY`` when no sense-giving rule applies."""
    if m is None:
        return EMPTY
    if proof is not None and proof.trace:
        return _from_trace(m, proof.trace)
    return _from_fields(m)


def annotate_word(word: Word) -> Word:
    meaning = derived_meaning(word.morph, word.proof)
    return dataclasses.replace(word, derived_meaning=meaning.english)


def annotate(reading: Reading) -> Reading:
    """A new Reading whose words carry ``derived_meaning``; nothing else changes."""
    return dataclasses.replace(reading, words=[annotate_word(w) for w in reading.words])
