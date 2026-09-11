# Sutra प.7.1.22: षड्भ्यो लुक्
# (Taddhita (secondary derivations)) — zaqByo luk

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.22"
SUTRA_TEXT = "षड्भ्यो लुक्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — zaqByo luk"


class Sutra7122:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.22: अग्निः'),
		('रामः', '', 'प.7.1.22: रामः'),
		('सीता', '', 'प.7.1.22: सीता'),
	]

