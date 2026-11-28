"""Neural sound-level word-boundary model: for every sound of the compact line, what follows it.

Coordinates are those of ``segmenter._prepare(line)``: ``text`` is the space-free canon varna
tuple, ``spaces`` the indices i such that a space precedes ``text[i]``. One label per sound i:

* ``N``  – sound i and sound i+1 belong to the same word;
* ``P``  – a pada boundary follows sound i, and sound i belongs to the left word only (it may be
  sandhi-altered: ओ from अस्, ः from स्, य् from इ before a vowel, a doubled न्/ङ्);
* ``C``  – the same, compound-internal (the left word is a compound member);
* ``FP`` – sound i is a FUSED vowel: one surface vowel standing for the last sound of the left
  word AND the first sound of the right word (अ+इ→ए, अ+अ→आ, अ+ए→ऐ, इ+इ→ई …). The boundary lies
  inside sound i; in the lattice the left word ends at i and the right word starts at i;
* ``FC`` – the same, compound-internal.

Elision (ए/ओ + अ → ए/ओ, with or without ऽ) is NOT fusion: the ए/ओ gets ``P`` and a written ऽ
starts the right word (as in the lattice: रामोऽपि → रामस् [0,4) अपि [4,7)). Sounds inserted at
a junction (गच्छन्नत्र: the second न्) belong to the left word. The last sound gets ``P``.

torch is optional: it is imported lazily and ``enabled()`` is False without it or the model.
"""

from __future__ import annotations

import difflib
import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional, Sequence

from mayur import sandhi as sd

LABELS = ("N", "P", "C", "FP", "FC")
MODEL_FILE = Path(__file__).with_name("models") / "boundary.pt"
META_FILE = Path(__file__).with_name("models") / "boundary.json"
UNK, PAD = "<unk>", "<pad>"
_ELIDING = ("ए", "ओ")
_MAX_COST = 0.15  # alignment cost per sound above which a gold line is dropped

Varnas = tuple[str, ...]


# ---------------------------------------------------------------- label extraction (alignment)

def _sub_cost(g: str, t: str) -> float:
    if g == t:
        return 0.0
    gv, tv = sd.is_vowel(g), sd.is_vowel(t)
    if gv and (tv or t == sd.AVAGRAHA):
        return 0.4
    if not gv and not tv and t != sd.AVAGRAHA:
        return 0.5
    if g in ("इ", "ई", "उ", "ऊ", "ऋ") and t in ("य्", "व्", "र्"):
        return 0.4
    return 1.2


def _region(gold: Varnas, text: Varnas) -> tuple[list[Optional[int]], float]:
    """Edit alignment of a small region: per gold sound the aligned text offset (None: deleted)."""
    n, m = len(gold), len(text)
    inf = float("inf")
    d = [[inf] * (m + 1) for _ in range(n + 1)]
    back: list[list[Any]] = [[None] * (m + 1) for _ in range(n + 1)]
    d[0][0] = 0.0
    for i in range(n + 1):
        for j in range(m + 1):
            if i == j == 0:
                continue
            best, how = inf, None
            if i and j and d[i - 1][j - 1] + _sub_cost(gold[i - 1], text[j - 1]) < best:
                best, how = d[i - 1][j - 1] + _sub_cost(gold[i - 1], text[j - 1]), "s"
            if i and d[i - 1][j] + 0.6 < best:
                best, how = d[i - 1][j] + 0.6, "d"
            if j and d[i][j - 1] + 0.7 < best:
                best, how = d[i][j - 1] + 0.7, "i"
            d[i][j], back[i][j] = best, how
    out: list[Optional[int]] = [None] * n
    i, j = n, m
    while i or j:
        how = back[i][j]
        if how == "s":
            out[i - 1] = j - 1
            i, j = i - 1, j - 1
        elif how == "d":
            i -= 1
        else:
            j -= 1
    return out, d[n][m]


def align(gold: Varnas, text: Varnas) -> tuple[list[Optional[int]], float]:
    """Per gold sound its text index (None when it has no own surface sound), and the cost."""
    sm = difflib.SequenceMatcher(None, gold, text, autojunk=False)
    out: list[Optional[int]] = [None] * len(gold)
    cost = 0.0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                out[i1 + k] = j1 + k
            continue
        sub, c = _region(gold[i1:i2], text[j1:j2])
        cost += c
        for k, o in enumerate(sub):
            out[i1 + k] = None if o is None else j1 + o
    return out, cost


def _form_varnas(form: str) -> Varnas:
    return tuple(v for v in sd.canon_varnas(form) if v != " ")


