"""Neural sound-level boundary model: label extraction, API shape, a tiny training smoke test."""

import pytest

from mayur import neural_boundary as nb
from mayur import segmenter


def _labels(line: str, words: list[tuple[str, bool]]) -> list[tuple[str, str]]:
    text, _ = segmenter._prepare(line)
    labels = nb.extract_labels(text, words)
    assert labels is not None
    return list(zip(text, labels))


def test_sandhi_altered_final_is_pada_boundary():
    got = _labels("श्वेतो धावति", [("श्वेतस्", False), ("धावति", False)])
    assert [l for _, l in got] == ["N", "N", "N", "N", "P", "N", "N", "N", "N", "N", "P"]
    assert got[4] == ("ओ", "P")


def test_fused_vowel_gets_fp():
    assert _labels("चैव", [("च", False), ("एव", False)]) == [("च्", "N"), ("ऐ", "FP"), ("व्", "N"), ("अ", "P")]


def test_compound_boundaries_and_fusion_inside_compound():
    got = _labels("तपःस्वाध्यायनिरतं", [("तपस्", True), ("स्वाध्याय", True), ("निरतम्", False)])
    assert [i for i, (_, l) in enumerate(got) if l != "N"] == [4, 12, 19]
    assert got[4] == ("ः", "C") and got[12] == ("अ", "C") and got[19][1] == "P"
    got = _labels("देवेन्द्रः", [("देव", True), ("इन्द्रस्", False)])
    assert got[3] == ("ए", "FC")


def test_elision_and_semivowel_are_not_fusion():
    assert [l for _, l in _labels("रामोऽपि", [("रामस्", False), ("अपि", False)])] == ["N", "N", "N", "P", "N", "N", "P"]
    assert _labels("इत्यपि", [("इति", False), ("अपि", False)])[2] == ("य्", "P")
    assert _labels("गच्छन्नत्र", [("गच्छन्", False), ("अत्र", False)])[6] == ("न्", "P")


def test_misaligned_gold_is_dropped():
    text, _ = segmenter._prepare("रामो गच्छति")
    assert nb.extract_labels(text, [("कृष्णस्", False), ("पठति", False)]) is None


def test_greedy_spans():
    assert nb.boundaries(["N", "FP", "N", "P"]) == [(0, 2), (1, 4)]
    assert nb.boundaries(["N", "P", "N", "C", "N"]) == [(0, 2), (2, 4), (4, 5)]


def test_api_shape_and_determinism():
    pytest.importorskip("torch")
    if not nb.enabled():
        pytest.skip("boundary model not trained")
    text, spaces = segmenter._prepare("स जगाम वनं वीरः प्रतिज्ञामनुपालयन्")
    a = nb.logprobs(text, spaces)
    nb._cached.cache_clear()
    b = nb.logprobs(text, spaces)
    assert len(a) == len(text) and a == b
    assert all(set(d) == set(nb.LABELS) for d in a)
    assert all(abs(sum(2.718281828 ** v for v in d.values()) - 1) < 1e-4 for d in a)
    assert max(a[-1], key=a[-1].get) == "P"


def test_tiny_training_smoke():
    torch = pytest.importorskip("torch")
    torch.manual_seed(0)
    data = []
    for line, words in [("चैव", [("च", False), ("एव", False)]), ("रामोऽपि", [("रामस्", False), ("अपि", False)])]:
        text, spaces = segmenter._prepare(line)
        data.append((text, spaces, nb.extract_labels(text, words)))
    vocab_list = [nb.PAD, nb.UNK] + sorted({v for t, _, _ in data for v in t})
    vocab = {v: i for i, v in enumerate(vocab_list)}
    net = nb.build_model(len(vocab), emb=8, hidden=8, layers=1, dropout=0.0)
    opt = torch.optim.Adam(net.parameters(), lr=0.05)
    li = {l: i for i, l in enumerate(nb.LABELS)}
    for _ in range(60):
        for text, spaces, labels in data:
            ids, sp = nb.encode(text, spaces, vocab)
            out = net(torch.tensor([ids]), torch.tensor([sp]))[0]
            loss = torch.nn.functional.cross_entropy(out, torch.tensor([li[l] for l in labels]))
            opt.zero_grad(); loss.backward(); opt.step()
    net.eval()
    text, spaces, labels = data[0]
    ids, sp = nb.encode(text, spaces, vocab)
    pred = [nb.LABELS[k] for k in net(torch.tensor([ids]), torch.tensor([sp]))[0].argmax(-1).tolist()]
    assert pred == labels
