"""Analyse the Itihāsa verses into the translator's input, in resumable shards.

    python scripts/build_translation_data.py [--workers 2] [--train-shards 60] [--dev-shards 4]
                                             [--test-shards 5] [--time-limit-min N] [--bench 200]

Needs ``scripts/fetch_data.py --with-itihasa``. Each shard holds 250 verses of one split, taken in a
fixed random order (so any prefix of the shards is a random sample), written to
``data/derived/translation/shards/<split>_<k>.jsonl`` once complete; a finished shard is never redone.
The work order is dev, train, test, so a first model can be trained while the rest is built.
The analysis is the fast path of ``mayur.translator_prep`` (split ranker, analyses, tagger, gloss).
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import resource
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import resources, translator_data as td  # noqa: E402

MEMORY_LIMIT = 9_000_000 * 1024  # bytes of address space per process


def ids_file(split: str) -> Path:
    return resources.derived_dir() / "translation" / f"ids_{split}.json"


def plan_ids(split: str) -> list[int]:
    """The split's verse order (written once so that every worker sees the same one)."""
    path = ids_file(split)
    if not path.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(td.corpus_ids(split)), encoding="utf-8")
    return json.loads(path.read_text(encoding="utf-8"))


def _init_worker() -> None:
    resource.setrlimit(resource.RLIMIT_AS, (MEMORY_LIMIT, MEMORY_LIMIT))


def build_shard(job: tuple[str, int]) -> tuple[str, int, int, float]:
    """Analyse shard ``k`` of ``split``; returns (split, k, verses failed, seconds)."""
    from mayur import translator_prep as prep

    split, k = job
    start = time.time()
    ids = plan_ids(split)[k * td.SHARD_SIZE:(k + 1) * td.SHARD_SIZE]
    lines = td.read_lines(split, "sn")
    path = td.shard_path(split, k)
    path.parent.mkdir(parents=True, exist_ok=True)
    failed = 0
    tmp = path.with_suffix(".tmp")
    with open(tmp, "w", encoding="utf-8") as out:
        for i in ids:
            try:
                rows = prep.dump_reading(prep.fast_reading(lines[i]))
            except Exception as err:  # a verse the engine chokes on stays in the shard, empty
                rows, failed = [], failed + 1
                sys.stderr.write(f"{split} {i}: {type(err).__name__}: {err}\n")
            out.write(json.dumps({"i": i, "r": rows}, ensure_ascii=False) + "\n")
    tmp.rename(path)
    return split, k, failed, time.time() - start


def work_plan(args: argparse.Namespace) -> list[tuple[str, int]]:
    """Shards still to build, in the order dev, train (first N), test, train (the rest)."""
    sizes = {s: -(-len(plan_ids(s)) // td.SHARD_SIZE) for s in ("train", "dev", "test")}
    first = min(args.train_shards, sizes["train"])
    order = ([("dev", k) for k in range(min(args.dev_shards, sizes["dev"]))]
             + [("train", k) for k in range(first)]
             + [("test", k) for k in range(min(args.test_shards, sizes["test"]))]
             + [("train", k) for k in range(first, min(args.max_train_shards, sizes["train"]))])
    return [job for job in order if not td.shard_path(*job).exists()]


def bench(count: int) -> None:
    """Seconds per verse of the fast path on ``count`` dev verses (a cold start, one process)."""
    from mayur import translator_prep as prep

    lines = td.read_lines("dev", "sn")
    ids = plan_ids("dev")[:count]
    start = time.time()
    for i in ids:
        prep.fast_reading(lines[i])
    sys.stdout.write(f"{count} verses in {time.time() - start:.1f} s\n")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--train-shards", type=int, default=60, help="train shards built before the test shards")
    ap.add_argument("--max-train-shards", type=int, default=60, help="train shards in all (300 = everything)")
    ap.add_argument("--dev-shards", type=int, default=4)
    ap.add_argument("--test-shards", type=int, default=5)
    ap.add_argument("--time-limit-min", type=float, default=0.0, help="stop starting shards after this long")
    ap.add_argument("--bench", type=int, default=0, help="time the fast path on N dev verses and exit")
    args = ap.parse_args(argv)
    if args.bench:
        bench(args.bench)
        return 0
    jobs = work_plan(args)
    sys.stdout.write(f"{len(jobs)} shards to build\n")
    deadline = time.time() + args.time_limit_min * 60 if args.time_limit_min else None
    ctx = mp.get_context("spawn")
    with ctx.Pool(args.workers, initializer=_init_worker, maxtasksperchild=2) as pool:
        for split, k, failed, secs in pool.imap(build_shard, _until(jobs, deadline)):
            sys.stdout.write(f"{split} {k}: {secs:.0f} s, {failed} failed\n")
            sys.stdout.flush()
    return 0


def _until(jobs: list[tuple[str, int]], deadline: float | None):
    for job in jobs:
        if deadline is not None and time.time() > deadline:
            return
        yield job


if __name__ == "__main__":
    raise SystemExit(main())
