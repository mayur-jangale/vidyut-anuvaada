"""Closed paradigms the kosha lists wrongly or not at all, forward-derived once and cached.

* पुंस्: the kosha lists the bare stem as a pada; vidyut derives the real forms (पुमान्, पुमांसम्:
  7.1.89 पुंसोऽसुङ्, 7.1.70, 6.4.10, 8.2.23).
* त्व: the corpus often cites an abstract noun X-त्व as X + त्व (5.1.119 तस्य भावस्त्वतलौ); the member
  त्व is then declined alone (त्वात्, त्वे). vidyut's basic stem त्व is the sarvanāma (1.1.27), so
  the endings are read off vidyut's forward derivation of the taddhitānta भव + त्व and the
  analysis is "special" (not derivable as a free word). Quality 2: the pronoun stays first for त्वम्.
* kaṇḍvādi dhātus (3.1.27 कण्ड्वादिभ्यो यक्): महीयते, which the kosha lacks.

Apart from the त्व member (source "special"), every analysis is an exact match of a vidyut forward
derivation. All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge
from mayur.model import Morph

# (stem as vidyut spells it, lemma, gender): पुम्स् because vidyut needs म् (7.1.89), not ं
_STEMS = (("पुम्स्", "पुंस्", "पुंलिङ्ग"),)
_TVA_NOTE = ("the taddhita त्व (5.1.119 तस्य भावस्त्वतलौ) cited by the corpus as its own member; its ending "
             "is that of vidyut's derivation of भवत्व in the same case, since vidyut's bare त्व is the "
             "सर्वनाम (1.1.27)")
_TA_NOTE = ("the taddhita तल् (5.1.119 तस्य भावस्त्वतलौ), feminine -ता, cited by the corpus as its own member; "
            "its ending is that of vidyut's derivation of भवता in the same case")
# कण्ड्वादि roots in their Dhatupatha form, with the text every form of them contains (the gate)
_KANDVADI = (("महीङ्", "महीय"),)


@lru_cache(maxsize=1)
def _nominal_table() -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    for stem, lemma, linga in _STEMS:
        for pada, template in bridge.subanta_paradigm(stem, linga):
            for text in bridge.derived_texts(pada):
                table.setdefault(text, []).append(replace(template, form=text, lemma=lemma, quality=3))
    for suffix, lemma, linga, note in (("त्व", "त्व", "नपुंसकलिङ्ग", _TVA_NOTE), ("तल्", "ता", "स्त्रीलिङ्ग", _TA_NOTE)):
        for pada, template in bridge.subanta_paradigm("भव", linga, taddhita=suffix):
            for text in bridge.derived_texts(pada):
                if text.startswith("भवत"):
                    member = text[len("भव"):]
                    table.setdefault(member, []).append(replace(
                        template, form=member, lemma=lemma, source="special", quality=2, handle=("special", note)))
    return {k: tuple(dict.fromkeys(v)) for k, v in table.items()}


@lru_cache(maxsize=None)
def _kandvadi_table(aupadeshika: str) -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    for text, m in bridge.kandvadi_paradigm(aupadeshika):
        table.setdefault(text, []).append(replace(m, form=text))
    return {k: tuple(dict.fromkeys(v)) for k, v in table.items()}


def closed_paradigms(form: str) -> tuple[Morph, ...]:
    """Analyses of ``form`` from the closed paradigms above (cheap: a dict probe after one build)."""
    out = list(_nominal_table().get(form, ()))
    for aupadeshika, gate in _KANDVADI:
        if gate in form:
            out.extend(_kandvadi_table(aupadeshika).get(form, ()))
    return tuple(out)
