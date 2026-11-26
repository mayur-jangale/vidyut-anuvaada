"""Rule-based fluent English: each rule, each invariant check, and a real verse. Offline."""

from __future__ import annotations

from dataclasses import replace

import pytest

from mayur import fluent, fluent_checks as fc
from mayur.model import Alignment, Compound, Morph, Reading, Word

SG, PL = "एकवचन", "बहुवचन"


def word(form, kind, gloss, role, head, lemma=None, **m):
    return Word(form=form, line=0, start=0, end=1, role=role, head=head, gloss=gloss,
                analyses=[Morph(form=form, lemma=lemma or form, kind=kind, **m)])


def reading(words, template, spans, **kw):
    """spans: (word index, substring) pairs located left to right in ``template``."""
    out, pos = [], 0
    for i, sub in spans:
        s = template.index(sub, pos)
        out.append(Alignment(i, s, s + len(sub)))
        pos = s + len(sub)
    return Reading(words=words, translation=template, alignment=out, **kw)


def rama():  # Rama asked Narada.
    ws = [word("रामः", "subanta", "Rāma", "कर्ता", 2, vacana=SG, vibhakti="प्रथमा"),
          word("नारदम्", "subanta", "Nārada", "कर्म", 2, vacana=SG, vibhakti="द्वितीया"),
          word("पप्रच्छ", "tinanta", "ask", "क्रिया", None, lakara="लिट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    return reading(ws, "Rāma asked Nārada.", [(0, "Rāma"), (2, "asked"), (1, "Nārada")])


def gods():  # Gods fear.  (plural agent, present)
    ws = [word("देवाः", "subanta", "god", "कर्ता", 1, vacana=PL, vibhakti="प्रथमा"),
          word("बिभ्यति", "tinanta", "fear", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=PL)]
    return reading(ws, "Gods fear.", [(0, "Gods"), (1, "fear")])


def rends(*pairs):
    return [fc.Rendering(i, t) for i, t in pairs]


def codes(reading_, text, rendering):
    return {f.code for f in fc.run_checks(reading_, text, rends(*rendering), {})[1]}


# ---------------------------------------------------------------- checks

def test_good_rewording_passes_with_exact_spans():
    r = rama()
    spans, fails = fc.run_checks(r, "Rāma asked Nārada.", rends((0, "Rāma"), (2, "asked"), (1, "Nārada")), {})
    assert not fails and [(a.word, "Rāma asked Nārada."[a.start:a.end]) for a in spans] == [
        (0, "Rāma"), (2, "asked"), (1, "Nārada")]


def test_dropped_word_rejected():
    assert "alignment" in codes(rama(), "Rāma asked.", [(0, "Rāma"), (2, "asked")])


def test_substring_not_present_rejected():
    assert "substring" in codes(rama(), "Rāma asked Nārada.", [(0, "Rāma"), (2, "asked"), (1, "Nārad")])


def test_added_content_word_rejected():
    assert "vocabulary" in codes(rama(), "Rāma angrily asked Nārada.", [(0, "Rāma"), (2, "angrily asked"), (1, "Nārada")]) \
        or "vocabulary" in codes(rama(), "Rāma angrily asked Nārada.", [(0, "Rāma"), (2, "asked"), (1, "Nārada")])


def test_numeral_rejected():
    assert "vocabulary" in codes(rama(), "Rāma asked Nārada 2 times.", [(0, "Rāma"), (2, "asked"), (1, "Nārada")])


def test_tense_change_rejected():
    assert "tense" in codes(rama(), "Rāma will ask Nārada.", [(0, "Rāma"), (2, "will ask"), (1, "Nārada")])


def test_number_change_rejected():
    assert fc.check_number(gods(), rends((0, "god"), (1, "fear")))
    assert "number" in codes(gods(), "God fears.", [(0, "God"), (1, "fears")])
    assert not codes(gods(), "Gods fear.", [(0, "Gods"), (1, "fear")])


def test_agent_object_swap_rejected():
    assert "order" in codes(rama(), "Nārada asked Rāma.", [(0, "Rāma"), (2, "asked"), (1, "Nārada")])


def test_passive_agent_needs_by():
    r = rama()
    r.words[2] = replace(r.words[2], analyses=[replace(r.words[2].morph, prayoga="कर्मणि")])
    ok = fc.run_checks(r, "Nārada was asked by Rāma.", rends((1, "Nārada"), (2, "was asked"), (0, "Rāma")), {})[1]
    assert not [f for f in ok if f.code == "order"]
    bad = fc.check_voice_order(r, "Nārada was asked Rāma.", [Alignment(1, 0, 6), Alignment(2, 7, 16), Alignment(0, 17, 21)])
    assert bad


def test_negation_must_be_preserved():
    r = reading(rama().words, "Rāma did not ask Nārada.", [(0, "Rāma"), (2, "did not ask"), (1, "Nārada")])
    assert fc.check_negation(r, "Rāma did not ask Nārada.") == []
    assert fc.check_negation(r, "Rāma asked Nārada.")
    assert fc.check_negation(rama(), "Rāma never asked Nārada.")


def test_length_ratio():
    assert fc.check_length("Rāma asked Nārada.", "Rāma asked Nārada.") == []
    assert fc.check_length("Rāma asked Nārada.", "Rāma " + "asked " * 30)
    assert fc.check_length("x" * 20, "")


def test_synonyms_are_bounded_and_must_be_used():
    assert fc.check_synonyms({0: ["a"] * 6})
    assert fc.check_synonyms({0: ["a very long alternative phrase indeed"]})
    r = rama()
    assert fc.check_content_words(r, rends((0, "Rāma"), (2, "questioned"), (1, "Nārada")), {})
    assert not fc.check_content_words(r, rends((0, "Rāma"), (2, "questioned"), (1, "Nārada")), {2: ["questioned"]})
    assert fc.check_content_words(r, rends((0, "Rama"), (2, "asked"), (1, "Nārada")), {})  # name not verbatim


def test_overlapping_and_boundary_spans():
    spans, fails = fc.locate("ask asked", rends((0, "ask"), (1, "asked")))
    assert not fails and [(a.start, a.end) for a in spans] == [(0, 3), (4, 9)]
    assert fc.locate("asked", rends((0, "ask")))[1]  # not a whole word
    assert fc.locate("big", rends((0, "big"), (1, "big")))[1]  # only one place for two words


# ---------------------------------------------------------------- rules

def toks(r):
    return fluent.tokenize(r)


def test_tokenize_render_roundtrip_with_spans():
    r = rama()
    text, spans = fluent.render(toks(r))
    assert text == r.translation and spans == r.alignment


def test_unbracket_and_capitals_and_final_punctuation():
    ws = [word("राम", "subanta", "Rāma", "कर्ता", None)]
    r = reading(ws, "[He is] Rāma", [(0, "Rāma")])
    new, _ = fluent.rewrite(r)
    assert new.reworded == "He is Rāma." and new.reworded_note == fluent.NOTE_OK


def test_dangling_conjunction_removed():
    r = reading(rama().words, "and Rāma asked Nārada and", [(0, "Rāma"), (2, "asked"), (1, "Nārada")])
    new, _ = fluent.rewrite(r)
    assert new.reworded == "Rāma asked Nārada."


def test_article_before_singular_common_noun_only():
    ws = [word("राजा", "subanta", "king", "कर्ता", 2, vacana=SG, vibhakti="प्रथमा"),
          word("देवाः", "subanta", "god", "कर्म", 2, vacana=PL, vibhakti="द्वितीया"),
          word("पूजयति", "tinanta", "worship", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    r = reading(ws, "king worships gods", [(0, "king"), (2, "worships"), (1, "gods")])
    new, spans = fluent.rewrite(r)
    assert new.reworded == "The king worships gods."
    assert all(a.word != 0 or new.reworded[a.start:a.end] == "king" for a in spans)  # article never aligned
    assert fluent.articles(toks(rama()), rama()) == toks(rama())  # names get none


def test_verb_takes_third_singular_s():
    ws = [word("राजा", "subanta", "king", "कर्ता", 1, vacana=SG, vibhakti="प्रथमा"),
          word("पूजयति", "tinanta", "worship", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    r = reading(ws, "king worship", [(0, "king"), (1, "worship")])
    assert fluent.rewrite(r)[0].reworded == "The king worships."


def test_possessive_for_short_name():
    ws = [word("पुत्रः", "subanta", "son", "कर्ता", 2, vacana=SG, vibhakti="प्रथमा"),
          word("रामस्य", "subanta", "Rāma", "सम्बन्ध", 0, vacana=SG, vibhakti="षष्ठी"),
          word("गच्छति", "tinanta", "go", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    r = reading(ws, "son of Rāma goes", [(0, "son"), (1, "Rāma"), (2, "goes")])
    assert "Rāma's son" in fluent.rewrite(r)[0].reworded


def test_vocative_set_off_and_relative_comma():
    ws = [word("मुने", "subanta", "sage", "सम्बोधन", 2, vacana=SG, vibhakti="सम्बोधन"),
          word("रामः", "subanta", "Rāma", "कर्ता", 2, vacana=SG, vibhakti="प्रथमा"),
          word("गच्छति", "tinanta", "go", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    r = reading(ws, "O sage Rāma goes", [(0, "sage"), (1, "Rāma"), (2, "goes")])
    assert fluent.rewrite(r)[0].reworded == "O sage, Rāma goes."
    ws2 = [word("रामः", "subanta", "Rāma", "कर्ता", 2, vacana=SG, vibhakti="प्रथमा"),
           word("यः", "subanta", "who", "कर्ता", 2, lemma="यद्", vacana=SG, vibhakti="प्रथमा"),
           word("गच्छति", "tinanta", "go", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    r2 = reading(ws2, "Rāma who goes", [(0, "Rāma"), (1, "who"), (2, "goes")])
    assert "Rāma, who goes" in fluent.rewrite(r2)[0].reworded


def test_coordination_and_dvandva():
    ws = [word("राम", "subanta", "Rāma", "कर्ता", 4)]
    ws += [word(f, "subanta", g, "विधेय", None, vacana=SG, vibhakti="प्रथमा")
           for f, g in (("शूरः", "brave"), ("धीरः", "steady"), ("वीरः", "bold"))]
    ws.insert(1, word("अस्ति", "tinanta", "be", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG))
    r = reading(ws, "Rāma is brave, steady, bold", [(0, "Rāma"), (1, "is"), (2, "brave"), (3, "steady"), (4, "bold")])
    out = fluent.coordination(toks(r), r)
    assert fluent.render(out)[0] == "Rāma is brave, steady and bold"
    d = reading([word("पुत्र", "stem", "son", "समासपूर्वपद", 1), word("पौत्रः", "subanta", "grandson", "कर्ता", None, vacana=SG)],
                "son-grandson", [(0, "son"), (1, "grandson")],
                compounds=[Compound(id=0, members=[0, 1], samasa="द्वन्द्व")])
    assert fluent.render(fluent.smooth_compounds(toks(d), d))[0] == "son and grandson"


def test_tatpurusha_agent_noun_reordered():
    d = reading([word("वाच्", "stem", "speech", "समासपूर्वपद", 1), word("विदः", "subanta", "knower", "कर्ता", None, vacana=PL)],
                "speech-knowers", [(0, "speech"), (1, "knowers")], compounds=[Compound(id=0, members=[0, 1], samasa="तत्पुरुष")])
    assert fluent.render(fluent.smooth_compounds(toks(d), d))[0] == "knowers of speech"


def test_question_inversion():
    ws = [word("किम्", "subanta", "what", "कर्म", 2, lemma="किम्", vacana=SG, vibhakti="द्वितीया"),
          word("रामः", "subanta", "Rāma", "कर्ता", 2, vacana=SG, vibhakti="प्रथमा"),
          word("पश्यति", "tinanta", "see", "क्रिया", None, lakara="लट्", prayoga="कर्तरि", purusha="प्रथमपुरुष", vacana=SG)]
    r = reading(ws, "what Rāma [is] seeing?", [(0, "what"), (1, "Rāma"), (2, "seeing")])
    out = fluent.rewrite(r)[0].reworded
    assert out.startswith("What is Rāma seeing") and out.endswith("?")


# ---------------------------------------------------------------- invariants guard the output

def test_failing_check_leaves_reworded_empty(monkeypatch):
    def add_word(t, r):
        return [fluent.Tok("angrily")] + list(t)

    monkeypatch.setattr(fluent, "RULES", (add_word,) + fluent.RULES)
    new, spans = fluent.rewrite(rama())
    assert new.reworded == "" and spans == [] and "vocabulary" in new.reworded_note
    assert new.translation == rama().translation


def test_lost_aligned_word_is_caught(monkeypatch):
    monkeypatch.setattr(fluent, "RULES", (lambda t, r: [x for x in t if x.word != 1],))
    new, _ = fluent.rewrite(rama())
    assert new.reworded == "" and "alignment" in new.reworded_note


# ---------------------------------------------------------------- real verse (needs vidyut data)

def test_real_verse_one():
    pipeline = pytest.importorskip("mayur.pipeline")
    from mayur import gold

    r = pipeline.analyze_verse(gold.verse_text(1)).readings[0]
    new, spans = fluent.rewrite(r)
    assert (new.translation, new.alignment) == (r.translation, r.alignment)
    assert new.reworded and new.reworded_note == fluent.NOTE_OK
    assert len(spans) == len(r.alignment) and all(a.start < a.end for a in spans)
    for a, b in zip(spans, spans[1:]):
        assert a.end <= b.start
    assert fluent.rewrite(new)[0].reworded  # deterministic and re-runnable


def test_pipeline_fills_reworded_offline():
    """The analysis itself carries the fluent English; no network or language-model module is loaded."""
    import sys

    from mayur import jsonout
    from mayur.pipeline import analyze_verse

    data = jsonout.to_json(analyze_verse("श्वेतो धावति"))
    assert data["fluent"]["text"] and data["fluent"]["note"] == "rule-based; checks passed"
    for a in data["fluent"]["alignment"]:
        assert data["fluent"]["text"][a["start"]:a["end"]] == a["text"]
    assert not {"anthropic", "openai", "requests", "httpx"} & set(sys.modules)

