# Sutra प.8.1.70: गतिर्गतौ
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.70"
SUTRA_TEXT = "गतिर्गतौ"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8170:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.70: अग्निः'),
		('रामः', '', 'प.8.1.70: रामः'),
		('सीता', '', 'प.8.1.70: सीता'),
	]

