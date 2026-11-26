"""One self-contained static HTML page for a list of verse analyses."""

from __future__ import annotations

from html import escape as _esc
from typing import Any, Iterable

from . import jsonout
from .model import VerseAnalysis

TITLE = "मयूरस्य अष्टाध्यायी — Mayur's Ashtadhyayi · वाल्मीकिरामायणम्, बालकाण्डः १"
LEGEND = (
    "Each card analyses one verse of the Valmiki Ramayana, Bala-kanda 1. Sandhi is split back into words, "
    "every word is given its grammar, and each form is re-derived with Panini's rules (via vidyut). "
    "VERIFIED means the words re-join to the verse exactly. A tick means the word itself was derived by rules; "
    "words that are not (आर्ष) are labelled, never forced. Hover or tap a rule number, or a part of the translation."
)

CSS = """
:root{--bg:#faf8f4;--card:#fff;--ink:#1d1b18;--mute:#6b665e;--line:#e6e1d8;--accent:#8a3b12;--tint:#f6ece4;--ok:#2f6b3a;--no:#a23b2a;--hl:#ffe9a8}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#15130f;--card:#1e1b16;--ink:#ece7de;--mute:#a39c8f;--line:#35302a;--accent:#e59a68;--tint:#2b231c;--ok:#7bc58a;--no:#e58a7a;--hl:#5c4a14}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,"Noto Sans","Noto Sans Devanagari","Mangal","Nirmala UI","Lohit Devanagari",sans-serif}
.sa{font-family:"Noto Serif Devanagari","Noto Sans Devanagari","Sanskrit Text","Nirmala UI","Mangal","Lohit Devanagari",serif}
.wrap{max-width:62rem;margin:0 auto;padding:0 16px 3rem}
header{padding:2.5rem 0 1rem}
h1{font-size:1.7rem;line-height:1.3;margin:0 0 .6rem;font-weight:600}
.legend{color:var(--mute);max-width:46rem;margin:0 0 1rem}
.sum{display:flex;flex-wrap:wrap;gap:.5rem 1.5rem;margin:0;padding:0;list-style:none}
.sum b{color:var(--accent);font-size:1.25rem;font-variant-numeric:tabular-nums}
button.tog{margin-top:1rem;background:none;border:1px solid var(--line);color:var(--ink);padding:.3rem .8rem;border-radius:999px;font:inherit;cursor:pointer}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:1.4rem 1.2rem;margin:1.6rem 0;overflow-wrap:anywhere}
.verse{font-size:1.7rem;line-height:1.7;margin:0}
.iast{color:var(--mute);font-style:italic;margin:.2rem 0 .8rem}
.meta{display:flex;flex-wrap:wrap;gap:.4rem 1rem;align-items:center;color:var(--mute);font-size:.9rem}
.badge{display:inline-block;padding:.05rem .6rem;border-radius:999px;font-size:.78rem;font-weight:600;letter-spacing:.04em;border:1px solid}
.badge.verified{color:var(--ok);border-color:var(--ok)}
.badge.unverified{color:var(--no);border-color:var(--no)}
h2{font-size:.82rem;letter-spacing:.09em;text-transform:uppercase;color:var(--accent);margin:1.6rem 0 .5rem;font-weight:600}
h2 span{text-transform:none;letter-spacing:0;color:var(--mute);font-weight:400}
.scroll{overflow-x:auto;max-width:100%}
table{border-collapse:collapse;width:100%;font-size:.93rem;overflow-wrap:normal;word-break:normal}
.scroll table{min-width:38rem}
.scroll table.g{min-width:50rem}
th,td{text-align:left;vertical-align:top;padding:.45rem .6rem;border-bottom:1px solid var(--line)}
th{font-weight:600;color:var(--mute);font-size:.8rem;white-space:nowrap}
td .en{display:block;color:var(--mute);font-size:.82rem}
.big{font-size:1.1rem}
.pc{margin:.2rem 0}
.w{display:inline-block;padding:0 .15rem;border-radius:4px;font-size:1.2rem}
.w.hl,mark.al.hl,tr.hl td,.chip.hl{background:var(--hl)}
.jn{position:relative;display:inline-block;color:var(--accent);font-size:.75rem;cursor:pointer;margin:0 .35rem;vertical-align:super;outline:none}
.jn .tip{display:none;position:absolute;left:0;top:1.4em;z-index:5;min-width:14rem;max-width:80vw;background:var(--card);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:.5rem .7rem;font-size:.82rem;vertical-align:baseline;box-shadow:0 4px 18px rgba(0,0,0,.18)}
.jn .tip .r{display:block}.jn:hover .tip,.jn:focus .tip,.jn.open .tip{display:block}
.chips{display:flex;flex-wrap:wrap;gap:.4rem}
.chip{border:1px solid var(--line);border-radius:8px;padding:.15rem .6rem;font-size:.9rem}
.chip i{color:var(--mute);font-style:normal}
mark.al{background:var(--tint);color:inherit;border-radius:4px;padding:0 .1rem;cursor:pointer}
.ok{color:var(--ok);font-weight:700}.no{color:var(--no);font-weight:700}
.tag{white-space:nowrap;font-size:.75rem;border:1px solid var(--accent);color:var(--accent);border-radius:4px;padding:0 .35rem;margin-left:.3rem}
details{border:1px solid var(--line);border-radius:8px;margin:.4rem 0;padding:.3rem .8rem}
summary{cursor:pointer;color:var(--ink)}
summary::marker{color:var(--accent)}
.small{font-size:.85rem;color:var(--mute)}
ul.notes{margin:.3rem 0;padding-left:1.2rem}
footer{border-top:1px solid var(--line);margin-top:2.5rem;padding-top:1rem;color:var(--mute);font-size:.85rem}
a{color:var(--accent)}
@media (max-width:600px){h1{font-size:1.3rem}.verse{font-size:1.35rem}.card{padding:1rem .8rem}}
"""

