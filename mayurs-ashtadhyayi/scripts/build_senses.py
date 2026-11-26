"""Build and measure the word-sense model: data/derived/sense_model.json.

    python scripts/build_senses.py [--eval-only] [--out FILE]

Trains on split_files("train") only, tunes the smoothing on "dev_pool" and "dev", reports on
"dev" and "test" (never "sealed_test"). Run with `ulimit -v 5000000`; the corpus is streamed.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path
from typing import Any, Callable, Iterable, Iterator, NamedTuple

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import dcs, resources, senses  # noqa: E402
from mayur.lipi import devanagari  # noqa: E402

MIN_OCCURRENCES = 20  # annotated occurrences of an ambiguous lemma
MIN_LABEL = 2.0  # a label needs this much weight to count as a sense of the lemma
MIN_FEATURE = 3.0  # a context feature needs this much weight in total
VOCAB_MIN = 20  # neighbour lemmas must occur this often in the corpus
CONTENT_UPOS = frozenset({"NOUN", "VERB", "ADJ", "PROPN"})
DEFAULT_OUT = resources.derived_dir() / "sense_model.json"
LABEL_FILE = "dcs/sanskrit/dcs/data/conllu/lookup/word-senses.csv"


class Rec(NamedTuple):
    """One sense-annotated token with its context."""

    lemma: str
    labels: tuple[str, ...]
    ctx: senses.SenseContext
    book: str
    text: str


def sense_labels(path: Path) -> dict[str, str]:
    with open(path, encoding="utf-8", newline="") as fh:
        rows = csv.reader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        next(rows, None)
        return {r[0]: r[1] for r in rows if len(r) > 1}


def labels_of(word_sem: str, names: dict[str, str]) -> tuple[str, ...]:
    """The distinct sense labels of a ``WordSem`` field (comma-separated ids)."""
    out = [names[i] for i in word_sem.split(",") if i in names]
    return tuple(dict.fromkeys(out))


def read_split(entries: Iterable[dict], names: dict[str, str], keep_text: bool = False
               ) -> tuple[list[Rec], Counter, Counter]:
    """(annotated tokens with contexts, lemma counts, content-token counts per (book, lemma))."""
    recs: list[Rec] = []
    lemmas: Counter = Counter()
    content: Counter = Counter()
    for entry in entries:
        path, span = entry["file"], entry.get("verses")
        book = devanagari(Path(path).parent.name.lower(), "iast")
        for sent in dcs.iter_sentences(path):
            if span and not span[0] <= sent["sent_counter"] <= span[1]:
                continue
            toks = sent["tokens"]
            slots = [senses.slot_of_token(t) for t in toks]
            for i, tok in enumerate(toks):
                lemmas[slots[i].lemma] += 1
                if tok["upos"] in CONTENT_UPOS:
                    content[(book, slots[i].lemma)] += 1
                labels = labels_of(tok["word_sem"], names) if tok["word_sem"] else ()
                if labels:
                    recs.append(Rec(slots[i].lemma, labels, senses.context_at(slots, i), book,
                                    sent["text"] if keep_text else ""))
    return recs, lemmas, content


def _weights(labels: tuple[str, ...]) -> Iterator[tuple[str, float]]:
    for lab in labels:
        yield lab, 1.0 / len(labels)


def _num(x: float) -> float | int:
    x = round(x, 2)
    return int(x) if x == int(x) else x


def build_model(recs: Iterable[Rec], lemma_count: Counter, gloss: Callable[[str], str],
                min_occ: int = MIN_OCCURRENCES, min_label: float = MIN_LABEL,
                min_feat: float = MIN_FEATURE, vocab_min: int = VOCAB_MIN) -> dict[str, Any]:
    """The model table from training tokens (pure; see mayur.senses for the meaning of the parts)."""
    recs = list(recs)
    counts: dict[str, Counter] = defaultdict(Counter)
    for r in recs:
        for lab, w in _weights(r.labels):
            counts[r.lemma][lab] += w
    top = {lm: max(c, key=lambda lab: (c[lab], lab)) for lm, c in counts.items()}
    keep: dict[str, dict[str, float]] = {}
    for lm, c in counts.items():
        labels = {lab: n for lab, n in c.items() if n >= min_label}
        if sum(c.values()) >= min_occ and len(labels) >= 2:
            keep[lm] = labels
    vocab = {lm for lm, n in lemma_count.items() if n >= vocab_min}
    feats: dict[str, dict[str, Counter]] = {lm: defaultdict(Counter) for lm in keep}
    for r in recs:
        if r.lemma not in keep:
            continue
        names = senses.features(r.ctx, top, vocab)
        for lab, w in _weights(r.labels):
            if lab in keep[r.lemma]:
                for f in names:
                    feats[r.lemma][f][lab] += w
    lemmas = {}
    for lm, labels in keep.items():
        table = {f: {lab: _num(n) for lab, n in c.items()} for f, c in feats[lm].items() if sum(c.values()) >= min_feat}
        lemmas[lm] = {"p": {lab: _num(n) for lab, n in labels.items()}, "f": table}
    used = {lab for e in lemmas.values() for lab in e["p"]}
    return {"version": 1, "params": dict(senses.DEFAULT_PARAMS), "top": top, "lemmas": lemmas,
            "gloss": {lab: gloss(lab) for lab in sorted(used)},
            "stats": {"lemmas": len(lemmas), "annotated_tokens": len(recs)}}


def predict(model: dict, rec: Rec) -> tuple[str, str]:
    """(baseline label, model label) of one token; "" when the lemma has no label at all."""
    base = model["top"].get(rec.lemma, "")
    if rec.lemma in model["lemmas"]:
        return base, senses.choose(rec.lemma, rec.ctx, model)[0]
    return base, base


def grade(model: dict, recs: Iterable[Rec]) -> dict[str, Counter]:
    """Per book (and "all"): counts of tokens and hits for baseline and model, ambiguous and all."""
    out: dict[str, Counter] = defaultdict(Counter)
    for r in recs:
        base, pred = predict(model, r)
        gold = set(r.labels)
        for key in (r.book, "all"):
            c = out[key]
            c["n"] += 1
            c["base"] += base in gold
            c["model"] += pred in gold
            if r.lemma in model["lemmas"]:
                c["amb_n"] += 1
                c["amb_base"] += base in gold
                c["amb_model"] += pred in gold
    return out


def tune(model: dict, recs: list[Rec]) -> dict[str, Any]:
    """Pick the smoothing constant and group weights that give the best accuracy on ``recs``."""
    amb = [r for r in recs if r.lemma in model["lemmas"]]
    best, best_hits = dict(senses.DEFAULT_PARAMS), -1
    for k, bag, own in product((0.01, 0.05, 0.15, 0.5), (0.05, 0.1, 0.2, 0.4, 0.7), (0.3, 0.6, 1.0)):
        params = {"k": k, "weights": {"w": bag, "s": bag, "g": own, "u": own, "m": own, "n": own, "p": own, "v": own}}
        trial = {**model, "params": params}
        hits = sum(predict(trial, r)[1] in set(r.labels) for r in amb)
        if hits > best_hits:
            best, best_hits = params, hits
    return best


def pct(hits: int, n: int) -> str:
    return f"{100 * hits / n:5.1f}%" if n else "  n/a "


def report(name: str, model: dict, recs: list[Rec], content: Counter) -> None:
    print(f"\n== {name} ==")
    for book, c in sorted(grade(model, recs).items(), key=lambda kv: (kv[0] == "all", kv[0])):
        print(f"{book:<14} ambiguous n={c['amb_n']:5d} baseline {pct(c['amb_base'], c['amb_n'])} model "
              f"{pct(c['amb_model'], c['amb_n'])} | all annotated n={c['n']:5d} baseline {pct(c['base'], c['n'])} "
              f"model {pct(c['model'], c['n'])}")
    total = sum(content.values())
    any_label = sum(n for (_, lm), n in content.items() if lm in model["top"])
    modelled = sum(n for (_, lm), n in content.items() if lm in model["lemmas"])
    print(f"coverage of {total} content tokens: any sense label {pct(any_label, total)}, "
          f"context-chosen (ambiguous lemma) {pct(modelled, total)}")


def changed_examples(model: dict, recs: list[Rec], top_n: int = 15) -> None:
    """Lemmas where context changes the choice most often, with two examples each."""
    changes: Counter = Counter()
    shown: dict[str, list[str]] = defaultdict(list)
    for r in recs:
        base, pred = predict(model, r)
        if r.lemma in model["lemmas"] and pred != base:
            changes[r.lemma] += 1
            if len(shown[r.lemma]) < 2 and r.text:
                mark = "ok" if pred in r.labels else "wrong"
                shown[r.lemma].append(f"    {r.text}  gold={'/'.join(r.labels)} baseline={base} model={pred} ({mark})")
    print(f"\n== {top_n} most frequent lemmas where context changes the choice (dev_pool+dev+test) ==")
    for lm, n in changes.most_common(top_n):
        print(f"{lm}  changed {n}x")
        print("\n".join(shown[lm]))


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--eval-only", action="store_true", help="measure the existing table, do not rebuild")
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)
    names = sense_labels(resources.data_dir() / LABEL_FILE)
    pool, _, _ = read_split(dcs.split_files("dev_pool") + dcs.split_files("dev"), names)
    if args.eval_only:
        model = json.loads(args.out.read_text(encoding="utf-8"))
    else:
        from mayur import gloss

        train, lemma_count, _ = read_split(dcs.split_files("train"), names)
        model = build_model(train, lemma_count, lambda lab: gloss.first_sense(lab) or lab)
        del train
        model["params"] = tune(model, pool)
        args.out.write_text(json.dumps(model, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        size = args.out.stat().st_size
        feats = sum(len(e["f"]) for e in model["lemmas"].values())
        print(f"wrote {args.out}: {size / 1e6:.2f} MB, {len(model['lemmas'])} ambiguous lemmas, {feats} features, "
              f"params {model['params']}")
    shown: list[Rec] = []
    for name in ("dev", "test"):
        recs, _, content = read_split(dcs.split_files(name), names, keep_text=True)
        report(name, model, recs, content)
        shown += recs
    pool_text, _, _ = read_split(dcs.split_files("dev_pool"), names, keep_text=True)
    changed_examples(model, pool_text + shown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
