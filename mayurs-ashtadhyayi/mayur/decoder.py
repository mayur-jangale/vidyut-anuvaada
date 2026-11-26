"""Learned first-order decoding INSIDE the segmenter's lattice (validity stays rule-based).

Score(path) = Σ w·f(edge) + Σ w·g(previous word, word). Edge features include a sound-level
boundary model and junction-rule statistics estimated from TRAIN gold (tables in the model file).
Viterbi over lattice states keeps a beam of hypotheses per state; no path list is materialised.
Weights: mayur/models/lattice_decoder.json (trained on Digital Corpus of Sanskrit annotations, CC BY 4.0).
The segmenter's lattice is used read-only (``_Lattice``, ``_prepare``, ``_START``, ``_END``).
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from mayur import freq, ranker
from mayur import sandhi as sd
from mayur import segmenter as sg
from mayur.lipi import from_varnas
from mayur.segmenter import Split

MODEL_FILE = Path(__file__).with_name("models") / "lattice_decoder.json"
BEAM = 12
SAME_PREV = 4  # hypotheses kept per distinct previous word at one state
BOUNDARY_K = 3
BOUNDARY_MIN = 3
KINDS = ("none", "pada", "cpd")
_START_TAG, _END_TAG = ranker._START_TAG, ranker._END_TAG
Feats = tuple[tuple[str, float], ...]


@dataclass(frozen=True)
class Edge:
    src: int
    dst: int
    form: str
    samasa: bool
    tag: str
    feats: Feats
    start: int = 0  # first sound position of the word in the text
    end: int = 0  # position where the right junction's surface starts
    kind: str = "end"  # right junction: end | cpd | space | inner
    jsurf: str = ""  # junction surface + following sound
    jcls: str = ""  # junction rule class
    q0: bool = False


@dataclass(frozen=True)
class Graph:
    """Compact lattice: node 0 is the start, ``end`` the final node, ``out[n]`` edge ids, topological."""
    edges: tuple[Edge, ...]
    out: tuple[tuple[int, ...], ...]
    order: tuple[int, ...]
    end: int
    text: tuple[str, ...] = ()
    spaces: frozenset = frozenset()


def _junction_kind(lat: Any, e: tuple) -> str:
    _, k, jn, _, _, nxt = e
    if nxt == sg._END:
        return "end"
    if jn.samasa:
        return "cpd"
    return "space" if any(k <= s <= nxt[0] for s in lat.sp) else "inner"


def _endings(form: str, samasa: bool) -> dict[str, float]:
    v = sd.varnas(form)
    role = "C" if samasa else "P"
    return {f"end{n}:{''.join(v[-n:])}|{role}": 1.0 for n in (1, 2, 3) if len(v) > n}


def edge_features(lat: Any, state: tuple, e: tuple, table: Mapping[str, float]) -> dict[str, float]:
    """Generic static features of one lattice edge (word + its right junction)."""
    form, k, jn, base, plain, nxt = e
    i, _, after_samasa = state
    f: dict[str, float] = {"base": float(base), "bias": 1.0}
    f.update(ranker._word_feats(form, jn.samasa))
    f.update(_endings(form, jn.samasa))
    kind = _junction_kind(lat, e)
    f[f"j_{kind}"] = 1.0
    f[f"j_{kind}_{'sandhi' if jn.sutras else 'plain'}"] = 1.0
    left_inner = i > 0 and i not in lat.sp and not after_samasa
    if (kind == "inner" or left_inner) and ranker.syllables(form) <= 2:
        f["j_short_inner"] = 1.0
    if sg._unmarked_elision(jn):
        f["j_unmarked_elision"] = 1.0
    if "८.३.२२" in jn.sutras:
        f["j_aas_as_aa"] = 1.0
    if after_samasa and not jn.samasa:
        f["cpd_final"] = 1.0
    if not jn.left_ctx and base <= -40.0:
        f["chunk_fallback"] = 1.0
    if not plain:
        f["not_plain"] = 1.0
    if nxt == sg._END:
        f["tag_end"] = table.get(f"{ranker.word_tag(form, jn.samasa)}|{_END_TAG}", table.get("<unk>", -8.0))
    return f


def _bigram(a: str, b: str) -> float:
    fn = getattr(freq, "bigram_count", None)
    return math.log1p(fn(a, b)) if fn is not None else 0.0


@lru_cache(maxsize=500_000)
def pair_features(prev: Optional[tuple[str, bool, str]], cur: tuple[str, bool, str], table_id: int = 0) -> Feats:
    """Features of (previous word, word); words are (form, in_compound, tag). ``prev`` None = line start."""
    table = _TABLES.get(table_id, {})
    unk = table.get("<unk>", -8.0)
    pf, ps, pt = prev if prev is not None else ("", False, _START_TAG)
    cf, cs, ct = cur
    out: dict[str, float] = {"tag_bigram": table.get(f"{pt}|{ct}", unk)}
    if prev is None:
        return tuple(out.items())
    if not ps:
        out["pair_logbigram"] = _bigram(pf, cf)
    if pt.startswith("subanta:") and ct.startswith("subanta:"):
        out["pair_case_agree" if pt == ct else "pair_case_differ"] = 1.0
    if pt == "subanta:प्रथमा" and ct == "tinanta":
        out["pair_nom_verb"] = 1.0
    if pt == "subanta:षष्ठी" and ct.startswith("subanta:"):
        out["pair_gen_nominal"] = 1.0
    if ps and not cs and ct.startswith("subanta:"):
        out["pair_cpd_nominal_final"] = 1.0
    if ps and not cs and ct == "tinanta":
        out["pair_cpd_verb_final"] = 1.0
    return tuple(out.items())


_TABLES: dict[int, dict[str, float]] = {}


def register_table(table: Mapping[str, float]) -> int:
    """Make a tag-bigram table available to ``pair_features`` under a stable id."""
    tid = len(_TABLES) + 1
    _TABLES[tid] = dict(table)
    return tid


# ---------------------------------------------------------------- boundary + junction statistics

def boundary_keys(text: Sequence[str], spaces: frozenset, p: int) -> list[str]:
    """Context keys (most specific first) of the position before sound ``p``."""
    sp = "_" if p in spaces else "."
    return [f"{k}|{''.join(text[max(0, p - k):p])}|{''.join(text[p:p + k])}|{sp}" for k in range(BOUNDARY_K, 0, -1)]


def boundary_logprobs(text: Sequence[str], spaces: frozenset, table: Mapping[str, Sequence[int]]) -> list[tuple]:
    """Per position p (0..n): log P(none), log P(pada), log P(cpd) with back-off; zeros when unknown."""
    out = []
    for p in range(len(text) + 1):
        lp = (0.0, 0.0, 0.0)
        for key in boundary_keys(text, spaces, p):
            c = table.get(key)
            if c and sum(c) >= BOUNDARY_MIN:
                tot = sum(c) + 0.3
                lp = tuple(math.log((x + 0.1) / tot) for x in c)
                break
        out.append(lp)
    return out


def dynamic_features(g: Graph, tables: Mapping[str, Any]) -> list[Feats]:
    """Per edge: boundary-model and junction-statistics features (tables from the model)."""
    btab, jtab = tables.get("boundary", {}), tables.get("junction", {})
    if not btab and not jtab:
        return [()] * len(g.edges)
    lps = boundary_logprobs(g.text, g.spaces, btab) if btab else []
    out = []
    for e in g.edges:
        f: list[tuple[str, float]] = []
        if lps:
            inside = sum(lps[p][0] for p in range(e.start + 1, min(e.end, len(lps))))
            f.append(("bnd_inside", inside))
            if e.kind != "end" and e.end < len(lps):
                f.append(("bnd_right", lps[e.end][2 if e.kind == "cpd" else 1]))
        if jtab and e.kind != "end":
            dist = jtab.get(e.jsurf)
            if dist:
                tot = sum(dist.values()) + 0.5 * (len(dist) + 1)
                f.append(("junc_logp", math.log((dist.get(e.jcls, 0) + 0.5) / tot)))
            else:
                f.append(("junc_unseen", 1.0))
        out.append(tuple(f))
    return out


# ---------------------------------------------------------------- lattice -> graph

def lattice(line: str) -> Optional[Any]:
    """The segmenter's lattice at the first tier that has a valid path (or None)."""
    text, spaces = sg._prepare(line)
    for tier in (0, 1, 2):
        lat = sg._Lattice(text, spaces, tier)
        if _reachable(lat)[1]:
            return lat
    return None


