"""Reader-facing output must be Devanagari, not SLP1."""

from mayur import display, jsonout
from mayur.model import Morph, SutraStep


def test_terms_and_states_are_devanagari():
    assert display.term("praTamA") == "प्रथमा"
    assert display.term("puM") == "पुंलिङ्ग"
    assert display.term(None) == ""
    assert display.state("ni +  + ra + ta + m") == "नि + र + त + म्"


def test_sutra_text_lookup():
    assert display.sutra("azwADyAyI", "6.1.87")["devanagari"] == "आद्गुणः"
    assert display.sutra("azwADyAyI", "99.9.9")["devanagari"] == ""


def test_json_carries_devanagari_grammar_and_trace():
    morph = Morph(form="rAmas", lemma="rAma", kind="subanta", linga="puM", vibhakti="praTamA", vacana="eka")
    analysis = jsonout._analysis_json(morph)
    assert analysis["devanagari"]["case"] == "प्रथमा"
    assert analysis["devanagari"]["lemma"] == "राम"
    step = jsonout._step_json(SutraStep("azwADyAyI", "6.1.87", "rAma + s"))
    assert step["sutra"]["devanagari"] == "आद्गुणः"
    assert step["result_devanagari"] == "राम + स्"
