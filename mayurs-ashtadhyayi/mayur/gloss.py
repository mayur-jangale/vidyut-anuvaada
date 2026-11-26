"""Short English glosses for words.

Order of sources: hand-written overrides, DCS dictionary (CC BY 4.0), vidyut dhatupatha
root gloss for verbal forms, Monier-Williams (optional, local data only, never committed).
"""

from __future__ import annotations

import json
import re
from functools import lru_cache
from pathlib import Path
from typing import Optional

from mayur.model import Morph
from mayur.resources import data_dir, derived_dir

_OVERRIDES = Path(__file__).with_name("annotations") / "gloss_overrides.json"
_MAX_LEN = 48


def first_sense(text: str, max_senses: int = 2, max_len: int = _MAX_LEN) -> str:
    """Reduce a ';'-separated meanings string to its first one or two clean senses."""
    text = re.sub(r"\[\[.*?\]\]", "", text or "")
    text = "; ".join(p for p in text.split(";") if not p.strip().startswith("["))
    text = re.sub(r"\[[^\]]*\]", "", text)
    text = re.sub(r"\([^)]*\)", "", text)
    parts = [re.sub(r"\s+", " ", p).strip(" ,.") for p in text.split(";")]
    parts = [p for p in parts if p]
    if not parts:
        return ""
    out = parts[0]
    if max_senses > 1 and len(parts) > 1 and len(out) + len(parts[1]) + 2 <= max_len:
        out = f"{out}, {parts[1]}"
    return out


@lru_cache(maxsize=1)
def _overrides() -> dict[str, str]:
    try:
        d = json.loads(_OVERRIDES.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return {k: v for k, v in d.items() if not k.startswith("_")}


@lru_cache(maxsize=1)
def _dcs_dict() -> dict[str, list[dict[str, str]]]:
    try:
        return json.loads((derived_dir() / "dcs_dict.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _is_verb_entry(e: dict[str, str]) -> bool:
    return bool(re.match(r"\s*\d", e.get("grammar", "")))


def _dcs_gloss(lemma: str, want_verb: bool) -> str:
    entries = _dcs_dict().get(lemma, [])
    for e in entries:
        if _is_verb_entry(e) != want_verb:
            continue
        if e["meanings"].startswith("[gramm.]"):
            continue
        g = first_sense(e["meanings"])
        if g:
            return g
    return ""


def _verb_lemmas(m: Morph) -> list[str]:
    cands = [m.lemma]
    if m.root:
        cands.append("".join(m.prefixes) + m.root)
        cands.append(m.root)
    seen: list[str] = []
    for c in cands:
        if c and c not in seen:
            seen.append(c)
    return seen


@lru_cache(maxsize=1)
def _mw() -> dict[str, str]:
    path = data_dir() / "mw" / "mw.txt"
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    k1: Optional[str] = None
    buf: list[str] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("<L>"):
                m = re.search(r"<k1>([^<]+)<", line)
                k1 = m.group(1) if m else None
                buf = []
            elif line.startswith("<LEND>"):
                if k1 and k1 not in out and buf:
                    g = _mw_first(" ".join(buf))
                    if g:
                        out[k1] = g
                k1 = None
            elif k1 is not None:
                buf.append(line.strip())
    return out


def _mw_first(raw: str) -> str:
    body = raw.split("¦", 1)[1] if "¦" in raw else raw
    body = re.sub(r"<ls>.*?</ls>|<lex>.*?</lex>|<info[^>]*/>|<s>.*?</s>", "", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = re.sub(r"\([^)]*\)", "", body)
    body = body.replace("‘", "").replace("’", "")
    parts = [p.strip(" .,") for p in re.split(r"[;,]", body)]
    parts = [p for p in parts if p and re.search(r"[A-Za-z]{3}", p) and not re.match(r"^[A-Z]{1,4}\.?$", p)]
    return first_sense("; ".join(parts[:2]), max_senses=2)


def _participle_note(m: Morph) -> str:
    if m.krt in ("kta", "ktavatu"):
        return "past participle"
    if m.krt in ("Sat", "Satf", "SAnac", "SAnan"):
        return "present participle"
    return "participle"


def lookup(m: Morph) -> tuple[str, str]:
    """Return (short English gloss, source name); ("", "none") if nothing is known."""
    ov = _overrides()
    verbal = m.is_verb or bool(m.root)
    for key in (m.lemma, m.root or ""):
        if key and key in ov and (key == m.lemma or m.is_verb):
            return ov[key], "override"
    if m.is_verb:
        for c in _verb_lemmas(m):
            g = _dcs_gloss(c, True)
            if g:
                return g, "dcs"
        if m.root_gloss:
            return m.root_gloss, "vidyut-dhatupatha"
    else:
        g = _dcs_gloss(m.lemma, False)
        if g:
            return g, "dcs"
        if verbal and m.root_gloss:
            return f"{m.root_gloss} ({_participle_note(m)})", "vidyut-dhatupatha"
        if verbal:
            for c in _verb_lemmas(m):
                g = _dcs_gloss(c, True)
                if g:
                    return f"{g} ({_participle_note(m)})", "dcs"
    g = _mw().get(m.lemma, "")
    if g:
        return g, "monier-williams"
    return "", "none"
