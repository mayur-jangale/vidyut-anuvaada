# Sutra प.8.1.26: सपूर्वायाः प्रथमाया विभाषा
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.26"
SUTRA_TEXT = "सपूर्वायाः प्रथमाया विभाषा"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8126:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.26: अग्निः'),
		('रामः', '', 'प.8.1.26: रामः'),
		('सीता', '', 'प.8.1.26: सीता'),
	]

