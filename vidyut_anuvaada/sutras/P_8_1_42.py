# Sutra प.8.1.42: पुरा च परीप्सायाम्
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.42"
SUTRA_TEXT = "पुरा च परीप्सायाम्"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8142:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.42: अग्निः'),
		('रामः', '', 'प.8.1.42: रामः'),
		('सीता', '', 'प.8.1.42: सीता'),
	]

