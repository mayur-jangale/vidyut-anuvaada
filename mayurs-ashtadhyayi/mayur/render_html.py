"""One self-contained static HTML page for a list of verse analyses."""

from __future__ import annotations

from html import escape as e
from typing import Any

from mayur.jsonout import to_json
from mayur.model import VerseAnalysis

TITLE = "Mayur's Ashtadhyayi – Vālmīki Rāmāyaṇa, Bālakāṇḍa 1"

CSS = """
:root{--bg:#fbfaf7;--fg:#222;--mut:#6b675f;--line:#e4e0d6;--card:#fff;--acc:#a4491f;--ok:#2d7a46;--bad:#b3392b;
--hi:#f6dfc9;--code:#f1eee6}
@media (prefers-color-scheme:dark){:root{--bg:#161513;--fg:#e8e4da;--mut:#a09b8f;--line:#33302a;--card:#1e1c19;
--acc:#e08a5a;--ok:#6cc189;--bad:#ef7d6d;--hi:#4a3322;--code:#27241f}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);line-height:1.6;font-size:17px;
font-family:Georgia,"Noto Serif","Noto Serif Devanagari","Nirmala UI","Mangal","Kohinoor Devanagari","Devanagari Sangam MN",serif}
.dev{font-family:"Noto Serif Devanagari","Noto Sans Devanagari","Nirmala UI","Mangal","Kohinoor Devanagari","Devanagari Sangam MN","Lohit Devanagari",serif}
main,header.top,footer{max-width:62rem;margin:0 auto;padding:0 16px}
header.top{padding-top:2.5rem}
h1{font-size:1.7rem;margin:0 0 .5rem;line-height:1.25}
h2{font-size:.78rem;letter-spacing:.09em;text-transform:uppercase;color:var(--acc);margin:1.6rem 0 .5rem;font-weight:600;
font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
.legend,.summary,.mut{color:var(--mut);font-size:.92rem}
.summary b{color:var(--fg)}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;margin:2rem 0;padding:1.2rem 1.4rem 1.4rem}
.head{display:flex;flex-wrap:wrap;gap:.5rem 1rem;align-items:center;font-size:.9rem;color:var(--mut);
font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
.vid{font-weight:700;color:var(--fg);font-size:1rem}
.badge{padding:.1rem .6rem;border-radius:999px;font-weight:700;font-size:.78rem;letter-spacing:.05em;border:1px solid}
.badge.verified{color:var(--ok)}.badge.unverified{color:var(--bad)}
.verse{font-size:1.75rem;line-height:1.7;margin:.8rem 0 0;white-space:pre-line}
.iast{color:var(--mut);font-style:italic;white-space:pre-line;margin:.2rem 0 0}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;width:100%;font-size:.95rem}
th,td{text-align:left;padding:.4rem .6rem;border-bottom:1px solid var(--line);vertical-align:top}
th{font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-size:.75rem;color:var(--mut);font-weight:600;white-space:nowrap}
.tick{color:var(--ok);font-weight:700}.cross{color:var(--bad);font-weight:700}
.tag{font-size:.75rem;border:1px solid var(--acc);color:var(--acc);border-radius:4px;padding:0 .35rem;margin-left:.3rem}
.wd.hl,.al.hl,tr.hl td{background:var(--hi);border-radius:3px}
.al{cursor:pointer;border-bottom:1px dotted var(--acc)}
.pada .wd{padding:0 .1rem}
details{margin:.4rem 0}summary{cursor:pointer;color:var(--acc);font-size:.95rem}
code,.mono{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:.86rem;background:var(--code);
border-radius:3px;padding:0 .25rem}
ol.gl{padding-left:0;list-style:none;display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;margin:0}
ol.gl li span{display:block;color:var(--mut);font-size:.85rem}
ul.notes{margin:.2rem 0;padding-left:1.2rem}
footer{color:var(--mut);font-size:.85rem;padding-bottom:3rem}
@media (max-width:600px){body{font-size:16px}.card{padding:1rem}.verse{font-size:1.45rem}h1{font-size:1.4rem}}
"""

JS = """
document.addEventListener('mouseover',hl);document.addEventListener('click',hl);
function hl(ev){var t=ev.target.closest&&ev.target.closest('.al');
document.querySelectorAll('.hl').forEach(function(n){n.classList.remove('hl')});
if(!t)return;var c=t.closest('.card');t.classList.add('hl');
c.querySelectorAll('[data-w="'+t.dataset.w+'"]').forEach(function(n){n.classList.add('hl')});}
function setAll(open){document.querySelectorAll('details').forEach(function(d){d.open=open});}
"""


def _tag(name: str, text: str, cls: str = "") -> str:
    return f'<{name}{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>{text}</{name}>'


