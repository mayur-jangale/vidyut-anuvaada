"""Sanskrit lemmatizer driven by the Panini sutra system.

Uses the 32 consolidated chapter modules (P_1_1 .. P_8_4) for fast loading.
"""
from __future__ import annotations

import importlib
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Devanagari character inventories
# ---------------------------------------------------------------------------

DEVANAGARI_VOWELS = set("अआइईउऊऋॠऌॡएऐओऔ")
DEVANAGARI_CONSONANTS = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")

_VOWEL_CHARS = DEVANAGARI_VOWELS
_CONSONANT_CHARS = DEVANAGARI_CONSONANTS

# ---------------------------------------------------------------------------
# Path helpers
# ---------------------------------------------------------------------------

_SUTRAS_DIR: Path = Path(__file__).resolve().parent


# ---------------------------------------------------------------------------
# Sutra table loading (consolidated modules only)
# ---------------------------------------------------------------------------

def _code_from_apply_name(func_name: str) -> Optional[str]:
	m = re.match(r"^apply_(\d+)_(\d+)_(\d+)$", func_name)
	if m:
		return f"प.{m.group(1)}.{m.group(2)}.{m.group(3)}"
	return None


def _load_sutra_table(sutras_dir: Path) -> Dict[str, Any]:
	"""Load apply functions from the 32 consolidated chapter modules only."""
	table: Dict[str, Any] = {}
	sys.path.insert(0, str(sutras_dir))
	try:
		for ch in range(1, 9):
			for pa in range(1, 5):
				mod_name = f"P_{ch}_{pa}"
				try:
					mod = importlib.import_module(mod_name)
				except ImportError:
					continue
				for attr in dir(mod):
					if not attr.startswith("apply_"):
						continue
					func = getattr(mod, attr)
					if not callable(func):
						continue
					code = _code_from_apply_name(attr)
					if code not in table:
						table[code] = func
	finally:
		if str(sutras_dir) in sys.path:
			sys.path.remove(str(sutras_dir))
	return table


# ---------------------------------------------------------------------------
# Sandhi-splitting helpers
# ---------------------------------------------------------------------------

_VOWELS = set("अआइईउऊऋॠऌॡएऐओऔ")
_CONSONANTS = set("कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहळर्")
_HALANT = set("्")
# Maps vowel cluster → list of possible original vowel pairs
_VOWEL_SANDHI = {
	"अ": [("अ", ""), ("आ", "")],
	"आ": [("आ", ""), ("अ", "अ"), ("अ", "आ")],
	"इ": [("इ", ""), ("ई", ""), ("अ", "इ")],
	"ई": [("ई", ""), ("इ", "इ")],
	"उ": [("उ", ""), ("ऊ", ""), ("अ", "उ")],
	"ऊ": [("ऊ", ""), ("उ", "उ")],
	"ए": [("ए", ""), ("अ", "ए"), ("अ", "इ")],
	"ऐ": [("ऐ", ""), ("अ", "ऐ"), ("आ", "इ")],
	"ओ": [("ओ", ""), ("अ", "ओ"), ("अ", "उ")],
	"औ": [("औ", ""), ("अ", "औ"), ("आ", "उ")],
}

def _try_sandhi_split(word: str, lookup_fn, max_splits: int = 8) -> List[Tuple[str, str]]:
	"""Rule-based sandhi splitter.
	Returns candidate (left, right) splits that both appear in lookup_fn."""
	results: List[Tuple[str, str]] = []
	if len(word) < 5:
		return results

	# Collect vowel positions
	vowel_positions = [i for i, c in enumerate(word) if c in _VOWELS]
	if not vowel_positions:
		return results

	# Try splitting at each vowel boundary
	for vi, pos in enumerate(vowel_positions):
		if vi == 0:
			continue
		left = word[:vowel_positions[vi - 1] + 1]
		right_start = vowel_positions[vi - 1] + 1
		right = word[right_start:]
		if len(left) < 2 or len(right) < 2:
			continue
		# Both halves must be dictionary words
		try:
			_l = lookup_fn(left)
			_r = lookup_fn(right)
		except Exception:
			continue
		if _l is not None and _r is not None:
			results.append((left, right))
			if len(results) >= max_splits:
				return results

	# Also try visarga-based splits (P6.1.69 etc.)
	if "ः" in word:
		h_pos = word.find("ः")
		left = word[:h_pos + 1]
		right = word[h_pos + 1:]
		if len(left) >= 2 and len(right) >= 2:
			try:
				_l = lookup_fn(left)
				_r = lookup_fn(right)
			except Exception:
				pass
			else:
				if _l is not None and _r is not None:
					results.append((left, right))

	return results


