"""mayur/treebank.py: relation mapping, compound units, CoNLL-U reading, reference files (hand-made data)."""

import json

from mayur import treebank as tb


def test_map_role_core_relations():
    assert tb.map_role("nsubj", {"Case": "Nom"}, "NOUN", {"Voice": "Act"}) == "कर्ता"
    assert tb.map_role("nsubj", {"Case": "Nom"}, "NOUN", {"VerbForm": "Part", "Tense": "Past"}) == "कर्म"
    assert tb.map_role("obj", {"Case": "Acc"}, "NOUN") == "कर्म"
    assert tb.map_role("iobj", {"Case": "Dat"}, "NOUN") == "सम्प्रदान"
    assert tb.map_role("vocative", {"Case": "Voc"}, "NOUN") == "सम्बोधन"
    assert tb.map_role("amod", {}, "ADJ") == "विशेषण"
    assert tb.map_role("nmod", {"Case": "Gen"}, "NOUN") == "सम्बन्ध"
    assert tb.map_role("nmod", {"Case": "Loc"}, "NOUN") == ""
    assert tb.map_role("nmod:appos", {"Case": "Gen"}, "NOUN") == ""


def test_map_role_oblique_by_case_and_subtype():
    assert tb.map_role("obl", {"Case": "Ins"}, "NOUN", {}) == "करण"
    assert tb.map_role("obl", {"Case": "Ins"}, "NOUN", {"Voice": "Pass"}) == "कर्ता"
    assert tb.map_role("obl", {"Case": "Dat"}, "NOUN") == "सम्प्रदान"
    assert tb.map_role("obl", {"Case": "Abl"}, "NOUN") == "अपादान"
    assert tb.map_role("obl", {"Case": "Loc"}, "NOUN") == "अधिकरण"
    assert tb.map_role("obl:agent", {"Case": "Ins"}, "NOUN") == "कर्ता"
    assert tb.map_role("obl:temp", {"Case": "Loc"}, "NOUN") == "अधिकरण"
    assert tb.map_role("obl:soc", {"Case": "Ins"}, "NOUN") == ""  # not forced into करण
    assert tb.map_role("obl:goal", {"Case": "Acc"}, "NOUN") == ""


def test_map_role_verbal_forms_and_particles():
    assert tb.map_role("root", {"Person": "3", "Tense": "Pres"}, "VERB") == "क्रिया"
    assert tb.map_role("advcl", {"VerbForm": "Conv"}, "VERB") == "पूर्वकालक्रिया"
    assert tb.map_role("conj", {"VerbForm": "Conv"}, "VERB") == "पूर्वकालक्रिया"
    assert tb.map_role("xcomp", {"VerbForm": "Inf"}, "VERB") == "तुमर्थ"
    assert tb.map_role("advmod", {}, "ADV") == "अव्यय"
    assert tb.map_role("cc", {}, "CONJ") == "अव्यय"
    assert tb.map_role("advmod", {}, "NOUN") == ""
    assert tb.map_role("conj", {"Case": "Nom"}, "NOUN") == ""


def row(i, form, head, rel, upos="NOUN", feats=None):
    feats = feats or {}
    return {"id": i, "form": form, "lemma": form, "upos": upos, "feats": feats, "member": tb.is_member(feats),
            "head": head, "rel": rel}


def test_compound_unit_is_one_node_attached_by_its_final_member():
    rows = [row(1, "राज", 2, "nmod", feats={"Compound": "Yes"}),
            row(2, "पुत्रः", 3, "nsubj", feats={"Case": "Nom"}),
            row(3, "गच्छति", 0, "root", "VERB", {"Person": "3", "Tense": "Pres"}),
            row(4, "वनम्", 3, "obj", feats={"Case": "Acc"})]
    w = tb.build_words(rows)
    assert (w[0]["role"], w[0]["head_index"], w[0]["compound_member"]) == (tb.MEMBER, 1, True)
    assert (w[1]["role"], w[1]["head_index"]) == ("कर्ता", 2)
    assert (w[2]["role"], w[2]["head_index"]) == ("क्रिया", None)
    assert (w[3]["role"], w[3]["head_index"]) == ("कर्म", 2)


