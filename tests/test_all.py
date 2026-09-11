"""Test all chapter modules and NLP infrastructure."""
import importlib.util
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "vidyut_anuvaada" / "sutras"))


def _chapter_modules():
	return sorted((ROOT / "vidyut_anuvaada" / "sutras").glob("P_[0-9]_[0-9].py"))


def _per_sutra_files():
	return sorted((ROOT / "vidyut_anuvaada" / "sutras").glob("P_[0-9]_[0-9]_[0-9]_[0-9]*.py"))


class TestChapterModules:
	"""Every P_X_Y.py chapter module must load and have apply functions."""

	@pytest.mark.parametrize("path", _chapter_modules(), ids=lambda p: p.name)
	def test_chapter_loads(self, path):
		spec = importlib.util.spec_from_file_location(path.stem, path)
		mod = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(mod)
		assert mod is not None

	@pytest.mark.parametrize("path", _chapter_modules(), ids=lambda p: p.name)
	def test_has_apply_functions(self, path):
		spec = importlib.util.spec_from_file_location(path.stem, path)
		mod = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(mod)
		apply_funcs = [x for x in dir(mod) if x.startswith("apply_")]
		assert len(apply_funcs) > 0, f"{path.name} has no apply_ functions"


class TestPerSutraFiles:
	"""Per-sutra files must have Sutra class with apply and EXAMPLES."""

	@pytest.mark.parametrize("path", _per_sutra_files()[:200], ids=lambda p: p.name)
	def test_per_sutra_structure(self, path):
		spec = importlib.util.spec_from_file_location(path.stem, path)
		mod = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(mod)
		cls_name = "Sutra" + path.stem.replace("P_", "").replace("_", "")
		cls = getattr(mod, cls_name, None)
		assert cls is not None
		assert callable(getattr(cls, "apply", None))
		assert hasattr(cls, "EXAMPLES")


class TestApplyFunctions:
	"""apply() must run without error on sample input."""

	@pytest.mark.parametrize("path", _chapter_modules()[:10], ids=lambda p: p.name)
	def test_chapter_apply_runs(self, path):
		spec = importlib.util.spec_from_file_location(path.stem, path)
		mod = importlib.util.module_from_spec(spec)
		spec.loader.exec_module(mod)
		apply_funcs = [getattr(mod, x) for x in dir(mod) if x.startswith("apply_") and callable(getattr(mod, x))]
		if not apply_funcs:
			return
		try:
			result = apply_funcs[0]("test", "")
		except Exception as e:
			pytest.fail(f"{path.name}.{apply_funcs[0].__name__} raised {e}")
		assert result is not None


class TestNLPModules:
	"""NLP modules must import and work."""

	def test_characters(self):
		from vidyut_anuvaada.sutras.characters import VOWELS_INDEPENDENT, CONSONANTS, HAL_SET, is_vowel, is_consonant
		assert len(VOWELS_INDEPENDENT) == 14
		assert len(CONSONANTS) >= 33
		assert is_vowel("अ")
		assert is_consonant("क")

	def test_tokenizer(self):
		from vidyut_anuvaada.sutras.tokenizer import SanskritTokenizer
		t = SanskritTokenizer()
		tokens = t.tokenize("रामो राजा हनुमान् च")
		assert "रामो" in tokens

	def test_sutra_engine(self):
		from vidyut_anuvaada.sutras.sutra_engines import SutraEngine
		engine = SutraEngine()
		assert len(engine._loaded_modules) > 0

	def test_sandhi_functions(self):
		from vidyut_anuvaada.sutras.P_6_1 import apply_6_1_66
		from vidyut_anuvaada.sutras.P_6_2 import apply_6_2_139
		from vidyut_anuvaada.sutras.P_6_3 import apply_6_3_2
		from vidyut_anuvaada.sutras.P_6_4 import apply_6_4_64
		assert apply_6_1_66 is not None
		assert apply_6_2_139 is not None
		assert apply_6_3_2 is not None
		assert apply_6_4_64 is not None


class TestDictionary:
	"""Dictionary lookup must work for common words."""

	def test_lookup_agni(self):
		from vidyut_anuvaada.sutras.dictionary import lookup
		r = lookup("अग्नि")
		assert r is not None

	def test_all_entries_nonempty(self):
		from vidyut_anuvaada.sutras.dictionary import all_entries
		entries = all_entries()
		assert len(entries) > 100
