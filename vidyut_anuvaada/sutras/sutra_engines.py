"""Sutra engine dispatcher: NLP-oriented engine that loads all Panini chapter
modules (P_1_1 through P_8_4), builds a code-to-apply-function dispatch table,
and exposes high-level Sanskrit derivation and translation methods.

All functions use TAB indentation only.
"""
import re
import importlib
from vidyut_anuvaada.sutras.characters import VRDDHI, GUNA, IK, VOWELS, CONSONANTS, HAL, MATRA_MAP, is_vowel, is_consonant, is_matra, strip_ending
from vidyut_anuvaada.sutras.tokenizer import tokenize_sanskrit, SanskritTokenizer
from vidyut_anuvaada.sutras.lemmatizer import SanskritLemmatizer, lemmatize_sanskrit

# Chapter/pada ranges covered by the Ashtadhyayi
_CHAPTERS = list(range(1, 9))
_PADAS = list(range(1, 5))


class SutraEngine:
	"""Core NLP engine that dispatches to Panini sutra chapter modules."""

	def __init__(self):
		self._dispatch: dict = {}
		self._lemmatizer = SanskritLemmatizer()
		self._tokenizer = SanskritTokenizer()
		self._loaded_modules: dict = {}
		self._load_all_chapters()

	def _load_module(self, ch, pa):
		"""Dynamically import P_{ch}_{pa}.py and return the module.

		Results are cached so each chapter module is imported exactly once.
		Returns None on ImportError.
		"""
		key = (ch, pa)
		if key in self._loaded_modules:
			return self._loaded_modules[key]
		mod_name = f"P_{ch}_{pa}"
		try:
			mod = importlib.import_module(mod_name)
			self._loaded_modules[key] = mod
			return mod
		except ImportError:
			self._loaded_modules[key] = None
			return None

	def _load_all_chapters(self):
		"""Load every consolidated chapter module (P_1_1 .. P_8_4) and build
		a dispatch table mapping sutra codes (e.g. 'प.1.1.1') to apply
		functions."""
		for ch in _CHAPTERS:
			for pa in _PADAS:
				mod = self._load_module(ch, pa)
				if mod is None:
					continue
				for attr in dir(mod):
					if not attr.startswith("apply_"):
						continue
					func = getattr(mod, attr)
					if not callable(func):
						continue
					code = _func_name_to_code(attr)
					if code not in self._dispatch:
						self._dispatch[code] = func

	# ------------------------------------------------------------------
	# Basic dispatch
	# ------------------------------------------------------------------

	def apply(self, sutra_code, word, pos=""):
		"""Look up an apply function by sutra code and call it.

		sutra_code format: 'प.1.1.1' (devanagari dot separators) or
		'P.1.1.1' (latin). Returns the function result, or *word*
		unchanged if the code is not in the dispatch table.
		"""
		normalized = _normalize_sutra_code(sutra_code)
		func = self._dispatch.get(normalized)
		if func is None:
			return word
		try:
			result = func(word, pos)
		except Exception:
			result = word
		return result if isinstance(result, str) else word

	def apply_chapter(self, ch, pa, word, pos=""):
		"""Apply every sutra found in chapter *ch* pada *pa* to *word*
		in numeric order. Returns the final transformed word."""
		mod = self._load_module(ch, pa)
		if mod is None:
			return word
		codes = _collect_ordered_codes(mod)
		result = word
		for code in codes:
			func = self._dispatch.get(code)
			if func is None:
				continue
			try:
				transformed = func(result, pos)
			except Exception:
				continue
			if isinstance(transformed, str):
				result = transformed
		return result

	# ------------------------------------------------------------------
	# Sandhi
	# ------------------------------------------------------------------

	def sandhi_apply(self, w1, w2):
		"""Apply sandhi sutras (P_6_1 – P_6_4) to combine two words.

		Returns the combined form as a string.
		"""
		combined = f"{w1}+{w2}"
		for ch in (6,):
			for pa in (1, 2, 3, 4):
				combined = self.apply_chapter(ch, pa, combined)
		return combined

	def sandhi_split(self, word):
		"""Apply sandhi rules in reverse to split a compound/sandhi word.

		Returns a list of word parts (at minimum [word]).
		"""
		from vidyut_anuvaada.sutras.sandhi import split_sandhi
		try:
			result = split_sandhi(word)
			if isinstance(result, list) and result:
				return result
		except (ImportError, AttributeError):
			pass
		return [word]

	# ------------------------------------------------------------------
	# Derivation helpers
	# ------------------------------------------------------------------

	def subanta_derive(self, stem, vibhakti, vacana, linga):
		"""Derive a subanta (declinable nominal) form.

		Steps: P_4_1 sup-sthana (select endings) -> P_6_1 sandhi.
		Returns the derived word string.
		"""
		base = stem
		base = self.apply_chapter(4, 1, base, pos=f"subanta:{linga}:{vibhakti}:{vacana}")
		base = self.apply_chapter(6, 1, base)
		return base

	def tinanta_derive(self, dhatu, purusha, vacana, lakara, pada=""):
		"""Derive a tinanta (finite verb) form.

		Steps: P_3_4 tiG (select tiG ending) -> P_3_1 vikaraNa ->
		P_6_1 sandhi.
		Returns the derived word string.
		"""
		word = dhatu
		word = self.apply_chapter(3, 4, word, pos=f"tinanta:{purusha}:{vacana}:{lakara}:{pada}")
		word = self.apply_chapter(3, 1, word, pos=f"vikarana:{purusha}:{vacana}")
		word = self.apply_chapter(6, 1, word)
		return word

	def krdanta_derive(self, dhatu, krt_suffix):
		"""Derive a krdanta (participial / verbal noun) form.

		Steps: P_3_2 krt rules (affix selection) -> P_6_1 sandhi.
		Returns the derived word string.
		"""
		word = dhatu
		word = self.apply_chapter(3, 2, word, pos=f"krdanta:{krt_suffix}")
		word = self.apply_chapter(6, 1, word)
		return word

	def taddhita_derive(self, stem, taddhita_suffix):
		"""Derive a taddhita (secondary derivative) form.

		Steps: P_5.x taddhita rules -> P_6_1 sandhi.
		Returns the derived word string.
		"""
		word = stem
		for ch in (5,):
			for pa in range(1, 5):
				word = self.apply_chapter(ch, pa, word, pos=f"taddhita:{taddhita_suffix}")
		word = self.apply_chapter(6, 1, word)
		return word

	def samasa_form(self, members, samasa_type):
		"""Form a compound word from *members*.

		Steps: P_2_1 (general samasa) + P_2_2 (dvandva) rules.
		*members* is a list of stem strings.
		*samasa_type* is a string like 'dvandva', 'tatpurusha', 'bahuvrihi',
		'avyayibhava'.
		Returns the compound form string.
		"""
		combined = "+".join(members)
		combined = self.apply_chapter(2, 1, combined, pos=f"samasa:{samasa_type}")
		combined = self.apply_chapter(2, 2, combined, pos=f"samasa:{samasa_type}")
		return combined

	# ------------------------------------------------------------------
	# Translation pipeline
	# ------------------------------------------------------------------

	def translate_word(self, word, pos=""):
		"""Full NLP pipeline for a single word:

		1. Tokenize
		2. Lemmatize (dictionary + suffix stripping + sutra application)
		3. Sutra derivation
		4. Return translation with features dict
		"""
		lemma, features = self._lemmatizer.lemmatize(word, pos)
		sutra_path = self._trace_sutras(word, lemma, pos)
		translation = self._lookup_translation(word, lemma, pos)
		return {
			"word": word,
			"lemma": lemma,
			"pos": pos,
			"features": features,
			"translation": translation,
			"sutra_path": sutra_path,
		}

	def translate_sentence(self, sentence):
		"""Tokenize a Sanskrit sentence and translate each word.

		Returns a list of dicts, one per token, in order.
		"""
		tokens = self._tokenizer.tokenize(sentence)
		return [self.translate_word(t) for t in tokens]

	# ------------------------------------------------------------------
	# Internal helpers
	# ------------------------------------------------------------------

	def _trace_sutras(self, word, lemma, pos):
		"""Return a list of sutra codes that were relevant during lookup."""
		path = []
		for code in sorted(self._dispatch.keys()):
			ch = _code_chapter(code)
			if ch in (1, 2, 6, 7, 8):
				path.append(code)
		return path[:20]

	def _lookup_translation(self, word, lemma, pos):
		"""Dictionary lookup with fallback."""
		try:
			from vidyut_anuvaada.sutras.dictionary import lookup
			entry = lookup(word)
			if entry is not None:
				return entry[2]
		except ImportError:
			pass
		try:
			from vidyut_anuvaada.sutras.dictionary import lookup
			entry = lookup(lemma)
			if entry is not None:
				return entry[2]
		except (ImportError, NameError):
			pass
		return f"[{lemma}]"


