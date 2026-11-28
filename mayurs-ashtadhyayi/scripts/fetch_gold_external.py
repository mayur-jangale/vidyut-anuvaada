"""Fetch the openly licensed gold treebanks into data/gold_external/ (git-ignored).

    python scripts/fetch_gold_external.py [--only ufal vedic] [--dcs-index]

Research result (checked 2026-11-26 by reading the sources named; nothing here is from memory):

| dataset | licence | size | usable? |
|---|---|---|---|
| UD_Sanskrit-UFAL (github.com/UniversalDependencies/UD_Sanskrit-UFAL) | CC BY-SA 4.0 | 230 sentences (sa_ufal-ud-test.conllu, 425 kB), Pancatantra preface + Mitrabheda start; Devanagari | YES, fetched. UD labels (nsubj obj obl nmod amod ...), manual; surface (sandhied) words, compounds split into members (Compound=Yes) |
| UD_Sanskrit-Vedic (github.com/UniversalDependencies/UD_Sanskrit-Vedic) | CC BY-SA 4.0 | 27,182 sentences, 206,440 non-punctuation tokens counted from the fetched v2 files (the README's "4,000 sentences" is outdated; train 24 MB, dev 3.5 MB, test 3 MB); IAST | YES, fetched, but Vedic prose/hymns (RV, SS, MS, AB, SB): a domain-shift check, not our target; UD labels with Sanskrit subtypes (obl:instr obl:source obl:loc advcl:tcl ...); words are padapatha (Unsandhied in MISC) |
| DCS dependency chapters (data/dcs, CC BY 4.0, Hellwig) | CC BY 4.0 | 884 sentences / 8,455 tokens in 48 chapter files: Mahabharata 519, Manusmrti 210, Buddhacarita 100, Ramayana 50, Visnupurana 4, Matsyapurana 1 | YES, already local (--dcs-index lists the files). Same label set as UD-Vedic; classical epic/dharma text = our target; padapatha forms + lemmas |
| Hyderabad Sanskrit Consortium gold data (sanskrit.uohyd.ac.in/scl/GOLD_DATA: Dependency_analysis/*.txt karaka-tagged stories and sentences ~0.9 MB, samAsa_WX.txt 1.2 MB compound-tagged, POS.tgz) | file `copyright`: use must be acknowledged AND "the receiver of this data will not distribute it to others" | not counted | NO: not an open licence, redistribution barred. NOT fetched. Would map directly (karaka tags) and has compound types (T6, K1, Bv, Di ... in WX); the owner may ask Amba Kulkarni for permission |
| STBC (Sanskrit Treebank Corpus, ~3,000 sentences per Kulkarni et al. 2020, karaka labels) | unknown | ~3,000 sentences | NO: no download location or licence found; not fetched |
| SaCTI compound types (github.com/ashishgupta2598/SaCTI, COLING 2022; data/{coling,english,marathi,sacti}) | none found (no LICENSE at repo root, 404) | not checked | NO: unclear licence, so not fetched. DepNeCTI repo (yaswanth-iitkgp) not reachable at the guessed URL |
| IIT Kharagpur / other samasa sets | not found | - | NOT verified |

No usable open compound-TYPE dataset exists among these. UD gives only a weak proxy
(compound:coord / conj inside a compound -> dvandva; see eval/eval_compounds.py).
Each fetched file is recorded with URL, licence, sha256 in data/gold_external/SOURCES.json.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from mayur import treebank  # noqa: E402

RAW = "https://raw.githubusercontent.com/UniversalDependencies"
DATASETS = {
    "ufal": {"dir": "ud_sanskrit_ufal", "licence": "CC BY-SA 4.0", "home": "https://github.com/UniversalDependencies/UD_Sanskrit-UFAL",
             "attribution": "UD_Sanskrit-UFAL: Dwivedi, Zeman, Biagetti (Charles University, UFAL)",
             "files": {"sa_ufal-ud-test.conllu": f"{RAW}/UD_Sanskrit-UFAL/master/sa_ufal-ud-test.conllu"}},
    "vedic": {"dir": "ud_sanskrit_vedic", "licence": "CC BY-SA 4.0", "home": "https://github.com/UniversalDependencies/UD_Sanskrit-Vedic",
              "attribution": "UD_Sanskrit-Vedic: Scarlata, Ackermann, Hellwig, Biagetti, Widmer, Sellmer",
              "files": {f"sa_vedic-ud-{part}.conllu": f"{RAW}/UD_Sanskrit-Vedic/master/sa_vedic-ud-{part}.conllu"
                        for part in ("test", "dev", "train")}},
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def download(url: str, timeout: int = 120) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as resp:  # honours the proxy environment
        return resp.read()


def manifest_entry(name: str, filename: str, url: str, data: bytes, spec: dict) -> dict:
    return {"dataset": name, "file": f"{spec['dir']}/{filename}", "url": url, "licence": spec["licence"],
            "home": spec["home"], "attribution": spec["attribution"], "bytes": len(data), "sha256": sha256(data),
            "fetched": time.strftime("%Y-%m-%d", time.gmtime())}


def fetch(name: str, root: Path) -> list[dict]:
    spec, entries = DATASETS[name], []
    (root / spec["dir"]).mkdir(parents=True, exist_ok=True)
    for filename, url in spec["files"].items():
        data = download(url)
        (root / spec["dir"] / filename).write_bytes(data)
        entries.append(manifest_entry(name, filename, url, data, spec))
    return entries


def write_manifest(root: Path, entries: list[dict]) -> None:
    path = root / "SOURCES.json"
    old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    keep = [e for e in old if e["file"] not in {x["file"] for x in entries}]
    path.write_text(json.dumps(keep + entries, ensure_ascii=False, indent=1), encoding="utf-8")


def write_dcs_index(root: Path) -> int:
    """List the DCS chapter files that carry HEAD/DEPREL (relative to the DCS files directory)."""
    names = sorted(str(p.relative_to(treebank.DCS_FILES)) for p in treebank.dcs_dependency_files(index=root / "none"))
    (root / treebank.DCS_INDEX.name).write_text(json.dumps(names, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(names)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", nargs="*", choices=sorted(DATASETS), default=sorted(DATASETS))
    ap.add_argument("--dcs-index", action="store_true", help="index the DCS chapters that carry dependencies")
    args = ap.parse_args(argv)
    root = treebank.EXTERNAL
    root.mkdir(parents=True, exist_ok=True)
    entries: list[dict] = []
    for name in args.only:
        try:
            entries += fetch(name, root)
            print(f"{name}: fetched {len(DATASETS[name]['files'])} file(s), {DATASETS[name]['licence']}")
        except OSError as exc:
            print(f"{name}: NOT fetched ({exc})", file=sys.stderr)
    write_manifest(root, entries)
    if args.dcs_index:
        print(f"dcs: {write_dcs_index(root)} chapter files with dependencies indexed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