JS = """
(function(){
var d=document;
function hl(card,w,on){card.querySelectorAll('[data-w="'+w+'"]').forEach(function(e){e.classList.toggle('hl',on)})}
d.querySelectorAll('.card').forEach(function(card){
  card.addEventListener('mouseover',function(e){var t=e.target.closest('[data-w]');if(t)hl(card,t.dataset.w,true)});
  card.addEventListener('mouseout',function(e){var t=e.target.closest('[data-w]');if(t)hl(card,t.dataset.w,false)});
  card.addEventListener('click',function(e){
    var j=e.target.closest('.jn');if(j){j.classList.toggle('open')}
    var t=e.target.closest('[data-w]');
    if(t&&t.matches('mark.al, .w')){var on=!t.classList.contains('hl');card.querySelectorAll('.hl').forEach(function(x){x.classList.remove('hl')});hl(card,t.dataset.w,on)}
  });
});
var b=d.getElementById('tog');
if(b){b.addEventListener('click',function(){var o=b.dataset.open!=='1';d.querySelectorAll('details').forEach(function(x){x.open=o});b.dataset.open=o?'1':'0';b.textContent=o?'Collapse all':'Expand all'})}
})();
"""


def esc(x: Any) -> str:
    return _esc("" if x is None else str(x), quote=True)


def _sa(v: dict[str, str] | None, cls: str = "") -> str:
    """A Sanskrit value: Devanagari with IAST beneath (when different and wanted)."""
    return f'<span class="sa {cls}">{esc((v or {}).get("devanagari", ""))}</span>'


def _iast(v: dict[str, str] | None) -> str:
    text = (v or {}).get("iast", "")
    return f'<span class="en">{esc(text)}</span>' if text else ""


