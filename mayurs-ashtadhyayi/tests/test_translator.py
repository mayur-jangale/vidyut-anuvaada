"""The trained translator: tokenizer, input builder, degrade-cleanly check and a tiny overfit run."""

from __future__ import annotations

import importlib.util

import pytest

from mayur import translator, translator_input as ti, translator_prep as prep
from mayur.model import Morph, Reading, Word
from mayur.translator_vocab import Vocab, is_atomic, pretokens, train_vocab

HAS_TORCH = importlib.util.find_spec("torch") is not None


def _word(form, line=0, member=False, gloss="", **morph) -> Word:
    analyses = [Morph(form=form, lemma=morph.pop("lemma", form), **morph)] if morph else []
    return Word(form=form, line=line, start=0, end=0, in_compound=member, analyses=analyses, gloss=gloss)


def _reading() -> Reading:
    return Reading(words=[
        _word("राम", member=True, kind="stem", gloss="rama"),
        _word("वनम्", kind="subanta", lemma="वन", vibhakti="द्वितीया", vacana="एकवचन", linga="नपुंसकलिङ्ग",
              gloss="forest"),
        _word("गच्छति", line=1, kind="tinanta", lemma="गम्", lakara="लट्", purusha="प्रथमपुरुष",
              vacana="एकवचन", gloss="go"),
        _word("च", line=1, kind="avyaya", gloss="and"),
    ])


def test_pretokens_keep_spaces_and_punctuation():
    assert pretokens("Rāma, who went.") == ["Rāma", ",", "▁who", "▁went", "."]


def test_atomic_tags():
    assert all(is_atomic(t) for t in ("N3pm", "V.lat.3s", "V.lat.3s.pas", "<C>", "<L>", "K.क्त"))
    assert not any(is_atomic(t) for t in ("राम", "forest", "N"))


def test_vocab_roundtrip_and_json(tmp_path):
    texts = ["The king went to the forest.", "The forest was dark, and the king wept."] * 5
    vocab = train_vocab([["राम", "N1sm", "king"]] * 5, texts, size=120)
    ids = vocab.encode_text(texts[0])
    assert vocab.decode(ids) == texts[0]
    assert vocab.encode_source(["N1sm"]) == [vocab.index["N1sm"]]
    vocab.save(tmp_path / "v.json")
    again = Vocab.load(tmp_path / "v.json")
    assert again.encode_text(texts[1]) == vocab.encode_text(texts[1])


def test_unknown_characters_become_unk():
    vocab = train_vocab([], ["abc abc"], size=20)
    assert 3 in vocab.encode_text("xyz")


def test_input_form_a_has_stem_and_tag_only():
    assert ti.encode_reading(_reading(), "A") == [
        "राम", "<C>", "वन", "N2sn", "<L>", "गम्", "V.lat.3s", "च", "<AV>", "<L>"]


def test_input_form_b_adds_glosses():
    tokens = ti.encode_reading(_reading(), "B")
    assert tokens[:6] == ["राम", "<C>", "rama", "वन", "N2sn", "forest"]
    assert tokens.count(ti.LINE_END) == 2


def test_bad_form_is_refused():
    with pytest.raises(ValueError):
        ti.encode_reading(_reading(), "C")


def test_every_tag_is_atomic():
    assert all(is_atomic(t) for t in ti.special_tokens())


def test_dump_and_load_reading_give_the_same_input():
    reading = _reading()
    again = prep.load_reading(prep.dump_reading(reading))
    for form in ti.FORMS:
        assert ti.encode_reading(again, form) == ti.encode_reading(reading, form)


def test_unanalysed_word_is_kept_as_written():
    tokens = ti.encode_reading(Reading(words=[Word(form="अज्ञात", line=0, start=0, end=0)]), "A")
    assert tokens[:2] == ["अज्ञात", "<UNK>"]


def test_unavailable_degrades_cleanly(tmp_path):
    assert not translator.available(tmp_path)
    assert translator.meta(tmp_path) == {}
    if not translator.available():
        assert translator.translate(_reading()) is None
        assert translator.translate_many([_reading(), _reading()]) == ["", ""]


@pytest.mark.skipif(not HAS_TORCH, reason="torch is not installed")
def test_tiny_model_overfits_and_translates(tmp_path):
    import torch

    from mayur.translator_beam import beam_search
    from mayur.translator_model import Config, Seq2Seq

    torch.manual_seed(0)
    sources = [["राम", "N1sm", "king", "वन", "N2sn", "forest", "गम्", "V.lat.3s", "go", "<L>"],
               ["सीता", "N1sf", "queen", "गृह", "N2sn", "house", "गम्", "V.lat.3s", "go", "<L>"]]
    targets = ["The king goes to the forest.", "The queen goes to the house."]
    vocab = train_vocab(sources, targets, size=150)
    model = Seq2Seq(Config(vocab=len(vocab), d_model=32, heads=2, d_ff=64, enc_layers=1, dec_layers=1, dropout=0.0))
    src_ids = [vocab.encode_source(s) for s in sources]
    tgt_ids = [[1, *vocab.encode_text(t), 2] for t in targets]
    width_s, width_t = max(map(len, src_ids)), max(map(len, tgt_ids))
    src = torch.tensor([s + [0] * (width_s - len(s)) for s in src_ids])
    tgt = torch.tensor([t + [0] * (width_t - len(t)) for t in tgt_ids])
    opt = torch.optim.Adam(model.parameters(), lr=3e-3)
    for _ in range(150):
        model.train()
        logits = model(src, tgt[:, :-1])
        loss = torch.nn.functional.cross_entropy(logits.reshape(-1, logits.shape[-1]), tgt[:, 1:].reshape(-1),
                                                 ignore_index=0)
        opt.zero_grad()
        loss.backward()
        opt.step()
    out = beam_search(model, src, beam=3, max_len=20)
    assert [vocab.decode(o) for o in out] == targets
    assert float(loss.detach()) < 0.1


@pytest.mark.skipif(not HAS_TORCH, reason="torch is not installed")
def test_saved_model_loads_and_translates(tmp_path):
    import json

    import torch

    from mayur.translator_model import Config, Seq2Seq

    vocab = train_vocab([["राम", "N1sm", "king"]], ["The king."], size=60)
    config = Config(vocab=len(vocab), d_model=16, heads=2, d_ff=32, enc_layers=1, dec_layers=1)
    torch.save({k: v.half() for k, v in Seq2Seq(config).state_dict().items()}, tmp_path / translator.WEIGHTS)
    vocab.save(tmp_path / translator.VOCAB)
    (tmp_path / translator.META).write_text(json.dumps({"config": config.to_json(), "input_form": "A"}))
    assert translator.available(tmp_path)
    assert translator.input_form(tmp_path) == "A"
    out = translator.translate_tokens([ti.encode_reading(_reading(), "A")], beam=2, directory=tmp_path)
    assert len(out) == 1 and isinstance(out[0], str)
