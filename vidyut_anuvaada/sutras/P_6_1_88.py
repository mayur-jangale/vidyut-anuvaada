# Sutra प.6.1.88: वृद्धिरेचि
# sandhi-sūtra प.6.1.88

from P_6_1 import apply_6_1_88

SUTRA_CODE = "प.6.1.88"
SUTRA_TEXT = "वृद्धिरेचि"
SUTRA_DESC = "sandhi-sūtra प.6.1.88"


class Sutra6188:
	def apply(self, word, pos):
		return apply_6_1_88(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.88:input=अग्निः'),
		('रामः', '', '6.1.88:input=रामः'),
		('सीता', '', '6.1.88:input=सीता'),
	]