def _terms(g: dict[str, Any]) -> str:
    keys = ("gender", "case", "number", "person", "tense_mood", "voice", "krt")
    return " ".join(esc(g[k]["devanagari"]) for k in keys if g.get(k))


def _badge(status: str) -> str:
    label = "VERIFIED" if status == "verified" else "UNVERIFIED"
    return f'<span class="badge {esc(status)}">{label}</span>'


def _metre(m: dict[str, Any]) -> str:
    parts = [str(m[k]) for k in ("name", "english") if m.get(k)]
    return " · ".join(esc(p) for p in parts)


# ---------------------------------------------------------------- sections

def _junction_tip(j: dict[str, Any]) -> str:
    rows = "".join(
        f'<span class="r"><b>{esc(s["source"]["devanagari"])} {esc(s["code"])}</b> '
        f'<span class="sa">{esc(s["text"]["devanagari"])}</span></span>'
        for s in j["sutras"]
    )
    surf = esc(j["surface"]["devanagari"])
    return f'<span class="tip"><span class="sa">{surf}</span>{rows}</span>'


def _padaccheda(data: dict[str, Any]) -> str:
    by_left = {j["left"]: j for j in data["junctions"]}
    lines: list[str] = []
    for ln in range(max(len(data["lines"]), 1 if data["words"] else 0)):
        out: list[str] = []
        words = [w for w in data["words"] if w["line"] == ln]
        for k, w in enumerate(words):
            out.append(f'<span class="w sa" data-w="{w["index"]}">{esc(w["form"]["devanagari"])}</span>')
            nxt_same = k + 1 < len(words) and w["compound"] is not None and words[k + 1]["compound"] == w["compound"]
            j = by_left.get(w["index"])
            if nxt_same:
                out.append("-")
            if j and j["sutras"]:
                nums = ", ".join(esc(s["code"]) for s in j["sutras"])
                out.append(f'<span class="jn" tabindex="0" title="{nums}">§{nums}{_junction_tip(j)}</span>')
            elif not nxt_same:
                out.append(" ")
        lines.append(f'<p class="pc">{"".join(out)}</p>')
    detail = "".join(
        f"<tr><td>{_sa(j['between'][0])} + {_sa(j['between'][1])}</td><td>{_sa(j['surface'])}</td>"
        f"<td>{'compound' if j['in_compound'] else 'words'}</td>"
        f"<td>{'<br>'.join(esc(s['code']) + ' ' + _sa(s['text']) for s in j['sutras']) or '—'}</td></tr>"
        for j in data["junctions"]
    )
    table = (f'<details><summary>Sandhi rules ({len(data["junctions"])} junctions)</summary><div class="scroll"><table>'
             f"<tr><th>Junction</th><th>Surface</th><th>In</th><th>Rules</th></tr>{detail}</table></div></details>"
             if data["junctions"] else "")
    return f"<h2>पदच्छेदः <span>word split</span></h2>{''.join(lines)}{table}"


def _compounds(data: dict[str, Any]) -> str:
    if not data["compounds"]:
        return ""
    rows = "".join(
        f"<tr><td>{' + '.join(_sa(m) for m in c['member_forms'])}</td>"
        f"<td>{esc(c['type']['devanagari'])}<span class='en'>{esc(c['type']['english'])}</span></td>"
        f"<td>{_sa(c['vigraha'])}</td><td class='small'>{esc(c['basis'])}</td></tr>"
        for c in data["compounds"]
    )
    return (f'<h2>समासः <span>compounds</span></h2><div class="scroll"><table><tr><th>Members</th><th>Type</th>'
            f"<th>Vigraha</th><th>Basis</th></tr>{rows}</table></div>")


