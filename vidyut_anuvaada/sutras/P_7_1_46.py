# Sutra प.7.1.46: इदन्तो मसि
# (Taddhita (secondary derivations)) — idanto masi

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.46"
SUTRA_TEXT = "इदन्तो मसि"
SUTRA_DESC = "(Taddhita (secondary derivations)) — idanto masi"


class Sutra7146:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.46: अग्निः'),
		('रामः', '', 'प.7.1.46: रामः'),
		('सीता', '', 'प.7.1.46: सीता'),
	]

