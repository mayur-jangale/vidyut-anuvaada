# Sutra प.6.1.55: प्रजने वीयतेः
# sandhi-sūtra प.6.1.55

from P_6_1 import apply_6_1_55

SUTRA_CODE = "प.6.1.55"
SUTRA_TEXT = "प्रजने वीयतेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.55"


class Sutra6155:
	def apply(self, word, pos):
		return apply_6_1_55(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.55:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.55:marker=padartha;input=रामः'),
		('सीता', '', '6.1.55:marker=padartha;input=सीता'),
	]
