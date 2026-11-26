"""Train the neural sound-level boundary model (mayur/neural_boundary.py).

    ulimit -v 8000000; python scripts/train_boundary.py --minutes 25
    python scripts/train_boundary.py --eval-only
    python scripts/train_boundary.py --validate 300   # label extraction vs lattice gold paths

TRAIN = split_files("train"); early stopping on dev_pool + dev; TEST reported only.
"""

from __future__ import annotations

import argparse
import json
import pickle
import random
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import dcs, segmenter  # noqa: E402
from mayur import neural_boundary as nb  # noqa: E402
from mayur.lipi import devanagari  # noqa: E402

CACHE = Path("/tmp/claude-0/-home-user-vidyut-anuvaada/d033d477-145c-50bb-a9f3-c7728989a8e6/scratchpad/boundary_cache")


def book_of(entry: dict) -> str:
    return devanagari(Path(entry["file"]).parent.name.lower(), "iast")


def items(split: str) -> tuple[list[tuple], int]:
    """(text, spaces, labels, book) of a split's usable gold lines, and the number dropped."""
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{split}.pkl"
    if path.exists():
        return pickle.loads(path.read_bytes())
    out, dropped = [], 0
    for entry in dcs.split_files(split):
        book = book_of(entry)
        for line in dcs.gold_lines([entry]):
            text, spaces = segmenter._prepare(line["compact"])
            labels = nb.extract_labels(text, [(w["form"], w["compound_member"]) for w in line["words"]])
            if labels is None:
                dropped += 1
            else:
                out.append((text, spaces, tuple(labels), book))
    path.write_bytes(pickle.dumps((out, dropped)))
    return out, dropped


# ---------------------------------------------------------------- validation against the lattice

def lattice_marks(line: str, words: list[dict]) -> set | None:
    """Boundary marks of the lattice path equal to the gold: ('B', i) after sound i, ('F', i) fused."""
    text, spaces = segmenter._prepare(line)
    forms = [segmenter._norm(w["form"]) for w in words]
    flags = [w["compound_member"] for w in words]
    for tier in (0, 1):
        lat = segmenter._Lattice(text, spaces, tier)
        frontier = {segmenter._START: frozenset()}
        for n, form in enumerate(forms):
            last = n == len(forms) - 1
            nxt: dict = {}
            for state, marks in frontier.items():
                for e in lat.edges(state):
                    if segmenter._norm(e[0]) != form or e[2].samasa != bool(flags[n]) or ((e[5] == segmenter._END) != last):
                        continue
                    if last:
                        nxt[e[5]] = marks
                        continue
                    mark = _lattice_mark(text, e[2], e[1], e[5])
                    nxt.setdefault(e[5], marks | {mark})
            frontier = nxt
            if not frontier:
                break
        if segmenter._END in frontier:
            return set(frontier[segmenter._END])
    return None


def _lattice_mark(text: tuple, jn, k: int, nxt: tuple) -> tuple[str, int]:
    """The junction of a lattice edge in label terms (see the label semantics in neural_boundary)."""
    j, head, _ = nxt
    if not head:
        if jn.left_tail and nb.sd.is_vowel(jn.left_tail[-1]) and not jn.surface and nb.sd.is_vowel(text[j]):
            return ("F", j)  # अ + आ → आ written once: the left word's vowel is the right word's initial
        return ("B", j - 1)
    s = j - len(head)
    surface = text[k:j]
    if head == ("अ",) and any(v in nb._ELIDING for v in surface):
        return ("B", k + max(i for i, v in enumerate(surface) if v in nb._ELIDING))
    if nb.sd.is_vowel(head[0]) and nb.sd.is_vowel(text[s]):
        return ("F", s)
    return ("B", s - 1)


def validate(n: int) -> None:
    lines = list(dcs.gold_lines(dcs.split_files("dev_pool"), limit=n, seed=1))
    agree = covered = dropped = 0
    bad = []
    for line in lines:
        text, _ = segmenter._prepare(line["compact"])
        labels = nb.extract_labels(text, [(w["form"], w["compound_member"]) for w in line["words"]])
        lat = lattice_marks(line["compact"], line["words"])
        if labels is None:
            dropped += 1
            continue
        if lat is None:
            continue
        covered += 1
        ours = {("F" if lab.startswith("F") else "B", i) for i, lab in enumerate(labels[:-1]) if lab != "N"}
        if ours == lat:
            agree += 1
        else:
            bad.append((line["compact"], " ".join(w["form"] for w in line["words"]), sorted(ours ^ lat)))
    print(f"VALIDATE {len(lines)} dev_pool lines: dropped {dropped}; gold path in lattice {covered}; "
          f"label/lattice agreement {agree}/{covered} = {agree / max(covered, 1):.3f}")
    for b in bad[:15]:
        print("   ", b)


