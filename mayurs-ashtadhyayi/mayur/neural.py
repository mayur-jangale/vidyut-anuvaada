"""Neural context model: grammatical features of every word of a verse, from the whole verse.

Trained by ``scripts/train_neural.py`` on gold word forms of DCS verses (CC BY 4.0). Each word is
encoded from its sounds (``mayur.lipi.varnas``: embedding -> 1-D CNN -> max-pool) and a hashed
form embedding, with its half-verse index and compound flag; a 2-layer BiLSTM runs over the verse
and factorised softmax heads predict Case, Number, Gender, Person, Tense, Mood, VerbForm and a
coarse word class. ``"none"`` is the value of a feature the word does not have.

The model only rescores rule-valid candidates (``candidate_scores``); torch is optional and
imported lazily: without torch or the model file ``enabled()`` is False.
"""

from __future__ import annotations

import json
import zlib
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional, Sequence

from mayur.lipi import varnas

MODEL_DIR = Path(__file__).resolve().parent / "models"
WEIGHTS_FILE = MODEL_DIR / "neural_tagger.pt"
CONFIG_FILE = MODEL_DIR / "neural_tagger.json"
HEADS = ("Case", "Number", "Gender", "Person", "Tense", "Mood", "VerbForm", "Class")
NONE = "none"
PAD, UNK = "<pad>", "<unk>"
MAX_SOUNDS = 24
INDECLINABLE_UPOS = frozenset({"ADV", "PART", "CCONJ", "SCONJ", "INTJ", "ADP"})
DEFAULT_CONFIG: dict[str, Any] = {"sound_dim": 48, "conv_dim": 128, "buckets": 50_000, "form_dim": 64,
                                  "hidden": 192, "dropout": 0.3}


def word_class(feats: dict[str, str]) -> str:
    """Coarse class from corpus-style features (also of a candidate, via ``ud.feats``)."""
    if feats.get("Case") == "Cpd":
        return "cpd"
    if "Mood" in feats:
        return "finite"
    vf = feats.get("VerbForm")
    if vf in ("Part", "Gdv"):
        return "participle"
    if vf in ("Conv", "Inf"):
        return vf.lower()
    return "nominal" if "Case" in feats else "indecl"


def targets(upos: str, feats: dict[str, str], compound_member: bool) -> dict[str, str]:
    """Head -> gold value of one corpus word (``"none"`` for absent features)."""
    if compound_member:
        f = {"Case": "Cpd"}
    elif upos in INDECLINABLE_UPOS:
        f = {}
    else:
        f = {k: v for k, v in feats.items() if k in HEADS}
    out = {h: f.get(h, NONE) for h in HEADS[:-1]}
    out["Class"] = word_class(f)
    return out


@lru_cache(maxsize=300_000)
def sounds(form: str) -> tuple[str, ...]:
    try:
        return tuple(varnas(form))
    except Exception:
        return tuple(form)


def bucket(form: str, n: int) -> int:
    return 1 + zlib.crc32(form.encode("utf-8")) % (n - 1)


def encode(forms: Sequence[str], sound_ix: dict[str, int], n_buckets: int) -> tuple[list[list[int]], list[int]]:
    """Sound indices (truncated to the last ``MAX_SOUNDS``) and form buckets of a verse."""
    unk = sound_ix.get(UNK, 1)
    snd = [[sound_ix.get(s, unk) for s in sounds(f)][-MAX_SOUNDS:] or [unk] for f in forms]
    return snd, [bucket(f, n_buckets) for f in forms]


def build_model(cfg: dict[str, Any], n_sounds: int, head_sizes: dict[str, int]):
    """The torch module (torch imported here)."""
    import torch
    from torch import nn

    class Tagger(nn.Module):
        def __init__(self) -> None:
            super().__init__()
            self.snd = nn.Embedding(n_sounds, cfg["sound_dim"], padding_idx=0)
            self.conv = nn.Conv1d(cfg["sound_dim"], cfg["conv_dim"], 3, padding=1)
            self.form = nn.Embedding(cfg["buckets"], cfg["form_dim"], padding_idx=0)
            self.line = nn.Embedding(4, 8)
            self.cpd = nn.Embedding(2, 8)
            d_in = cfg["conv_dim"] + cfg["form_dim"] + 16
            self.drop = nn.Dropout(cfg["dropout"])
            self.lstm = nn.LSTM(d_in, cfg["hidden"], num_layers=2, bidirectional=True, batch_first=True,
                                dropout=cfg["dropout"])
            self.heads = nn.ModuleDict({h: nn.Linear(2 * cfg["hidden"], k) for h, k in head_sizes.items()})

        def forward(self, snd, form, line, cpd, lengths):
            b, t, s = snd.shape
            x = self.snd(snd.view(b * t, s)).transpose(1, 2)
            x = torch.relu(self.conv(x))
            x = x.masked_fill((snd.view(b * t, 1, s) == 0), -1e4).max(dim=2).values.clamp(min=0.0).view(b, t, -1)
            x = torch.cat([x, self.form(form), self.line(line), self.cpd(cpd)], dim=-1)
            packed = nn.utils.rnn.pack_padded_sequence(self.drop(x), lengths, batch_first=True, enforce_sorted=False)
            h, _ = self.lstm(packed)
            h, _ = nn.utils.rnn.pad_packed_sequence(h, batch_first=True, total_length=t)
            h = self.drop(h)
            return {k: head(h) for k, head in self.heads.items()}

    return Tagger()