def extract_labels(text: Varnas, words: Sequence[tuple[str, bool]]) -> Optional[list[str]]:
    """Labels for ``text`` from the gold words ``(form, compound_member)``; None if they do not align."""
    gold: list[str] = []
    bounds: list[tuple[int, bool]] = []  # (index of the first gold sound of the right word, compound)
    words = [(f, c) for f, c in words if _form_varnas(f)]
    for n, (form, cpd) in enumerate(words):
        if n:
            bounds.append((len(gold), bool(words[n - 1][1])))
        gold.extend(_form_varnas(form))
    if not gold or not text:
        return None
    amap, cost = align(tuple(gold), text)
    if cost > _MAX_COST * len(text) + 0.6:
        return None
    labels = ["N"] * len(text)
    for g, cpd in bounds:
        left, right = gold[g - 1], gold[g]
        a, b = amap[g - 1], amap[g]
        if sd.is_vowel(left) and sd.is_vowel(right) and (a is None) != (b is None):
            t = a if a is not None else b
            if sd.is_vowel(text[t]) and not (left in _ELIDING and right == "अ"):
                labels[t] = "FC" if cpd else "FP"
                continue
        nxt = next((amap[k] for k in range(g, len(gold)) if amap[k] is not None), len(text))
        pos = nxt - 1
        if pos < 0 or labels[pos] != "N":
            return None
        labels[pos] = "C" if cpd else "P"
    labels[-1] = "P"
    return labels


def boundaries(labels: Sequence[str]) -> list[tuple[int, int]]:
    """Word spans ``(start, end)`` of a greedy segmentation by labels (F: shared sound)."""
    spans, start = [], 0
    for i, lab in enumerate(labels):
        if lab in ("P", "C"):
            spans.append((start, i + 1))
            start = i + 1
        elif lab in ("FP", "FC"):
            spans.append((start, i + 1))
            start = i
    if start < len(labels):
        spans.append((start, len(labels)))
    return spans


# ---------------------------------------------------------------- model

def build_model(n_vocab: int, emb: int = 64, hidden: int = 192, layers: int = 2, dropout: float = 0.25) -> Any:
    import torch
    from torch import nn

    class BoundaryNet(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.emb = nn.Embedding(n_vocab, emb, padding_idx=0)
            self.conv = nn.Conv1d(emb + 1, emb, 5, padding=2)
            self.lstm = nn.LSTM(2 * emb + 1, hidden, num_layers=layers, bidirectional=True, batch_first=True,
                                dropout=dropout if layers > 1 else 0.0)
            self.drop = nn.Dropout(dropout)
            self.out = nn.Linear(2 * hidden, len(LABELS))

        def forward(self, ids: "torch.Tensor", space: "torch.Tensor") -> "torch.Tensor":
            x = torch.cat([self.drop(self.emb(ids)), space.unsqueeze(-1)], -1)
            c = torch.relu(self.conv(x.transpose(1, 2))).transpose(1, 2)
            h, _ = self.lstm(torch.cat([x, c], -1))
            return self.out(self.drop(h))

    return BoundaryNet()


def encode(text: Varnas, spaces: frozenset, vocab: dict[str, int]) -> tuple[list[int], list[float]]:
    unk = vocab.get(UNK, 1)
    return [vocab.get(v, unk) for v in text], [1.0 if i in spaces else 0.0 for i in range(len(text))]


@lru_cache(maxsize=1)
def _load() -> Optional[tuple[Any, dict[str, int]]]:
    try:
        import torch
    except ImportError:
        return None
    if not (MODEL_FILE.exists() and META_FILE.exists()):
        return None
    torch.set_num_threads(1)  # one short line per call: threads only contend (≈200x slower on a busy machine)
    meta = json.loads(META_FILE.read_text(encoding="utf-8"))
    vocab = {v: i for i, v in enumerate(meta["vocab"])}
    net = build_model(len(vocab), **meta["arch"])
    net.load_state_dict(torch.load(MODEL_FILE, map_location="cpu", weights_only=True))
    net.eval()
    return net, vocab


def enabled() -> bool:
    return _load() is not None


@lru_cache(maxsize=4096)
def _cached(text: Varnas, spaces: frozenset) -> tuple[tuple[float, ...], ...]:
    import torch

    loaded = _load()
    if loaded is None or not text:
        return ()
    net, vocab = loaded
    ids, sp = encode(text, spaces, vocab)
    with torch.no_grad():
        lp = torch.log_softmax(net(torch.tensor([ids]), torch.tensor([sp])), -1)[0]
    return tuple(tuple(row) for row in lp.tolist())


def logprobs(text: Sequence[str], spaces: frozenset) -> list[dict[str, float]]:
    """Per sound i of ``text``: log-probabilities of the five LABELS (see module docstring)."""
    rows = _cached(tuple(text), frozenset(spaces))
    return [dict(zip(LABELS, row)) for row in rows]
