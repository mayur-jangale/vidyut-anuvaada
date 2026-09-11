# Sutra प.6.4.57: विभाषापः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.57"
SUTRA_TEXT = "विभाषापः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6457:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.57: अग्निः'),
		('रामः', '', 'प.6.4.57: रामः'),
		('सीता', '', 'प.6.4.57: सीता'),
	]

