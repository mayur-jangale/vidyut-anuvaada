"""Sound-level boundary statistics, junction-rule statistics and neural-boundary features for
mayur/decoder.py (per-edge features computed from tables stored in the model file)."""

from __future__ import annotations

import math
from functools import lru_cache
from typing import Any, Mapping, Sequence

BOUNDARY_K = 3
BOUNDARY_MIN = 3
Feats = tuple[tuple[str, float], ...]



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


def neural_available() -> bool:
    try:
        from mayur import neural_boundary
    except ImportError:
        return False
    try:
        return bool(neural_boundary.enabled())
    except Exception:  # noqa: BLE001
        return False


@lru_cache(maxsize=20_000)
def _neural(text: tuple, spaces: frozenset) -> tuple:
    from mayur import neural_boundary

    return tuple(neural_boundary.logprobs(text, spaces))




def neural_features(g: Any, e: Any, lps: Sequence[Mapping[str, float]]) -> list[tuple[str, float]]:
    """Σ log P(N) strictly inside the word + log P(label implied by the right junction)."""
    n = len(lps)
    inside = sum(lps[i].get("N", -10.0) for i in range(e.start, min(e.end - 1, n)))
    out = [("nb_inside", inside)]
    if e.kind == "end":
        return out
    lab = "C" if e.kind == "cpd" else "P"
    if e.slen == 0:
        idx, label = e.end - 1, lab
    elif e.rhead and not e.elide:
        idx, label = e.end + e.slen - 1, "F" + lab
    else:
        idx, label = e.end + e.slen - 1, lab
    junc = lps[idx].get(label, -10.0) if 0 <= idx < n else -10.0
    out += [("nb_junc", junc), (f"nb_junc_b{min(int(-junc), 6)}", 1.0), ("nb_sum", inside + junc)]
    if e.unknown:
        out.append(("unk_nb_inside", inside))
    return out


def dynamic_features(g: Any, tables: Mapping[str, Any]) -> list[Feats]:
    """Per edge: boundary-model, junction-statistics and neural-boundary features (tables from the model)."""
    btab, jtab, neural = tables.get("boundary", {}), tables.get("junction", {}), tables.get("neural", False)
    if not btab and not jtab and not neural:
        return [()] * len(g.edges)
    lps = boundary_logprobs(g.text, g.spaces, btab) if btab else []
    nlps = _neural(g.text, g.spaces) if neural and neural_available() else ()
    out = []
    for e in g.edges:
        f: list[tuple[str, float]] = []
        if nlps:
            f.extend(neural_features(g, e, nlps))
        if lps:
            inside = sum(lps[p][0] for p in range(e.start + 1, min(e.end, len(lps))))
            f.append(("bnd_inside", inside))
            if e.unknown:
                f.append(("unk_bnd_inside", inside))
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


