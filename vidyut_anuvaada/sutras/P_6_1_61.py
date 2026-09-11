# Sutra प.6.1.61: ये च तद्धिते
# sandhi-sūtra प.6.1.61

from P_6_1 import apply_6_1_61

SUTRA_CODE = "प.6.1.61"
SUTRA_TEXT = "ये च तद्धिते"
SUTRA_DESC = "sandhi-sūtra प.6.1.61"


class Sutra6161:
	def apply(self, word, pos):
		return apply_6_1_61(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.61:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.61:marker=padartha;input=रामः'),
		('सीता', '', '6.1.61:marker=padartha;input=सीता'),
	]
