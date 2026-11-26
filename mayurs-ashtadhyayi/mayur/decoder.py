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
import warnings
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from mayur import decoder_words as dw
from mayur import sandhi as sd
from mayur import segmenter as sg
from mayur.lipi import from_varnas
from mayur.segmenter import Split

MODEL_FILE = Path(__file__).with_name("models") / "lattice_decoder.json"
FALLBACK_FILE = Path(__file__).with_name("models") / "lattice_decoder_base.json"  # trained without neural
BEAM = 12
SAME_PREV = 4  # hypotheses kept per distinct previous word at one state
KINDS = ("none", "pada", "cpd")
_START_TAG, _END_TAG = dw.START_TAG, dw.END_TAG
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
    unknown: bool = False  # no dictionary analysis: offered via lexicon.generated (see UnknownLattice)
    slen: int = 0  # number of surface sounds of the right junction
    rhead: bool = False  # the junction surface contains the right word's first sound (vowel fusion)
    elide: bool = False  # अ elided after ए/ओ (6.1.109)


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


def edge_features(lat: Any, state: tuple, e: tuple, table: Mapping[str, float],
                  prefix: Optional[dict] = None) -> dict[str, float]:
    """Generic static features of one lattice edge (word + its right junction)."""
    form, k, jn, base, plain, nxt = e
    i, _, after_samasa = state
    f: dict[str, float] = {"base": float(base), "bias": 1.0}
    f.update(dw.word_features(form, jn.samasa))
    f.update(dw.prefix_features(form, jn.samasa, prefix or {}))
    f.update(_endings(form, jn.samasa))
    kind = _junction_kind(lat, e)
    f[f"j_{kind}"] = 1.0
    f[f"j_{kind}_{'sandhi' if jn.sutras else 'plain'}"] = 1.0
    left_inner = i > 0 and i not in lat.sp and not after_samasa
    if (kind == "inner" or left_inner) and dw.syllables(form) <= 2:
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
    if sg.word_score(form, jn.samasa, lat.tier) is None and base == UNK_BASE:
        n = len(sd.varnas(form))
        f["unknown"] = 1.0
        f[f"unknown_len{min(n // 3, 5)}"] = 1.0
    if nxt == sg._END:
        f["tag_end"] = table.get(f"{dw.word_tag(form, jn.samasa)}|{_END_TAG}", table.get("<unk>", -8.0))
    return f


def _bigram(a: str, b: str) -> float:
    return math.log1p(dw.bigram_count(a, b))


@lru_cache(maxsize=500_000)
def pair_features(prev: Optional[tuple[str, bool, str]], cur: tuple[str, bool, str], table_id: int = 0) -> Feats:
    """Features of (previous word, word); words are (form, in_compound, tag). ``prev`` None = line start."""
    tabs = _TABLES.get(table_id, {})
    table, prefix = tabs.get("tag", {}), tabs.get("prefix", {})
    unk = table.get("<unk>", -8.0)
    pf, ps, pt = prev if prev is not None else ("", False, _START_TAG)
    cf, cs, ct = cur
    out: dict[str, float] = {"tag_bigram": table.get(f"{pt}|{ct}", unk)}
    if prev is None:
        return tuple(out.items())
    if not ps:
        out["pair_logbigram"] = _bigram(pf, cf)
        out.update(dw.prefix_pair_features(pf, cf, prefix))
    elif not cs:
        out.update(dw.compound_pair_features(pf, cf))
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


_TABLES: dict[int, dict[str, Any]] = {}


def register_table(table: Mapping[str, float], prefix: Optional[Mapping[str, Any]] = None) -> int:
    """Make a tag-bigram table (and prefix table) available to ``pair_features`` under a stable id."""
    tid = len(_TABLES) + 1
    _TABLES[tid] = {"tag": dict(table), "prefix": dict(prefix or {})}
    return tid


from mayur.decoder_stats import (  # noqa: E402,F401 - re-exported
    BOUNDARY_K, BOUNDARY_MIN, boundary_keys, boundary_logprobs, dynamic_features, neural_available, neural_features)


# ---------------------------------------------------------------- lattice -> graph