def batch_tensors(verses: Sequence[tuple[Sequence[str], Sequence[int], Sequence[bool]]],
                  sound_ix: dict[str, int], n_buckets: int):
    """Padded tensors (sounds, forms, lines, compound flags, lengths) of several verses."""
    import torch

    enc = [encode(f, sound_ix, n_buckets) for f, _, _ in verses]
    t = max(len(f) for f, _, _ in verses)
    s = max(len(x) for snd, _ in enc for x in snd)
    pad_word = [0] * s
    snd = torch.tensor([[x + [0] * (s - len(x)) for x in sx] + [pad_word] * (t - len(sx)) for sx, _ in enc])
    form = torch.tensor([fx + [0] * (t - len(fx)) for _, fx in enc])
    line = torch.tensor([[min(int(v), 3) for v in ln] + [0] * (t - len(ln)) for _, ln, _ in verses])
    cpd = torch.tensor([[int(bool(v)) for v in cf] + [0] * (t - len(cf)) for _, _, cf in verses])
    return snd, form, line, cpd, torch.tensor([len(f) for f, _, _ in verses])


@lru_cache(maxsize=1)
def _load(weights: str = str(WEIGHTS_FILE), config: str = str(CONFIG_FILE)) -> Optional[tuple]:
    try:
        import torch
    except ImportError:
        return None
    wp, cp = Path(weights), Path(config)
    if not (wp.exists() and cp.exists()):
        return None
    meta = json.loads(cp.read_text(encoding="utf-8"))
    if not meta.get("enabled", True):
        return None
    torch.set_num_threads(min(3, torch.get_num_threads()))
    model = build_model(meta["config"], len(meta["sounds"]), {h: len(v) for h, v in meta["values"].items()})
    model.load_state_dict(torch.load(wp, map_location="cpu", weights_only=True))
    model.eval()
    return model, meta


def enabled() -> bool:
    """The neural model and torch are available and the saved model is marked enabled."""
    return _load() is not None


def weight() -> float:
    """λ: weight of the neural score next to the perceptron score (tuned on DEV)."""
    loaded = _load()
    return float(loaded[1].get("lambda", 0.0)) if loaded else 0.0


def logprobs_with(model, meta: dict, verses: Sequence[tuple[Sequence[str], Sequence[int], Sequence[bool]]]
                  ) -> list[list[dict[str, dict[str, float]]]]:
    """Per verse, per word: head -> value -> log-probability."""
    import torch

    if not verses:
        return []
    sound_ix = {s: i for i, s in enumerate(meta["sounds"])}
    with torch.no_grad():
        out = model(*batch_tensors(verses, sound_ix, meta["config"]["buckets"]))
        lp = {h: torch.log_softmax(x, dim=-1).tolist() for h, x in out.items()}
    return [[{h: dict(zip(meta["values"][h], lp[h][b][i])) for h in meta["values"]} for i in range(len(v[0]))]
            for b, v in enumerate(verses)]


def feature_logprobs(forms: Sequence[str], lines: Sequence[int],
                     compound_flags: Sequence[bool]) -> list[dict[str, dict[str, float]]]:
    """Per word: feature -> value -> log-probability ([] without a model or for an empty verse)."""
    loaded = _load()
    if loaded is None or not forms:
        return []
    return logprobs_with(*loaded, [(list(forms), list(lines), list(compound_flags))])[0]


def candidate_score(feats: dict[str, str], lp: dict[str, dict[str, float]]) -> float:
    """Σ log P(value) over the heads, ``feats`` as given by ``ud.feats`` (absent -> "none")."""
    want = {h: feats.get(h, NONE) for h in HEADS[:-1]}
    want["Class"] = word_class(feats)
    floor = -20.0
    return sum(lp[h].get(v, floor) for h, v in want.items() if h in lp)


def candidate_scores(cands: Sequence[Sequence[Any]], lps: Sequence[dict[str, dict[str, float]]]
                     ) -> list[list[float]]:
    """Neural score of every candidate Morph (via ``ud.feats``); zeros when ``lps`` is empty."""
    from mayur import ud

    if not lps:
        return [[0.0] * len(c) for c in cands]
    return [[candidate_score(ud.feats(m), lp) for m in c] for c, lp in zip(cands, lps)]