def _reachable(lat: Any) -> tuple[list[tuple], bool]:
    """States reachable from the start that can reach the end, in topological order."""
    seen, stack, post = {sg._START}, [(sg._START, 0)], []
    while stack:
        st, idx = stack.pop()
        es = lat.edges(st) if st != sg._END else []
        if idx < len(es):
            stack.append((st, idx + 1))
            nxt = es[idx][5]
            if nxt not in seen:
                seen.add(nxt)
                stack.append((nxt, 0))
        else:
            post.append(st)
    if sg._END not in seen:
        return [], False
    alive = {sg._END}
    for st in post:  # post-order: successors first
        if st != sg._END and any(e[5] in alive for e in lat.edges(st)):
            alive.add(st)
    return [s for s in reversed(post) if s in alive], True


def _jkey(lat: Any, e: tuple) -> tuple[str, str]:
    _, k, jn, _, _, nxt = e
    j = nxt[0] if nxt != sg._END else -1
    follow = lat.t[j] if 0 <= j < lat.n else "#"
    surf = f"{from_varnas(jn.surface)}+{follow}"
    cls = f"{from_varnas(jn.left_tail)}>{from_varnas(jn.right_head)}:{int(jn.samasa)}:{','.join(jn.sutras)}"
    return surf, cls


