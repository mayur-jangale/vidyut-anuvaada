# Sutra प.7.2.45: रधादिभ्यश्च
# (Taddhita (secondary derivations)) — raDAdiByaSca

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.45"
SUTRA_TEXT = "रधादिभ्यश्च"
SUTRA_DESC = "(Taddhita (secondary derivations)) — raDAdiByaSca"


class Sutra7245:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.45: अग्निः'),
		('रामः', '', 'प.7.2.45: रामः'),
		('सीता', '', 'प.7.2.45: सीता'),
	]

