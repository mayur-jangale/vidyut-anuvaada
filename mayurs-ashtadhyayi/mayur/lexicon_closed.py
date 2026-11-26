"""A few closed sets of forms the kosha lacks or vidyut derives otherwise. All strings Devanagari.

* लक्ष्मीः, तन्त्रीः, तरीः, अवीः, स्तरीः: ई-stems formed with an उणादि suffix, not with ङी, so the
  nominative singular keeps its सु (6.1.68 हल्ङ्याब्भ्यो… does not apply). vidyut derives the form
  from the plain stem; the kosha lists these words only as ङी-stems.
* इमानि: नपुंसक प्रथमा/द्वितीया बहुवचन of इदम् (7.2.109 दश्च, 7.1.20 जश्शसोः शिः, 6.4.8). vidyut's
  Python API yields इदानि here, so the form is given as a listed form and is not proof-verified.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge
from mayur.model import Morph

UNADI_I = ("लक्ष्मी", "तन्त्री", "तरी", "अवी", "स्तरी")
IMANI_NOTE = ("इदम् नपुंसक बहुवचन: इद → इम by 7.2.109 दश्च, शि for जस्/शस् by 7.1.20, नुम् and दीर्घ by 7.1.72, 6.4.8; "
              "vidyut's Python API derives इदानि instead, so this listed form is not proof-verified")


@lru_cache(maxsize=1)
def _table() -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    for stem in UNADI_I:
        for pada, template in bridge.subanta_paradigm(stem, "स्त्रीलिङ्ग"):
            if (template.vibhakti, template.vacana) != ("प्रथमा", "एकवचन"):
                continue
            for text in bridge.derived_texts(pada):
                if text == stem + "स्":
                    table.setdefault(text, []).append(replace(template, form=text, stem=stem, quality=3))
    for vibhakti in ("प्रथमा", "द्वितीया"):
        table.setdefault("इमानि", []).append(Morph(
            form="इमानि", lemma="इदम्", kind="subanta", linga="नपुंसकलिङ्ग", vibhakti=vibhakti, vacana="बहुवचन",
            source="special", quality=3, handle=("special", IMANI_NOTE)))
    return {k: tuple(v) for k, v in table.items()}


def closed_forms(form: str) -> tuple[Morph, ...]:
    return _table().get(form, ())


KAP_NOTE = ("{base} + कप् (5.4.153 नद्यृतश्च कप्: after a stem in ई, ऊ or ऋ at the end of a बहुव्रीहि); the stem "
            "{stem} is inflected by vidyut, the suffixation itself is not derived")


@lru_cache(maxsize=2048)
def _kap_paradigm(stem: str, linga: str) -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    for pada, template in bridge.subanta_paradigm(stem, linga):
        for text in bridge.derived_texts(pada):
            table.setdefault(text, []).append(replace(template, form=text, lemma=stem, stem=stem, quality=2))
    return {k: tuple(v) for k, v in table.items()}


def kap_padas(form: str, is_stem) -> tuple[Morph, ...]:
    """-लक्ष्मीकः, -स्त्रीकः, -कर्तृकः: the last member of a बहुव्रीहि with कप्."""
    from mayur import lipi
    from mayur.lexicon_gen import _ENDINGS

    sounds = lipi.varnas(form)
    out: list[Morph] = []
    for ending, stem_end, lingas in _ENDINGS:
        ev = lipi.varnas(ending)
        if stem_end != "अ" or len(sounds) <= len(ev) + 3 or sounds[-len(ev):] != ev:
            continue
        stem = sounds[:-len(ev)] + ("अ",)
        if stem[-2] != "क्" or stem[-3] not in ("ई", "ऊ", "ऋ") or not is_stem(lipi.from_varnas(stem[:-2])):
            continue
        text = lipi.from_varnas(stem)
        for linga in lingas:
            out.extend(_kap_paradigm(text, linga).get(form, ()))
    return tuple(dict.fromkeys(out))
