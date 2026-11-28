"""Context-dependent senses and supplied words of the literal line (translate_sense), through the pipeline."""

import pytest

from mayur import pipeline

CASES = [
    ("माता पुत्राय फलं यच्छति", "gives"),            # यम् with a dative receiver
    ("पिता पुत्राय धनं यच्छति", "gives"),
    ("नद्यां मत्स्याः तरन्ति", "swim"),              # तॄ with the water in the locative
    ("बालकाः नद्यां तरन्ति", "swim"),
    ("बालकः संस्कृतं वदति", "Sanskrit"),             # a participle that names the language
    ("सा बालिका गीतं गायति", "sings song"),          # a participle used as a noun
    ("बालकः स्वगृहं गच्छति", "[his] own"),           # स्व refers to the subject
    ("सीता स्वपुत्रं पश्यति", "[her] own"),
    ("रामः हस्ताभ्यां धनुः गृह्णाति", "[his] two hands"),  # a body part as instrument
    ("बालकः हस्तेन फलं खादति", "[his] hand"),
    ("मामकाः पाण्डवाश्चैव किमकुर्वत", "my [men]"),   # an adjective of possession as head
    ("रामे वनं गते सीता अरोदीत्", "had gone to forest"),  # the object of the absolute participle
    ("धर्मो रक्षति रक्षितः", "when protected"),      # a participle after the verb
]


@pytest.mark.parametrize("text,expect", CASES)
def test_literal_line_has(text, expect):
    reading = pipeline.analyze_verse(text).readings[0]
    assert expect in reading.translation


def test_fluent_keeps_pronouns_of_literal():
    reading = pipeline.analyze_verse("सीता स्वपुत्रं पश्यति").readings[0]
    assert reading.reworded == "Sītā sees her own son."
