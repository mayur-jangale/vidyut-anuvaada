"""Build data/derived/freq.json and dcs_dict.json from the DCS Ramayana files."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import resources  # noqa: E402
from mayur.dcs import iter_sentences, pada_form  # noqa: E402
from mayur.translit import iast_to_slp1  # noqa: E402

HELD_OUT = ["Rām, Bā, 1"]



def build(data_dir: Path) -> dict:
    base = data_dir / "dcs" / "sanskrit" / "dcs" / "data" / "conllu"
    files = sorted((base / "files" / "Rāmāyaṇa").glob("*.conllu"))
    if not files:
        raise FileNotFoundError(f"no Ramayana files under {base}")
    forms: Counter = Counter()
    lemmas: Counter = Counter()
    skipped = 0
    for fp in files:
        for sent in iter_sentences(fp):
            if sent["chapter"] in HELD_OUT:
                skipped += 1
                continue
            for t in sent["tokens"]:
                forms[pada_form(t["unsandhied"], t["lemma"])] += 1
                lemmas[t["lemma"]] += 1
    out = data_dir / "derived"
    out.mkdir(parents=True, exist_ok=True)
    freq = {"forms": dict(forms), "lemmas": dict(lemmas),
            "tokens": sum(forms.values()), "held_out": HELD_OUT}
    (out / "freq.json").write_text(json.dumps(freq, ensure_ascii=False), encoding="utf-8")

    d: dict[str, list] = {}
    with open(base / "lookup" / "dictionary.csv", encoding="utf-8", newline="") as f:
        rd = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE)
        next(rd, None)
        for row in rd:
            if len(row) < 5:
                row = row + [""] * (5 - len(row))
            d.setdefault(iast_to_slp1(row[1]), []).append(
                {"grammar": row[2], "preverbs": row[3], "meanings": row[4]})
    (out / "dcs_dict.json").write_text(json.dumps(d, ensure_ascii=False), encoding="utf-8")
    return {"files": len(files), "held_out_sentences": skipped, "tokens": freq["tokens"],
            "forms": len(forms), "lemmas": len(lemmas), "dict_lemmas": len(d)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", type=Path, default=None)
    a = ap.parse_args()
    stats = build(a.data_dir or resources.data_dir())
    for k, v in stats.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
