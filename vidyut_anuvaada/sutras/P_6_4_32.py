# Sutra प.6.4.32: जान्तनशां विभाषा
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.32"
SUTRA_TEXT = "जान्तनशां विभाषा"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.32: अग्निः'),
		('रामः', '', 'प.6.4.32: रामः'),
		('सीता', '', 'प.6.4.32: सीता'),
	]

