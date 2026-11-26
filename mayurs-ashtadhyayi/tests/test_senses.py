import importlib.util
from collections import Counter
from pathlib import Path

from mayur import senses
from mayur.model import Morph, Reading, Word

_SPEC = importlib.util.spec_from_file_location(
    "build_senses", Path(__file__).resolve().parent.parent / "scripts" / "build_senses.py")
build = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(build)


def ctx(*neighbours: str, verb: str = "") -> senses.SenseContext:
    return senses.SenseContext(neighbours=tuple(neighbours), case="Nom/Sing", upos="N", verb=verb)


def tiny_records() -> list:
    rows = []
    for _ in range(12):
        rows.append(build.Rec("पति", ("husband",), ctx("पत्नी", "गृह"), "x", ""))
        rows.append(build.Rec("पति", ("king",), ctx("राजन्", "प्रजा"), "x", ""))
    rows += [build.Rec("एक", ("one",), ctx("दश"), "x", "")] * 30  # unambiguous
    return rows


def tiny_model() -> dict:
    counts = Counter({"पत्नी": 50, "गृह": 50, "राजन्": 50, "प्रजा": 50, "दश": 50})
    return build.build_model(tiny_records(), counts, lambda label: label.upper())


def test_build_model_keeps_only_ambiguous_lemmas():
    model = tiny_model()
    assert set(model["lemmas"]) == {"पति"}
    assert model["lemmas"]["पति"]["p"] == {"husband": 12, "king": 12}
    assert model["top"]["एक"] == "one"
    assert model["lemmas"]["पति"]["f"]["w:पत्नी"] == {"husband": 12}
    assert model["gloss"]["king"] == "KING"


def test_build_model_prunes_rare_features():
    rows = tiny_records() + [build.Rec("पति", ("king",), ctx("दुर्लभ"), "x", "")]
    model = build.build_model(rows, Counter({"दुर्लभ": 99, "पत्नी": 50}), str)
    assert "w:दुर्लभ" not in model["lemmas"]["पति"]["f"]


def test_choose_prefers_sense_seen_with_context():
    model = tiny_model()
    assert senses.choose("पति", ctx("पत्नी"), model)[0] == "husband"
    label, conf = senses.choose("पति", ctx("प्रजा", "राजन्"), model)
    assert label == "king" and 0.5 < conf <= 1.0


def test_unknown_or_unambiguous_lemma_gives_nothing():
    model = tiny_model()
    assert senses.choose("अज्ञात", ctx("पत्नी"), model) == ("", 0.0)
    assert senses.choose("एक", ctx("दश"), model) == ("", 0.0)
    assert senses.choose("पति", ctx("पत्नी"), {}) == ("", 0.0)


def test_context_of_reading():
    def word(form, lemma, line=0, **kw):
        return Word(form, line, 0, 0, analyses=[Morph(form, lemma, kw.pop("kind", "subanta"), **kw)])

    reading = Reading(words=[word("रामस्", "राम"), word("पतिस्", "पति"), word("गच्छति", "गम्", kind="tinanta"),
                             word("अन्यस्", "अन्य", line=1)])
    c = senses.context_of(reading, 1)
    assert "राम" in c.neighbours and "अन्य" not in c.neighbours
    assert c.verb != ""