# ------------------------------------------------------------------
# Module-level convenience functions
# ------------------------------------------------------------------

_ENGINE_SINGLETON = None


def apply_general(word, pos="", SUTRA_TOKEN=""):
	"""Try every loaded chapter module in order (ch 1..8, pa 1..4)
	and return the last non-trivial result.

	If nothing matches, returns *word* unchanged.
	"""
	global _ENGINE_SINGLETON
	if _ENGINE_SINGLETON is None:
		_ENGINE_SINGLETON = SutraEngine()
	result = word
	for ch in _CHAPTERS:
		for pa in _PADAS:
			transformed = _ENGINE_SINGLETON.apply_chapter(ch, pa, word, pos)
			if transformed != word:
				result = transformed
	return result


def apply_sandhi(w1, w2):
	"""Convenience wrapper: apply sandhi_apply via a singleton engine."""
	global _ENGINE_SINGLETON
	if _ENGINE_SINGLETON is None:
		_ENGINE_SINGLETON = SutraEngine()
	return _ENGINE_SINGLETON.sandhi_apply(w1, w2)


def translate_sanskrit(text):
	"""Full translation pipeline: tokenize -> lemmatize -> sutra -> translate.

	Returns a list of per-word result dicts.
	"""
	global _ENGINE_SINGLETON
	if _ENGINE_SINGLETON is None:
		_ENGINE_SINGLETON = SutraEngine()
	return _ENGINE_SINGLETON.translate_sentence(text)