def build_graph(lat: Any, table: Mapping[str, float]) -> tuple[Graph, list[tuple]]:
    """Compact graph of ``lat`` plus, per edge, the raw (state, edge) for ``Split`` construction."""
    states, _ = _reachable(lat)
    index = {s: n for n, s in enumerate(states)}
    edges, raw, out = [], [], [[] for _ in states]
    for st in states:
        if st == sg._END:
            continue
        for e in lat.edges(st):
            if e[5] not in index:
                continue
            feats = edge_features(lat, st, e, table)
            surf, cls = _jkey(lat, e)
            out[index[st]].append(len(edges))
            edges.append(Edge(index[st], index[e[5]], e[0], e[2].samasa, ranker.word_tag(e[0], e[2].samasa),
                              tuple(sorted(feats.items())), st[0], e[1], _junction_kind(lat, e), surf, cls,
                              "w_q0" in feats))
            raw.append((st, e))
    return Graph(tuple(edges), tuple(map(tuple, out)), tuple(range(len(states))), index.get(sg._END, -1),
                 tuple(lat.t), frozenset(lat.sp)), raw


# ---------------------------------------------------------------- decoding

def _dot(w: Mapping[str, float], feats: Sequence[tuple[str, float]]) -> float:
    return sum(w.get(k, 0.0) * v for k, v in feats)


def _word(e: Edge) -> tuple[str, bool, str]:
    return e.form, e.samasa, e.tag


