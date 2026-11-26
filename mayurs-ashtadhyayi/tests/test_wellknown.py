"""Rules found by running well-known lines from outside the corpus (eval/eval_wellknown.py)."""

from mayur import lexicon, lipi, segmenter
from mayur.pipeline import analyze_verse


def test_merged_vowel_cannot_straddle_a_written_space():
    # कृत्वा + अयम् is written कृत्वायम्; with a space the second word is यम्
    assert segmenter.contains("कृत्वायं न", ["कृत्वा", "अयम्", "न"], [False, False, False])
    assert not segmenter.contains("कृत्वा यं न", ["कृत्वा", "अयम्", "न"], [False, False, False])
    assert segmenter.contains("कृत्वा यं न", ["कृत्वा", "यम्", "न"], [False, False, False])


def test_unmarked_elision_after_e_o_stays_possible_across_a_space():
    assert segmenter.contains("सो पि", ["सस्", "अपि"], [False, False])


def test_particle_does_not_end_a_compound():
    seg = segmenter.segment_line("वसुधैव कुटुम्बकम्", top_k=50)
    for split in seg.splits:
        for left, right in zip(split.words, split.words[1:]):
            final = left.in_compound and not right.in_compound
            assert not (final and right.form in segmenter.NIPATA_NEVER_FINAL), split


def test_gati_sat_only_before_kr():
    assert not any(m.source == "generated" and m.kind == "tinanta" for m in lexicon.padas("सद्गमय"))
    assert lexicon.padas("सत्कृत्य")


def test_simple_prose_sentence_is_split_and_verified():
    analysis = analyze_verse("बालको ग्रामं गच्छति")
    assert [lipi.pausa(w.form) for w in analysis.readings[0].words] == ["बालकः", "ग्रामम्", "गच्छति"]
    assert analysis.status == "verified"


def test_split_score_decides_between_readings_of_two_lines():
    """The trained split score is not drowned out when two half-verses are combined."""
    analysis = analyze_verse("विद्या ददाति विनयं विनयाद्याति पात्रताम् । पात्रत्वाद्धनमाप्नोति धनाद्धर्मं ततः सुखम् ॥")
    forms = [lipi.pausa(w.form) for w in analysis.readings[0].words]
    assert "विनयात्" in forms and "याति" in forms and "अद्य" not in forms
