"""Frequency lookups against hand-made tables."""

import pytest

from mayur import freq
from mayur.model import Morph

TABLES = {
    "freq.json": {"forms": {"रामस्": 5}, "lemmas": {"राम": 7}, "tokens": 100},
    "lemma_class.json": {"राम": "noun"},
    "form_tags.json": {"रामस्": {"राम|NOUN|Case=Nom|Gender=Masc|Number=Sing": 4,
                                 "राम|NOUN|Case=Voc|Gender=Masc|Number=Sing": 1}},
}


@pytest.fixture
def tables(monkeypatch):
    monkeypatch.setattr(freq, "derived", lambda name: TABLES.get(name, {}))
    freq._parsed.cache_clear()
    yield
    freq._parsed.cache_clear()


def test_counts(tables):
    assert freq.form_count("रामस्") == 5 and freq.form_count("सीता") == 0
    assert freq.lemma_count("राम") == 7 and freq.total_tokens() == 100
    assert freq.lemma_class("राम") == "noun" and freq.lemma_class("सीता") == ""


def test_analysis_count(tables):
    nom = Morph(form="रामस्", lemma="राम", kind="subanta", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन")
    acc = Morph(form="रामस्", lemma="राम", kind="subanta", linga="पुंलिङ्ग", vibhakti="द्वितीया", vacana="एकवचन")
    other = Morph(form="रामस्", lemma="रम", kind="subanta", vibhakti="प्रथमा")
    assert freq.analysis_count(nom) == 4
    assert freq.analysis_count(acc) == 0
    assert freq.analysis_count(other) == 0


def test_missing_tables(monkeypatch):
    monkeypatch.setattr(freq, "derived", lambda name: {})
    freq._parsed.cache_clear()
    assert freq.form_count("रामस्") == 0 and freq.total_tokens() == 0 and freq.lemma_class("राम") == ""
    assert freq.analysis_count(Morph(form="रामस्", lemma="राम", kind="subanta")) == 0
    freq._parsed.cache_clear()