# ------------------------------------------------------------------
# Private helpers
# ------------------------------------------------------------------

def _func_name_to_code(func_name):
	"""Convert 'apply_1_1_1' -> 'प.1.1.1'. Return None on mismatch."""
	m = re.match(r"^apply_(\d+)_(\d+)_(\d+)$", func_name)
	if m:
		return f"प.{m.group(1)}.{m.group(2)}.{m.group(3)}"
	return None


def _normalize_sutra_code(code):
	"""Accept both 'प.X.Y.Z' and 'P.X.Y.Z' formats, return Devanagari."""
	if code.startswith("P."):
		parts = code.split(".")
		if len(parts) == 4:
			return f"प.{parts[1]}.{parts[2]}.{parts[3]}"
	return code


def _collect_ordered_codes(mod):
	"""Scan *mod* for apply_* functions, extract their codes, sort numerically."""
	codes = []
	for attr in dir(mod):
		if not attr.startswith("apply_"):
			continue
		code = _func_name_to_code(attr)
		if code:
			codes.append((_code_sort_key(code), code))
	codes.sort()
	return [c for (_, c) in codes]


def _code_sort_key(code):
	"""Turn 'प.1.1.1' into a 3-tuple of ints for sorting."""
	m = re.match(r"प\.(\d+)\.(\d+)\.(\d+)", code)
	if m:
		return (int(m.group(1)), int(m.group(2)), int(m.group(3)))
	return (0, 0, 0)


def _code_chapter(code):
	"""Extract chapter number from a sutra code string."""
	m = re.match(r"प\.(\d+)", code)
	if m:
		return int(m.group(1))
	return 0
