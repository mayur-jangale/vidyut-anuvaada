"""Sampler (ledger exclusion, determinism) and the end-to-end metric."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace

from mayur.model import Morph

ROOT = Path(__file__).resolve().parent.parent


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


st = _load("sample_test", "scripts/sample_test.py")
ev = _load("eval_dcs2", "eval/eval_dcs.py")
CANDIDATES = [(f"{c}.{n}", "ग्रन्थ", []) for c in (1, 2) for n in range(1, 21)]


def test_draw_is_deterministic_and_respects_ledger():
    a = st.draw(CANDIDATES, 10, seed=5)
    assert a == st.draw(CANDIDATES, 10, seed=5) and a != st.draw(CANDIDATES, 10, seed=6)
    banned = [c[0] for c in a]
    b = st.draw(CANDIDATES, 30, seed=5, exclude=banned)
    assert not {c[0] for c in b} & set(banned) and len(b) == 30
    assert len(st.draw(CANDIDATES, 100, seed=1, exclude=banned)) == 30


def test_ledger_ids_and_missing_ledger(tmp_path):
    assert st.read_ledger(tmp_path / "none.json") == {"draws": []}
    ledger = {"draws": [{"label": "a", "time": "t", "ids": ["1.1", "1.2"]}, {"label": "b", "time": "t", "ids": ["2.1"]}]}
    assert st.ledger_ids(ledger) == {"1.1", "1.2", "2.1"}


def sent(text, forms):
    return {"text": text, "tokens": [{"form": f, "lemma": f} for f in forms]}


def test_verse_ok_rules():
    assert st.verse_ok([sent("रामः", ["रामस्"])])
    assert not st.verse_ok([sent("रामः", ["रामस्", ""])])
    assert not st.verse_ok([sent("रामः", ["_"])])
    assert not st.verse_ok([sent("र" * 61, ["रामस्"])])
    assert st.syllables("रामस्य") == 3


def test_refuses_existing_label(tmp_path, capsys):
    (tmp_path / "x.json").write_text("{}", encoding="utf-8")
    assert st.main(["--pool", "dev_pool", "--n", "1", "--label", "x", "--out-dir", str(tmp_path),
                    "--ledger", str(tmp_path / "l.json")]) == 1


def word(form, in_compound, morph):
    return SimpleNamespace(form=form, in_compound=in_compound, morph=morph)


def test_end_to_end_ok():
    m = Morph(form="रामस्", lemma="राम", kind="subanta", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन")
    good = {"form": "रामस्", "lemma": "राम", "compound_member": False,
            "feats": {"Case": "Nom", "Gender": "Masc", "Number": "Sing"}}
    assert ev.end_to_end_ok(word("रामस्", False, m), good)
    assert not ev.end_to_end_ok(word("रामस्", False, m), {**good, "lemma": "रम"})
    assert not ev.end_to_end_ok(word("रामस्", False, m), {**good, "feats": {"Case": "Acc"}})
    member = {"form": "तपस्", "lemma": "तपस्", "compound_member": True, "feats": {}}
    assert ev.end_to_end_ok(word("तपस्", True, None), member)
    assert not ev.end_to_end_ok(word("तपस्", False, m), member)
