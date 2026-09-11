# Sutra प.8.1.62: चाहलोप एवेत्यवधारणम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.62"
SUTRA_TEXT = "चाहलोप एवेत्यवधारणम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8162:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.62: अग्निः'),
		('रामः', '', 'प.8.1.62: रामः'),
		('सीता', '', 'प.8.1.62: सीता'),
	]

