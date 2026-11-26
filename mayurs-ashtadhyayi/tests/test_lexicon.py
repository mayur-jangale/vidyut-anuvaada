"""Lexicon tests on real words of Ramayana, Bala-kanda, sarga 1 (DCS unsandhied forms)."""

from __future__ import annotations

import time

import pytest

from mayur import lexicon as L
from mayur.model import Morph


def _first(form: str, **want) -> Morph:
    for m in L.analyses(form):
        if all(getattr(m, k) == v for k, v in want.items()):
            return m
    raise AssertionError(f"no analysis of {form} with {want}: {L.analyses(form)[:5]}")


def _stem(form: str, **want) -> Morph:
    for m in L.stem_analyses(form):
        if all(getattr(m, k) == v for k, v in want.items()):
            return m
    raise AssertionError(f"no stem analysis of {form} with {want}: {L.stem_analyses(form)[:5]}")


# ---------------------------------------------------------------- 1. upasarga + verb


@pytest.mark.parametrize(
    "form, lemma, prefixes, kind",
    [
        ("paripapracCa", "paripracC", ("pari",), "tinanta"),
        ("paryapfcCat", "paripracC", ("pari",), "tinanta"),
        ("anupaSyati", "anudfS", ("anu",), "tinanta"),
        ("upAgamat", "upagam", ("upa",), "tinanta"),
        ("pratyuvAca", "prativac", ("prati",), "tinanta"),
    ],
)
def test_prefixed_verbs_are_derived_forward(form, lemma, prefixes, kind):
    m = _first(form, kind=kind, lemma=lemma)
    assert m.prefixes[: len(prefixes)] == prefixes
    proof = L.prove(m)
    assert proof.derivable and proof.derived_form == form
    assert proof.method == "vidyut-prakriya" and proof.trace


def test_paripapraccha_is_generated_with_lit():
    m = _first("paripapracCa", kind="tinanta")
    assert m.source == "generated" and m.lakara == "li~w" and m.purusha == "praTama"


@pytest.mark.parametrize("form", ["niratam", "samAgamya", "praviSya", "Agamya"])
def test_prefixed_krdantas(form):
    m = L.analyses(form)[0]
    assert m.prefixes and m.krt is not None
    assert L.prove(m).derivable


def test_generated_lyap_for_double_prefix():
    ms = L._lyap_from("samAgamya", ("sam",), L._verbal_entries("Agamya"))
    assert ms and ms[0].krt == "lyap" and ms[0].prefixes == ("sam", "AN")
    assert L.prove(ms[0]).derivable


def test_no_prefixed_parse_without_exact_derivation():
    assert not L._upasarga_morphs("pravxyzati")


# ---------------------------------------------------------------- 2. out-of-kosha nominals


def test_generated_nominal_only_by_exact_derivation():
    found = L._generated_nominals("SvetaketUnA")  # not attested: no stem guess derives it
    assert all(L.prove(m).derived_form == "SvetaketUnA" for m in found)
    gen = L._generated_nominals("kOsalyAputreRa")
    assert any(m.lemma == "kOsalyAputra" and m.vibhakti == "tftIyA" for m in gen)
    assert all(m.source == "generated" and L.quality(m) == 1 for m in gen)


def test_generated_nominal_not_used_when_kosha_is_good():
    assert all(m.source == "kosha" for m in L.analyses("nAradam"))


# ---------------------------------------------------------------- 3. compound-member stems


