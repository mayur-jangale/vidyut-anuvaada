from __future__ import annotations

import sys
from html.parser import HTMLParser
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from ui_fixture import make_analysis  # noqa: E402

from mayur import jsonout, render_html  # noqa: E402
from mayur.model import VerseAnalysis  # noqa: E402


@pytest.fixture(autouse=True)
def _rules(monkeypatch):
    monkeypatch.setattr(jsonout, "rule_texts", lambda: {("अष्टाध्यायी", "6.1.87"): "आद्गुणः"})


class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags, self.classes, self.scripts = [], [], 0

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.classes += (dict(attrs).get("class") or "").split()
        if tag == "script":
            self.scripts += 1


def parse(page: str) -> Collect:
    p = Collect()
    p.feed(page)
    return p


def test_one_card_per_verse_and_parts():
    page = render_html.render([make_analysis("1.1"), make_analysis("1.2")])
    p = parse(page)
    assert p.classes.count("card") == 2
    assert "verified" in p.classes and "details" in p.tags and "table" in p.tags
    assert "VERIFIED" in page and "आद्गुणः" in page and "आर्ष" in page
    assert "Digital Corpus of Sanskrit" in page and "vidyut" in page
    assert page.startswith("<!doctype html>")


def test_header_title_and_counts():
    page = render_html.render([make_analysis()])
    assert render_html.esc(render_html.TITLE) in page
    assert "words proof-verified" in page


def test_script_in_gloss_is_escaped():
    a = make_analysis()
    a.readings[0].words[0].gloss = "<script>alert(1)</script>"
    a.notes = ['<img src=x onerror=alert(1)>']
    page = render_html.render([a])
    assert "<script>alert(1)</script>" not in page
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in page
    assert "<img src=x" not in page
    assert parse(page).scripts == 1  # only our own inline script


def test_empty_fields_and_no_verses():
    parse(render_html.render([]))
    page = render_html.render([VerseAnalysis(id="", input="")])
    assert parse(page).classes.count("card") == 1


def test_no_external_assets():
    page = render_html.render([make_analysis()])
    assert "http://" not in page.replace("http://www.w3.org", "")
    assert "<link" not in page and "src=" not in page


def test_translation_alignment_marks():
    page = render_html.render([make_analysis()])
    assert 'class="al" data-w="8"' in page
