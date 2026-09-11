# Sutra प.7.3.45: न यासयोः
# (Taddhita (secondary derivations)) — na yAsayoH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.45"
SUTRA_TEXT = "न यासयोः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — na yAsayoH"


class Sutra7345:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.45: अग्निः'),
		('रामः', '', 'प.7.3.45: रामः'),
		('सीता', '', 'प.7.3.45: सीता'),
	]

