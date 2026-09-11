import re
from vidyut_anuvaada.sutras.characters import DEVANAGARI_VOWELS, CONSONANTS, COMBINING, is_vowel, is_consonant, is_combining, strip_ending

DEVANAGARI_WORD_PATTERN = r'[ऀ-ॿ]+'

SANSKRIT_PUNCTUATION = '।॥.,;:!?—–""''॰'


class SanskritTokenizer:
	"""Tokenizer for Sanskrit text in Devanagari script."""

	def __init__(self):
		self.pattern = re.compile(DEVANAGARI_WORD_PATTERN)

	def tokenize(self, text):
		"""Tokenize text into a list of Devanagari word tokens.

		Removes punctuation and splits on whitespace.
		Returns only Devanagari word tokens.
		"""
		if not text:
			return []

		# Build a character class for punctuation to strip
		escaped_punct = re.escape(SANSKRIT_PUNCTUATION)
		clean = re.sub(r'[' + escaped_punct + r']', ' ', text)
		clean = re.sub(r'\s+', ' ', clean).strip()

		if not clean:
			return []

		tokens = []
		for word in clean.split(' '):
			matches = self.pattern.findall(word)
			tokens.extend(matches)

		return tokens

	def tokenize_with_positions(self, text):
		"""Tokenize text and return list of (token, start, end) tuples.

		Uses re.finditer to capture character positions in the original text.
		Only returns tokens that are Devanagari words.
		"""
		if not text:
			return []

		results = []
		for match in self.pattern.finditer(text):
			token = match.group()
			if token:
				results.append((token, match.start(), match.end()))

		return results

	def split_compound(self, word):
		"""Split a potentially sandhi-merged word into constituent parts.

		Uses simple heuristics: if word ends with common Sanskrit suffixes
		(visarga + consonant, visarga + vowel, etc.), attempt to split.

		Returns list of word parts. Returns [word] if no split found.
		"""
		if not word or len(word) < 3:
			return [word]

		# Common endings to try stripping (in order of preference)
		# Format: (suffix, description)
		common_endings = [
			('ःस्', 'visarga + s'),
			('ः', 'visarga'),
			('स्', 's suffix'),
			('अम्', 'am suffix'),
			('एन', 'ena suffix'),
			('अय', 'aya suffix'),
			('स्य', 'sya suffix'),
			('स्याः', 'syaah suffix'),
			('स्यै', 'syai suffix'),
			('स्याः', 'syaah suffix'),
			('त्', 't suffix'),
			('त्वा', 'tvaa suffix'),
			('त्व', 'tv suffix'),
		]

		for suffix, _ in common_endings:
			if word.endswith(suffix) and len(word) > len(suffix):
				stem = word[:-len(suffix)]
				if stem and len(stem) >= 2:
					return [stem, suffix]

		# Try stripping visarga + any consonant(s)
		visarga_idx = word.rfind('ः')
		if visarga_idx != -1 and visarga_idx < len(word) - 1:
			stem = word[:visarga_idx]
			if stem and len(stem) >= 2:
				return [stem, word[visarga_idx:]]

		return [word]

	def normalize(self, text):
		"""Normalize Devanagari text.

		Replaces full-width/alternate Devanagari variants with standard forms.
		Handles common spacing issues (multiple spaces, spaces before punctuation).
		"""
		if not text:
			return ''

		# Full-width Devanagari variants mapped to standard forms
		fullwidth_map = {
			'ँ': 'ँ', # candrabindu (if variant exists)
			'ं': 'ं', # anusvara
			'ः': 'ः', # visarga
			'ऄ': 'ऄ', # short e variant
		}

		result = text
		for fullwidth, standard in fullwidth_map.items():
			result = result.replace(fullwidth, standard)

		# Remove spaces before Devanagari punctuation
		result = re.sub(r'\s+([।॥])', r'\1', result)

		# Collapse multiple spaces
		result = re.sub(r'[ \t]+', ' ', result)

		return result.strip()


def tokenize_sanskrit(text):
	"""Module-level convenience function.

	Creates a SanskritTokenizer and returns tokenize(text).
	"""
	tokenizer = SanskritTokenizer()
	return tokenizer.tokenize(text)


def tokenize_sanskrit_with_positions(text):
	"""Module-level convenience function.

	Creates a SanskritTokenizer and returns tokenize_with_positions(text).
	"""
	tokenizer = SanskritTokenizer()
	return tokenizer.tokenize_with_positions(text)
