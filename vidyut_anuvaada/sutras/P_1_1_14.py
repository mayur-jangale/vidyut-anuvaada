# Sutra प.1.1.14: निपात एकाजनाङ्
# nipāta (particles) are of single syllable ending in a short vowel or consonant

from sutra_engines import apply_general

SUTRA_CODE = "प.1.1.14"
SUTRA_TEXT = "निपात एकाजनाङ्"
SUTRA_DESC = "nipāta (particles) are of single syllable ending in a short vowel or consonant"


class Sutra1114:
	def apply(self, word, pos):
		from P_1_1 import apply_1_1_14
		return apply_1_1_14(word, pos)

	EXAMPLES = [
		('च', '', 'nipāta:च'),
		('तु', '', 'nipāta:तु'),
		('देव', '', 'candidate:देव'),
	]

