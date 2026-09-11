# Sutra प.6.4.144: नस्तद्धिते
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.144"
SUTRA_TEXT = "नस्तद्धिते"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64144:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.144: अग्निः'),
		('रामः', '', 'प.6.4.144: रामः'),
		('सीता', '', 'प.6.4.144: सीता'),
	]

