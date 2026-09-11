# Sutra प.6.1.93: औतोऽम्शसोः
# sandhi-sūtra प.6.1.93

from P_6_1 import apply_6_1_93

SUTRA_CODE = "प.6.1.93"
SUTRA_TEXT = "औतोऽम्शसोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.93"


class Sutra6193:
	def apply(self, word, pos):
		return apply_6_1_93(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.93:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.93:marker=padartha;input=रामः'),
		('सीता', '', '6.1.93:marker=padartha;input=सीता'),
	]
