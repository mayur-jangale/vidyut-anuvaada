"""Fetch all external data into data/ (idempotent).

    python scripts/fetch_data.py [--with-mw] [--data-dir DIR]

Steps: vidyut data, DCS sparse clone (Ramayana only), optional Monier-Williams
(licence unclear: local use only, never commit), then the derived tables.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

DCS_REPO = "https://github.com/OliverHellwig/sanskrit.git"
SPARSE = ["/dcs/data/conllu/files/Rāmāyaṇa/", "/dcs/data/conllu/lookup/", "/dcs/data/conllu/readme.md"]
MW_URL = "https://raw.githubusercontent.com/sanskrit-lexicon/csl-orig/master/v02/mw/mw.txt"


def say(msg: str) -> None:
    print(f"[fetch_data] {msg}", flush=True)


def fetch_vidyut(data: Path) -> None:
    target = data / "vidyut"
    if (target / "kosha").exists():
        say("vidyut: already present, skipping")
        return
    say("vidyut: downloading ...")
    import vidyut

    target.mkdir(parents=True, exist_ok=True)
    vidyut.download_data(str(target))
    if not (target / "kosha").exists():
        raise RuntimeError(f"vidyut download did not produce {target / 'kosha'}")


def _git(*args: str, cwd: Path) -> None:
    subprocess.run(["git", *args], cwd=cwd, check=True)


def fetch_dcs(data: Path) -> None:
    base = data / "dcs"
    repo = base / "sanskrit"
    files = repo / "dcs/data/conllu/files/Rāmāyaṇa"
    if files.exists() and any(files.glob("*.conllu")) and (repo / "dcs/data/conllu/lookup/dictionary.csv").exists():
        say("DCS: already present, skipping")
        return
    base.mkdir(parents=True, exist_ok=True)
    if not repo.exists():
        say("DCS: sparse clone ...")
        _git("clone", "--depth", "1", "--filter=blob:none", "--sparse", DCS_REPO, "sanskrit", cwd=base)
    say("DCS: sparse checkout ...")
    _git("-c", "core.quotepath=off", "sparse-checkout", "set", "--no-cone", *SPARSE, cwd=repo)
    if not any(files.glob("*.conllu")):
        raise RuntimeError(f"DCS checkout produced no Ramayana files in {files}")


def fetch_mw(data: Path) -> None:
    dest = data / "mw" / "mw.txt"
    if dest.exists():
        say("MW: already present, skipping")
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    part = dest.with_suffix(".part")
    say("MW: downloading (about 50 MB; local use only, never commit) ...")
    with urllib.request.urlopen(MW_URL) as r, open(part, "wb") as out:
        shutil.copyfileobj(r, out)
    part.rename(dest)


def build_tables(data: Path) -> None:
    from build_tables import build  # same directory

    say("tables: building ...")
    stats = build(data)
    say("tables: " + ", ".join(f"{k}={v}" for k, v in stats.items()))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--with-mw", action="store_true", help="also download Monier-Williams (optional)")
    ap.add_argument("--data-dir", type=Path, default=None)
    a = ap.parse_args()
    from mayur import resources

    data = (a.data_dir or resources.data_dir()).resolve()
    data.mkdir(parents=True, exist_ok=True)
    say(f"data dir: {data}")
    try:
        fetch_vidyut(data)
        fetch_dcs(data)
        if a.with_mw:
            fetch_mw(data)
        build_tables(data)
    except Exception as e:  # noqa: BLE001 - report and exit non-zero
        say(f"FAILED: {type(e).__name__}: {e}")
        return 1
    say("done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
