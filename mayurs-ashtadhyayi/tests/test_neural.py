"""Neural context model: API shape, determinism, a small training smoke test (skipped without torch)."""

from __future__ import annotations

import pytest

from mayur import neural

torch = pytest.importorskip("torch")


def test_targets_and_classes():
    assert neural.targets("NOUN", {"Case": "Nom", "Number": "Sing", "Gender": "Masc"}, False)["Class"] == "nominal"
    t = neural.targets("ADV", {"Case": "Acc"}, False)
    assert t["Case"] == "none" and t["Class"] == "indecl"
    assert neural.targets("NOUN", {}, True)["Case"] == "Cpd"
    assert neural.word_class({"Tense": "Pres", "Mood": "Ind"}) == "finite"


def _toy():
    cfg = {**neural.DEFAULT_CONFIG, "buckets": 101, "hidden": 16, "conv_dim": 16, "form_dim": 8, "sound_dim": 8}
    forms = ["रामस्", "वनम्", "गच्छति"]
    sounds = [neural.PAD, neural.UNK] + sorted({s for f in forms for s in neural.sounds(f)})
    values = {h: ["none", "x"] for h in neural.HEADS}
    torch.manual_seed(0)
    model = neural.build_model(cfg, len(sounds), {h: 2 for h in values})
    model.eval()
    return model, {"config": cfg, "sounds": sounds, "values": values}, forms


def test_api_shape_and_determinism():
    model, meta, forms = _toy()
    a = neural.logprobs_with(model, meta, [(forms, [0, 0, 1], [False, False, False])])
    b = neural.logprobs_with(model, meta, [(forms, [0, 0, 1], [False, False, False])])
    assert a == b and len(a) == 1 and len(a[0]) == 3
    assert set(a[0][0]) == set(neural.HEADS) and set(a[0][0]["Case"]) == {"none", "x"}
    assert neural.candidate_score({}, a[0][0]) <= 0.0


def test_public_api_falls_back_without_model(monkeypatch):
    monkeypatch.setattr(neural, "_load", lambda *a: None)
    assert not neural.enabled()
    assert neural.feature_logprobs(["रामस्"], [0], [False]) == []
    assert neural.candidate_scores([[object()]], []) == [[0.0]]


def test_saved_model_shape():
    if not neural.enabled():
        pytest.skip("no saved neural model")
    out = neural.feature_logprobs(["रामस्", "वनम्", "गच्छति"], [0, 0, 1], [False, False, False])
    assert len(out) == 3 and "Case" in out[0]
    assert out == neural.feature_logprobs(["रामस्", "वनम्", "गच्छति"], [0, 0, 1], [False, False, False])


def test_training_smoke_loss_decreases():
    import sys
    from pathlib import Path

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
    import train_neural as tn

    data = tn.load_train(1)[:300] if tn.dcs.split_files("train") else []
    if len(data) < 50:
        pytest.skip("corpus not available")
    torch.manual_seed(0)
    cfg = {**neural.DEFAULT_CONFIG, "buckets": 2000, "hidden": 32, "conv_dim": 32, "form_dim": 16}
    sounds, values = tn.vocab(data)
    meta = {"config": cfg, "sounds": sounds, "values": values}
    model = neural.build_model(cfg, len(sounds), {h: len(v) for h, v in values.items()})
    opt = torch.optim.Adam(model.parameters(), lr=3e-3)
    loss_fn = torch.nn.CrossEntropyLoss(ignore_index=-100)
    six = {s: i for i, s in enumerate(sounds)}
    losses = []
    for epoch in range(3):
        tot = 0.0
        for b in tn.batches(data, 800, epoch):
            out = model(*neural.batch_tensors([(r["forms"], r["lines"], r["cpd"]) for r in b], six, cfg["buckets"]))
            y = tn.target_tensor(b, values)
            loss = sum(loss_fn(out[h].reshape(-1, out[h].shape[-1]), y[h].reshape(-1)) for h in values)
            opt.zero_grad()
            loss.backward()
            opt.step()
            tot += float(loss.detach())
        losses.append(tot)
    assert losses[-1] < losses[0]
    model.eval()
    assert len(neural.logprobs_with(model, meta, [(data[0]["forms"], data[0]["lines"], data[0]["cpd"])])[0]) == len(
        data[0]["forms"])
