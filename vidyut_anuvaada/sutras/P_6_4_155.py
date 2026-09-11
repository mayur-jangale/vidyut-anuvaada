# Sutra प.6.4.155: टेः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.155"
SUTRA_TEXT = "टेः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64155:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.155: अग्निः'),
		('रामः', '', 'प.6.4.155: रामः'),
		('सीता', '', 'प.6.4.155: सीता'),
	]

