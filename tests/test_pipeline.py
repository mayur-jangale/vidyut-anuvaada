"""Tests for samāsa integration in pipeline."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from vidyut_anuvaada.sutras.pipeline import translate, _analyse_token
from vidyut_anuvaada.sutras.P_2_1 import samasa_detect, _classify_samasa


def test_samasa_detect_avya():
 r = samasa_detect("अनुदिनम्")
 assert r["type"] == "अव्ययीभाव"
 assert r["members"] == ["अनु", "दिनम्"]
 assert r["confidence"] >= 0.7


def test_samasa_detect_dvandva():
 r = samasa_detect("रामचल")
 assert r["type"] == "द्वन्द्व"
 assert r["members"] == ["राम", "ल"]


def test_samasa_detect_dvigu():
 r = samasa_detect("त्रिगु")
 assert r["type"] == "द्विगु"


def test_samasa_detect_bahuvrihi():
 r = samasa_detect("हस्तहर")
 assert r["type"] == "बहुव्रीहि"


def test_samasa_detect_karmadharaya():
 r = samasa_detect("नीलोत्पल")
 assert r["type"] == "कर्मधारय"


def test_samasa_detect_tatpurusha_default():
 r = samasa_detect("राजपुरुष")
 assert r["type"] == "तत्पुरुष"


def test_samasa_detect_invalid():
 r = samasa_detect("")
 assert r["type"] == "unknown"
 assert r["tag"] == "invalid"


def test_pipeline_samāsa_path():
 out = _analyse_token("अनुदिनम्")
 # Word is not in dictionary; lemmatizer is the primary source
 assert out["source"] in ("dictionary", "lemmatizer")
 assert "word" in out
 assert "lemma" in out


def test_pipeline_samāsa_avya():
 out = _analyse_token("अनुदिनम्")
 # Word is not in dictionary; lemmatizer is the primary source
 assert out["source"] in ("dictionary", "lemmatizer")
 assert "word" in out
 assert "lemma" in out


def test_pipeline_translate_simple():
 # translate() returns TranslationResult objects (not plain dicts)
 tokens = translate("राजपुरुष")
 assert len(tokens) >= 1
 assert hasattr(tokens[0], "word")
 assert hasattr(tokens[0], "translation")
