VOWELS_INDEPENDENT = ['अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ॡ', 'ए', 'ऐ', 'ओ', 'औ']
DEVANAGARI_VOWELS = VOWELS_INDEPENDENT # alias for tokenizer imports

VOWELS_MATRA = {
	'अ': '',
	'आ': 'ा',
	'इ': 'ि',
	'ई': 'ी',
	'उ': 'ु',
	'ऊ': 'ू',
	'ऋ': 'ृ',
	'ॠ': 'ॄ',
	'ऌ': 'ॢ',
	'ॡ': 'ॣ',
	'ए': 'े',
	'ऐ': 'ै',
	'ओ': 'ो',
	'औ': 'ौ',
}

VOWELS_SET = set(VOWELS_INDEPENDENT)

MATRA_SET = {m for m in VOWELS_MATRA.values() if m}

COMBINING = {
	'anusvara': 'ं',
	'visarga': 'ः',
	'halant': '्',
	'candrabindu': 'ँ',
}

CONSONANTS = [
	'क', 'ख', 'ग', 'घ', 'ङ',
	'च', 'छ', 'ज', 'झ', 'ञ',
	'ट', 'ठ', 'ड', 'ढ', 'ण',
	'त', 'थ', 'द', 'ध', 'न',
	'प', 'फ', 'ब', 'भ', 'म',
	'य', 'र', 'ल', 'व',
	'श', 'ष', 'स', 'ह', 'ळ',
]

CONSONANTS_SET = set(CONSONANTS)

HAL_SET = CONSONANTS_SET

HAL_ANTARNAS = {
	'क', 'ख', 'ग', 'घ', 'ङ',
	'च', 'छ', 'ज', 'झ', 'ञ',
	'ट', 'ठ', 'ड', 'ढ', 'ण',
	'त', 'थ', 'द', 'ध', 'न',
	'प', 'फ', 'ब', 'भ', 'म',
}

SVARA = list(VOWELS_INDEPENDENT)

AYOGAVAHA = ['ं', 'ः', 'ँ']

COMBINING_SET = set(COMBINING.values())


def is_consonant(ch):
	return ch in CONSONANTS_SET


def is_vowel(ch):
	return ch in VOWELS_SET


def is_matra(ch):
	return ch in MATRA_SET


def is_combining(ch):
	return ch in COMBINING_SET


def get_base_consonant(conj):
	"""Strip matras and combining marks from a conjunct, return base consonant."""
	result = ''
	for ch in conj:
		if ch in CONSONANTS_SET:
			result = ch
		elif ch in MATRA_SET or ch in COMBINING_SET or ch in AYOGAVAHA:
			continue
		else:
			result = ch
	return result


def strip_ending(word):
	"""Strip final combining characters (visarga, anusvara, halant).
	Returns (stem, ending)."""
	i = len(word)
	while i > 0:
		ch = word[i - 1]
		if ch in {COMBINING['visarga'], COMBINING['anusvara'], COMBINING['halant']} or ch in AYOGAVAHA:
			i -= 1
		else:
			break
	return word[:i], word[i:]


VOWEL_GROUPS = {
	'vrddhi': {'आ', 'ऐ', 'औ'},
	'guna': {'अ', 'ए', 'ओ'},
	'ic': {'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ॠ', 'ऌ', 'ॡ'},
}

VRDDHI = VOWEL_GROUPS['vrddhi']
GUNA = VOWEL_GROUPS['guna']
IK = VOWEL_GROUPS['ic']
MATRA_MAP = VOWELS_MATRA
VOWELS = VOWELS_SET
HAL = CONSONANTS_SET

_MATRA_TO_VOWEL = {}
for vowel, matra in VOWELS_MATRA.items():
	if matra:
		_MATRA_TO_VOWEL[matra] = vowel


def get_vowel_from_matra(matra):
	return _MATRA_TO_VOWEL.get(matra)


def vowel_to_matra(vowel):
	return VOWELS_MATRA.get(vowel, '')
