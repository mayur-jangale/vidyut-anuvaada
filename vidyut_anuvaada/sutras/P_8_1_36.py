# Sutra प.8.1.36: यावद्यथाभ्याम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.36"
SUTRA_TEXT = "यावद्यथाभ्याम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8136:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.36: अग्निः'),
		('रामः', '', 'प.8.1.36: रामः'),
		('सीता', '', 'प.8.1.36: सीता'),
	]

