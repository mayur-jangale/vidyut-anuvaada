"""A small sequence-to-sequence transformer in plain PyTorch (pre-norm, tied embeddings).

Needs torch; import this module only after checking ``mayur.translator.available()``.
"""

from __future__ import annotations

import math
from dataclasses import asdict, dataclass
from typing import Optional

import torch
import torch.nn.functional as F
from torch import nn

PAD = 0


@dataclass
class Config:
    vocab: int
    d_model: int = 256
    heads: int = 4
    d_ff: int = 1024
    enc_layers: int = 3
    dec_layers: int = 3
    dropout: float = 0.1
    max_src: int = 320
    max_tgt: int = 192

    def to_json(self) -> dict:
        return asdict(self)


class Attention(nn.Module):
    def __init__(self, d: int, heads: int, dropout: float):
        super().__init__()
        self.heads, self.dropout = heads, dropout
        self.q, self.k, self.v, self.o = (nn.Linear(d, d) for _ in range(4))

    def split(self, x: torch.Tensor) -> torch.Tensor:
        b, n, d = x.shape
        return x.view(b, n, self.heads, d // self.heads).transpose(1, 2)

    def project_kv(self, mem: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]:
        return self.split(self.k(mem)), self.split(self.v(mem))

    def forward(self, x: torch.Tensor, kv: tuple[torch.Tensor, torch.Tensor], mask: Optional[torch.Tensor],
                causal: bool = False) -> torch.Tensor:
        q = self.split(self.q(x))
        drop = self.dropout if self.training else 0.0
        out = F.scaled_dot_product_attention(q, kv[0], kv[1], attn_mask=mask, dropout_p=drop,
                                             is_causal=causal and mask is None)
        b, h, n, dh = out.shape
        return self.o(out.transpose(1, 2).reshape(b, n, h * dh))


class FeedForward(nn.Module):
    def __init__(self, d: int, d_ff: int, dropout: float):
        super().__init__()
        self.a, self.b, self.drop = nn.Linear(d, d_ff), nn.Linear(d_ff, d), nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.b(self.drop(F.gelu(self.a(x))))


class EncoderLayer(nn.Module):
    def __init__(self, c: Config):
        super().__init__()
        self.n1, self.n2 = nn.LayerNorm(c.d_model), nn.LayerNorm(c.d_model)
        self.att = Attention(c.d_model, c.heads, c.dropout)
        self.ff = FeedForward(c.d_model, c.d_ff, c.dropout)
        self.drop = nn.Dropout(c.dropout)

    def forward(self, x: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
        h = self.n1(x)
        x = x + self.drop(self.att(h, self.att.project_kv(h), mask))
        return x + self.drop(self.ff(self.n2(x)))


class DecoderLayer(nn.Module):
    def __init__(self, c: Config):
        super().__init__()
        self.n1, self.n2, self.n3 = (nn.LayerNorm(c.d_model) for _ in range(3))
        self.self_att = Attention(c.d_model, c.heads, c.dropout)
        self.cross = Attention(c.d_model, c.heads, c.dropout)
        self.ff = FeedForward(c.d_model, c.d_ff, c.dropout)
        self.drop = nn.Dropout(c.dropout)

    def forward(self, x: torch.Tensor, memory_kv: tuple[torch.Tensor, torch.Tensor], src_mask: torch.Tensor,
                cache: Optional[dict] = None) -> torch.Tensor:
        h = self.n1(x)
        k, v = self.self_att.project_kv(h)
        if cache is not None:  # incremental decoding: keys and values of the steps so far
            if "k" in cache:
                k, v = torch.cat([cache["k"], k], 2), torch.cat([cache["v"], v], 2)
            cache["k"], cache["v"] = k, v
        x = x + self.drop(self.self_att(h, (k, v), None, causal=cache is None))
        x = x + self.drop(self.cross(self.n2(x), memory_kv, src_mask))
        return x + self.drop(self.ff(self.n3(x)))


def sinusoid(length: int, d: int) -> torch.Tensor:
    pos = torch.arange(length).unsqueeze(1)
    div = torch.exp(torch.arange(0, d, 2) * (-math.log(10000.0) / d))
    table = torch.zeros(length, d)
    table[:, 0::2], table[:, 1::2] = torch.sin(pos * div), torch.cos(pos * div)
    return table


class Seq2Seq(nn.Module):
    def __init__(self, config: Config):
        super().__init__()
        self.config = c = config
        self.embed = nn.Embedding(c.vocab, c.d_model, padding_idx=PAD)
        nn.init.normal_(self.embed.weight, 0.0, c.d_model ** -0.5)
        self.register_buffer("positions", sinusoid(max(c.max_src, c.max_tgt) + 2, c.d_model), persistent=False)
        self.enc = nn.ModuleList(EncoderLayer(c) for _ in range(c.enc_layers))
        self.dec = nn.ModuleList(DecoderLayer(c) for _ in range(c.dec_layers))
        self.enc_norm, self.dec_norm = nn.LayerNorm(c.d_model), nn.LayerNorm(c.d_model)
        self.drop = nn.Dropout(c.dropout)

    def embed_at(self, ids: torch.Tensor, start: int = 0) -> torch.Tensor:
        x = self.embed(ids) * math.sqrt(self.config.d_model)
        return self.drop(x + self.positions[start:start + ids.shape[1]])

    def encode(self, src: torch.Tensor) -> tuple[list[tuple[torch.Tensor, torch.Tensor]], torch.Tensor]:
        """Per decoder layer the cross-attention keys and values of the source, and the source mask."""
        mask = (src != PAD)[:, None, None, :]
        x = self.embed_at(src)
        for layer in self.enc:
            x = layer(x, mask)
        x = self.enc_norm(x)
        return [layer.cross.project_kv(x) for layer in self.dec], mask

    def decode(self, tgt_in: torch.Tensor, memory: list, mask: torch.Tensor, caches: Optional[list] = None,
               start: int = 0) -> torch.Tensor:
        """Logits for each position of ``tgt_in`` (with ``caches``: the next step only)."""
        x = self.embed_at(tgt_in, start)
        for i, layer in enumerate(self.dec):
            x = layer(x, memory[i], mask, None if caches is None else caches[i])
        return F.linear(self.dec_norm(x), self.embed.weight)

    def forward(self, src: torch.Tensor, tgt_in: torch.Tensor) -> torch.Tensor:
        memory, mask = self.encode(src)
        return self.decode(tgt_in, memory, mask)


def parameter_count(model: nn.Module) -> int:
    return sum(p.numel() for p in model.parameters())
