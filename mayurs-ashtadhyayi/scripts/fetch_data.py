"""Fetch every external data set into data/ (idempotent) and build the derived tables.

    python scripts/fetch_data.py [--with-mw] [--data-dir DIR]

* data/vidyut/      vidyut's own data (``vidyut.download_data``)
* data/dcs/sanskrit sparse clone of the Digital Corpus of Sanskrit (CC BY 4.0), Ramayana only
* data/mw/mw.txt    optional Monier-Williams; licence unclear, local only, never committed
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
# The Ramayana feeds the frequency tables; the Kumarasambhava is fetched only as an unseen
# second book for evaluation and is never counted.
DCS_PATHS = ("/dcs/data/conllu/files/Rāmāyaṇa/", "/dcs/data/conllu/files/Kumārasaṃbhava/",
             "/dcs/data/conllu/lookup/", "/dcs/data/conllu/readme.md")
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
        _git(["clone", "--depth", "1", "--filter=blob:none", "--sparse", DCS_REPO, str(target)])
    _git(["sparse-checkout", "set", "--no-cone", *DCS_PATHS], cwd=target)
    return target


def fetch_mw(data_dir: Path) -> Path:
    target = data_dir / "mw" / "mw.txt"
    if not target.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(MW_URL, timeout=120) as resp:  # noqa: S310 - fixed https URL
            target.write_bytes(resp.read())
    return target


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--with-mw", action="store_true", help="also download Monier-Williams (local use only)")
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
    from build_tables import build

    print("tables:", build(data_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