@pytest.mark.parametrize(
    "form, lemma",
    [
        ("muni", "muni"), ("tapas", "tapas"), ("vAk", "vAc"), ("vAc", "vAc"), ("rAja", "rAjan"),
        ("Atma", "Atman"), ("tapasvi", "tapasvin"), ("mahA", "mahat"), ("tad", "tad"), ("tat", "tad"),
        ("mad", "asmad"), ("tvad", "yuzmad"), ("sarva", "sarva"), ("eka", "eka"), ("satya", "satya"),
        ("svADyAya", "svADyAya"), ("ikzvAku", "ikzvAku"), ("su", "su"), ("dus", "dus"), ("an", "naY"),
    ],
)
def test_stems(form, lemma):
    assert L.is_stem(form)
    m = _stem(form, lemma=lemma)
    proof = L.prove(m)
    assert proof.derivable
    assert proof.method in ("kosha-pratipadika", "vidyut-prakriya", "special-stem")


@pytest.mark.parametrize("form, root", [("jita", "ji"), ("jAta", "jan"), ("kfta", "kf"), ("nirata", "niram")])
def test_krdanta_stems_are_derived(form, root):
    m = next(m for m in L.stem_analyses(form) if m.krt == "kta")
    proof = L.prove(m)
    assert proof.derivable and proof.method == "vidyut-prakriya" and proof.derived_form == form
    assert m.root is not None


def test_listed_stem_cites_pratipadika_sutras():
    proof = L.prove(_stem("muni", lemma="muni"))
    assert proof.method == "kosha-pratipadika" and "1.2.45" in proof.note and not proof.trace


def test_non_stem():
    assert not L.is_stem("xyzq")


# ---------------------------------------------------------------- 4. pronouns, avyayas, variants


@pytest.mark.parametrize(
    "form",
    ["kas", "asmin", "aham", "me", "tvam", "etat", "kasya", "sas", "saH", "punar", "hi", "nu", "ca",
     "eva", "iti", "SrotuM", "Srotum", "jYAtum", "asi", "icCAmi", "biByati", "puMgavam", "sAMpratam"],
)
def test_common_words_analyse_and_prove(form):
    assert L.is_pada(form, min_quality=2)
    assert any(L.prove(m).derivable for m in L.analyses(form)[:5])


def test_pronoun_preferred():
    assert L.analyses("aham")[0].lemma == "asmad"
    assert L.analyses("tvam")[0].lemma == "yuzmad"
    assert L.analyses("asmin")[0].lemma == "idam"


def test_indeclinables_first():
    for form in ("ca", "eva", "iti", "punar"):
        assert L.analyses(form)[0].kind == "avyaya"


def test_nasal_variant_resolves():
    m = L.analyses("puMgavam")[0]
    assert m.lemma == "puMgava" and m.form == "puMgavam"
    assert L.prove(m).derivable


def test_absolutive_and_infinitive():
    assert _first("gatvA", kind="avyaya").krt == "ktvA"
    assert _first("Srotum", kind="avyaya").krt == "tumu~n"


# ---------------------------------------------------------------- 5. ordering and pruning


def test_junk_kept_at_end():
    ms = L.analyses("vAk")
    qs = [L.quality(m) for m in ms]
    assert qs == sorted(qs, reverse=True)
    assert len(set(ms)) == len(ms)


def test_vocative_ranked_after_nominative():
    assert L.analyses("Agamya")[0].vibhakti != "samboDanam"


# ---------------------------------------------------------------- 6. prove


def test_prove_honest_failure():
    m = _first("niyujyamAnas")
    proof = L.prove(m)
    assert not proof.derivable and "not" in proof.note


def test_prove_matup():
    proof = L.prove(_first("guRavAn"))
    assert proof.derivable and "5.2.94" in proof.note


def test_prove_without_handle():
    assert not L.prove(Morph(form="x", lemma="x", kind="unknown")).derivable


# ---------------------------------------------------------------- speed / API


def test_signatures_and_speed():
    words = [f"x{i}gacCati" for i in range(200)]
    t = time.perf_counter()
    for w in words:
        L.analyses(w)
        L.stem_analyses(w)
        L.is_pada(w)
    assert (time.perf_counter() - t) / len(words) < 0.01
    assert isinstance(L.analyses("rAmas"), tuple) and isinstance(L.stem_analyses("rAma"), tuple)
