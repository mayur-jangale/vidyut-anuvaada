# Sutra प.7.1.18: औङ आपः
# (Taddhita (secondary derivations)) — ONa ApaH

from sutra_engines import apply_general

SUTRA_CODE = "प.7.1.18"
SUTRA_TEXT = "औङ आपः"
SUTRA_DESC = "(Taddhita (secondary derivations)) — ONa ApaH"


class Sutra7118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.1.18: अग्निः'),
		('रामः', '', 'प.7.1.18: रामः'),
		('सीता', '', 'प.7.1.18: सीता'),
	]