def _section(title: str, body: str) -> str:
    return f"<section><h2>{e(title)}</h2>{body}</section>" if body else ""


def _metre(m: dict[str, Any]) -> str:
    if not m:
        return "metre: –"
    name = m.get("name_devanagari") or m.get("name")
    return "metre: " + (str(name) if name else "not identified")


def _pada(d: dict[str, Any]) -> str:
    out = []
    for line in range(len(d["lines"])):
        ws = [w for w in d["words"] if w["line"] == line]
        parts: list[str] = []
        for k, w in enumerate(ws):
            glue = w["in_compound"] and k + 1 < len(ws) and ws[k + 1]["compound"] == w["compound"]
            parts.append(f'<span class="wd" data-w="{w["index"]}">{e(w["form"]["devanagari"])}</span>'
                         + ("-" if glue else " "))
        out.append(f'<div class="dev">{"".join(parts).strip()}</div>')
    return "".join(out) or '<span class="mut">no split</span>'


def _compounds(d: dict[str, Any]) -> str:
    rows = "".join(
        f'<tr><td class="dev">{e("-".join(m["devanagari"] for m in c["members"]))}<br>'
        f'<span class="mut">{e("-".join(m["iast"] for m in c["members"]))}</span></td>'
        f'<td>{e(c["type"] or "?")}</td><td class="dev">{e(c["vigraha"]["devanagari"])}<br>'
        f'<span class="mut">{e(c["vigraha"]["iast"])}</span></td><td class="mut">{e(c["basis"])}</td></tr>'
        for c in d["compounds"])
    if not rows:
        return ""
    return ('<div class="scroll"><table><tr><th>members</th><th>type</th><th>vigraha</th><th>basis</th></tr>'
            + rows + "</table></div>")


def _grammar(d: dict[str, Any]) -> str:
    rows = []
    for w in d["words"]:
        a = w["analysis"]
        dv = a.get("devanagari", {})
        lemma = (f'<span class="dev">{e(dv.get("lemma", ""))}</span><br><span class="mut">'
                 f'{e(a.get("lemma_iast", "") or a["lemma"])}</span>'
                 + (f'<br><span class="mut">धातु <span class="dev">{e(dv.get("root", ""))}</span></span>'
                    if a.get("root") else ""))
        terms = " ".join(dv.get(k, "") for k in ("gender", "case", "number", "person", "tense_mood", "voice", "krt"))
        mark = ('<span class="tick" title="derived">✓</span>' if w["verified"]
                else f'<span class="cross">✗</span> <span class="mut">{e(w["verified_reason"])}</span>')
        arsha = '<span class="tag">ārṣa</span>' if w["arsha"] else ""
        rows.append(
            f'<tr data-w="{w["index"]}" class="wd"><td><span class="dev">{e(w["form"]["devanagari"])}</span><br>'
            f'<span class="mut">{e(w["form"]["iast"])}</span>{arsha}</td><td>{lemma}</td>'
            f'<td><span class="dev">{e(" ".join(terms.split()))}</span><br><span class="mut">'
            f'{e(a["description"])}</span></td><td>{e(w["role"])}</td><td>{e(w["gloss"])}</td><td>{mark}</td></tr>')
    if not rows:
        return ""
    return ('<div class="scroll"><table><tr><th>word</th><th>lemma / root</th><th>grammar</th><th>role</th>'
            '<th>gloss</th><th>verified</th></tr>' + "".join(rows) + "</table></div>")


def _translation(d: dict[str, Any]) -> str:
    text = d["translation"]
    if not text:
        return ""
    out, pos = [], 0
    for a in sorted(d["alignment"], key=lambda x: (x["start"], x["end"])):
        if a["start"] < pos or a["end"] > len(text) or a["start"] >= a["end"]:
            continue
        out.append(e(text[pos:a["start"]]))
        out.append(f'<span class="al" data-w="{a["word"]}">{e(text[a["start"]:a["end"]])}</span>')
        pos = a["end"]
    out.append(e(text[pos:]))
    return f'<p>{"".join(out)}</p>'


def _alternatives(d: dict[str, Any]) -> str:
    items = []
    for alt in d["alternatives"]:
        sc = ", ".join(f"{k} {v:.2f}" for k, v in alt["scores"].items())
        split = " / ".join(f'<span class="dev">{e(p["devanagari"])}</span> <span class="mut">{e(p["iast"])}</span>'
                           for p in alt["padaccheda"])
        items.append(f'<details><summary>Reading {alt["rank"] + 1} – {e(alt["status"])}</summary>'
                     f'<p>{split}</p><p class="mut">{e(sc)}</p>'
                     f'<p>{e(alt["translation"])}</p></details>')
    return "".join(items)


