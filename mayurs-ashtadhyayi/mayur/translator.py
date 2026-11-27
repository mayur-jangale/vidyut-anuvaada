"""The trained translator: simplified Sanskrit (from the rule engine) to English, offline, on a CPU.

The engine undoes sandhi, splits compounds and gives each word its stem, grammar and gloss;
``encode_reading`` writes that as tokens (``mayur.translator_input``) and a small transformer
trained on the Itihāsa corpus (``scripts/train_translator.py``) turns them into English.
The output is machine translation: it can be free where the engine's literal line is traceable.

Without torch or without the weights in ``mayur/models/``, ``available()`` is False, ``translate``
returns None and nothing else in the package is affected. This module imports torch only inside
``_load``.
"""

from __future__ import annotations

import importlib.util
import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional, Sequence

from mayur import translator_input
from mayur.model import Reading

MODEL_DIR = Path(__file__).with_name("models")
WEIGHTS, META, VOCAB = "translator.pt", "translator.json", "translator_vocab.json"
BEAM, ALPHA = 4, 0.8
DEFAULT_FORM = "B"


def _files_present(directory: Path = MODEL_DIR) -> bool:
    return all((directory / name).exists() for name in (WEIGHTS, META, VOCAB))


def available(directory: Path = MODEL_DIR) -> bool:
    """True when torch is installed and the weights, vocabulary and their JSON are present."""
    return importlib.util.find_spec("torch") is not None and _files_present(directory)


def meta(directory: Path = MODEL_DIR) -> dict[str, Any]:
    """The JSON beside the weights (data revision, training command, sizes, DEV scores); {} if missing."""
    try:
        return json.loads((directory / META).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def input_form(directory: Path = MODEL_DIR) -> str:
    """The input form ("A" or "B") the saved model was trained on."""
    return meta(directory).get("input_form", DEFAULT_FORM)


def encode_reading(reading: Reading, form: Optional[str] = None) -> list[str]:
    """The model's input for ``reading``: tokens (stems, grammar tags, glosses), see ``translator_input``."""
    return translator_input.encode_reading(reading, form or input_form())


@lru_cache(maxsize=2)
def _load(directory: Path = MODEL_DIR):
    import torch

    from mayur.translator_model import Config, Seq2Seq
    from mayur.translator_vocab import Vocab

    info = meta(directory)
    model = Seq2Seq(Config(**info["config"]))
    state = torch.load(directory / WEIGHTS, map_location="cpu", weights_only=True)
    model.load_state_dict({k: v.float() for k, v in state.items()})
    model.eval()
    return model, Vocab.load(directory / VOCAB), info


def translate_tokens(token_lists: Sequence[Sequence[str]], beam: int = BEAM, batch: int = 16,
                     directory: Path = MODEL_DIR) -> list[str]:
    """English for each list of input tokens (batched, longest last to keep padding small)."""
    import torch

    from mayur.translator_beam import beam_search

    model, vocab, _ = _load(directory)
    limit = model.config.max_src
    ids = [vocab.encode_source(t)[:limit] for t in token_lists]
    order = sorted(range(len(ids)), key=lambda i: len(ids[i]))
    out = [""] * len(ids)
    for start in range(0, len(order), batch):
        chunk = order[start:start + batch]
        width = max((len(ids[i]) for i in chunk), default=1) or 1
        src = torch.tensor([ids[i] + [0] * (width - len(ids[i])) for i in chunk])
        hyps = beam_search(model, src, beam, model.config.max_tgt - 2, ALPHA)
        for i, hyp in zip(chunk, hyps):
            out[i] = vocab.decode(hyp)
    return out


def translate_many(readings: Sequence[Reading], beam: int = BEAM, form: Optional[str] = None) -> list[str]:
    """English for several readings; "" for each when the translator is not available or fails."""
    if not available():
        return ["" for _ in readings]
    try:
        return translate_tokens([encode_reading(r, form) for r in readings], beam)
    except Exception:  # a broken install must never break the caller
        return ["" for _ in readings]


def translate(reading: Reading, beam: int = BEAM) -> Optional[str]:
    """Machine translation of ``reading`` into English; None when torch or the weights are missing."""
    text = translate_many([reading], beam)[0]
    return text or None


def translate_verse(text: str, beam: int = BEAM) -> str:
    """Machine translation of a verse given as text, through the fast analysis path."""
    from mayur import translator_prep

    return translate(translator_prep.fast_reading(text), beam)
