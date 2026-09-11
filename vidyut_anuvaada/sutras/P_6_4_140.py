# Sutra प.6.4.140: आतो धातोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.140"
SUTRA_TEXT = "आतो धातोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64140:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.140: अग्निः'),
		('रामः', '', 'प.6.4.140: रामः'),
		('सीता', '', 'प.6.4.140: सीता'),
	]

