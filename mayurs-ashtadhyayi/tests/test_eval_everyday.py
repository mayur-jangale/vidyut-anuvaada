"""Scoring functions of eval/eval_everyday.py on hand-made readings (not the scores of the check set)."""

import importlib.util
import json
import sys
from pathlib import Path

from mayur.model import Morph, Reading, VerseAnalysis, Word

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("eval_everyday", ROOT / "eval" / "eval_everyday.py")
ev = importlib.util.module_from_spec(_spec)
sys.modules["eval_everyday"] = ev  # (its dataclass needs its module registered)
_spec.loader.exec_module(ev)


def noun(form, lemma, linga, vibhakti, vacana="एकवचन", **kw):
    return Morph(form=form, lemma=lemma, kind="subanta", linga=linga, vibhakti=vibhakti, vacana=vacana, **kw)


def verb(form, lemma, lakara="लट्", purusha="प्रथमपुरुष", vacana="एकवचन", prayoga="कर्तरि"):
    return Morph(form=form, lemma=lemma, kind="tinanta", lakara=lakara, purusha=purusha, vacana=vacana,
                 prayoga=prayoga, root=lemma)


def word(form, morph, in_compound=False, role="", head=None):
    return Word(form=form, line=0, start=0, end=0, in_compound=in_compound, analyses=[morph], role=role, head=head)


def stem(form, lemma=None):
    return Morph(form=form, lemma=lemma or form, kind="stem", stem=form)


ITEM = {"id": "t1", "group": "a", "text": "रामो वनं गच्छति", "padas": ["रामः", "वनम्", "गच्छति"],
        "words": [{"pada": "रामः", "lemma": "राम", "grammar": "पुंलिङ्ग प्रथमा एकवचन"},
                  {"pada": "वनम्", "lemma": "वन", "grammar": "नपुंसकलिङ्ग द्वितीया एकवचन"},
                  {"pada": "गच्छति", "lemma": "गम्", "grammar": "लट् प्रथमपुरुष एकवचन"}],
        "roles": [{"pada": "रामः", "at": 0, "role": "कर्ता", "head": "गच्छति", "head_at": 2},
                  {"pada": "वनम्", "at": 1, "role": "कर्म", "head": "गच्छति", "head_at": 2}],
        "english": "Rāma goes to the forest."}


def rama_reading(case="द्वितीया", role="कर्म"):
    return Reading(words=[word("रामस्", noun("रामस्", "राम", "पुंलिङ्ग", "प्रथमा"), role="कर्ता", head=2),
                          word("वनम्", noun("वनम्", "वन", "नपुंसकलिङ्ग", case), role=role, head=2),
                          word("गच्छति", verb("गच्छति", "गम्"), role="क्रिया")])


def test_split_matches_pausa_and_su_lopa():
    assert ev.split_right(rama_reading(), ITEM["padas"])
    sa = Reading(words=[word("स", noun("स", "तद्", "पुंलिङ्ग", "प्रथमा"))])
    assert ev.split_right(sa, ["सः"])
    assert not ev.split_right(rama_reading(), ["रामः", "वनम्"])


def test_compound_pada_matches_by_members_or_rejoin():
    members = Reading(words=[word("राज", stem("राज", "राजन्"), in_compound=True),
                             word("पुरुषस्", noun("पुरुषस्", "पुरुष", "पुंलिङ्ग", "प्रथमा"))])
    assert ev.split_right(members, ["राज-पुरुषः"])
    whole = Reading(words=[word("नीलोत्पलम्", noun("नीलोत्पलम्", "नीलोत्पल", "नपुंसकलिङ्ग", "प्रथमा"))])
    assert ev.split_right(whole, ["नील-उत्पलम्"])
    assert ev.lemma_right(whole, [0], "नील-उत्पल", "नपुंसकलिङ्ग प्रथमा एकवचन")  # a listed compound stem
    assert ev.lemma_right(members, [0, 1], "राजन्-पुरुष", "पुंलिङ्ग प्रथमा एकवचन")
    assert not ev.lemma_right(members, [0, 1], "राज्-पुरुष", "पुंलिङ्ग प्रथमा एकवचन")


def test_lemma_alternatives_and_feminine_stem():
    r = Reading(words=[word("धवला", noun("धवला", "धवला", "स्त्रीलिङ्ग", "प्रथमा"))])
    assert ev.lemma_right(r, [0], "धवल", "स्त्रीलिङ्ग प्रथमा एकवचन")
    assert not ev.lemma_right(r, [0], "धवल", "पुंलिङ्ग प्रथमा एकवचन")
    assert ev.lemma_right(r, [0], "शुक्ल | धवल", "स्त्रीलिङ्ग प्रथमा एकवचन")


def test_grammar_terms():
    assert ev.grammar_right(verb("दृश्यते", "दृश्", prayoga="कर्मणि"), "लट् प्रथमपुरुष एकवचन कर्मणि")
    assert not ev.grammar_right(verb("दृश्यते", "दृश्", prayoga="कर्मणि"), "लट् प्रथमपुरुष एकवचन")
    assert ev.grammar_right(verb("पश्यति", "दृश्"), "लट् प्रथमपुरुष एकवचन")
    gatva = Morph(form="गत्वा", lemma="गम्", kind="avyaya", krt="क्त्वा", root="गम्")
    assert ev.grammar_right(gatva, "क्त्वा")
    assert ev.grammar_right(Morph(form="च", lemma="च", kind="avyaya"), "अव्यय")
    aham = noun("अहम्", "अस्मद्", "स्त्रीलिङ्ग", "प्रथमा")
    assert ev.grammar_right(aham, "प्रथमा एकवचन")  # no gender written: ours not scored
    assert not ev.grammar_right(aham, "पुंलिङ्ग प्रथमा एकवचन")
    assert ev.grammar_right(aham, "पुंलिङ्ग प्रथमा एकवचन | प्रथमा एकवचन")


def test_roles_and_whole_item_score():
    ok = ev.score(VerseAnalysis(id="", input="", readings=[rama_reading()], status="verified"), ITEM)
    assert all(ok.checks[c] for c in ev.CHECKS) and not ok.problems
    bad = ev.score(VerseAnalysis(id="", input="", readings=[rama_reading("प्रथमा", "कर्ता")]), ITEM)
    assert bad.checks["split"] and not bad.checks["grammar"] and not bad.checks["roles"]
    assert not bad.checks["verified"] and bad.checks["lemma"]
    assert any("वनम्" in p and "कर्म" in p for p in bad.problems)


def test_tally_counts_roles_only_where_listed():
    a = ev.Result("x", "a", {**{c: True for c in ev.CHECKS}, "has_roles": False})
    b = ev.Result("y", "a", {**{c: False for c in ev.CHECKS}, "has_roles": True})
    t = ev.tally([a, b])
    assert t["split"] == (1, 2) and t["roles"] == (0, 1)


def test_check_set_shape():
    doc = json.loads((ROOT / "eval" / "samples" / "everyday_120.json").read_text(encoding="utf-8"))
    items = doc["items"]
    assert len(items) == 120 and doc["groups"] == {"a": 40, "b": 40, "c": 40}
    for item in items:
        assert len(item["words"]) == len(item["padas"])
        for r in item["roles"]:
            assert item["padas"][r["at"]] == r["pada"]
