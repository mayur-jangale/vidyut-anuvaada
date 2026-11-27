"""Batched beam search with a key/value cache for ``translator_model.Seq2Seq``."""

from __future__ import annotations

import torch

from mayur.translator_model import Seq2Seq

BOS, EOS = 1, 2
NEG = -1e9


def length_penalty(length: torch.Tensor, alpha: float) -> torch.Tensor:
    return ((5.0 + length) / 6.0) ** alpha


def _expand(memory: list, mask: torch.Tensor, beam: int) -> tuple[list, torch.Tensor]:
    memory = [(k.repeat_interleave(beam, 0), v.repeat_interleave(beam, 0)) for k, v in memory]
    return memory, mask.repeat_interleave(beam, 0)


def _reorder(caches: list[dict], index: torch.Tensor) -> None:
    for cache in caches:
        for key in ("k", "v"):
            cache[key] = cache[key].index_select(0, index)


def _step_scores(logprobs: torch.Tensor, scores: torch.Tensor, lengths: torch.Tensor, done: torch.Tensor,
                 alpha: float) -> tuple[torch.Tensor, torch.Tensor]:
    """Raw and length-normalised scores of every (beam, token) continuation; a finished beam only repeats."""
    b, k = scores.shape
    lp = logprobs.view(b, k, -1).clone()
    lp[done] = NEG
    lp[..., 0][done] = 0.0  # a finished beam continues with pad, at no cost
    raw = scores.unsqueeze(-1) + lp
    grown = (lengths + (~done).long()).unsqueeze(-1).float()
    return raw, raw / length_penalty(grown, alpha)


@torch.no_grad()
def beam_search(model: Seq2Seq, src: torch.Tensor, beam: int = 4, max_len: int = 160,
                alpha: float = 0.8) -> list[list[int]]:
    """Best hypothesis (ids without BOS/EOS) for each row of ``src``."""
    model.eval()
    b = src.shape[0]
    memory, mask = _expand(*model.encode(src), beam)
    caches: list[dict] = [{} for _ in model.dec]
    last = torch.full((b * beam, 1), BOS, dtype=torch.long)
    scores = torch.zeros(b, beam)
    scores[:, 1:] = NEG
    lengths = torch.zeros(b, beam, dtype=torch.long)
    done = torch.zeros(b, beam, dtype=torch.bool)
    history = torch.zeros(b, beam, 0, dtype=torch.long)
    vocab = model.config.vocab
    for step in range(max_len):
        logprobs = torch.log_softmax(model.decode(last, memory, mask, caches, step)[:, -1].float(), -1)
        raw, norm = _step_scores(logprobs, scores, lengths, done, alpha)
        top = norm.view(b, -1).topk(beam, -1).indices
        which, token = top // vocab, top % vocab
        scores = raw.view(b, -1).gather(1, top)
        flat = (which + torch.arange(b).unsqueeze(1) * beam).view(-1)
        _reorder(caches, flat)
        lengths = lengths.gather(1, which) + (~done.gather(1, which)).long()
        done = done.gather(1, which) | (token == EOS)
        history = torch.cat([history.gather(1, which.unsqueeze(-1).expand(-1, -1, history.shape[2])),
                             token.unsqueeze(-1)], 2)
        last = token.view(-1, 1)
        if bool(done.all()):
            break
    final = (scores / length_penalty(lengths.float(), alpha)).argmax(1)
    return [_clean(history[i, final[i]].tolist()) for i in range(b)]


def _clean(ids: list[int]) -> list[int]:
    out = []
    for i in ids:
        if i in (EOS, 0):
            break
        out.append(i)
    return out
