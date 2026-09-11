# Sutra प.6.4.14: अत्वसन्तस्य चाधातोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.14"
SUTRA_TEXT = "अत्वसन्तस्य चाधातोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6414:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.14: अग्निः'),
		('रामः', '', 'प.6.4.14: रामः'),
		('सीता', '', 'प.6.4.14: सीता'),
	]

