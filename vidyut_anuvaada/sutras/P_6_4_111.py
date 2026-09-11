# Sutra प.6.4.111: श्नसोरल्लोपः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.111"
SUTRA_TEXT = "श्नसोरल्लोपः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64111:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.111: अग्निः'),
		('रामः', '', 'प.6.4.111: रामः'),
		('सीता', '', 'प.6.4.111: सीता'),
	]

