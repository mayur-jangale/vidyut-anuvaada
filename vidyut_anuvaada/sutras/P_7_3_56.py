# Sutra प.7.3.56: हेरचङि
# (Taddhita (secondary derivations)) — heracaNi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.56"
SUTRA_TEXT = "हेरचङि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — heracaNi"


class Sutra7356:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.56: अग्निः'),
		('रामः', '', 'प.7.3.56: रामः'),
		('सीता', '', 'प.7.3.56: सीता'),
	]

