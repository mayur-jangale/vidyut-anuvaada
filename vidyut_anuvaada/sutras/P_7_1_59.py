# Sutra प.7.1.59: शे मुचादीनाम्
# (Taddhita (secondary derivations)) — Se mucAdInAm

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.59"
SUTRA_TEXT = "शे मुचादीनाम्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Se mucAdInAm"


class Sutra7159:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.59: अग्निः'),
		('रामः', '', 'प.7.1.59: रामः'),
		('सीता', '', 'प.7.1.59: सीता'),
	]

