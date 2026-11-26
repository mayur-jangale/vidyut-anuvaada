"""Lattice access for mayur/decoder.py: the segmenter's lattice (read-only) and the gated
unknown-word edges of round 3 (off unless a model asks for them). Candidates to move upstream."""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Optional

from mayur import segmenter as sg
from mayur.lipi import from_varnas


UNK_BASE = -30.0
UNK_CAP = 3  # unknown-word edges per lattice state
UNK_MAX = 18  # sounds


@lru_cache(maxsize=200_000)
def _generated_nominal(form: str) -> bool:
    from mayur import lexicon

    try:
        return any(m.kind == "subanta" for m in lexicon.generated(form))
    except Exception:  # noqa: BLE001 - the generator must never break decoding
        return False


class UnknownLattice(sg._Lattice):
    """Tier-0 lattice plus gated edges for words with no dictionary analysis (should move upstream)."""

    def __init__(self, text, spaces, tier: int = 0):
        super().__init__(text, spaces, tier)
        self._base = sg._Lattice(text, spaces, tier)

    def edges(self, state) -> list:
        if state in self._edges:
            return self._edges[state]
        res = list(self._base.edges(state)) + self._unknown_edges(state)
        self._edges[state] = res
        return res

    def _unknown_edges(self, state) -> list:
        i, head, after_samasa = state
        if after_samasa or head or not (i == 0 or i in self.sp):
            return []  # unknown words only start a written chunk
        nxt_space = min((s for s in self.sp if s > i), default=self.n)
        out: list = []
        for k in range(min(nxt_space, self.n, i + UNK_MAX), i, -1):
            core = head + self.t[i:k]
            for jn, j in self.cands[k]:
                word = core + jn.left_tail
                if jn.samasa or len(word) < 4 or word[-len(jn.left_ctx):] != jn.left_ctx:
                    continue
                form = from_varnas(word)
                if (jn.whole and form != jn.whole) or sg.word_score(form, False, self.tier) is not None:
                    continue
                nxt = sg._END if j < 0 else (j, jn.right_head, False)
                at_chunk_end = j < 0 or any(k <= s <= j for s in self.sp)
                if not at_chunk_end and not self._base.edges(nxt):
                    continue
                if _generated_nominal(form):
                    out.append((form, k, jn, UNK_BASE, True, nxt))
                    if len(out) >= UNK_CAP:
                        return out
        return out


def lattice(line: str, unknown: bool = False) -> Optional[Any]:
    """The segmenter's lattice at the first tier that has a valid path (or None).

    With ``unknown`` tier 0 also offers gated edges for words the dictionary does not know.
    """
    text, spaces = sg._prepare(line)
    for tier in (0, 1, 2):
        lat = UnknownLattice(text, spaces, tier) if unknown and tier == 0 else sg._Lattice(text, spaces, tier)
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


