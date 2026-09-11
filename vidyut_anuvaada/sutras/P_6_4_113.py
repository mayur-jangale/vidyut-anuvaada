# Sutra प.6.4.113: ई हल्यघोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.113"
SUTRA_TEXT = "ई हल्यघोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64113:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.113: अग्निः'),
		('रामः', '', 'प.6.4.113: रामः'),
		('सीता', '', 'प.6.4.113: सीता'),
	]

