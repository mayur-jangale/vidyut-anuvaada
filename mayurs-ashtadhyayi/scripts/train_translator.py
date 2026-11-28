"""Train the Sanskrit-to-English transformer on the prepared Itihāsa shards (CPU, from scratch).

    python scripts/train_translator.py --form B --train-shards 60 --minutes 120 --threads 2 --tag b1

Reads shards from scripts/build_translation_data.py, writes checkpoints and the vocabulary to
``data/derived/translation/<tag>/`` and, with ``--export``, the fp16 weights + JSON to
``mayur/models/``. The learning rate warms up, then follows a cosine to zero over the time budget
(measured in steps after a short timing run). Resumes from ``--tag``'s last checkpoint.
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
import torch.nn.functional as F  # noqa: E402

from mayur import resources, translator_data as td, translator_input as ti  # noqa: E402
from mayur import translator_prep as prep  # noqa: E402
from mayur.translator_beam import beam_search  # noqa: E402
from mayur.translator_model import Config, Seq2Seq, parameter_count  # noqa: E402
from mayur.translator_vocab import BOS, EOS, PAD, Vocab, train_vocab  # noqa: E402

MODELS = Path(__file__).resolve().parent.parent / "mayur" / "models"
VOCAB_SIZE = 8000


def verse_pairs_of(path: Path, split: str, form: str, vocab: Vocab, cfg: Config) -> list:
    """[(source ids, target ids with BOS/EOS)] of one shard."""
    english = td.english_lines(split)
    out = []
    for i, rows in td.read_shard(path):
        if rows:
            src = vocab.encode_source(ti.encode_reading(prep.load_reading(rows), form))
            out.append((src[:cfg.max_src], [BOS, *vocab.encode_text(english[i]), EOS][:cfg.max_tgt]))
    return out


def verse_pairs(split: str, form: str, vocab: Vocab, shards: int | None, cfg: Config) -> list:
    """Pairs of the first ``shards`` shards of ``split``."""
    return [p for path in td.available_shards(split)[:shards] for p in verse_pairs_of(path, split, form, vocab, cfg)]


def get_vocab(path: Path, shards: int, split: str = "train") -> Vocab:
    """The saved vocabulary, or one trained on all English of ``split``, the words of its verses
    and the analysed input (form B) of the first ``shards`` shards."""
    if path.exists():
        return Vocab.load(path)
    english = td.english_lines(split)
    ids = td.corpus_ids(split)
    sanskrit = td.read_lines(split, "sn")
    rows = td.load_verses(split, shards)
    sources = [ti.encode_reading(prep.load_reading(r), "B") for _, r in rows if r]
    surface = [w for i in ids for w in sanskrit[i].replace("।", " ").replace("॥", " ").split()]
    vocab = train_vocab(sources, [english[i] for i in ids], VOCAB_SIZE, surface)
    vocab.save(path)
    return vocab


def batches(pairs: list, max_tokens: int, rng: random.Random):
    """Length-bucketed batches of at most ``max_tokens`` padded source + target positions, shuffled."""
    order = sorted(range(len(pairs)), key=lambda i: (len(pairs[i][0]) + rng.random() * 8, len(pairs[i][1])))
    groups, cur, width = [], [], 0
    for i in order:
        width_i = max(width, len(pairs[i][0]) + len(pairs[i][1]))
        if cur and width_i * (len(cur) + 1) > max_tokens:
            groups.append(cur)
            cur, width_i = [], len(pairs[i][0]) + len(pairs[i][1])
        cur.append(i)
        width = width_i
    groups.append(cur)
    rng.shuffle(groups)
    return groups


def collate(pairs: list, idx: list[int]):
    ws = max(len(pairs[i][0]) for i in idx)
    wt = max(len(pairs[i][1]) for i in idx)
    src = torch.tensor([pairs[i][0] + [PAD] * (ws - len(pairs[i][0])) for i in idx])
    tgt = torch.tensor([pairs[i][1] + [PAD] * (wt - len(pairs[i][1])) for i in idx])
    return src, tgt


def loss_of(model: Seq2Seq, src, tgt, smoothing: float) -> torch.Tensor:
    logits = model(src, tgt[:, :-1])
    return F.cross_entropy(logits.reshape(-1, logits.shape[-1]), tgt[:, 1:].reshape(-1),
                           ignore_index=PAD, label_smoothing=smoothing)


@torch.no_grad()
def dev_loss(model: Seq2Seq, pairs: list) -> float:
    model.eval()
    total, count = 0.0, 0
    for idx in batches(pairs, 4000, random.Random(0)):
        src, tgt = collate(pairs, idx)
        n = int((tgt[:, 1:] != PAD).sum())
        total += float(loss_of(model, src, tgt, 0.0)) * n
        count += n
    return total / max(count, 1)


def dev_bleu(model: Seq2Seq, vocab: Vocab, pairs: list, refs: list[str], beam: int) -> tuple[float, float]:
    """(BLEU, chrF) of beam search on ``pairs`` against ``refs`` (sacrebleu)."""
    import sacrebleu

    model.eval()
    hyps = []
    for start in range(0, len(pairs), 16):
        chunk = pairs[start:start + 16]
        width = max(len(s) for s, _ in chunk)
        src = torch.tensor([s + [PAD] * (width - len(s)) for s, _ in chunk])
        hyps += [vocab.decode(h) for h in beam_search(model, src, beam, model.config.max_tgt - 2)]
    return (sacrebleu.corpus_bleu(hyps, [refs]).score, sacrebleu.corpus_chrf(hyps, [refs]).score)


def lr_at(step: int, state: dict, args: argparse.Namespace) -> float:
    """Warm-up, then inverse square root (open-ended runs) or a cosine over the run's own steps."""
    if args.schedule == "isqrt":
        return args.lr * min((step + 1) / args.warmup, math.sqrt(args.warmup / (step + 1)))
    done = step - state["begin"]
    if done < args.warmup:
        return args.lr * (done + 1) / args.warmup
    frac = min(1.0, (done - args.warmup) / max(state["total"] - state["begin"] - args.warmup, 1))
    return args.lr * 0.5 * (1 + math.cos(math.pi * frac)) + 1e-6


