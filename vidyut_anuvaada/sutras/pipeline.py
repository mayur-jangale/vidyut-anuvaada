"""Sanskrit-to-English translation pipeline with NLTK integration and Ashtadhyayi sutra system."""
import re
import sys
from pathlib import Path

from vidyut_anuvaada.sutras.characters import (
	DEVANAGARI_VOWELS, CONSONANTS, COMBINING,
	is_vowel, is_consonant, is_combining, strip_ending,
)
from vidyut_anuvaada.sutras.tokenizer import tokenize_sanskrit, SanskritTokenizer
from vidyut_anuvaada.sutras.lemmatizer import SanskritLemmatizer, lemmatize_sanskrit
from vidyut_anuvaada.sutras.sutra_engines import SutraEngine, apply_general, translate_sanskrit


class TranslationResult:
	"""Container for a single word's translation result."""

	def __init__(self, word="", lemma="", pos="", features=None, translation="", sutra_path=None):
		self.word = word
		self.lemma = lemma
		self.pos = pos
		self.features = features if features is not None else {}
		self.translation = translation
		self.sutra_path = sutra_path if sutra_path is not None else []

	def __repr__(self):
		return (
			f"TranslationResult(word={self.word!r}, lemma={self.lemma!r}, "
			f"pos={self.pos!r}, translation={self.translation!r})"
		)


