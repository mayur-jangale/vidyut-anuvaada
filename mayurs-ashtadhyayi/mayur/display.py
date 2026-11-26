"""Devanagari presentation of grammar terms, sutras and derivation states.

SLP1 is only the internal encoding; everything a reader sees goes through here.
"""

from __future__ import annotations

from functools import lru_cache

from mayur import resources
from mayur.translit import to_deva

# Fuller traditional names where the vidyut value is an abbreviation.
TERMS = {
    "puM": "पुंलिङ्ग",
    "strI": "स्त्रीलिङ्ग",
    "napuMsaka": "नपुंसकलिङ्ग",
    "eka": "एकवचन",
    "dvi": "द्विवचन",
    "bahu": "बहुवचन",
    "praTama": "प्रथमपुरुष",
    "maDyama": "मध्यमपुरुष",
    "uttama": "उत्तमपुरुष",
    "subanta": "सुबन्त",
    "tinanta": "तिङन्त",
    "avyaya": "अव्यय",
    "stem": "प्रातिपदिक",
    "unknown": "अज्ञात",
}


def term(value: str | None) -> str:
    """Devanagari name of a grammatical category value (``praTamA`` -> ``प्रथमा``)."""
    if not value:
        return ""
    return TERMS.get(value) or to_deva(value)


def state(result: str) -> str:
    """A derivation state in Devanagari; empty (elided) terms are dropped."""
    return " + ".join(to_deva(part) for part in result.split(" + ") if part.strip())


@lru_cache(maxsize=1)
def _sutras() -> dict[tuple[str, str], str]:
    from vidyut.prakriya import Data

    data = Data(str(resources.vidyut_dir() / "prakriya"))
    return {(str(s.source), s.code): s.text for s in data.load_sutras()}


def sutra_text(source: str, code: str) -> str:
    """SLP1 text of a rule, or "" if vidyut's sutrapatha does not list it."""
    return _sutras().get((source, code), "")


def sutra(source: str, code: str) -> dict[str, str]:
    text = sutra_text(source, code)
    return {"slp1": text, "devanagari": to_deva(text) if text else "", "source_devanagari": to_deva(source)}
