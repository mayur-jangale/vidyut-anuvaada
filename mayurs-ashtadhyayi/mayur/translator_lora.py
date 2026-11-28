"""Low-rank adapters (LoRA) written in plain PyTorch: wrap the linear layers of a frozen model.

``add_lora`` freezes the model and wraps every ``nn.Linear`` whose name is one of ``targets``;
``adapter_state`` is the small dict of the new weights (what is saved), ``load_adapter`` puts it back.
"""

from __future__ import annotations

import math
from typing import Sequence

import torch
from torch import nn


class LoraLinear(nn.Module):
    """``base(x) + (alpha / rank) * B(A(dropout(x)))``; B starts at zero, so the model starts unchanged."""

    def __init__(self, base: nn.Linear, rank: int, alpha: float, dropout: float):
        super().__init__()
        self.base, self.scale = base, alpha / rank
        self.a = nn.Linear(base.in_features, rank, bias=False)
        self.b = nn.Linear(rank, base.out_features, bias=False)
        nn.init.kaiming_uniform_(self.a.weight, a=math.sqrt(5))
        nn.init.zeros_(self.b.weight)
        self.drop = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.base(x) + self.scale * self.b(self.a(self.drop(x)))


def add_lora(model: nn.Module, targets: Sequence[str], rank: int = 16, alpha: float = 32.0,
             dropout: float = 0.05) -> int:
    """Freeze ``model`` and wrap its target linear layers; returns how many were wrapped."""
    for p in model.parameters():
        p.requires_grad = False
    count = 0
    for parent in list(model.modules()):
        for name, child in list(parent.named_children()):
            if isinstance(child, nn.Linear) and name in targets:
                setattr(parent, name, LoraLinear(child, rank, alpha, dropout))
                count += 1
    return count


def adapter_state(model: nn.Module) -> dict[str, torch.Tensor]:
    return {k: v.detach().half() for k, v in model.state_dict().items() if ".a." in k or ".b." in k}


def load_adapter(model: nn.Module, state: dict[str, torch.Tensor]) -> None:
    result = model.load_state_dict({k: v.float() for k, v in state.items()}, strict=False)
    if result.unexpected_keys:
        raise ValueError(f"adapter does not fit the model: {result.unexpected_keys[:3]}")