def viterbi(g: Graph, w: Mapping[str, float], table_id: int, top_k: int = 1, beam: int = BEAM,
            extra: Optional[Sequence[Feats]] = None) -> list[tuple[float, tuple[int, ...]]]:
    """Up to ``top_k`` best (score, edge ids) paths; beam of hypotheses per node."""
    if g.end < 0:
        return []
    edge_score = [_dot(w, e.feats) + (_dot(w, extra[n]) if extra else 0.0) for n, e in enumerate(g.edges)]
    hyps: dict[int, list] = {0: [(0.0, -1, None, 0)]}  # (score, edge id, parent hyp, word-sequence hash)
    width = max(beam, top_k)
    for n in g.order:
        cur = hyps.pop(n, None)
        if not cur:
            continue
        cur = _prune(cur, g, top_k, top_k) if n == g.end else _prune(cur, g, width, SAME_PREV)
        if n == g.end:
            hyps[n] = cur
            break
        for h in cur:
            prev = None if h[1] < 0 else _word(g.edges[h[1]])
            for eid in g.out[n]:
                e = g.edges[eid]
                s = h[0] + edge_score[eid] + _dot(w, pair_features(prev, _word(e), table_id))
                hyps.setdefault(e.dst, []).append((s, eid, h, hash((h[3], e.form, e.samasa))))
    out = []
    for h in sorted(hyps.get(g.end, []), key=lambda t: -t[0])[:top_k]:
        path, node = [], h
        while node is not None and node[1] >= 0:
            path.append(node[1])
            node = node[2]
        out.append((h[0], tuple(reversed(path))))
    return out


def _prune(cands: list, g: Graph, width: int, same_prev: int) -> list:
    cands.sort(key=lambda t: -t[0])
    kept, per_prev, seqs = [], {}, set()
    for h in cands:
        key = g.edges[h[1]].form if h[1] >= 0 else ""
        if per_prev.get(key, 0) >= same_prev or h[3] in seqs:
            continue  # same word sequence via another junction analysis, or too many with this word
        seqs.add(h[3])
        per_prev[key] = per_prev.get(key, 0) + 1
        kept.append(h)
        if len(kept) >= width:
            break
    return kept


def path_features(g: Graph, path: Sequence[int], table_id: int,
                  extra: Optional[Sequence[Feats]] = None) -> dict[str, float]:
    acc: dict[str, float] = {}
    prev = None
    for eid in path:
        e = g.edges[eid]
        for k, v in (*e.feats, *(extra[eid] if extra else ()), *pair_features(prev, _word(e), table_id)):
            acc[k] = acc.get(k, 0.0) + v
        prev = _word(e)
    return acc


def order_alternatives(g: Graph, paths: list[tuple[float, tuple[int, ...]]], top_k: int) -> list:
    """Distinct word sequences; after the best, paths with a quality-0 word go after clean ones."""
    seen, uniq = set(), []
    for score, path in paths:
        key = tuple((g.edges[i].form, g.edges[i].samasa) for i in path)
        if key not in seen:
            seen.add(key)
            uniq.append((score, path))
    if len(uniq) <= 1:
        return uniq
    rest = sorted(uniq[1:], key=lambda sp: any(g.edges[i].q0 for i in sp[1]))  # stable
    return [uniq[0], *rest][:top_k]


@lru_cache(maxsize=1)
def _model() -> dict[str, Any]:
    try:
        m = json.loads(MODEL_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    m["table_id"] = register_table(m.get("tag_bigram", {}))
    return m


def enabled() -> bool:
    m = _model()
    return bool(m.get("enabled") and m.get("weights"))


def decode(line: str, top_k: int = 12, model: Optional[Mapping[str, Any]] = None) -> list[Split]:
    """Best ``top_k`` valid splits under the learned model; the segmenter's order when disabled."""
    m = model if model is not None else _model()
    if not (m.get("enabled") and m.get("weights")):
        return list(sg.segment_line(line, top_k).splits)
    lat = lattice(line)
    if lat is None:
        return list(sg.segment_line(line, top_k).splits)
    table = m.get("tag_bigram", {})
    tid = m.get("table_id") or register_table(table)
    g, raw = build_graph(lat, table)
    extra = dynamic_features(g, m)
    paths = viterbi(g, m["weights"], tid, top_k * 3, extra=extra)
    return [lat._split([raw[i] for i in path], score) for score, path in order_alternatives(g, paths, top_k)]
