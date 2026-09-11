# Sutra प.6.4.72: आडजादीनाम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.72"
SUTRA_TEXT = "आडजादीनाम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6472:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.72: अग्निः'),
		('रामः', '', 'प.6.4.72: रामः'),
		('सीता', '', 'प.6.4.72: सीता'),
	]