# ---------------------------------------------------------------- training / evaluation

def batches(data: list, size: int, shuffle: bool, rng: random.Random) -> list[list]:
    order = sorted(range(len(data)), key=lambda i: (len(data[i][0]), rng.random() if shuffle else 0))
    out = [[data[i] for i in order[s:s + size]] for s in range(0, len(order), size)]
    if shuffle:
        rng.shuffle(out)
    return out


def tensors(batch: list, vocab: dict, with_labels: bool = True):
    import torch

    n = max(len(b[0]) for b in batch)
    ids = torch.zeros(len(batch), n, dtype=torch.long)
    sp = torch.zeros(len(batch), n)
    lab = torch.full((len(batch), n), -100, dtype=torch.long)
    li = {l: i for i, l in enumerate(nb.LABELS)}
    for r, b in enumerate(batch):
        x, s = nb.encode(b[0], b[1], vocab)
        ids[r, :len(x)] = torch.tensor(x)
        sp[r, :len(x)] = torch.tensor(s)
        if with_labels:
            lab[r, :len(x)] = torch.tensor([li[l] for l in b[2]])
    return ids, sp, lab


def predict(net, data: list, vocab: dict) -> list[list[str]]:
    import torch

    net.eval()
    preds: dict[int, list[str]] = {}
    order = sorted(range(len(data)), key=lambda i: len(data[i][0]))
    with torch.no_grad():
        for s in range(0, len(order), 256):
            idx = order[s:s + 256]
            ids, sp, _ = tensors([data[i] for i in idx], vocab, False)
            arg = net(ids, sp).argmax(-1).tolist()
            for r, i in enumerate(idx):
                preds[i] = [nb.LABELS[k] for k in arg[r][:len(data[i][0])]]
    net.train()
    return [preds[i] for i in range(len(data))]


def _f1(tp: int, np_: int, ng: int) -> float:
    return 2 * tp / max(np_ + ng, 1)


def metrics(data: list, preds: list) -> dict[str, dict[str, float]]:
    acc = defaultdict(Counter)
    for (text, _, gold, book), pred in zip(data, preds):
        for key in (book, "ALL"):
            c = acc[key]
            c["sounds"] += len(gold)
            c["correct"] += sum(g == p for g, p in zip(gold, pred))
            gb = {i for i, l in enumerate(gold[:-1]) if l != "N"}
            pb = {i for i, l in enumerate(pred[:-1]) if l != "N"}
            c["b_tp"] += len(gb & pb); c["b_p"] += len(pb); c["b_g"] += len(gb)
            gp = {i for i, l in enumerate(gold[:-1]) if l in ("P", "FP")}
            pp = {i for i, l in enumerate(pred[:-1]) if l in ("P", "FP")}
            c["p_tp"] += len(gp & pp); c["p_p"] += len(pp); c["p_g"] += len(gp)
            gw, pw = set(nb.boundaries(gold)), set(nb.boundaries(pred))
            c["w_tp"] += len(gw & pw); c["w_p"] += len(pw); c["w_g"] += len(gw)
    return {k: {"lines_sounds": c["sounds"], "label_acc": c["correct"] / c["sounds"],
                "b_prec": c["b_tp"] / max(c["b_p"], 1), "b_rec": c["b_tp"] / max(c["b_g"], 1),
                "b_f1": _f1(c["b_tp"], c["b_p"], c["b_g"]), "pada_f1": _f1(c["p_tp"], c["p_p"], c["p_g"]),
                "word_f1": _f1(c["w_tp"], c["w_p"], c["w_g"])} for k, c in acc.items()}


def report(name: str, m: dict) -> None:
    for k in sorted(m, key=lambda k: (k == "ALL", k)):
        r = m[k]
        print(f"{name:5s} {k:16s} sounds {r['lines_sounds']:7d} acc {r['label_acc']:.4f} boundary P/R/F1 "
              f"{r['b_prec']:.4f}/{r['b_rec']:.4f}/{r['b_f1']:.4f} pada-F1 {r['pada_f1']:.4f} naive-word-F1 {r['word_f1']:.4f}")


