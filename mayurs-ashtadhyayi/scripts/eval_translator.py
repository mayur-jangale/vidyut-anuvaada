"""Score a trained translator and the baselines on Itihāsa DEV or TEST verses (BLEU, chrF).

    python scripts/eval_translator.py --tag b1 --form B --split dev --verses 1000 [--engine 300]
    python scripts/eval_translator.py --tag b1 --form B --split test --verses 1250 --export

Systems scored on the same verses: the model (beam search), a copy of the glosses in text order
and, with ``--engine N``, the full pipeline's own rule-built English (``reworded``) on the first
N of them (slow). ``--export`` writes the fp16 weights, the vocabulary and the JSON record to
mayur/models/. Hypotheses go to ``data/derived/translation/eval_<tag>_<split>.json``.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sacrebleu  # noqa: E402
import torch  # noqa: E402

from mayur import resources, translator_data as td, translator_input as ti  # noqa: E402
from mayur import translator_prep as prep  # noqa: E402
from mayur.translator_beam import beam_search  # noqa: E402
from mayur.translator_model import Config, Seq2Seq  # noqa: E402
from mayur.translator_vocab import Vocab  # noqa: E402
from train_translator import MODELS, export  # noqa: E402

DIACRITICS_NOTE = "t5 outputs are ASCII (no diacritics); compare on folded text with --fold"


def score(hyps: list[str], refs: list[str]) -> dict:
    return {"bleu": round(sacrebleu.corpus_bleu(hyps, [refs]).score, 2),
            "chrf": round(sacrebleu.corpus_chrf(hyps, [refs]).score, 2), "verses": len(hyps)}


def load(tag: str, form_cfg: dict | None = None):
    work = resources.derived_dir() / "translation" / tag
    vocab = Vocab.load(resources.derived_dir() / "translation" / "vocab.json")
    state = torch.load(work / "last.pt", weights_only=False)["state"]
    cfg = Config(**(form_cfg or json.loads((work / "config.json").read_text(encoding="utf-8"))))
    model = Seq2Seq(cfg)
    model.load_state_dict(torch.load(work / "best.pt", weights_only=True))
    return model.eval(), vocab, state


def translate_rows(model, vocab, rows: list, form: str, beam: int) -> list[str]:
    """English for each dumped reading (beam search, batches sorted by length)."""
    ids = [vocab.encode_source(ti.encode_reading(prep.load_reading(r), form))[:model.config.max_src] for r in rows]
    order = sorted(range(len(ids)), key=lambda i: len(ids[i]))
    out = [""] * len(ids)
    for start in range(0, len(order), 16):
        chunk = order[start:start + 16]
        width = max(len(ids[i]) for i in chunk)
        src = torch.tensor([ids[i] + [0] * (width - len(ids[i])) for i in chunk])
        for i, hyp in zip(chunk, beam_search(model, src, beam, model.config.max_tgt - 2)):
            out[i] = vocab.decode(hyp)
    return out


def translate_t5(tag: str, rows: list, beam: int) -> list[str]:
    """English from the adapter run ``tag`` (the base model is read from data/translator_base)."""
    from mayur import translator_t5 as t5

    work = resources.derived_dir() / "translation" / tag
    prompts = [t5.prompt_of(prep.load_reading(r)) for r in rows]
    return t5.translate_prompts(prompts, beam, 8, work)


def gloss_copy(rows: list) -> list[str]:
    """Baseline: the glosses of the words, in text order."""
    return [" ".join(prep.load_reading(r).words[k].gloss for k in range(len(r)) if r[k][3]) for r in rows]


def engine_english(sanskrit: list[str]) -> list[str]:
    """The full pipeline's own rule-built English (``reworded``, else the literal line)."""
    from mayur import pipeline

    out = []
    for text in sanskrit:
        readings = pipeline.analyze_verse(text, max_readings=1).readings
        out.append((readings[0].reworded or readings[0].translation) if readings else "")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--system", choices=("scratch", "t5"), default="scratch",
                    help="t5: the flan-t5-small + adapter run in <tag> (mayur.translator_t5)")
    ap.add_argument("--form", choices=ti.FORMS, default="B")
    ap.add_argument("--split", choices=("dev", "test"), default="dev")
    ap.add_argument("--verses", type=int, default=1000)
    ap.add_argument("--beam", type=int, default=4)
    ap.add_argument("--threads", type=int, default=2)
    ap.add_argument("--engine", type=int, default=0, help="also score the rule-built English on N verses")
    ap.add_argument("--fold", action="store_true", help="also score every system on diacritic-folded text")
    ap.add_argument("--export", action="store_true", help="write the weights and JSON to mayur/models/")
    args = ap.parse_args(argv)
    torch.set_num_threads(args.threads)
    model, vocab, state = load(args.tag) if args.system == "scratch" else (None, None, {})
    english, sanskrit = td.english_lines(args.split), td.read_lines(args.split, "sn")
    pairs = [(i, r) for i, r in td.load_verses(args.split) if r][:args.verses]
    rows, refs = [r for _, r in pairs], [english[i] for i, _ in pairs]
    start = time.time()
    hyps = (translate_rows(model, vocab, rows, args.form, args.beam) if args.system == "scratch"
            else translate_t5(args.tag, rows, args.beam))
    result = {"tag": args.tag, "form": args.form, "split": args.split, "model": score(hyps, refs),
              "gloss_copy": score(gloss_copy(rows), refs), "decode_seconds": round(time.time() - start, 1)}
    if args.engine:
        n = min(args.engine, len(pairs))
        eng = engine_english([sanskrit[i] for i, _ in pairs[:n]])
        result["engine"] = score(eng, refs[:n])
        result["model_on_engine_verses"] = score(hyps[:n], refs[:n])
        result["gloss_copy_on_engine_verses"] = score(gloss_copy(rows[:n]), refs[:n])
        result["engine_hyps"] = eng
    if args.fold:
        from mayur.translator_t5 import fold

        f_refs = [fold(r) for r in refs]
        result["model_folded"] = score([fold(h) for h in hyps], f_refs)
        result["gloss_copy_folded"] = score([fold(h) for h in gloss_copy(rows)], f_refs)
    result.update(ids=[i for i, _ in pairs], hyps=hyps, refs=refs)
    path = resources.derived_dir() / "translation" / f"eval_{args.tag}_{args.split}.json"
    path.write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
    sys.stdout.write(json.dumps({k: v for k, v in result.items() if k not in ("ids", "hyps", "refs", "engine_hyps")},
                                indent=1) + "\n")
    if args.export and args.system == "scratch":
        info = {"input_form": args.form, "config": model.config.to_json(), "state": state.get("log", [])[-3:],
                "dev_scores": result["model"] if args.split == "dev" else None}
        export(model, vocab, info, MODELS)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
