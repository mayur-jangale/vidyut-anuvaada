"""Learned first-order decoding INSIDE the segmenter's lattice (validity stays rule-based).

Score(path) = Σ w·f(edge) + Σ w·g(previous word, word). Viterbi over lattice states with a
beam of hypotheses per state, so no path list is ever materialised. Weights live in
mayur/models/lattice_decoder.json (trained on Digital Corpus of Sanskrit annotations, CC BY 4.0).
The segmenter's lattice is used read-only through ``_Lattice.edges``.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from mayur import freq, ranker
from mayur import segmenter as sg
from mayur.segmenter import Split

MODEL_FILE = Path(__file__).with_name("models") / "lattice_decoder.json"
BEAM = 8
SAME_PREV = 2  # hypotheses kept per distinct previous word at one state
_START_TAG, _END_TAG = ranker._START_TAG, ranker._END_TAG


@dataclass(frozen=True)
class Edge:
    src: int
    dst: int
    form: str
    samasa: bool
    tag: str
    feats: tuple[tuple[str, float], ...]


@dataclass(frozen=True)
class Graph:
    """Compact lattice: node 0 is the start, ``end`` the final node, ``out[n]`` edge ids, topological."""
    edges: tuple[Edge, ...]
    out: tuple[tuple[int, ...], ...]
    order: tuple[int, ...]
    end: int


def _junction_kind(lat: Any, state: tuple, e: tuple) -> str:
    form, k, jn, _, _, nxt = e
    if nxt == sg._END:
        return "end"
    if jn.samasa:
        return "cpd"
    return "space" if any(k <= s <= nxt[0] for s in lat.sp) else "inner"


def edge_features(lat: Any, state: tuple, e: tuple, table: Mapping[str, float]) -> dict[str, float]:
    """Generic features of one lattice edge (word + its right junction)."""
    form, k, jn, base, plain, nxt = e
    i, _, after_samasa = state
    f: dict[str, float] = {"base": float(base), "bias": 1.0}
    f.update(ranker._word_feats(form, jn.samasa))
    kind = _junction_kind(lat, state, e)
    sandhi = "sandhi" if jn.sutras else "plain"
    f[f"j_{kind}"] = 1.0
    f[f"j_{kind}_{sandhi}"] = 1.0
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
def pair_features(prev: Optional[tuple[str, bool, str]], cur: tuple[str, bool, str],
                  table_id: int = 0) -> tuple[tuple[str, float], ...]:
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


def build_graph(lat: Any, table: Mapping[str, float]) -> tuple[Graph, list[tuple]]:
    """Compact graph of ``lat`` plus, per edge, the raw (state, edge) for ``Split`` construction."""
    states, ok = _reachable(lat)
    index = {s: n for n, s in enumerate(states)}
    edges, raw, out = [], [], [[] for _ in states]
    for st in states:
        if st == sg._END:
            continue
        for e in lat.edges(st):
            if e[5] not in index:
                continue
            feats = edge_features(lat, st, e, table)
            out[index[st]].append(len(edges))
            edges.append(Edge(index[st], index[e[5]], e[0], e[2].samasa, ranker.word_tag(e[0], e[2].samasa),
                              tuple(sorted(feats.items()))))
            raw.append((st, e))
    return Graph(tuple(edges), tuple(map(tuple, out)), tuple(range(len(states))), index.get(sg._END, -1)), raw


def _dot(w: Mapping[str, float], feats: Sequence[tuple[str, float]]) -> float:
    return sum(w.get(k, 0.0) * v for k, v in feats)


def viterbi(g: Graph, w: Mapping[str, float], table_id: int, top_k: int = 1,
            beam: int = BEAM) -> list[tuple[float, tuple[int, ...]]]:
    """Up to ``top_k`` best (score, edge ids) paths; beam of hypotheses per node."""
    if g.end < 0:
        return []
    edge_score = [_dot(w, e.feats) for e in g.edges]
    hyps: dict[int, list] = {0: [(0.0, -1, None)]}  # (score, edge id, parent hyp)
    width = max(beam, top_k)
    for n in g.order:
        cur = hyps.pop(n, None)
        if not cur:
            continue
        cur = _prune(cur, g, top_k if n == g.end else width)
        if n == g.end:
            hyps[n] = cur
            break
        for h in cur:
            prev = None if h[1] < 0 else _word(g.edges[h[1]])
            for eid in g.out[n]:
                e = g.edges[eid]
                s = h[0] + edge_score[eid] + _dot(w, pair_features(prev, _word(e), table_id))
                hyps.setdefault(e.dst, []).append((s, eid, h))
    out = []
    for h in sorted(hyps.get(g.end, []), key=lambda t: -t[0])[:top_k]:
        path, node = [], h
        while node is not None and node[1] >= 0:
            path.append(node[1])
            node = node[2]
        out.append((h[0], tuple(reversed(path))))
    return out


def _word(e: Edge) -> tuple[str, bool, str]:
    return e.form, e.samasa, e.tag


def _prune(cands: list, g: Graph, width: int) -> list:
    cands.sort(key=lambda t: -t[0])
    kept, per_prev = [], {}
    for h in cands:
        key = g.edges[h[1]].form if h[1] >= 0 else ""
        if per_prev.get(key, 0) >= SAME_PREV:
            continue
        per_prev[key] = per_prev.get(key, 0) + 1
        kept.append(h)
        if len(kept) >= width:
            break
    return kept


def path_features(g: Graph, path: Sequence[int], table_id: int) -> dict[str, float]:
    acc: dict[str, float] = {}
    prev = None
    for eid in path:
        e = g.edges[eid]
        for k, v in (*e.feats, *pair_features(prev, _word(e), table_id)):
            acc[k] = acc.get(k, 0.0) + v
        prev = _word(e)
    return acc


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
    out, seen = [], set()
    for score, path in viterbi(g, m["weights"], tid, top_k * 3):
        key = tuple((g.edges[i].form, g.edges[i].samasa) for i in path)
        if key not in seen:  # one word sequence can arise from several junction analyses
            seen.add(key)
            out.append(lat._split([raw[i] for i in path], score))
        if len(out) >= top_k:
            break
    return out
