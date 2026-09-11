# Sutra प.8.1.34: हि च
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.34"
SUTRA_TEXT = "हि च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.34: अग्निः'),
		('रामः', '', 'प.8.1.34: रामः'),
		('सीता', '', 'प.8.1.34: सीता'),
	]

