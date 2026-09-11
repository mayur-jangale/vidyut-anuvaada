# Sutra प.6.1.97: अतो गुणे
# sandhi-sūtra प.6.1.97

from P_6_1 import apply_6_1_97

SUTRA_CODE = "प.6.1.97"
SUTRA_TEXT = "अतो गुणे"
SUTRA_DESC = "sandhi-sūtra प.6.1.97"


class Sutra6197:
	def apply(self, word, pos):
		return apply_6_1_97(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.97:input=अग्निः'),
		('रामः', '', '6.1.97:input=रामः'),
		('सीता', '', '6.1.97:input=सीता'),
	]