def _grammar(data: dict[str, Any]) -> str:
    rows = []
    for w in data["words"]:
        g = w["grammar"]
        lemma = " ".join(_sa(g[k]) for k in ("lemma",) if g[k])
        root = f' <span class="small">धातुः {_sa(g["root"])}</span>' if g["root"] else ""
        mark = ('<span class="ok" title="derived by rules">✓</span>' if w["verified"]
                else f'<span class="no" title="{esc(w["verified_reason"])}">✗</span>')
        reason = f'<span class="en">{esc(w["verified_reason"])}</span>' if w["verified_reason"] else ""
        arsha = '<span class="tag">आर्ष</span>' if w["arsha"] else ""
        rows.append(
            f'<tr data-w="{w["index"]}"><td>{_sa(w["form"], "big")}{arsha}{_iast(w["form"])}</td>'
            f"<td>{lemma}{root}</td>"
            f"<td>{esc(g['kind']['devanagari'])} {_terms(g)}<span class='en'>{esc(w['description'])}</span></td>"
            f"<td>{esc(w['role']['devanagari'])}<span class='en'>{esc(w['role']['english'])}</span></td>"
            f"<td>{esc(w['gloss'])}</td><td>{mark}{reason}</td></tr>"
        )
    return (f'<h2>व्याकरणम् <span>grammar</span></h2><div class="scroll"><table class="g"><tr><th>Word</th><th>Lemma</th>'
            f"<th>Grammar</th><th>Role</th><th>Gloss</th><th>Proof</th></tr>{''.join(rows)}</table></div>")


def _anvaya(data: dict[str, Any]) -> str:
    a = data["anvaya"]
    if not a["order"]:
        return ""
    spans = " ".join(f'<span class="w sa" data-w="{i}">{esc(data["words"][i]["form"]["devanagari"])}</span>'
                     for i in a["order"] if i < len(data["words"]))
    return f'<h2>अन्वयः <span>prose order</span></h2><p>{spans}</p>'


def _gloss(data: dict[str, Any]) -> str:
    if not data["gloss"]:
        return ""
    chips = "".join(
        f'<span class="chip" data-w="{g["index"]}">{_sa(g["word"])} <i>{esc(g["gloss"] or "—")}</i></span>'
        for g in data["gloss"]
    )
    return f'<h2>पदार्थः <span>word by word</span></h2><div class="chips">{chips}</div>'


def _translation(data: dict[str, Any]) -> str:
    text = data["translation"]
    if not text:
        return ""
    out, pos = [], 0
    for a in sorted(data["alignment"], key=lambda a: (a["start"], a["end"])):
        if a["start"] < pos or a["end"] > len(text) or a["start"] >= a["end"]:
            continue
        out.append(esc(text[pos:a["start"]]))
        out.append(f'<mark class="al" data-w="{a["word"]}">{esc(text[a["start"]:a["end"]])}</mark>')
        pos = a["end"]
    out.append(esc(text[pos:]))
    return f'<h2>Translation</h2><p>{"".join(out)}</p>'


MAX_ALTERNATIVES_SHOWN = 5


def _alternatives(data: dict[str, Any]) -> str:
    """The next-best readings, each with its split in the summary line; the rest stay in the JSON."""
    items = []
    for alt in data["alternatives"][:MAX_ALTERNATIVES_SHOWN]:
        split = " । ".join(" ".join(esc(w["devanagari"]) for w in line) for line in alt["padaccheda"])
        scores = ", ".join(f"{esc(k)} {v:.2f}" for k, v in alt["scores"].items())
        items.append(
            f'<details><summary>{alt["rank"]}. <span class="sa">{split}</span> {_badge(alt["status"])}</summary>'
            f'<p class="small">scores: {scores or "—"}</p><p>{esc(alt["translation"])}</p></details>'
        )
    more = len(data["alternatives"]) - len(items)
    if more > 0:
        items.append(f'<p class="small">{more} more readings are kept in the JSON output.</p>')
    return f'<h2>Alternatives</h2>{"".join(items)}' if items else ""


