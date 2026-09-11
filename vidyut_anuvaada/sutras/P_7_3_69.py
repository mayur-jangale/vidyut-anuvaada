# Sutra प.7.3.69: भोज्यं भक्ष्ये
# (Taddhita (secondary derivations)) — BojyaM Bakzye

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.69"
SUTRA_TEXT = "भोज्यं भक्ष्ये"
SUTRA_DESC = "(Taddhita (secondary derivations)) — BojyaM Bakzye"


class Sutra7369:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.69: अग्निः'),
		('रामः', '', 'प.7.3.69: रामः'),
		('सीता', '', 'प.7.3.69: सीता'),
	]