def test_head_into_a_compound_member_is_moved_to_the_final_member():
    rows = [row(1, "क", 2, "conj", feats={"Compound": "Yes"}),
            row(2, "ख", 0, "root", feats={"Case": "Nom"}),
            row(3, "ग", 1, "amod", "ADJ")]
    w = tb.build_words(rows)
    assert w[2]["head_index"] == 1 and w[2]["role"] == "विशेषण"


CONLLU_DEVA = """# sent_id = s1
# text = रामः वनं गच्छति ।
1\tरामः\tराम\tNOUN\t_\tCase=Nom|Gender=Masc|Number=Sing\t3\tnsubj\t_\t_
2\tवनं\tवन\tNOUN\t_\tCase=Acc|Gender=Neut|Number=Sing\t3\tobj\t_\t_
3\tगच्छति\tगम्\tVERB\t_\tPerson=3|Tense=Pres|Number=Sing\t0\troot\t_\t_
4\t।\t।\tPUNCT\t_\t_\t3\tpunct\t_\t_

# sent_id = s2
# text = अन्यत्
1\tअन्यत्\tअन्य\tNOUN\t_\t_\t_\t_\t_\t_

"""


def test_parse_conllu_devanagari_skips_unannotated_and_punctuation():
    sents = list(tb.parse_conllu(CONLLU_DEVA.splitlines(), "devanagari", "t"))
    assert len(sents) == 1
    s = sents[0]
    assert s["id"] == "s1" and [w["role"] for w in s["words"]] == ["कर्ता", "कर्म", "क्रिया"]
    assert [w["head_index"] for w in s["words"]] == [2, 2, None]


def test_parse_conllu_iast_is_converted_to_devanagari_once():
    iast = "# sent_id = d1\n# text = rāmaḥ gacchati\n" \
           "1\trāmaḥ\trāma\tNOUN\t_\tCase=Nom\t2\tnsubj\t_\tUnsandhied=rāmaḥ\n" \
           "2\tgacchati\tgam\tVERB\t_\tPerson=3|Tense=Pres\t0\troot\t_\tUnsandhied=gacchati\n\n"
    (s,) = list(tb.parse_conllu(iast.splitlines(), "iast", "t"))
    assert all(ord(ch) > 127 or ch == " " for ch in s["text"])
    assert s["words"][0]["lemma"] == "राम" and s["words"][1]["role"] == "क्रिया"


def test_unmapped_counts_lists_labels_without_forcing():
    sents = list(tb.parse_conllu(CONLLU_DEVA.replace("obj", "orphan").splitlines(), "devanagari", "t"))
    assert tb.unmapped_counts(sents)["orphan"] == 1
    assert tb.mapping_coverage(sents) == {"words": 3, "mapped": 2}


def test_read_claude_file(tmp_path):
    doc = {"annotator": "Claude (LLM), not human-verified", "verses": [{
        "id": "वि १", "number": 1, "text": "रामो गच्छति",
        "words": [{"index": 1, "line": 0, "form": "गच्छति", "lemma": "गम्", "compound_member": False,
                   "role": "क्रिया", "head": None},
                  {"index": 0, "line": 0, "form": "रामस्", "lemma": "राम", "compound_member": False,
                   "role": "कर्ता", "head": 1}],
        "compounds": [], "anvaya": [0, 1]}]}
    p = tmp_path / "a.json"
    p.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
    (s,) = tb.read_claude(p)
    assert [w["form"] for w in s["words"]] == ["रामस्", "गच्छति"]  # sorted by index
    assert s["words"][0]["head_index"] == 1 and s["words"][1]["head_index"] is None
    assert s["anvaya"] == [0, 1]