def train(args) -> None:
    import torch

    torch.manual_seed(0)
    rng = random.Random(0)
    tr, tr_drop = items("train")
    dv = items("dev_pool")[0] + items("dev")[0]
    print(f"TRAIN usable {len(tr)} dropped {tr_drop}; DEV(dev_pool+dev) {len(dv)}", flush=True)
    if args.limit:
        tr = rng.sample(tr, min(args.limit, len(tr)))
    counts = Counter(v for t in tr for v in t[0])
    vocab_list = [nb.PAD, nb.UNK] + sorted(v for v, c in counts.items() if c >= 3)
    vocab = {v: i for i, v in enumerate(vocab_list)}
    arch = {"emb": 64, "hidden": args.hidden, "layers": args.layers, "dropout": 0.25}
    net = nb.build_model(len(vocab), **arch)
    opt = torch.optim.Adam(net.parameters(), lr=2e-3)
    dev_sample = rng.sample(dv, min(len(dv), 6000))
    best, t0, step, seen = -1.0, time.time(), 0, 0
    deadline = t0 + args.minutes * 60
    for epoch in range(args.epochs):
        for batch in batches(tr, args.batch, True, rng):
            ids, sp, lab = tensors(batch, vocab)
            loss = torch.nn.functional.cross_entropy(net(ids, sp).reshape(-1, len(nb.LABELS)), lab.reshape(-1))
            opt.zero_grad(); loss.backward()
            torch.nn.utils.clip_grad_norm_(net.parameters(), 5.0)
            opt.step()
            step += 1; seen += int((lab >= 0).sum())
            if step % args.eval_every == 0 or time.time() > deadline:
                m = metrics(dev_sample, predict(net, dev_sample, vocab))["ALL"]
                el = time.time() - t0
                print(f"ep {epoch} step {step} loss {loss.item():.4f} {seen / el:.0f} sounds/s [{el:.0f}s] "
                      f"DEV b-F1 {m['b_f1']:.4f} word-F1 {m['word_f1']:.4f}", flush=True)
                if m["b_f1"] > best:
                    best = m["b_f1"]
                    torch.save(net.state_dict(), nb.MODEL_FILE)
                    nb.META_FILE.write_text(json.dumps({"vocab": vocab_list, "arch": arch, "labels": nb.LABELS,
                                                        "dev_b_f1": best, "train_lines": len(tr), "step": step},
                                                       ensure_ascii=False), encoding="utf-8")
            if time.time() > deadline:
                break
        if time.time() > deadline:
            break
        for g in opt.param_groups:
            g["lr"] *= 0.5
    print(f"trained {time.time() - t0:.0f}s, best DEV(sample) boundary F1 {best:.4f}")


def evaluate() -> None:
    nb._load.cache_clear()
    loaded = nb._load()
    if loaded is None:
        print("no model")
        return
    net, vocab = loaded
    for split in ("dev_pool", "dev", "test"):
        data, dropped = items(split)
        print(f"{split}: {len(data)} lines ({dropped} dropped by alignment)")
        report(split[:5].upper(), metrics(data, predict(net, data, vocab)))
    data = items("dev")[0][:200]
    t = time.time()
    for d in data:
        nb._cached.__wrapped__(d[0], d[1])
    n = sum(len(d[0]) for d in data)
    print(f"inference {1000 * (time.time() - t) / len(data):.2f} ms/line (avg {n / len(data):.0f} sounds); "
          f"model {nb.MODEL_FILE.stat().st_size / 1e6:.2f} MB")


def main() -> None:
    import torch

    torch.set_num_threads(2)
    ap = argparse.ArgumentParser()
    ap.add_argument("--eval-only", action="store_true")
    ap.add_argument("--validate", type=int, default=0)
    ap.add_argument("--minutes", type=float, default=25.0)
    ap.add_argument("--epochs", type=int, default=4)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--batch", type=int, default=64)
    ap.add_argument("--hidden", type=int, default=192)
    ap.add_argument("--layers", type=int, default=2)
    ap.add_argument("--eval-every", type=int, default=500)
    args = ap.parse_args()
    if args.validate:
        validate(args.validate)
        return
    if not args.eval_only:
        train(args)
    evaluate()


if __name__ == "__main__":
    main()