def save_ckpt(path: Path, model, opt, state: dict) -> None:
    torch.save({"model": model.state_dict(), "opt": opt.state_dict(), "state": state}, path)


def export(model: Seq2Seq, vocab: Vocab, info: dict, out: Path) -> None:
    """fp16 weights, the vocabulary and the JSON record next to them."""
    out.mkdir(parents=True, exist_ok=True)
    torch.save({k: v.half() for k, v in model.state_dict().items()}, out / "translator.pt")
    vocab.save(out / "translator_vocab.json")
    (out / "translator.json").write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding="utf-8")


def train(args: argparse.Namespace) -> None:
    torch.set_num_threads(args.threads)
    torch.manual_seed(args.seed)
    rng = random.Random(args.seed)
    work = resources.derived_dir() / "translation" / args.tag
    work.mkdir(parents=True, exist_ok=True)
    vocab = get_vocab(Path(args.vocab) if args.vocab else work.parent / "vocab.json", args.vocab_shards, args.train_split)
    cfg = Config(vocab=len(vocab), d_model=args.d_model, heads=args.heads, d_ff=args.d_ff,
                 enc_layers=args.layers, dec_layers=args.layers, dropout=args.dropout)
    (work / "config.json").write_text(json.dumps(cfg.to_json()), encoding="utf-8")
    (work / "command.json").write_text(json.dumps({"argv": sys.argv, "args": vars(args)}), encoding="utf-8")
    dev_pairs = verse_pairs("dev", args.form, vocab, None, cfg)
    dev_ids = [i for i, r in td.load_verses("dev", None) if r]
    english = td.english_lines("dev")
    dev_refs = [english[i] for i in dev_ids]
    model = Seq2Seq(cfg)
    opt = torch.optim.AdamW(model.parameters(), lr=args.lr, betas=(0.9, 0.98), weight_decay=0.01)
    sys.stdout.write(f"{parameter_count(model) / 1e6:.2f}M parameters, "
                     f"{len(dev_pairs)} dev verses, vocab {len(vocab)}\n")
    state = {"step": 0, "epoch": 0, "elapsed": 0.0, "best_bleu": -1.0, "log": []}
    if args.init:
        model.load_state_dict(torch.load(args.init, weights_only=True))
    ckpt = work / "last.pt"
    if ckpt.exists():
        data = torch.load(ckpt, weights_only=False)
        model.load_state_dict(data["model"])
        opt.load_state_dict(data["opt"])
        state = data["state"]
    run(args, model, opt, vocab, cfg, dev_pairs, dev_refs, state, rng, work)


def estimate_steps(model, opt, pairs, args, rng) -> int:
    """Steps that fit into ``--minutes``: time 12 steps (not applied: the weights are restored)."""
    saved = {k: v.clone() for k, v in model.state_dict().items()}
    model.train()
    groups = batches(pairs, args.max_tokens, rng)[:12]
    start = time.time()
    for idx in groups:
        src, tgt = collate(pairs, idx)
        opt.zero_grad()
        loss_of(model, src, tgt, args.smoothing).backward()
        opt.step()
    per_step = (time.time() - start) / len(groups)
    model.load_state_dict(saved)
    opt.state.clear()
    return int(args.minutes * 60 / per_step)


def plan_run(args, model, opt, pairs, state, rng) -> None:
    """Set the run's step budget: a fixed number of further steps, or what ``--minutes`` allow."""
    state["begin"] = state["step"]
    if args.schedule == "cosine":
        state["total"] = state["step"] + (args.steps or estimate_steps(model, opt, pairs, args, rng))
    else:
        state["total"] = 10 ** 9
    state["deadline"] = state["elapsed"] + args.minutes * 60


