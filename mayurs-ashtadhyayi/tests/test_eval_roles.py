"""Pure metric functions of eval/eval_roles.py and eval/eval_compounds.py on hand-made data."""

import importlib.util
from pathlib import Path

_EVAL = Path(__file__).resolve().parent.parent / "eval"


def load(name):
    spec = importlib.util.spec_from_file_location(name, _EVAL / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


er = load("eval_roles")
ec = load("eval_compounds")


def ow(form, role="", head=None, member=False):
    return {"form": form, "in_compound": member, "lemma": form, "role": role, "head": head}


def gw(form, role="", head=None, member=False):
    return {"form": form, "lemma": form, "role": role, "head_index": head, "compound_member": member}


def test_pairwise_agreement():
    assert er.pairwise_agreement([0, 1, 2], [0, 1, 2]) == (3, 3)
    assert er.pairwise_agreement([0, 1, 2], [2, 1, 0]) == (0, 3)
    assert er.pairwise_agreement([0, 1, 2], [0, 2]) == (1, 1)  # only common items count


def test_score_sentence_head_role_and_unaligned():
    ours = {"words": [ow("रामस्", "कर्ता", 2), ow("वनम्", "कर्म", 2), ow("गच्छति", "क्रिया", None)],
            "compounds": [], "anvaya": [0, 1, 2]}
    gold = {"words": [gw("रामस्", "कर्ता", 2), gw("वनम्", "करण", 2), gw("गच्छति", "क्रिया", None), gw("अन्यत्", "विशेषण", 0)],
            "anvaya": [0, 1, 2, 3]}
    c = er.score_sentence(ours, gold)
    assert (c["gold_words"], c["aligned"], c["unaligned_gold"]) == (4, 3, 1)
    assert (c["evaluated"], c["head_ok"]) == (3, 3)
    assert (c["role_eval"], c["role_ok"]) == (3, 2)
    assert c["roles"]["कर्ता"] == {"gold": 1, "pred": 1, "tp": 1}
    assert c["roles"]["करण"] == {"gold": 1, "pred": 0, "tp": 0}
    assert c["roles"]["कर्म"] == {"gold": 0, "pred": 1, "tp": 0}
    assert (c["anvaya_agree"], c["anvaya_pairs"]) == (3, 3)


def test_unmapped_gold_role_is_not_scored_but_head_is():
    ours = {"words": [ow("क", "कर्ता", None)], "compounds": [], "anvaya": []}
    gold = {"words": [gw("क", "", None)]}
    c = er.score_sentence(ours, gold)
    assert (c["head_ok"], c["role_eval"], c["unmapped_gold_role"]) == (1, 0, 1)


def test_compound_members_are_skipped_and_gold_heads_move_to_the_final_member():
    ours = {"words": [ow("राज", "समासपूर्वपद", 1, member=True), ow("पुत्रस्", "कर्ता", 2), ow("गच्छति", "क्रिया", None),
                      ow("अश्वम्", "कर्म", 1)], "compounds": [], "anvaya": []}
    gold = {"words": [gw("राज", "समासपूर्वपद", 1, member=True), gw("पुत्रस्", "कर्ता", 2), gw("गच्छति", "क्रिया", None),
                      gw("अश्वम्", "कर्म", 0)],
            "compounds": [{"members": [0, 1], "type": "तत्पुरुष"}]}
    c = er.score_sentence(ours, gold)
    assert c["members_skipped"] == 1 and c["evaluated"] == 3
    assert c["head_ok"] == 3  # gold head 0 (a member) is moved to its final member 1


def test_add_counts_and_per_role():
    a = {"head_ok": 1, "roles": {"कर्ता": {"gold": 2, "pred": 1, "tp": 1}}}
    b = {"head_ok": 2, "roles": {"कर्ता": {"gold": 1, "pred": 2, "tp": 1}, "कर्म": {"gold": 1, "pred": 0, "tp": 0}}}
    t = er.add_counts(a, b)
    assert t["head_ok"] == 3 and t["roles"]["कर्ता"] == {"gold": 3, "pred": 3, "tp": 2}
    row = er.per_role(t["roles"])[0]
    assert (row["role"], row["precision"], row["recall"]) == ("कर्ता", 0.667, 0.667)
    assert er.frac(1, 4) == "1/4 = 25.0%" and er.frac(0, 0) == "0/0"


def test_agreement_between_two_annotators():
    def sent(role2, order):
        return {"id": "v", "words": [
            {"form": "रामस्", "lemma": "राम", "compound_member": False, "role": "कर्ता", "head_index": 1},
            {"form": "गच्छति", "lemma": "गम्", "compound_member": False, "role": role2, "head_index": None}],
            "compounds": [{"members": [0, 1], "type": "तत्पुरुष"}], "anvaya": order}
    r = er.agreement([sent("क्रिया", [0, 1])], [sent("विधेय", [1, 0]), {"id": "other", "words": []}])
    assert r["sentences"] == 1
    c = r["counts"]
    assert (c["head_ok"], c["role_ok"], c["role_eval"]) == (2, 1, 2) and c["anvaya_agree"] == 0


def test_compound_grouping_and_type_scores():
    ours = {"words": [ow("क", member=True), ow("ख"), ow("ग", member=True), ow("घ")],
            "compounds": [{"members": [0, 1], "type": "कर्मधारय"}, {"members": [2, 3], "type": "बहुव्रीहि"}], "anvaya": []}
    gold = {"words": [gw("क", member=True), gw("ख"), gw("ग", member=True), gw("घ")],
            "compounds": [{"members": [0, 1], "type": "तत्पुरुष"}, {"members": [2, 3], "type": "द्वन्द्व"}]}
    c = ec.score_compounds(ours, gold)
    assert (c["found"], c["gold_compounds"], c["our_correct_group"]) == (2, 2, 2)
    assert (c["typed"], c["type_ok"], c["family_ok"]) == (2, 0, 1)  # कर्मधारय is in the तत्पुरुष family
    assert c["confusion"] == {"तत्पुरुष -> कर्मधारय": 1, "द्वन्द्व -> बहुव्रीहि": 1}


def test_wrong_grouping_is_not_found():
    ours = {"words": [ow("क"), ow("ख"), ow("ग")], "compounds": [{"members": [0, 1, 2], "type": "तत्पुरुष"}], "anvaya": []}
    gold = {"words": [gw("क"), gw("ख"), gw("ग")], "compounds": [{"members": [0, 1], "type": "तत्पुरुष"}]}
    c = ec.score_compounds(ours, gold)
    assert (c["found"], c["our_correct_group"], c["typed"]) == (0, 0, 0)


def test_proxy_compounds_only_types_coordinate_units():
    words = [gw("क", "समासपूर्वपद", 1, True), gw("ख", "", None), gw("ग", "समासपूर्वपद", 3, True), gw("घ", "", None)]
    words[0]["relation"], words[2]["relation"] = "conj", "amod"
    out = ec.proxy_compounds({"words": words})
    assert out == [{"members": [0, 1], "type": "द्वन्द्व", "vigraha": ""}, {"members": [2, 3], "type": "", "vigraha": ""}]
