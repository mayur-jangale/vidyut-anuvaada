# Sutra प.7.3.118: औत्
# (Taddhita (secondary derivations)) — Ot

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.118"
SUTRA_TEXT = "औत्"
SUTRA_DESC = "(Taddhita (secondary derivations)) — Ot"


class Sutra73118:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.118: अग्निः'),
		('रामः', '', 'प.7.3.118: रामः'),
		('सीता', '', 'प.7.3.118: सीता'),
	]

