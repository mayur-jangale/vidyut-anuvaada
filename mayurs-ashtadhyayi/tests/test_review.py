"""Review sheet export/import (scripts/export_review.py, scripts/import_review.py) on hand-made data."""

from types import SimpleNamespace as NS

from scripts import export_review as ex
from scripts import import_review as im


def fake_reading():
    morph = NS(lemma="राम", kind="subanta", linga="पुंलिङ्ग", vibhakti="प्रथमा", vacana="एकवचन", krt=None,
               lakara=None, purusha=None, prayoga=None)
    verb = NS(lemma="गम्", kind="tinanta", linga=None, vibhakti=None, vacana="एकवचन", krt=None,
              lakara="लट्", purusha="प्रथमपुरुष", prayoga="कर्तरि")
    words = [NS(form="राज", line=0, in_compound=True, morph=None, role="समासपूर्वपद", head=1, gloss="king"),
             NS(form="पुत्रस्", line=0, in_compound=False, morph=morph, role="कर्ता", head=2, gloss="son"),
             NS(form="गच्छति", line=1, in_compound=False, morph=verb, role="क्रिया", head=None, gloss="goes")]
    return NS(words=words, compounds=[NS(id=0, members=[0, 1], samasa="तत्पुरुष")], anvaya=[1, 2, 0])


def test_rows_for_numbers_words_from_one_and_marks_clause_head_zero():
    rows = ex.rows_for(fake_reading(), "वि १")
    assert [r["शब्दसङ्ख्या"] for r in rows] == ["1", "2", "3"]
    assert [r["शीर्ष_सं"] for r in rows] == ["2", "3", "0"]
    assert rows[0]["समासः"] == rows[1]["समासः"] == "तत्पुरुष" and rows[2]["समासः"] == ""
    assert rows[1]["व्याकरणम्"] == "पुंलिङ्ग प्रथमा एकवचन" and rows[2]["व्याकरणम्"] == "लट् प्रथमपुरुष एकवचन कर्तरि"
    assert [r["अन्वय_सं"] for r in rows] == ["3", "1", "2"]
    assert all(rows[0][c] == "" for c in ex.REVIEW_COLUMNS)


def test_tsv_roundtrip_has_comment_header_and_one_row_per_word():
    text = ex.to_tsv(ex.rows_for(fake_reading(), "वि १"))
    assert text.startswith("# ")
    rows = im.read_rows(text)
    assert len(rows) == 3 and rows[1]["शब्द"] == "पुत्रस्"


def test_unreviewed_verse_is_skipped_and_reviewed_one_imported():
    text = ex.to_tsv(ex.rows_for(fake_reading(), "वि १"))
    doc = im.import_sheet(text)
    assert doc["sentences"] == [] and doc["skipped_unreviewed"] == ["वि १"]
    assert len(im.import_sheet(text, accept_unreviewed=True)["sentences"]) == 1


def corrected(text):
    lines = text.splitlines()
    out = []
    for ln in lines:
        cells = ln.split("\t")
        if len(cells) > 10 and cells[3] == "पुत्रस्":
            cells[-5:] = ["कर्म", "3", "बहुव्रीहि", "1", "ठीक"]
            ln = "\t".join(cells)
        out.append(ln)
    return "\n".join(out) + "\n"


def test_corrections_override_our_values_and_empty_cells_keep_them():
    text = corrected(ex.to_tsv(ex.rows_for(fake_reading(), "वि १")))
    (s,) = im.import_sheet(text)["sentences"]
    assert [w["role"] for w in s["words"]] == ["समासपूर्वपद", "कर्म", "क्रिया"]
    assert [w["head_index"] for w in s["words"]] == [1, 2, None]  # 1-based sheet numbers -> 0-based, 0 -> None
    assert s["words"][0]["compound_member"] is True and s["words"][1]["compound_member"] is False
    assert s["compounds"] == [{"members": [0, 1], "type": "बहुव्रीहि", "vigraha": ""}]
    assert s["anvaya"] == [1, 2, 0] or s["anvaya"][0] == 1  # corrected position 1 for word 2 comes first


def test_bad_number_in_a_correction_is_reported():
    text = ex.to_tsv(ex.rows_for(fake_reading(), "वि १")).replace("\t\t\t\t\t\n", "\t\tx\t\t\t\n", 1)
    try:
        im.import_sheet(text)
    except ValueError as exc:
        assert "not a number" in str(exc)
    else:
        raise AssertionError("expected ValueError")
