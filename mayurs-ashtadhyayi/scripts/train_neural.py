"""Train the neural context model (mayur/neural.py) and tune its weight next to the perceptron.

    python scripts/train_neural.py [--max-words 2500000] [--epochs 4] [--eval-only]

TRAIN: gold word forms of whole verses of ``split_files("train")`` (no lexicon needed).
DEV:   ``split_files("dev")`` plus the fixed ``dev_pool`` sample of scripts/train_tagger.py:
       early stopping (gold-form head accuracy) and λ. TEST: report only. sealed_test is never read.
Writes mayur/models/neural_tagger.pt and neural_tagger.json.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import time
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import torch  # noqa: E402

import train_tagger as tt  # noqa: E402
from mayur import dcs, neural, tagger, ud  # noqa: E402

# the perceptron's score differences between candidates are in the tens to hundreds (sums of averaged
# weights over ~100 features), the neural Σ log P in units: λ is swept over that range
LAMBDAS = (2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 200.0, 500.0)


def verse_record(verse: list[dict]) -> dict:
    forms, lines, cpd, tg = [], [], [], []
    for line, sent in enumerate(verse):
        for t in sent["tokens"]:
            forms.append(t["form"])
            lines.append(line)
            cpd.append(t["compound_member"])
            tg.append(tuple(neural.targets(t["upos"], t["feats"], t["compound_member"])[h] for h in neural.HEADS))
    return {"forms": forms, "lines": lines, "cpd": cpd, "targets": tg}


def load_train(max_words: int, seed: int = 0) -> list[dict]:
    files = list(dcs.split_files("train"))
    random.Random(seed).shuffle(files)
    out, n = [], 0
    for e in files:
        for v in tt.verses_of(list(tt._sentences(e))):
            r = verse_record(v)
            if r["forms"] and len(r["forms"]) <= 80:
                out.append(r)
                n += len(r["forms"])
        if n >= max_words:
            break
    return out


def vocab(data: list[dict]) -> tuple[list[str], dict[str, list[str]]]:
    sc = Counter(s for r in data for f in r["forms"] for s in neural.sounds(f))
    sounds = [neural.PAD, neural.UNK] + sorted(s for s, c in sc.items() if c >= 2)
    values = {h: sorted({t[j] for r in data for t in r["targets"]}) for j, h in enumerate(neural.HEADS)}
    return sounds, values


def target_tensor(batch: list[dict], values: dict[str, list[str]]) -> dict[str, torch.Tensor]:
    t = max(len(r["forms"]) for r in batch)
    out = {}
    for j, (h, vals) in enumerate(values.items()):
        ix = {v: i for i, v in enumerate(vals)}
        y = torch.full((len(batch), t), -100, dtype=torch.long)
        for b, r in enumerate(batch):
            y[b, : len(r["targets"])] = torch.tensor([ix.get(x[j], -100) for x in r["targets"]])
        out[h] = y
    return out


def batches(data: list[dict], words_per_batch: int, seed: int) -> list[list[dict]]:
    order = sorted(range(len(data)), key=lambda i: (len(data[i]["forms"]), random.Random(seed + i).random()))
    out, cur, n = [], [], 0
    for i in order:
        cur.append(data[i])
        n += len(data[i]["forms"])
        if n >= words_per_batch:
            out.append(cur)
            cur, n = [], 0
    if cur:
        out.append(cur)
    random.Random(seed).shuffle(out)
    return out


def head_accuracy(model, meta: dict, data: list[dict]) -> dict[str, float]:
    model.eval()
    right, n = Counter(), 0
    for b in batches(data, 4000, 0):
        lps = neural.logprobs_with(model, meta, [(r["forms"], r["lines"], r["cpd"]) for r in b])
        for r, lp in zip(b, lps):
            for t, w in zip(r["targets"], lp):
                n += 1
                ok = True
                for j, h in enumerate(neural.HEADS):
                    good = max(w[h], key=w[h].get) == t[j]
                    right[h] += good
                    ok &= good
                right["all"] += ok
    return {h: round(right[h] / max(1, n), 4) for h in (*neural.HEADS, "all")}


def train(data, dev, epochs: int, log, cfg: dict, minutes: float = 1e9) -> tuple:
    sounds, values = vocab(data)
    meta = {"config": cfg, "sounds": sounds, "values": values}
    model = neural.build_model(cfg, len(sounds), {h: len(v) for h, v in values.items()})
    opt = torch.optim.Adam(model.parameters(), lr=2e-3)
    loss_fn = torch.nn.CrossEntropyLoss(ignore_index=-100)
    sound_ix = {s: i for i, s in enumerate(sounds)}
    best = {"acc": -1.0, "state": None, "epoch": 0}
    deadline = time.time() + 60 * minutes
    for epoch in range(epochs):
        model.train()
        t0, nw, tot = time.time(), 0, 0.0
        bs = batches(data, 1500, epoch)
        for k, b in enumerate(bs):
            x = neural.batch_tensors([(r["forms"], r["lines"], r["cpd"]) for r in b], sound_ix, cfg["buckets"])
            out = model(*x)
            y = target_tensor(b, values)
            loss = sum(loss_fn(out[h].reshape(-1, out[h].shape[-1]), y[h].reshape(-1)) for h in values)
            opt.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
            opt.step()
            nw += sum(len(r["forms"]) for r in b)
            tot += float(loss.detach())
            if time.time() > deadline:
                log(f"time budget reached in epoch {epoch + 1} after {nw} words")
                break
            if k % 200 == 0:
                log(f"epoch {epoch + 1} batch {k}/{len(bs)} loss {tot / (k + 1):.3f} {nw / (time.time() - t0):.0f} w/s")
        for g in opt.param_groups:
            g["lr"] *= 0.6
        acc = head_accuracy(model, meta, dev)
        log(f"epoch {epoch + 1}: train loss {tot / max(1, k):.3f}, DEV gold-form heads {acc}")
        if acc["all"] > best["acc"]:
            best.update(acc=acc["all"], state={k: v.clone() for k, v in model.state_dict().items()},
                        epoch=epoch + 1, heads=acc)
            torch.save(best["state"], neural.WEIGHTS_FILE)  # checkpoint (config written at the end)
        if time.time() > deadline:
            break
    model.load_state_dict(best["state"])
    model.eval()
    return model, {**meta, "epochs_best": best["epoch"], "dev_heads": best["heads"]}


def neural_scores(model, meta: dict, items) -> list[list[list[float]]]:
    out = []
    for _, it in items:
        w = it["words"]
        lp = neural.logprobs_with(model, meta, [([x.form for x in w], [x.line for x in w],
                                                 [x.in_compound for x in w])])[0]
        out.append(neural.candidate_scores(it["cands"], lp))
    return out


def choice(it: dict, w, bonus, use_enforce: bool = True) -> list[int]:
    return tt.learned_choice(it, w, use_enforce, bonus=bonus)


def systems(items, scores, w, lam: float, enforce: bool, conf=None) -> dict:
    lookup = {id(it): s for (_, it), s in zip(items, scores)}
    alone = lambda it: [max(range(len(r)), key=r.__getitem__) if r else 0 for r in lookup[id(it)]]
    scaled = lambda it: [[lam * x for x in r] for r in lookup[id(it)]]
    return {"perceptron": tt.evaluate(items, lambda it: choice(it, w, [], enforce)),
            "neural": tt.evaluate(items, alone),
            "combined": tt.evaluate(items, lambda it: choice(it, w, scaled(it), enforce), conf)}


def print_table(split: str, r: dict) -> None:
    for book in r["perceptron"]:
        cells = "  ".join(f"{name[:5]} {r[name][book]['all']:.3f}/{r[name][book]['Case']:.3f}/"
                          f"{r[name][book]['Gender']:.3f}" for name in r)
        print(f"{split:5} {book:28} n={r['perceptron'][book]['n']:5} {cells}  oracle "
              f"{r['perceptron'][book]['oracle']:.3f}")
    for name in r:
        acc = "  ".join(f"{k} {tt.micro(r[name], k):.3f}" for k in ("all", "Case", "Gender", "oracle"))
        print(f"{split:5} OVERALL {name:10} n={sum(x['n'] for x in r[name].values())} {acc}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-words", type=int, default=2_500_000)
    ap.add_argument("--epochs", type=int, default=4)
    ap.add_argument("--eval-only", action="store_true")
    ap.add_argument("--minutes", type=float, default=1e9, help="wall-clock budget for training")
    args = ap.parse_args()
    torch.manual_seed(0)
    random.seed(0)
    torch.set_num_threads(3)
    t0 = time.time()
    log = lambda m: print(f"[{time.time() - t0:5.0f}s] {m}", file=sys.stderr, flush=True)
    dev_gold = [verse_record(v) for e in dcs.split_files("dev") for v in tt.verses_of(list(tt._sentences(e)))]
    if args.eval_only:
        meta = json.loads(neural.CONFIG_FILE.read_text(encoding="utf-8"))
        model = neural.build_model(meta["config"], len(meta["sounds"]), {h: len(v) for h, v in meta["values"].items()})
        model.load_state_dict(torch.load(neural.WEIGHTS_FILE, weights_only=True))
        model.eval()
    else:
        data = load_train(args.max_words)
        log(f"train {len(data)} verses, {sum(len(r['forms']) for r in data)} words")
        model, meta = train(data, dev_gold, args.epochs, log, dict(neural.DEFAULT_CONFIG), args.minutes)
        meta["train_words"] = sum(len(r["forms"]) for r in data)
        del data
    print("neural alone, DEV gold forms, per head:", head_accuracy(model, meta, dev_gold))
    saved = json.loads(tt.MODEL.read_text(encoding="utf-8"))
    tt.TABLES.update(saved.get("tables", {}))
    w, enforce = (saved["weights"], saved.get("weights2")), saved.get("enforce", True)
    dev, test = tt.load_eval()
    log(f"candidates built: dev {len(dev)} verses, test {len(test)} verses")
    sd, st = neural_scores(model, meta, dev), neural_scores(model, meta, test)
    t1 = time.time()
    base = tt.micro(tt.evaluate(dev, lambda it: choice(it, w, [], enforce)))
    log(f"perceptron DEV {base:.4f} ({time.time() - t1:.0f}s)")
    best = (base, 0.0)
    for lam in LAMBDAS:
        lookup = {id(it): s for (_, it), s in zip(dev, sd)}
        acc = tt.micro(tt.evaluate(dev, lambda it: choice(it, w, [[lam * x for x in r] for r in lookup[id(it)]],
                                                          enforce)))
        log(f"λ={lam}: DEV all {acc:.4f}")
        best = max(best, (acc, lam))
    lam = best[1]
    conf: Counter = Counter()
    rd = systems(dev, sd, w, lam or 1.0, enforce, conf)
    rt = systems(test, st, w, lam or 1.0, enforce)
    print(f"chosen λ = {lam}   (cells: all/Case/Gender)")
    print_table("dev", rd)
    print_table("test", rt)
    print("top-10 remaining confusions, combined, DEV (gold -> predicted):")
    for (g, p), n in conf.most_common(10):
        print(f"{n:5}  {g}  ->  {p}")
    enabled = lam > 0 and tt.micro(rd["combined"]) > tt.micro(rd["perceptron"])
    print("enabled" if enabled else "NOT enabled (combination does not beat the perceptron on DEV)")
    if not args.eval_only:
        torch.save(model.state_dict(), neural.WEIGHTS_FILE)
    meta.update(enabled=enabled, **{"lambda": lam}, command="python scripts/train_neural.py " + " ".join(sys.argv[1:]),
                source="trained on Digital Corpus of Sanskrit annotations (Oliver Hellwig), CC BY 4.0",
                report={"dev": rd, "test": rt})
    neural.CONFIG_FILE.write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
    log("done")


if __name__ == "__main__":
    main()
