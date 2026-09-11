# Sutra प.8.1.24: न चवाहाहैवयुक्ते
# naścāpadāntasya ṅiḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.1.24"
SUTRA_TEXT = "न चवाहाहैवयुक्ते"
SUTRA_DESC = "naścāpadāntasya ṅiḥ — repeated"


class Sutra8124:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.1.24: अग्निः'),
		('रामः', '', 'प.8.1.24: रामः'),
		('सीता', '', 'प.8.1.24: सीता'),
	]

