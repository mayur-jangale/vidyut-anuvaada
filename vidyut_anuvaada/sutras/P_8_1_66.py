# Sutra प.8.1.66: यद्वृत्तान्नित्यं
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.66"
SUTRA_TEXT = "यद्वृत्तान्नित्यं"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8166:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.66: अग्निः'),
		('रामः', '', 'प.8.1.66: रामः'),
		('सीता', '', 'प.8.1.66: सीता'),
	]