# ---------------------------------------------------------------------------
# SanskritLemmatizer
# ---------------------------------------------------------------------------

class SanskritLemmatizer:
	"""Lemmatize Devanagari Sanskrit words using the Panini sutra system."""

	def __init__(self, sutras_dir: Optional[Path] = None) -> None:
		self._sutras_dir: Path = sutras_dir or _SUTRAS_DIR
		self._sutra_table: Dict[str, Any] = {}
		self._loaded: bool = False
		self._cache: Dict[str, str] = {}

	def _ensure_loaded(self) -> None:
		if self._loaded:
			return
		self._sutra_table = _load_sutra_table(self._sutras_dir)
		self._loaded = True

	def _strip_suffix(self, word: str, suffixes: List[str]) -> Tuple[str, str]:
		for suffix in suffixes:
			if word.endswith(suffix) and len(word) > len(suffix):
				return word[: len(word) - len(suffix)], suffix
		return word, ""

	def _apply_sutras(self, word: str, pos: str, sutra_list: List[str]) -> str:
		result = word
		for code in sutra_list:
			fn = self._sutra_table.get(code)
			if fn is None:
				continue
			try:
				transformed = fn(result, pos)
			except Exception:
				continue
			if transformed is not None and isinstance(transformed, str):
				result = transformed
		return result

	def get_features(self, word: str, lemma: str, pos: str = "") -> Dict[str, str]:
		features: Dict[str, str] = {}
		if not lemma:
			return features
		rel = word[len(lemma):]
		case_map = {
			"ः": ("NOM", "SG"), "ा": ("NOM", "SG"), "ौ": ("NOM", "DU"),
			"ाः": ("NOM", "PL"), "ाः": ("NOM", "PL"), "स्": ("ACC", "SG"),
			"ान्": ("ACC", "PL"), "ेने": ("INST", "SG"), "ेन": ("INST", "SG"),
			"ाय": ("DAT", "SG"), "े": ("LOC", "SG"), "स्य": ("GEN", "SG"),
			"ात्": ("ABL", "SG"), "अम्": ("ACC", "SG"), "अस्": ("ACC", "DU"),
			"आम्": ("GEN", "PL"), "इ": ("NOM", "DU"), "ई": ("NOM", "DU"),
			"योः": ("GEN", "DU"), "योस्": ("LOC", "DU"), "भ्याम्": ("", "DU"),
			"भ्यः": ("", "PL"), "सु": ("", "SG"), "ओस्": ("", "DU"),
			"इनाम्": ("GEN", "PL"),
		}
		for ending, (case_val, num_val) in case_map.items():
			if rel.endswith(ending):
				if case_val:
					features["case"] = case_val
				if num_val:
					features["number"] = num_val
				break
		if pos:
			clean_pos = pos.split("-")[0].split("_")[0]
			if clean_pos in ("noun-f", "strī", "feminine"):
				features["gender"] = "F"
			elif clean_pos in ("noun-n", "napuṃsakam", "neuter"):
				features["gender"] = "N"
			elif clean_pos in ("noun-m", "puṃ", "masculine"):
				features["gender"] = "M"
		if rel.endswith("क्त") or rel.endswith("क्तवत्"):
			features["tense"] = "PAST"
		if rel.endswith("त") or rel.endswith("ति"):
			features["tense"] = "PRESENT"
			features["person"] = "3"
			features["mood"] = "INDICATIVE"
		if rel.endswith("ति"):
			features["person"] = "3"
			features["mood"] = "INDICATIVE"
		if rel.endswith("सि"):
			features["person"] = "2"
			features["mood"] = "INDICATIVE"
		if rel.endswith("मि"):
			features["person"] = "1"
			features["mood"] = "INDICATIVE"
		if rel.endswith("न्ति"):
			features["person"] = "3"
			features["number"] = "PL"
			features["mood"] = "INDICATIVE"
		if rel.endswith("तु"):
			features["mood"] = "OPTATIVE"
		if rel.endswith("ताम्"):
			features["mood"] = "IMPERATIVE"
		if rel.endswith("ध्वम्"):
			features["mood"] = "IMPERATIVE"
			features["person"] = "2"
		return features

	def lemmatize(self, word: str, pos: str = "") -> Tuple[str, Dict[str, str]]:
		self._ensure_loaded()
		cache_key = f"{word}|{pos}"
		if cache_key in self._cache:
			lemma = self._cache[cache_key]
			return lemma, self.get_features(word, lemma, pos)

		# 1. direct dictionary lookup
		try:
			from vidyut_anuvaada.sutras.dictionary import lookup
			entry = lookup(word)
			if entry is not None:
				lemma, pos_tag, gloss = entry
				self._cache[cache_key] = lemma
				return lemma, self.get_features(word, lemma, pos_tag)
		except ImportError:
			pass

		# 2. reverse visarga
		reverse_visarga = self._reverse_visarga(word)
		if reverse_visarga:
			for candidate, _ in reverse_visarga:
				try:
					entry = lookup(candidate)
				except NameError:
					break
				if entry is not None:
					lemma, pos_tag, gloss = entry
					self._cache[cache_key] = lemma
					return lemma, self.get_features(word, lemma, pos_tag)

		# 3. strip tiG endings
		stem_tig, suffix_tig, pn_mood = self._strip_tig(word)
		if suffix_tig and stem_tig:
			try:
				entry = lookup(stem_tig)
			except NameError:
				entry = None
			if entry is not None:
				lemma, pos_tag, gloss = entry
				feats = self.get_features(word, stem_tig, pos_tag)
				feats.setdefault("tense", "INFERRED")
				feats["suffix_stripped"] = suffix_tig
				self._cache[cache_key] = lemma
				return lemma, feats

		# 4. strip sup endings
		stem_sup, suffix_sup, cn = self._strip_sup(word)
		if suffix_sup and stem_sup:
			try:
				entry = lookup(stem_sup)
			except NameError:
				entry = None
			if entry is not None:
				lemma, pos_tag, gloss = entry
				feats = self.get_features(word, stem_sup, pos_tag)
				if suffix_sup:
					feats["suffix_stripped"] = suffix_sup
				self._cache[cache_key] = lemma
				return lemma, feats

		# 5. try sandhi-split dictionary entries
		try:
			from vidyut_anuvaada.sutras.dictionary import sandhi_splits
			splits = sandhi_splits(word)
			if splits:
				left, right = splits[0]
				for candidate in (left, right):
					try:
						entry = lookup(candidate)
					except NameError:
						continue
					if entry is not None:
						lemma, pos_tag, gloss = entry
						self._cache[cache_key] = lemma
						return lemma, self.get_features(word, lemma, pos_tag)
		except ImportError:
			pass

		# 5b. compound split: try splitting at every position
		if len(word) >= 6:
			try:
				from vidyut_anuvaada.sutras.dictionary import lookup
				_split_cache = {}
				_BAD = {('कर्', 'मणि'), ('गुडा', 'केश')}

				def _ok(w):
					return len(w) >= 2 and lookup(w) is not None

				def _split(w):
					if w in _split_cache:
						return _split_cache[w]
					if len(w) < 4:
						_split_cache[w] = None
						return None
					if _ok(w):
						_split_cache[w] = w
						return w
					for _i in range(3, len(w) - 2):
						l, r = w[:_i], w[_i:]
						if len(l) < 2 or len(r) < 2 or (l, r) in _BAD:
							continue
						if _split(l) and _split(r):
							_split_cache[w] = l + '+' + r
							return _split_cache[w]
					_split_cache[w] = None
					return None

				_res = _split(word)
				if _res and '+' in _res:
					_first = _res.split('+')[0]
					feats = self.get_features(word, _first, 'noun')
					feats['compound_split'] = _res
					self._cache[cache_key] = _first
					return _first, feats
			except ImportError:
				pass

		# 6. apply krt suffix rules
		krt_result = self._apply_krt_rules(word, pos)
		if krt_result != word:
			lemma = krt_result
			feats = self.get_features(word, lemma, pos)
			feats["krt_applied"] = "yes"
			self._cache[cache_key] = lemma
			return lemma, feats

		# 7. apply taddhita / compound rules
		taddhita_result = self._apply_taddhita_rules(word, pos)
		if taddhita_result != word:
			lemma = taddhita_result
			feats = self.get_features(word, lemma, pos)
			feats["taddhita_applied"] = "yes"
			self._cache[cache_key] = lemma
			return lemma, feats

		# fallback
		self._cache[cache_key] = word
		return word, self.get_features(word, word, pos)

	def _apply_krt_rules(self, word: str, pos: str) -> str:
		_STRIP_SUFFIXES = [
			"क्तवत्", "क्त", "क्त्वा", "तुमुन्", "तव्य",
			"अनीयर", "शानच्", "शतृ", "कथक", "कत्थक",
			"ण्वुल्", "अञ्", "यत्", "इलच्", "क्वसुज्", "क्वसुन्",
		]
		for suffix in _STRIP_SUFFIXES:
			if word.endswith(suffix) and len(word) > len(suffix):
				stem = word[: len(word) - len(suffix)]
				if stem:
					return stem
		return word

	def _apply_taddhita_rules(self, word: str, pos: str) -> str:
		_STRIP_SUFFIXES = [
			"इक", "ीय", "अल", "अय", "त्व", "मय",
			"य", "क", "अन", "निक", "पा", "वत्",
			"िमत्", "मत्",
		]
		for suffix in _STRIP_SUFFIXES:
			if word.endswith(suffix) and len(word) > len(suffix):
				stem = word[: len(word) - len(suffix)]
				if stem:
					return stem
		return word

	def _reverse_visarga(self, word: str) -> List[Tuple[str, str]]:
		if "ः" not in word:
			return []
		candidates = []
		h_pos = word.find("ः")
		before = word[:h_pos + 1]
		after = word[h_pos + 2:]
		if not after:
			candidates.append((word, ""))
			return candidates
		first_after = after[0] if after else ""
		if before[-2] not in ("स्",) and first_after in {"च", "ए", "ऐ"}:
			candidates.append((before.rstrip("ः") + "स्" + after, "स्"))
		if first_after in {"ज", "ह", "ख"}:
			candidates.append((before.rstrip("ः") + "र" + after, "र"))
		if not candidates:
			candidates.append((word, ""))
		return candidates

	def _strip_tig(self, word: str) -> Tuple[str, str, str]:
		try:
			from vidyut_anuvaada.sutras.morphology import strip_tig
			return strip_tig(word)
		except ImportError:
			return word, "", ""

	def _strip_sup(self, word: str) -> Tuple[str, str, str]:
		try:
			from vidyut_anuvaada.sutras.morphology import strip_sup
			return strip_sup(word)
		except ImportError:
			return word, "", ""


_LEMMATIZER: Optional[SanskritLemmatizer] = None


def lemmatize_sanskrit(word: str, pos: str = "") -> Tuple[str, Dict[str, str]]:
	global _LEMMATIZER
	if _LEMMATIZER is None:
		_LEMMATIZER = SanskritLemmatizer()
	return _LEMMATIZER.lemmatize(word, pos)


if __name__ == "__main__":
	lem = SanskritLemmatizer()
	print("Sutra table loaded:", len(lem._sutra_table), "entries")
	print()
	test_words = [
		("अग्निः", ""), ("राजा", ""), ("पुरुषाः", ""),
		("कृत", ""), ("धर्मक्षेत्रे", ""), ("पाण्डवाः", ""),
		("देव", ""), ("सुखम्", ""), ("कृष्ण", ""),
	]
	for w, p in test_words:
		lemma, feats = lem.lemmatize(w, p)
		print(f" {w:20s} -> {lemma:20s} features={feats}")
