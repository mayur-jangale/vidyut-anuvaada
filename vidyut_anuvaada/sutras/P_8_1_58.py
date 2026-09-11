# Sutra प.8.1.58: चादिषु च
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.58"
SUTRA_TEXT = "चादिषु च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8158:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.58: अग्निः'),
		('रामः', '', 'प.8.1.58: रामः'),
		('सीता', '', 'प.8.1.58: सीता'),
	]

