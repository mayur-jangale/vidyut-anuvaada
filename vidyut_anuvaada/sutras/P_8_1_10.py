# Sutra प.8.1.10: आबाधे च
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.10"
SUTRA_TEXT = "आबाधे च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8110:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.10: अग्निः'),
		('रामः', '', 'प.8.1.10: रामः'),
		('सीता', '', 'प.8.1.10: सीता'),
	]

