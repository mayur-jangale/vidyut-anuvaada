# Sutra प.6.1.72: संहितायाम्
# sandhi-sūtra प.6.1.72

from P_6_1 import apply_6_1_72

SUTRA_CODE = "प.6.1.72"
SUTRA_TEXT = "संहितायाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.72"


class Sutra6172:
	def apply(self, word, pos):
		return apply_6_1_72(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.72:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.72:marker=padartha;input=रामः'),
		('सीता', '', '6.1.72:marker=padartha;input=सीता'),
	]