def _traces(d: dict[str, Any]) -> str:
    items = []
    for w in d["words"]:
        if not w["sutra_trace"]:
            continue
        rows = "".join(
            f'<tr><td class="mono">{e(s["code"])}</td><td class="dev">{e(s["sutra"]["devanagari"])}'
            f'<br><span class="mut">{e(s["sutra"]["source_devanagari"])}</span></td>'
            f'<td class="dev">{e(s["result_devanagari"])}</td></tr>' for s in w["sutra_trace"])
        items.append(f'<details><summary><span class="dev">{e(w["form"]["devanagari"])}</span> '
                     f'{e(w["form"]["iast"])} – {len(w["sutra_trace"])} steps</summary>'
                     f'<div class="scroll"><table><tr><th>rule</th><th>sūtra</th><th>state</th></tr>{rows}'
                     "</table></div></details>")
    return "".join(items)


def _gloss(d: dict[str, Any]) -> str:
    items = "".join(f'<li><b class="wd dev" data-w="{i}">{e(g["devanagari"])}</b>'
                    f'<span>{e(g["iast"])} · {e(g["gloss"])}</span></li>'
                    for i, g in enumerate(d["gloss"]))
    return f'<ol class="gl">{items}</ol>' if items else ""


def _notes(d: dict[str, Any]) -> str:
    notes = list(d["notes"]) + list(d["reading_notes"])
    notes += [f'{w["form"]["iast"]}: arsha (not forced into a Paninian parse)' for w in d["words"] if w["arsha"]]
    return "<ul class='notes'>" + "".join(f"<li>{e(n)}</li>" for n in notes) + "</ul>" if notes else ""


def _card(a: VerseAnalysis, n: int) -> str:
    d = to_json(a, full=True)
    st = a.status if a.status in ("verified", "unverified") else "unverified"
    splits = " · ".join(str(c) for c in d["split_counts"]) or "–"
    anv = d["anvaya"]
    parts = [
        f'<article class="card" id="v{n}"><div class="head"><span class="vid">{e(a.id or str(n))}</span>'
        f'<span class="badge {st}">{st.upper()}</span><span>{e(_metre(d["metre"]))}</span>'
        f'<span>valid splits per line: {e(splits)}</span></div>',
        f'<p class="verse dev">{e(chr(10).join(l["devanagari"] for l in d["lines"]) or a.input)}</p>',
        f'<p class="iast">{e(chr(10).join(l["iast"] for l in d["lines"]))}</p>',
        _section("Padaccheda", f'<div class="pada">{_pada(d)}</div>'),
        _section("Compounds", _compounds(d)),
        _section("Grammar", _grammar(d)),
        _section("Anvaya", f'<div class="dev">{e(anv["devanagari"])}</div><div class="mut">{e(anv["iast"])}</div>'
                 if anv["order"] else ""),
        _section("Word by word", _gloss(d)),
        _section("Translation (literal)", _translation(d)),
        _section("Alternatives", _alternatives(d)),
        _section("Sūtra trace", _traces(d)),
        _section("Notes", _notes(d)),
        "</article>",
    ]
    return "".join(parts)


def render(analyses: list[VerseAnalysis], title: str = TITLE) -> str:
    """Render ``analyses`` as a single offline HTML document."""
    words = [w for a in analyses for w in (a.readings[0].words if a.readings else [])]
    proven = sum(1 for w in words if w.proof and w.proof.derivable)
    verified = sum(1 for a in analyses if a.status == "verified")
    summary = (f"<b>{len(analyses)}</b> verses · <b>{verified}</b> verified · "
               f"<b>{proven}</b> of <b>{len(words)}</b> words proof-verified")
    legend = ("VERIFIED: the split re-joins to the text and every word is derived by Pāṇini's rules. "
              "UNVERIFIED: at least one check is missing; the reason is given in the grammar table. "
              "Compound types are heuristic. Tap a word of the translation to see its Sanskrit source.")
    cards = "".join(_card(a, i + 1) for i, a in enumerate(analyses))
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title>'
            f"<style>{CSS}</style></head><body><header class=\"top\"><h1>{e(title)}</h1>"
            f'<p class="legend">{e(legend)}</p><p class="summary">{summary}</p>'
            f'<p><a href="#" onclick="setAll(true);return false" class="mut">expand all</a> · '
            f'<a href="#" onclick="setAll(false);return false" class="mut">collapse all</a></p></header>'
            f"<main>{cards}</main><footer>Data: vidyut (Ambuda, MIT) and the Digital Corpus of Sanskrit "
            f"(Oliver Hellwig, CC BY 4.0).</footer><script>{JS}</script></body></html>")
