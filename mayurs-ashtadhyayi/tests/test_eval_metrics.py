"""Pure metric functions of eval/eval_dcs.py on hand-made data."""

import importlib.util
from pathlib import Path

from mayur.model import Morph

_spec = importlib.util.spec_from_file_location("eval_dcs", Path(__file__).resolve().parent.parent / "eval" / "eval_dcs.py")
ev = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ev)


def g(form, lemma=None, cm=False, **feats):
    return {"form": form, "lemma": lemma or form, "compound_member": cm, "feats": feats}


def test_normalize_nasals():
    assert ev.normalize("साम्प्रतम्") == ev.normalize("सांप्रतम्")
    assert ev.normalize("पुम्गवम्") == "पुंगवम्" or ev.normalize("पुङ्गवम्") == "पुंगवम्"
    assert ev.normalize("रामम्") == "रामम्"


def test_word_matches_compound_lemma():
    assert ev.word_matches("वाक्", "वाच्", "वाच्", True) is False
    assert ev.word_matches("वाच्", "वाक्", "वाच्", True) is True
    assert ev.word_matches("वाच्", "वाक्", "वाच्", False) is False


def test_lcs_pairs():
    assert ev.lcs_pairs(list("abcd"), list("axcd"), lambda x, y: x == y) == [(0, 0), (2, 2), (3, 3)]
    assert ev.lcs_pairs([], list("a"), lambda x, y: x == y) == []


def test_prf():
    r = ev.prf(3, 4, 6)
    assert (r["precision"], r["recall"]) == (0.75, 0.5)
    assert abs(r["f1"] - 0.6) < 1e-9
    assert ev.prf(0, 0, 0)["f1"] == 0.0


def test_split_equal_and_align():
    gold_words = [g("रामस्"), g("वाक्", "वाच्", True), g("गच्छति")]
    ours = [("रामस्", False), ("वाच्", True), ("गच्छति", False)]
    assert ev.split_equal(ours, gold_words)
    assert not ev.split_equal(ours[:2], gold_words)
    broken = [("राम", False), ("स्", False), ("गच्छति", False)]
    assert ev.align_words(broken, gold_words) == [(2, 2)]


def test_morphology_counts():
    m = Morph(form="रामस्", lemma="राम", kind="subanta", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन")
    right = g("रामस्", "राम", Case="Nom", Gender="Masc", Number="Sing")
    wrong = g("रामस्", "रम", Case="Acc", Gender="Masc", Number="Sing")
    c = ev.morphology_counts([(m, right), (m, wrong), (None, right)])
    assert c["words"] == 3 and c["lemma"] == 1 and c["all_features"] == 1
    assert (c["feat_Case"], c["feat_Case_total"]) == (1, 3)
    assert (c["feat_Number"], c["feat_Number_total"]) == (2, 3)
    assert c["feat_Tense_total"] == 0


def test_summarize_counts_failures():
    ok = {"verse": 1, "n_lines": 2, "gold_words": 10, "our_words": 8, "matched": 6, "lines_exact": [True, False],
          "verse_exact": False, "gold_in_readings": True, "morphology": {"words": 6, "lemma": 5},
          "proof_words": 8, "proof_verified": 4, "verified": True, "error": ""}
    bad = {**ok, "verse": 2, "our_words": 0, "matched": 0, "lines_exact": [False, False], "gold_in_readings": False,
           "morphology": {}, "proof_words": 0, "proof_verified": 0, "verified": False, "error": "ValueError"}
    s = ev.summarize([ok, bad])
    assert (s["verses"], s["failures"], s["lines"], s["lines_exact"]) == (2, 1, 4, 1)
    assert (s["gold_words"], s["our_words"], s["matched_words"]) == (20, 8, 6)
    assert s["precision"] == 0.75 and s["recall"] == 0.3
    assert s["morphology"]["lemma"] == 5 and s["verses_verified"] == 1
    assert "1/4" in ev.report([ok, bad], s)


def test_parse_range():
    assert ev.parse_range("1-3", 79) == [1, 2, 3] and ev.parse_range("5", 79) == [5]
    assert ev.parse_range(None, 3) == [1, 2, 3]
