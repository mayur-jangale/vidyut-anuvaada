"""Fetch every external data set into data/ (idempotent) and build the derived tables.

    python scripts/fetch_data.py [--with-mw] [--with-itihasa] [--with-translator-base] [--data-dir DIR]

* data/vidyut/      vidyut's own data (``vidyut.download_data``)
* data/dcs/sanskrit sparse clone of the Digital Corpus of Sanskrit (CC BY 4.0), Ramayana only
* data/mw/mw.txt    optional Monier-Williams; licence unclear, local only, never committed
* data/itihasa/      optional Itihasa corpus (Apache-2.0), pinned revision, for the trained translator
* data/translator_base/  optional pretrained base of the adapter translator (google/flan-t5-small, Apache-2.0)
* data/derived/     tables built by scripts/build_tables.py
"""

from __future__ import annotations

import argparse
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

DCS_REPO = "https://github.com/OliverHellwig/sanskrit.git"
# The revision every table, split and reported number was built from. Change it only together
# with a rebuild of data/derived and a fresh draw of the pools (see scripts/build_tables.py).
DCS_COMMIT = "8aeed5a1343d0e48b64eb32af8c00e8c6eb29359"
# Directory names of DCS texts (epic, kavya, purana, narrative, sastra). Everything fetched is
# counted into the frequency tables except the held-out chapters named in build_tables.py.
DCS_TEXTS = (
    "Mahābhārata", "Rāmāyaṇa", "Harivaṃśa", "Kumārasaṃbhava", "Kirātārjunīya", "Buddhacarita",
    "Meghadūta", "Bhāgavatapurāṇa", "Viṣṇupurāṇa", "Matsyapurāṇa", "Liṅgapurāṇa", "Kathāsaritsāgara",
    "Hitopadeśa", "Tantrākhyāyikā", "Manusmṛti", "Bodhicaryāvatāra", "Aṣṭāvakragīta", "Gītagovinda",
    "Saundarānanda", "Ṛtusaṃhāra", "Śatakatraya", "Yājñavalkyasmṛti", "Śukasaptati", "Vetālapañcaviṃśatikā",
)
DCS_PATHS = (*(f"/dcs/data/conllu/files/{t}/" for t in DCS_TEXTS),
             "/dcs/data/conllu/lookup/", "/dcs/data/conllu/readme.md")
# Itihasa (Aralikatte et al. 2021): 93,000 verses of the Ramayana and Mahabharata with M. N. Dutt's English.
ITIHASA_REVISION = "56645be151b61e1143597f922ccf666b43a5c02b"
ITIHASA_URL = "https://huggingface.co/datasets/rahular/itihasa/resolve/" + ITIHASA_REVISION + "/{name}"
ITIHASA_FILES = tuple(f"{split}.{lang}.csv" for split in ("train", "dev", "test") for lang in ("sn", "en"))
# The English-pretrained base the low-rank adapters of mayur/models/translator_t5_* are trained on.
BASE_MODEL = "google/flan-t5-small"
BASE_REVISION = "0fc9ddf78a1e988dac52e2dac162b0ede4fd74ab"
BASE_FILES = ("config.json", "generation_config.json", "model.safetensors", "special_tokens_map.json",
              "spiece.model", "tokenizer.json", "tokenizer_config.json")
MW_URL = "https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/mw/mw.txt"


def _git(args: list[str], cwd: Path | None = None) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True)


def fetch_vidyut(data_dir: Path) -> Path:
    target = data_dir / "vidyut"
    if (target / "kosha").exists():
        return target
    import vidyut

    target.mkdir(parents=True, exist_ok=True)
    vidyut.download_data(str(target))
    return target


def fetch_dcs(data_dir: Path) -> Path:
    target = data_dir / "dcs" / "sanskrit"
    if not (target / ".git").exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        _git(["clone", "--no-checkout", "--filter=blob:none", "--sparse", DCS_REPO, str(target)])
    _git(["sparse-checkout", "set", "--no-cone", *DCS_PATHS], cwd=target)
    head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=target, capture_output=True, text=True, check=True)
    if head.stdout.strip() != DCS_COMMIT:
        _git(["fetch", "--filter=blob:none", "origin", DCS_COMMIT], cwd=target)
        _git(["checkout", "--detach", DCS_COMMIT], cwd=target)
    return target


def fetch_mw(data_dir: Path) -> Path:
    target = data_dir / "mw" / "mw.txt"
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(MW_URL, timeout=120) as resp:  # noqa: S310 - fixed https URL
            target.write_bytes(resp.read())
    return target


def fetch_itihasa(data_dir: Path) -> Path:
    target = data_dir / "itihasa"
    target.mkdir(parents=True, exist_ok=True)
    for name in ITIHASA_FILES:
        if not (target / name).exists():
            with urllib.request.urlopen(ITIHASA_URL.format(name=name), timeout=300) as resp:  # noqa: S310 - fixed https URL
                (target / name).write_bytes(resp.read())
    return target


def fetch_translator_base(data_dir: Path) -> Path:
    target = data_dir / "translator_base" / BASE_MODEL.split("/")[1]
    target.mkdir(parents=True, exist_ok=True)
    for name in BASE_FILES:
        if not (target / name).exists():
            url = f"https://huggingface.co/{BASE_MODEL}/resolve/{BASE_REVISION}/{name}"
            with urllib.request.urlopen(url, timeout=600) as resp:  # noqa: S310 - fixed https URL
                (target / name).write_bytes(resp.read())
    return target


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--with-mw", action="store_true", help="also download Monier-Williams (local use only)")
    ap.add_argument("--with-itihasa", action="store_true",
                    help="also download the Itihasa corpus (for scripts/build_translation_data.py)")
    ap.add_argument("--with-translator-base", action="store_true",
                    help="also download google/flan-t5-small (pinned), the base of the adapter translator")
    ap.add_argument("--data-dir", type=Path, default=None)
    args = ap.parse_args(argv)
    if args.data_dir is None:
        from mayur.resources import data_dir
        args.data_dir = data_dir()
    data_dir = args.data_dir.resolve()
    data_dir.mkdir(parents=True, exist_ok=True)
    print("vidyut:", fetch_vidyut(data_dir))
    print("dcs:", fetch_dcs(data_dir))
    if args.with_mw:
        print("mw:", fetch_mw(data_dir))
    if args.with_itihasa:
        print("itihasa:", fetch_itihasa(data_dir))
    if args.with_translator_base:
        print("translator base:", fetch_translator_base(data_dir))
    from build_tables import build

    print("tables:", build(data_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
