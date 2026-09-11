# Sutra प.8.1.28: तिङ्ङतिङः
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.28"
SUTRA_TEXT = "तिङ्ङतिङः"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8128:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.28: अग्निः'),
		('रामः', '', 'प.8.1.28: रामः'),
		('सीता', '', 'प.8.1.28: सीता'),
	]