from mayur.decoder_lattice import UNK_BASE, UnknownLattice, _reachable, lattice  # noqa: E402,F401


def _jkey(lat: Any, e: tuple) -> tuple[str, str]:
    _, k, jn, _, _, nxt = e
    j = nxt[0] if nxt != sg._END else -1
    follow = lat.t[j] if 0 <= j < lat.n else "#"
    surf = f"{from_varnas(jn.surface)}+{follow}"
    cls = f"{from_varnas(jn.left_tail)}>{from_varnas(jn.right_head)}:{int(jn.samasa)}:{','.join(jn.sutras)}"
    return surf, cls


def build_graph(lat: Any, table: Mapping[str, float], prefix: Optional[dict] = None) -> tuple[Graph, list[tuple]]:
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
            feats = edge_features(lat, st, e, table, prefix)
            surf, cls = _jkey(lat, e)
            out[index[st]].append(len(edges))
            edges.append(Edge(index[st], index[e[5]], e[0], e[2].samasa, dw.word_tag(e[0], e[2].samasa),
                              tuple(sorted(feats.items())), st[0], e[1], _junction_kind(lat, e), surf, cls,
                              "w_q0" in feats, bool(feats.get("unknown")), len(e[2].surface),
                              bool(e[2].right_head), "६.१.१०९" in e[2].sutras and e[2].right_head == ("अ",)))
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


def _read(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


@lru_cache(maxsize=1)
def _model() -> dict[str, Any]:
    """The trained model; one trained WITH neural boundary features is refused (with one warning)
    when those are unavailable, and the model trained without them is used instead."""
    m = _read(MODEL_FILE)
    if m.get("neural") and not neural_available():
        warnings.warn("decoder: neural boundary model unavailable (torch or mayur/models/boundary.pt missing); "
                      f"using {FALLBACK_FILE.name}", RuntimeWarning, stacklevel=2)
        m = _read(FALLBACK_FILE)
        if m.get("neural"):
            m = {}
    if not m:
        return {}
    m["table_id"] = register_table(m.get("tag_bigram", {}), m.get("prefix", {}))
    return m


def score_scale() -> float:
    """Typical gap between the decoder's best and second-best scores on DEV (4 x the median), the
    temperature for turning decoder scores into probabilities; 1.0 when there is no model."""
    return float(_model().get("score_scale", 1.0))


def enabled() -> bool:
    m = _model()
    return bool(m.get("enabled") and m.get("weights"))


def decode(line: str, top_k: int = 12, model: Optional[Mapping[str, Any]] = None) -> list[Split]:
    """Best ``top_k`` valid splits under the learned model; the segmenter's order when disabled."""
    m = model if model is not None else _model()
    if not (m.get("enabled") and m.get("weights")):
        return list(sg.segment_line(line, top_k).splits)
    lat = lattice(line, bool(m.get("unknown_edges")))
    if lat is None:
        return list(sg.segment_line(line, top_k).splits)
    table = m.get("tag_bigram", {})
    tid = m.get("table_id") or register_table(table, m.get("prefix", {}))
    g, raw = build_graph(lat, table, m.get("prefix", {}))
    extra = dynamic_features(g, m)
    paths = viterbi(g, m["weights"], tid, top_k * 3, extra=extra)
    out = [lat._split([raw[i] for i in path], score) for score, path in order_alternatives(g, paths, top_k)]
    from mayur import unknown_guard  # a decode-time guard, not a feature (see that module)

    return unknown_guard.guard(line, out, top_k, m)


def decode_graph(line: str, m: Mapping[str, Any], unknown: bool, top_k: int) -> list[Split]:
    """Decode ``line`` with model ``m`` on the plain or the unknown-word lattice (no guard)."""
    lat = lattice(line, unknown)
    if lat is None:
        return []
    table = m.get("tag_bigram", {})
    tid = m.get("table_id") or register_table(table, m.get("prefix", {}))
    g, raw = build_graph(lat, table, m.get("prefix", {}))
    paths = viterbi(g, m["weights"], tid, top_k * 3, extra=dynamic_features(g, m))
    return [lat._split([raw[i] for i in path], score) for score, path in order_alternatives(g, paths, top_k)]
