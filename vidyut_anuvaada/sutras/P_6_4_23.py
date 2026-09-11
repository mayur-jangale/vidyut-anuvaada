# Sutra प.6.4.23: श्नान्नलोपः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.23"
SUTRA_TEXT = "श्नान्नलोपः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6423:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.23: अग्निः'),
		('रामः', '', 'प.6.4.23: रामः'),
		('सीता', '', 'प.6.4.23: सीता'),
	]

