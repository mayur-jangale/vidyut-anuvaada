"""Variant C of the translator: a pretrained English seq2seq model (flan-t5-small) with LoRA adapters.

The input is form B of ``mayur.translator_input`` written as plain ASCII text (T5's vocabulary has
no Devanagari): stems transliterated and folded to ASCII, grammar tags, English glosses.
The base weights are fetched by ``scripts/fetch_data.py --with-translator-base``; only the adapters
(``mayur/models/translator_t5_lora.pt`` and its JSON) are committed. Needs the optional extra
``pip install -e ".[translate]"`` (torch, transformers, sentencepiece); without them or without the
files ``available()`` is False. Neither transformers nor torch is imported until a model is loaded.
"""

from __future__ import annotations

import importlib.util
import json
import re
import unicodedata
from functools import lru_cache
from pathlib import Path
from typing import Any, Sequence

from mayur import resources, translator_input as ti
from mayur.model import Reading

MODEL_DIR = Path(__file__).with_name("models")
ADAPTER, META = "translator_t5_lora.pt", "translator_t5.json"
BASE_NAME = "flan-t5-small"
TARGETS = ("q", "k", "v", "o", "wi_0", "wi_1", "wo")
PREFIX = "translate Sanskrit to English: "
READABLE = {"<C>": "cpd", "<L>": "/", "<AV>": "ind", "<UNK>": "unk"}
MAX_SRC, MAX_NEW = 256, 96
_DEVANAGARI = re.compile(r"[ऀ-ॿ]+")


def base_dir() -> Path:
    return resources.data_dir() / "translator_base" / BASE_NAME


def fold(text: str) -> str:
    """``text`` without diacritics (Vālmīki -> Valmiki): T5's vocabulary has no ā, ī, ṣ ..."""
    folded = unicodedata.normalize("NFD", text)
    return "".join(c for c in folded if not unicodedata.combining(c))


def ascii_of(text: str) -> str:
    """Devanagari ``text`` in plain ASCII (IAST without diacritics)."""
    from mayur import lipi

    return fold(lipi.iast(text))


def _token(token: str) -> str:
    """One input token as ASCII; in ``K.क्त`` only the Devanagari part is transliterated."""
    return READABLE.get(token) or fold(_DEVANAGARI.sub(lambda m: ascii_of(m.group(0)), token))


def prompt_of(reading: Reading) -> str:
    """The model's input text for ``reading`` (form B, ASCII)."""
    return PREFIX + " ".join(_token(t) for t in ti.encode_reading(reading, "B"))


def available(directory: Path = MODEL_DIR) -> bool:
    """True when torch, transformers and sentencepiece are installed and the base model and adapters exist."""
    mods = all(importlib.util.find_spec(m) is not None for m in ("torch", "transformers", "sentencepiece"))
    files = (directory / ADAPTER).exists() and (directory / META).exists()
    return mods and files and (base_dir() / "model.safetensors").exists()


def meta(directory: Path = MODEL_DIR) -> dict[str, Any]:
    try:
        return json.loads((directory / META).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


@lru_cache(maxsize=1)
def _load(directory: Path = MODEL_DIR):
    import torch
    from transformers import AutoTokenizer, T5ForConditionalGeneration

    from mayur.translator_lora import add_lora, load_adapter

    info = meta(directory)
    tok = AutoTokenizer.from_pretrained(str(base_dir()))
    model = T5ForConditionalGeneration.from_pretrained(str(base_dir()))
    add_lora(model, TARGETS, info.get("rank", 16), info.get("alpha", 32.0), 0.0)
    load_adapter(model, torch.load(directory / ADAPTER, map_location="cpu", weights_only=True))
    return model.eval(), tok


def translate_prompts(prompts: Sequence[str], beam: int = 4, batch: int = 8,
                      directory: Path = MODEL_DIR) -> list[str]:
    import torch

    model, tok = _load(directory)
    order = sorted(range(len(prompts)), key=lambda i: len(prompts[i]))
    out = [""] * len(prompts)
    with torch.no_grad():
        for start in range(0, len(order), batch):
            chunk = order[start:start + batch]
            enc = tok([prompts[i] for i in chunk], return_tensors="pt", padding=True, truncation=True,
                      max_length=MAX_SRC)
            gen = model.generate(**enc, num_beams=beam, max_new_tokens=MAX_NEW, no_repeat_ngram_size=3)
            for i, text in zip(chunk, tok.batch_decode(gen, skip_special_tokens=True)):
                out[i] = text.strip()
    return out


def translate_many(readings: Sequence[Reading], beam: int = 4) -> list[str]:
    """English for several readings; "" for each when the variant is not available."""
    if not available():
        return ["" for _ in readings]
    return translate_prompts([prompt_of(r) for r in readings], beam)


def translate(reading: Reading, beam: int = 4) -> str:
    return translate_many([reading], beam)[0]
