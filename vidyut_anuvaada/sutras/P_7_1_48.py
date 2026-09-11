# Sutra प.7.1.48: इष्ट्वीनमिति च
# (Taddhita (secondary derivations)) — izwvInamiti ca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.48"
SUTRA_TEXT = "इष्ट्वीनमिति च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — izwvInamiti ca"


class Sutra7148:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.48: अग्निः'),
		('रामः', '', 'प.7.1.48: रामः'),
		('सीता', '', 'प.7.1.48: सीता'),
	]

