# Sutra प.8.1.54: हन्त च
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.54"
SUTRA_TEXT = "हन्त च"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8154:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.54: अग्निः'),
		('रामः', '', 'प.8.1.54: रामः'),
		('सीता', '', 'प.8.1.54: सीता'),
	]

