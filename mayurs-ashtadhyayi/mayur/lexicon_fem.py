"""Feminine padas of adjectives and bahuvrīhis the kosha lists only in the masculine/neuter
(सुन्दरास्, मुखी, पराङ्मुखी, साध्वी).

The feminine stem (ई or आ) is guessed from the ending; it is tried only when the kosha knows the
masculine base, and kept only when vidyut's forward derivation of the ङ्याप् stem in some case and
number yields exactly the form. The lemma is the feminine stem (``mayur.ud`` matches it with the
base the corpus cites). All strings Devanagari.
"""

from __future__ import annotations

from dataclasses import replace
from functools import lru_cache

from mayur import bridge
from mayur.model import Morph

# (ending of the form, ending of the feminine stem, how the masculine base ends)
_E_I = ("ी", "ीम्", "्या", "्यै", "्यास्", "्याम्", "ि", "्यौ", "्यस्", "ीस्", "ीभिस्", "ीभ्यस्", "ीनाम्", "ीणाम्", "ीषु")
_E_A = ("ास्", "ाम्", "या", "ायै", "ायास्", "ायाम्", "ाभिस्", "ाभ्यस्", "ानाम्", "ाणाम्", "ासु", "ा")
# masculine bases: an a-stem (मुख), a u-stem written with व् before the ending (साध्व् -> साधु)
_MIN_BASE = 2


def _known_base(base: str) -> bool:
    """The kosha lists ``base`` as a nominal stem (its masculine nominative, or as a stem)."""
    return any(e.entry in ("basic", "krdanta") and not e.is_avyaya for e in bridge.lookup(base + "स्"))


@lru_cache(maxsize=1024)
def _paradigm(fem: str) -> dict[str, tuple[Morph, ...]]:
    table: dict[str, list[Morph]] = {}
    for pada, template in bridge.subanta_paradigm(fem, "स्त्रीलिङ्ग", nyap=True):
        for text in bridge.derived_texts(pada):
            table.setdefault(text, []).append(replace(template, form=text, quality=2))
    return {k: tuple(v) for k, v in table.items()}


def _candidates(form: str) -> list[tuple[str, str]]:
    """(feminine stem, lemma): the lemma is the feminine stem, except for u-stems, where the corpus'
    masculine base is kept (``mayur.ud`` relates only ई/आ feminines to a-stems)."""
    out = []
    for endings, fem_end in ((_E_I, "ी"), (_E_A, "ा")):
        for ending in endings:
            if form.endswith(ending) and len(form) - len(ending) >= _MIN_BASE:
                base = form[: -len(ending)]
                if "क" <= base[-1] <= "ह" and _known_base(base):
                    out.append((base + fem_end, base + fem_end))
                if fem_end == "ा" and base.endswith("िक") and _known_base(base[:-2] + "क"):
                    out.append((base + "ा", base + "ा"))  # बालक -> बालिका (7.3.44 प्रत्ययस्थात्कात्पूर्वस्यात इदाप्यसुपः)
                if fem_end == "ी" and base.endswith("्व") and _known_base(base[:-2] + "ु"):
                    out.append((base + "ी", base[:-2] + "ु"))  # साधु -> साध्वी (4.1.44 वोतो गुणवचनात्)
    return list(dict.fromkeys(out))


def feminine_padas(form: str) -> tuple[Morph, ...]:
    """Forward-derived feminine analyses of ``form`` (quality 2)."""
    out: list[Morph] = []
    for fem, lemma in _candidates(form):
        out.extend(replace(m, lemma=lemma) for m in _paradigm(fem).get(form, ()))
    return tuple(out)
