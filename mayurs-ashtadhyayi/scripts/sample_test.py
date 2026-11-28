"""Draw a random sample of never-tested verses from a chapter pool.

    python scripts/sample_test.py --pool sealed_test --n 200 --label run1
    python scripts/sample_test.py --pool dev_pool --n 100 --label dev1 [--seed 3]

A verse is every half-verse of one chapter with the same sent_counter. Verses with an empty or
placeholder token, or with a half-verse longer than 60 syllables, are never drawn. The sealed_test
pool keeps a ledger (eval/sealed_ledger.json): a verse listed there is never drawn again, and the
newly drawn ids are appended under the label with a UTC timestamp. dev_pool never touches the ledger.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Optional

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from mayur import dcs, gold  # noqa: E402
from mayur.lipi import devanagari, varnas  # noqa: E402

LEDGER = ROOT / "eval" / "sealed_ledger.json"
SAMPLES = ROOT / "eval" / "samples"
MAX_SYLLABLES = 60
_NOT_VOWELS = frozenset({"ं", "ः", "ऽ", "ँ", " "})


def syllables(text: str) -> int:
    """Number of vowels in a Devanagari text."""
    return sum(1 for v in varnas(text) if v not in _NOT_VOWELS and not v.endswith("्"))


def verse_ok(sentences: list[dict]) -> bool:
    """No empty/placeholder token, no half-verse beyond 60 syllables."""
    for s in sentences:
        if not s["tokens"] or syllables(s["text"]) > MAX_SYLLABLES:
            return False
        if any(not t["form"] or not t["lemma"] or t["form"] == "_" for t in s["tokens"]):
            return False
    return True


def chapter_verses(path: str | Path) -> list[tuple[str, str, list[dict]]]:
    """(ledger id "chapter_id.verse", book directory name, sentences) of the eligible verses of a chapter."""
    by_verse: dict[int, list[dict]] = defaultdict(list)
    for s in dcs.iter_sentences(path):
        by_verse[s["sent_counter"]].append(s)
    book = Path(path).parent.name
    return [(f"{sents[0]['chapter_id']}.{n}", book, sents) for n, sents in sorted(by_verse.items())
            if verse_ok(sents)]


def draw(candidates: list[Any], n: int, seed: int, exclude: Iterable[str] = ()) -> list[Any]:
    """``n`` candidates (tuples whose first item is the verse id) chosen uniformly, never one of ``exclude``."""
    banned = set(exclude)
    rest = sorted((c for c in candidates if c[0] not in banned), key=lambda c: c[0])
    return random.Random(seed).sample(rest, min(n, len(rest)))


def read_ledger(path: Path = LEDGER) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"draws": []}


def ledger_ids(ledger: dict[str, Any]) -> set[str]:
    return {i for d in ledger["draws"] for i in d["ids"]}


def sample_document(chosen: list[tuple[str, str, list[dict]]], pool: str, label: str, seed: int) -> dict[str, Any]:
    verses = []
    for ledger_id, book, sents in chosen:
        chapter = ledger_id.split(".")[0]
        number = sents[0]["sent_counter"]
        label_dev = f"{devanagari(book.lower(), 'iast')} {devanagari(chapter, 'iast')}"
        verse = gold.build(sents, chapter_id=None, label=label_dev)["verses"][0]
        verses.append({**verse, "ledger_id": ledger_id, "book": devanagari(book.lower(), "iast"),
                       "text_name": book, "number": number})
    return {"source": "Digital Corpus of Sanskrit (Oliver Hellwig)", "license": gold.LICENSE, "pool": pool,
            "label": label, "seed": seed, "verses": verses}


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pool", choices=("sealed_test", "dev_pool"), required=True)
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--ledger", type=Path, default=LEDGER)
    ap.add_argument("--out-dir", type=Path, default=SAMPLES)
    args = ap.parse_args(argv)
    out = args.out_dir / f"{args.label}.json"
    ledger = read_ledger(args.ledger)
    if out.exists() or any(d["label"] == args.label for d in ledger["draws"]):
        print(f"label {args.label!r} already used; refusing to overwrite", file=sys.stderr)
        return 1
    seed = args.seed if args.seed is not None else random.SystemRandom().randrange(2**31)
    sealed = args.pool == "sealed_test"
    candidates = [v for e in dcs.split_files(args.pool, final_test=args.pool == dcs.SEALED) for v in chapter_verses(e["file"])]
    chosen = draw(candidates, args.n, seed, ledger_ids(ledger) if sealed else ())
    doc = sample_document(chosen, args.pool, args.label, seed)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    if sealed:
        ledger["draws"].append({"label": args.label, "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                "ids": [c[0] for c in chosen]})
        args.ledger.write_text(json.dumps(ledger, ensure_ascii=False, indent=1), encoding="utf-8")
    words = sum(len(ln["words"]) for v in doc["verses"] for ln in v["lines"])
    print(f"{args.pool}: {len(candidates)} eligible verses, drew {len(chosen)} ({words} words) -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
