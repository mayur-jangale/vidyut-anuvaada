"""Forms a rule gives only in context are proved in two steps, and only where the rule's condition holds."""

import pytest

from mayur import pipeline


def _word(text, form):
    analysis = pipeline.analyze_verse(text)
    return analysis, next(w for w in analysis.readings[0].words if w.form == form)


@pytest.mark.parametrize("text, form, rule", [
    ("रामो मे प्रियः", "मे", "8.1.22"), ("पिता ते गच्छति", "ते", "8.1.22"), ("देवो नः पातु", "नस्", "8.1.21"),
    ("स गच्छति", "स", "6.1.132"), ("स इच्छति", "स", "8.3.19"), ("महाराजो गच्छति", "महा", "6.3.46"),
])
def test_contextual_form_is_proved_with_its_rule(text, form, rule):
    analysis, word = _word(text, form)
    assert word.proof.derivable and rule in word.proof.method
    assert rule.split(",")[0] in {step.code for step in word.proof.trace}
    assert analysis.status == "verified"


@pytest.mark.parametrize("text, form", [
    ("मे प्रियो रामः", "मे"),   # 8.1.18: an enclitic does not stand first
    ("त्वा नमामि", "त्वा"),
])
def test_enclitic_at_the_start_stays_unverified(text, form):
    analysis, word = _word(text, form)
    assert not word.proof.derivable and analysis.status == "unverified"