def refresh_pairs(args, vocab, cfg, cache: dict) -> list:
    """Train verses of every shard built so far (up to ``--train-shards``); shards are encoded once."""
    for path in td.available_shards(args.train_split)[:args.train_shards]:
        if path.name not in cache:
            cache[path.name] = verse_pairs_of(path, args.train_split, args.form, vocab, cfg)
    return [p for rows in cache.values() for p in rows]


def run(args, model, opt, vocab, cfg, dev_pairs, dev_refs, state, rng, work) -> None:
    cache: dict = {}
    pairs = refresh_pairs(args, vocab, cfg, cache)
    plan_run(args, model, opt, pairs, state, rng)
    sample = min(args.eval_verses, len(dev_pairs))
    start = time.time() - state["elapsed"]
    while state["step"] < state["total"] and state["elapsed"] < state["deadline"]:
        pairs = refresh_pairs(args, vocab, cfg, cache)
        sys.stdout.write(f"epoch {state['epoch'] + 1}: {len(pairs)} train verses\n")
        model.train()
        for idx in batches(pairs, args.max_tokens, rng):
            if state["step"] >= state["total"] or time.time() - start >= state["deadline"]:
                break
            for g in opt.param_groups:
                g["lr"] = lr_at(state["step"], state, args)
            src, tgt = collate(pairs, idx)
            opt.zero_grad()
            loss = loss_of(model, src, tgt, args.smoothing)
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            opt.step()
            state["step"] += 1
            if state["step"] % 100 == 0:
                sys.stdout.write(f"step {state['step']} loss {float(loss):.3f} {(time.time() - start) / 60:.1f} min\n")
                sys.stdout.flush()
        state["epoch"] += 1
        state["elapsed"] = time.time() - start
        state["verses"] = len(pairs)
        if state["elapsed"] - state.get("last_eval", 0.0) >= args.eval_minutes * 60:
            evaluate_epoch(args, model, vocab, dev_pairs, dev_refs, sample, state, work, opt, cfg)
        else:
            save_ckpt(work / "last.pt", model, opt, state)
    if state.get("last_eval") != state["elapsed"]:
        evaluate_epoch(args, model, vocab, dev_pairs, dev_refs, sample, state, work, opt, cfg)


def evaluate_epoch(args, model, vocab, dev_pairs, dev_refs, sample, state, work, opt, cfg) -> None:
    dl = dev_loss(model, dev_pairs)
    bleu, chrf = dev_bleu(model, vocab, dev_pairs[:sample], dev_refs[:sample], args.beam)
    entry = {"epoch": state["epoch"], "step": state["step"], "minutes": round(state["elapsed"] / 60, 1),
             "dev_loss": round(dl, 3), "bleu": round(bleu, 2), "chrf": round(chrf, 2)}
    state["log"].append(entry)
    state["last_eval"] = state["elapsed"]
    sys.stdout.write(json.dumps(entry) + "\n")
    sys.stdout.flush()
    save_ckpt(work / "last.pt", model, opt, state)
    if bleu > state["best_bleu"]:
        state["best_bleu"] = bleu
        torch.save(model.state_dict(), work / "best.pt")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--form", choices=ti.FORMS, default="B")
    ap.add_argument("--tag", default="run")
    ap.add_argument("--train-split", default="train", help="split to train on (dev only for smoke tests)")
    ap.add_argument("--train-shards", type=int, default=60)
    ap.add_argument("--vocab", default="", help="vocabulary file (default: translation/vocab.json, made if absent)")
    ap.add_argument("--vocab-shards", type=int, default=40)
    ap.add_argument("--minutes", type=float, default=60.0)
    ap.add_argument("--steps", type=int, default=0, help="cosine schedule: further steps (else from --minutes)")
    ap.add_argument("--schedule", choices=("isqrt", "cosine"), default="isqrt")
    ap.add_argument("--init", default="", help="weights (best.pt of a run) to start from")
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--d-model", type=int, default=256)
    ap.add_argument("--heads", type=int, default=4)
    ap.add_argument("--d-ff", type=int, default=1024)
    ap.add_argument("--layers", type=int, default=3)
    ap.add_argument("--dropout", type=float, default=0.1)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--warmup", type=int, default=400)
    ap.add_argument("--smoothing", type=float, default=0.1)
    ap.add_argument("--max-tokens", type=int, default=3500)
    ap.add_argument("--eval-verses", type=int, default=100)
    ap.add_argument("--eval-minutes", type=float, default=20.0)
    ap.add_argument("--beam", type=int, default=4)
    ap.add_argument("--seed", type=int, default=1)
    args = ap.parse_args(argv)
    train(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
