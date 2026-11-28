"""Fine-tune flan-t5-small with LoRA adapters on input form B (variant C of the translator).

    python scripts/train_translator_t5.py --tag c1 --train-shards 12 --minutes 50 --threads 2

Needs ``scripts/fetch_data.py --with-translator-base`` and the shards of
``scripts/build_translation_data.py``. Only the low-rank adapters are trained and saved (the base
stays frozen). The English targets are folded to ASCII (T5's vocabulary has no ā, ī, ṣ ...).
Checkpoints go to ``data/derived/translation/<tag>/``; ``--export`` writes the adapters and their
JSON to ``mayur/models/``. The learning rate warms up, then follows a cosine to zero over the budget.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import torch  # noqa: E402
from transformers import AutoTokenizer, T5ForConditionalGeneration  # noqa: E402

from mayur import resources, translator_data as td, translator_prep as prep  # noqa: E402
from mayur import translator_t5 as t5  # noqa: E402
from mayur.translator_lora import add_lora, adapter_state  # noqa: E402

MODELS = Path(__file__).resolve().parent.parent / "mayur" / "models"


def encode_pairs(split: str, shards: int | None, tok) -> list[tuple[list[int], list[int]]]:
    """(prompt ids, folded English ids) for the first ``shards`` shards of ``split``."""
    english = td.english_lines(split)
    rows = [(i, r) for i, r in td.load_verses(split, shards) if r]
    prompts = [t5.prompt_of(prep.load_reading(r)) for _, r in rows]
    targets = [t5.fold(english[i]) for i, _ in rows]
    src = tok(prompts, truncation=True, max_length=t5.MAX_SRC).input_ids
    tgt = tok(text_target=targets, truncation=True, max_length=128).input_ids
    return list(zip(src, tgt))


def batches(pairs: list, max_tokens: int, rng: random.Random) -> list[list[int]]:
    order = sorted(range(len(pairs)), key=lambda i: len(pairs[i][0]) + rng.random() * 6)
    groups, cur, width = [], [], 0
    for i in order:
        w = max(width, len(pairs[i][0]) + len(pairs[i][1]))
        if cur and w * (len(cur) + 1) > max_tokens:
            groups.append(cur)
            cur, w = [], len(pairs[i][0]) + len(pairs[i][1])
        cur.append(i)
        width = w
    groups.append(cur)
    rng.shuffle(groups)
    return groups


def collate(pairs: list, idx: list[int], pad: int):
    ws, wt = max(len(pairs[i][0]) for i in idx), max(len(pairs[i][1]) for i in idx)
    src = torch.tensor([pairs[i][0] + [pad] * (ws - len(pairs[i][0])) for i in idx])
    tgt = torch.tensor([pairs[i][1] + [-100] * (wt - len(pairs[i][1])) for i in idx])
    return src, (src != pad).long(), tgt


def lr_at(step: int, total: int, warmup: int, peak: float) -> float:
    if step < warmup:
        return peak * (step + 1) / warmup
    return peak * 0.5 * (1 + math.cos(math.pi * min(1.0, (step - warmup) / max(total - warmup, 1)))) + 1e-7


def step_loss(model, pairs, idx, pad) -> torch.Tensor:
    src, mask, tgt = collate(pairs, idx, pad)
    return model(input_ids=src, attention_mask=mask, labels=tgt).loss


def plan_steps(model, opt, pairs, args, rng, pad) -> int:
    """Steps that fit into ``--minutes``, from timing 6 steps (the adapters are restored afterwards)."""
    saved = {k: v.clone() for k, v in adapter_state(model).items()}
    groups = batches(pairs, args.max_tokens, rng)[:6]
    start = time.time()
    for idx in groups:
        opt.zero_grad()
        step_loss(model, pairs, idx, pad).backward()
        opt.step()
    per_step = (time.time() - start) / len(groups)
    model.load_state_dict({k: v.float() for k, v in saved.items()}, strict=False)
    opt.state.clear()
    return max(int(args.minutes * 60 / per_step), 10)


def save(model, args, state, pairs_n: int) -> None:
    """Adapters and their JSON into the run's directory (and mayur/models/ with ``--export``)."""
    work = resources.derived_dir() / "translation" / args.tag
    work.mkdir(parents=True, exist_ok=True)
    info = {"base": "google/flan-t5-small", "base_revision": "0fc9ddf78a1e988dac52e2dac162b0ede4fd74ab",
            "input_form": "B (ASCII text)", "rank": args.rank, "alpha": args.alpha, "targets": list(t5.TARGETS),
            "train_verses": pairs_n, "steps": state["step"], "minutes": round(state["elapsed"] / 60, 1),
            "command": " ".join(sys.argv), "dev_scores": None}
    for folder in ([work, MODELS] if args.export else [work]):
        torch.save(adapter_state(model), folder / t5.ADAPTER)
        (folder / t5.META).write_text(json.dumps(info, indent=1), encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tag", default="c1")
    ap.add_argument("--train-shards", type=int, default=12)
    ap.add_argument("--minutes", type=float, default=50.0)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--rank", type=int, default=16)
    ap.add_argument("--alpha", type=float, default=32.0)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--warmup", type=int, default=30)
    ap.add_argument("--max-tokens", type=int, default=3000)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--export", action="store_true")
    args = ap.parse_args(argv)
    torch.set_num_threads(args.threads)
    torch.manual_seed(args.seed)
    rng = random.Random(args.seed)
    tok = AutoTokenizer.from_pretrained(str(t5.base_dir()))
    model = T5ForConditionalGeneration.from_pretrained(str(t5.base_dir()))
    wrapped = add_lora(model, t5.TARGETS, args.rank, args.alpha)
    trainable = [p for p in model.parameters() if p.requires_grad]
    pairs = encode_pairs("train", args.train_shards, tok)
    sys.stdout.write(f"{wrapped} layers, {sum(p.numel() for p in trainable) / 1e6:.2f}M adapter weights, "
                     f"{len(pairs)} train verses\n")
    opt = torch.optim.AdamW(trainable, lr=args.lr, weight_decay=0.0)
    total = plan_steps(model, opt, pairs, args, rng, tok.pad_token_id)
    sys.stdout.write(f"planned {total} steps\n")
    state = {"step": 0, "elapsed": 0.0, "epochs": 0}
    start = time.time()
    model.train()
    while state["step"] < total:
        for idx in batches(pairs, args.max_tokens, rng):
            if state["step"] >= total:
                break
            for g in opt.param_groups:
                g["lr"] = lr_at(state["step"], total, args.warmup, args.lr)
            opt.zero_grad()
            loss = step_loss(model, pairs, idx, tok.pad_token_id)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(trainable, 1.0)
            opt.step()
            state["step"] += 1
            if state["step"] % 20 == 0:
                sys.stdout.write(f"step {state['step']}/{total} loss {loss.item():.3f} "
                                 f"{(time.time() - start) / 60:.1f} min\n")
                sys.stdout.flush()
        state["epochs"] += 1
    state["elapsed"] = time.time() - start
    save(model, args, state, len(pairs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