def _traces(data: dict[str, Any]) -> str:
    items = []
    for w in data["words"]:
        if not w["sutra_trace"]:
            continue
        rows = "".join(
            f"<tr><td>{esc(s['code'])}<span class='en'>{_sa(s['source'])}</span></td>"
            f"<td>{_sa(s['sutra'])}</td><td>{_sa(s['result'])}</td></tr>"
            for s in w["sutra_trace"]
        )
        items.append(
            f'<details><summary>{_sa(w["form"])} <span class="small">{len(w["sutra_trace"])} steps</span></summary>'
            f'<div class="scroll"><table><tr><th>Rule</th><th>Text</th><th>Result</th></tr>{rows}</table></div></details>'
        )
    return f'<h2>सूत्राणि <span>sutra trace</span></h2>{"".join(items)}' if items else ""


def _notes(data: dict[str, Any]) -> str:
    notes = list(data["notes"])
    notes += [f"{w['form']['devanagari']}: आर्ष — {w['verified_reason']}" for w in data["words"] if w["arsha"]]
    if not notes:
        return ""
    return f'<h2>Notes</h2><ul class="notes">{"".join(f"<li>{esc(n)}</li>" for n in notes)}</ul>'


def _count(total: int, plain: int) -> str:
    """A split count for display: exact when small, a power of ten when huge."""
    def short(n: int) -> str:
        return str(n) if n < 100_000 else f"≈10^{len(str(n)) - 1}"
    return f"{short(total)} ({short(plain)})"


def _card(a: VerseAnalysis) -> str:
    data = jsonout.to_json(a)
    lines = "<br>".join(esc(x["devanagari"]) for x in data["lines"]) or esc(data["input"]["devanagari"])
    iast = "<br>".join(esc(x["iast"]) for x in data["lines"])
    splits = " · ".join(_count(n, m) for n, m in zip(data["split_counts"], data["split_counts_plain"])) or "—"
    meta = (f'<span>{esc(data["id"])}</span><span class="sa">{_metre(data["metre"])}</span>'
            f'{_badge(data["status"])}<span title="per half-verse: all dictionary words (ordinary words only)">valid splits: {esc(splits)}</span>')
    body = [_padaccheda(data), _compounds(data), _grammar(data), _anvaya(data), _gloss(data),
            _translation(data), _alternatives(data), _traces(data), _notes(data)]
    return (f'<article class="card" id="v-{esc(data["id"])}"><p class="verse sa">{lines}</p>'
            f'<p class="iast">{iast}</p><div class="meta">{meta}</div>{"".join(body)}</article>')


def _summary(analyses: Iterable[VerseAnalysis]) -> str:
    items = list(analyses)
    words = [w for a in items for w in (a.readings[0].words if a.readings else [])]
    proved = sum(1 for w in words if w.proof and w.proof.derivable)
    ok = sum(1 for a in items if a.status == "verified")
    return ("<ul class='sum'>"
            f"<li><b>{len(items)}</b> verses</li><li><b>{ok}</b> verified</li>"
            f"<li><b>{proved}</b> of {len(words)} words proof-verified</li></ul>")


def render(analyses: list[VerseAnalysis], title: str = TITLE) -> str:
    """The whole page as one HTML string."""
    cards = "".join(_card(a) for a in analyses)
    return (
        '<!doctype html><html lang="sa"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f"<title>{esc(title)}</title><style>{CSS}</style></head><body><div class=\"wrap\">"
        f'<header><h1 class="sa">{esc(title)}</h1><p class="legend">{esc(LEGEND)}</p>{_summary(analyses)}'
        '<button class="tog" id="tog" data-open="0">Expand all</button></header>'
        f"<main>{cards}</main>"
        "<footer>Grammar engine: <a href=\"https://github.com/ambuda-org/vidyut\">vidyut</a> (Ambuda, MIT). "
        "Corpus data: the Digital Corpus of Sanskrit (Oliver Hellwig, CC BY 4.0).</footer>"
        f"</div><script>{JS}</script></body></html>"
    )

