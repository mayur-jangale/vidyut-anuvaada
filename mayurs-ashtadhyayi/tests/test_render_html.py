from html.parser import HTMLParser

from mayur.model import VerseAnalysis
from mayur.render_html import render
from tests.fixtures_ui import XSS, make_analysis


class Collect(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags, self.classes, self.text = [], [], []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.classes += (dict(attrs).get("class") or "").split()

    def handle_data(self, data):
        self.text.append(data)


def parse(doc):
    p = Collect()
    p.feed(doc)
    p.close()
    return p


def test_one_card_per_verse_and_parts():
    doc = render([make_analysis("1.1"), make_analysis("1.2")])
    p = parse(doc)
    assert p.classes.count("card") == 2
    assert doc.count("badge unverified") == 2
    assert "details" in p.tags and "table" in p.tags
    assert "Reading 2" in doc and "3.2.123" in doc and "mahā-rāja-putras" in doc
    assert "VERIFIED" in doc.upper() and "Digital Corpus of Sanskrit" in doc
    assert "<script src" not in doc and "http" not in doc.replace("https://example.invalid", "")


def test_escaping():
    doc = render([make_analysis()])
    assert XSS not in doc
    assert "&lt;script&gt;alert" in doc
    assert doc.count("<script>") == 1  # only the inline expand/collapse JS


def test_alignment_spans_and_verified_marks():
    doc = render([make_analysis()])
    assert 'class="al" data-w="2"' in doc
    assert "✓" in doc and "✗" in doc


def test_empty_fields_and_no_readings():
    a = VerseAnalysis(id="", input="")
    doc = render([a], title="<b>t</b>")
    assert parse(doc).classes.count("card") == 1
    assert "<b>t</b>" not in doc
    assert "<article" not in render([])
