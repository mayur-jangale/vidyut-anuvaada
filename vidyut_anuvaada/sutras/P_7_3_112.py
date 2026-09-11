# Sutra प.7.3.112: आण्नद्याः
# (Taddhita (secondary derivations)) — ARnadyAH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.112"
SUTRA_TEXT = "आण्नद्याः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ARnadyAH"


class Sutra73112:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.112: अग्निः'),
		('रामः', '', 'प.7.3.112: रामः'),
		('सीता', '', 'प.7.3.112: सीता'),
	]

