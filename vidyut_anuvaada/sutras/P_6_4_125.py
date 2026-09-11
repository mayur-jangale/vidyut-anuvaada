# Sutra प.6.4.125: फणां च सप्तानाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.125"
SUTRA_TEXT = "फणां च सप्तानाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra64125:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.125: अग्निः'),
		('रामः', '', 'प.6.4.125: रामः'),
		('सीता', '', 'प.6.4.125: सीता'),
	]

