import pytest

from mayur import resources
from mayur.dcs import compact_orthography, iter_sentences, pada_form

CH1 = next(
    iter((resources.data_dir() / "dcs/sanskrit/dcs/data/conllu/files/Rāmāyaṇa").glob("*-0000-*.conllu")),
    None,
)
needs_dcs = pytest.mark.skipif(CH1 is None, reason="DCS data not fetched")


def test_pada_form_visarga_and_anusvara():
    assert pada_form("rAmaH", "rAma") == "rAmas"
    assert pada_form("niratam", "niram") == "niratam"
    assert pada_form("varaM", "vara") == "varam"
    assert pada_form("punaH", "punar") == "punar"
    assert pada_form("pitaH", "pitf") == "pitar"
    assert pada_form("kaH", "ka") == "kas"
    assert pada_form("guRavAn", "guRavat") == "guRavAn"


def test_compact_orthography():
    assert compact_orthography("ko nv asmin sAmpratam loke") == "ko nvasminsAmpratamloke"
    assert compact_orthography("kaS ca vIryavAn") == "kaSca vIryavAn"
    assert compact_orthography("nAradaM paripapracCa vAlmIkir munipuMgavam") == \
        "nAradaM paripapracCa vAlmIkirmunipuMgavam"
    assert compact_orthography("tapaH svAdhyAya") == "tapaH svAdhyAya"


@needs_dcs
def test_parser_first_sentence():
    s = next(iter_sentences(CH1))
    assert s["text"].startswith("tapaḥsvādhyāya")
    assert (s["sent_counter"], s["sent_subcounter"]) == (1, 1)
    t = s["tokens"]
    assert [x["lemma"] for x in t][:3] == ["tapas", "svADyAya", "niram"]
    assert t[0]["is_compound_member"] and t[0]["mwt"] == (1, 3)
    assert t[2]["feats"]["VerbForm"] == "Part" and t[2]["feats"]["Case"] == "Acc"
    assert pada_form(t[3]["unsandhied"], t[3]["lemma"]) == "tapasvI"


@needs_dcs
def test_compact_matches_real_line():
    lines = [compact_orthography(__import__("mayur.translit", fromlist=["x"]).iast_to_slp1(s["text"]))
             for s in iter_sentences(CH1)][:3]
    assert lines[1].endswith("vAlmIkirmunipuMgavam")
    assert lines[2].startswith("ko nvasmin")


def _load_eval():
    import importlib.util
    from pathlib import Path

    p = Path(__file__).resolve().parent.parent / "eval" / "eval_dcs.py"
    spec = importlib.util.spec_from_file_location("eval_dcs", p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_eval_metrics_on_handmade_input():
    ev = _load_eval()
    from mayur.model import Morph

    gold = [[{"form": "rAmas", "lemma": "rAma", "feats": {"Case": "Nom", "Number": "Sing", "Gender": "Masc"}},
             {"form": "puMgavam", "lemma": "puMgava", "feats": {"Case": "Acc"}}]]
    m = Morph(form="rAmas", lemma="rAma", kind="subanta", vibhakti="praTamA", vacana="eka", linga="puM")
    ours = [{"form": "rAmas", "line": 0, "in_compound": False, "morph": m, "proof_ok": True},
            {"form": "puNgavam", "line": 0, "in_compound": False, "morph": None, "proof_ok": False}]
    r = ev.compare_verse(ours, gold)
    assert r["verse_exact"] and r["lines_exact"] == 1 and r["tp"] == 2
    assert r["lemma_n"] == 2 and r["lemma_ok"] == 1
    assert r["feat_ok"]["Case"] == 1 and r["feat_n"]["Case"] == 2
    agg = ev.aggregate([r])
    assert agg["token_f1"] == 100.0 and agg["words_proof_verified"] == [1, 2]
    assert ev.normalise("puMgava") == ev.normalise("puNgava")
    assert ev.lcs_pairs(list("abc"), list("axc")) == [(0, 0), (2, 2)]
