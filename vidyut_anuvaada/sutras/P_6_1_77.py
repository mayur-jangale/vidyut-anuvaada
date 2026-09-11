# Sutra प.6.1.77: इको यणचि
# sandhi-sūtra प.6.1.77

from P_6_1 import apply_6_1_77

SUTRA_CODE = "प.6.1.77"
SUTRA_TEXT = "इको यणचि"
SUTRA_DESC = "sandhi-sūtra प.6.1.77"


class Sutra6177:
	def apply(self, word, pos):
		return apply_6_1_77(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.77:input=अग्निः'),
		('रामः', '', '6.1.77:input=रामः'),
		('सीता', '', '6.1.77:input=सीता'),
	]