class SanskritPipeline:
	"""Complete NLP translation pipeline for Sanskrit using NLTK and Ashtadhyayi sutras."""

	def __init__(self):
		self.sutra_engine = SutraEngine()
		self.tokenizer = SanskritTokenizer()
		self.lemmatizer = SanskritLemmatizer()

	def tokenize(self, text):
		"""Tokenize Devanagari Sanskrit text into word tokens."""
		return self.tokenizer.tokenize(text)

	def lemmatize(self, word, pos=""):
		"""Lemmatize a single Sanskrit word. Returns (lemma, features_dict)."""
		return self.lemmatizer.lemmatize(word, pos)

	def translate(self, text):
		"""Full pipeline: tokenize, lemmatize, dictionary lookup, sutra application, POS tagging.

		Args:
			text: Sanskrit text in Devanagari script.

		Returns:
			List of TranslationResult objects, one per word.
		"""
		results = []

		tokens = self.tokenize(text)
		for token in tokens:
			sutra_path = []
			features = {}

			lemma, feats = self.lemmatizer.lemmatize(token, pos="")
			features.update(feats)

			pos_tag = features.pop("pos", "")

			try:
				from vidyut_anuvaada.sutras.dictionary import lookup
				entry = lookup(token)
				if entry is not None:
					dict_lemma, dict_pos, gloss = entry
					if not lemma == token:
						lemma = dict_lemma
					if not pos_tag:
						pos_tag = dict_pos
					translation = gloss
				else:
					translation = lemma
			except ImportError:
				translation = lemma

			try:
				sutra_results = self.sutra_engine.apply_sandhi_sutras(token, pos_tag)
				sutra_path.extend([sr.sutra_code for sr in sutra_results])
			except Exception:
				pass

			if not pos_tag:
				pos_tag = self._infer_pos(token, lemma, features)

			try:
				enriched = translate_sanskrit(token, pos_tag)
				if enriched and not translation == lemma:
					translation = enriched
			except Exception:
				pass

			result = TranslationResult(
				word=token,
				lemma=lemma,
				pos=pos_tag,
				features=features,
				translation=translation,
				sutra_path=sutra_path,
			)
			results.append(result)

		return results

	def translate_sentence(self, sentence):
		"""Translate a single sentence. Returns list of TranslationResult objects."""
		return self.translate(sentence)

	def sandhi_split_text(self, text):
		"""Tokenize text then split sandhi compounds for each word.

		Returns list of (original_word, [split_parts]) tuples.
		"""
		results = []
		tokens = self.tokenize(text)
		for token in tokens:
			split_parts = self.sandhi_split_word(token)
			results.append((token, split_parts))
		return results

	def sandhi_split_word(self, word):
		"""Split a sandhi-merged word into constituent parts.

		Returns list of word parts.
		"""
		try:
			from vidyut_anuvaada.sutras.pipeline import reverse_sandhi
			candidates = reverse_sandhi(word)
			if candidates:
				parts = [c[0] for c in candidates]
				if len(parts) >= 2:
					return parts
		except ImportError:
			pass

		parts = self.tokenizer.split_compound(word)
		return parts if len(parts) > 1 else [word]

	def analyze(self, word):
		"""Full morphological analysis of a single word.

		Returns dict with keys: word, lemma, features, sutra_path, translation, source.
		"""
		features = {}
		sutra_path = []
		source = "fallback"

		lemma, feats = self.lemmatizer.lemmatize(word, pos="")
		features.update(feats)

		try:
			from vidyut_anuvaada.sutras.dictionary import lookup
			entry = lookup(word)
			if entry is not None:
				dict_lemma, dict_pos, gloss = entry
				if not lemma == word:
					lemma = dict_lemma
				translation = gloss
				features["pos"] = dict_pos
				source = "dictionary"
			else:
				translation = lemma
				source = "lemmatizer"
		except ImportError:
			translation = lemma

		try:
			sutra_results = self.sutra_engine.apply_sandhi_sutras(word, features.get("pos", ""))
			sutra_path = [sr.sutra_code for sr in sutra_results]
		except Exception:
			pass

		return {
			"word": word,
			"lemma": lemma,
			"features": features,
			"sutra_path": sutra_path,
			"translation": translation,
			"source": source,
		}

	def batch_translate(self, texts):
		"""Translate multiple texts.

		Args:
			texts: List of Sanskrit text strings.

		Returns:
			List of lists of TranslationResult objects.
		"""
		return [self.translate(text) for text in texts]

	def _infer_pos(self, word, lemma, features):
		"""Infer part-of-speech from word form and features."""
		suffix = features.get("suffix_stripped", "")

		if suffix in {"ति", "सि", "मि", "न्ति", "तु", "ताम्", "ध्वम्"}:
			return "verb"
		if suffix in {"क्त", "क्तवत्", "क्त्वा", "तुमुन्", "तव्य", "अनीयर"}:
			return "verb-participle"
		if suffix in {"ः", "ा", "ौ", "ाः", "स्", "ान्", "ेन", "ाय", "े", "स्य", "अम्"}:
			return "noun"

		ending = word[-1] if word else ""
		if ending in {"ः", "ा", "ौ", "स्"}:
			return "noun"
		if ending in {"ति", "सि", "मि"}:
			return "verb"

		return "unknown"

	def frequency_analysis(self, texts):
		"""Analyze word frequency using NLTK FreqDist.

		Args:
			texts: List of Sanskrit text strings.

		Returns:
			nltk.FreqDist object with word frequencies.
		"""
		try:
			import nltk
			all_tokens = []
			for text in texts:
				all_tokens.extend(self.tokenize(text))
			return nltk.FreqDist(all_tokens)
		except ImportError:
			raise ImportError("NLTK is required for frequency_analysis. Install with: pip install nltk")

	def phrase_detection(self, texts, n=2):
		"""Detect common phrases using NLTK ngrams.

		Args:
			texts: List of Sanskrit text strings.
			n: N-gram size (default 2 for bigrams).

		Returns:
			nltk.FreqDist of n-grams.
		"""
		try:
			import nltk
			all_tokens = []
			for text in texts:
				all_tokens.extend(self.tokenize(text))
			ngram_list = list(nltk.ngrams(all_tokens, n))
			return nltk.FreqDist(ngram_list)
		except ImportError:
			raise ImportError("NLTK is required for phrase_detection. Install with: pip install nltk")

	def concordance_analysis(self, text, word):
		"""Perform concordance analysis on text using NLTK Text.

		Args:
			text: Sanskrit text string.
			word: Word to find concordances for.

		Returns:
			List of concordance contexts.
		"""
		try:
			import nltk
			tokens = self.tokenize(text)
			nltk_text = nltk.Text(tokens)
			return list(nltk_text.concordance(word))
		except ImportError:
			raise ImportError("NLTK is required for concordance_analysis. Install with: pip install nltk")

	def corpus_summary(self, texts):
		"""Generate a summary of a Sanskrit corpus using NLTK.

		Args:
			texts: List of Sanskrit text strings.

		Returns:
			Dict with corpus statistics.
		"""
		try:
			import nltk
			all_tokens = []
			for text in texts:
				all_tokens.extend(self.tokenize(text))

			fdist = nltk.FreqDist(all_tokens)
			vocabulary = sorted(fdist.keys())

			bigrams = list(nltk.ngrams(all_tokens, 2))
			bigram_fd = nltk.FreqDist(bigrams)

			trigrams = list(nltk.ngrams(all_tokens, 3))
			trigram_fd = nltk.FreqDist(trigrams)

			return {
				"total_tokens": len(all_tokens),
				"vocabulary_size": len(vocabulary),
				"hapax_legomena": fdist.hapaxes(),
				"top_words": fdist.most_common(20),
				"top_bigrams": bigram_fd.most_common(10),
				"top_trigrams": trigram_fd.most_common(10),
			}
		except ImportError:
			raise ImportError("NLTK is required for corpus_summary. Install with: pip install nltk")

def _analyse_token(token):
	"""Analyse a single token and return a result dict (internal helper)."""
	pipeline = SanskritPipeline()
	return pipeline.analyze(token)


def translate(text):
	"""Module-level convenience function for translating Sanskrit text.

	Creates a SanskritPipeline and returns translation results.

	Args:
		text: Sanskrit text in Devanagari script.

	Returns:
		List of TranslationResult objects.
	"""
	pipeline = SanskritPipeline()
	return pipeline.translate(text)
