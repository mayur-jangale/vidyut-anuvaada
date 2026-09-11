# Sutra प.8.1.50: शेषे विभाषा
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.50"
SUTRA_TEXT = "शेषे विभाषा"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8150:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.50: अग्निः'),
		('रामः', '', 'प.8.1.50: रामः'),
		('सीता', '', 'प.8.1.50: सीता'),
	]

