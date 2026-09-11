# Sutra प.6.1.42: ज्यश्च
# sandhi-sūtra प.6.1.42

from P_6_1 import apply_6_1_42

SUTRA_CODE = "प.6.1.42"
SUTRA_TEXT = "ज्यश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.42"


class Sutra6142:
	def apply(self, word, pos):
		return apply_6_1_42(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.42:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.42:marker=padartha;input=रामः'),
		('सीता', '', '6.1.42:marker=padartha;input=सीता'),
	]
