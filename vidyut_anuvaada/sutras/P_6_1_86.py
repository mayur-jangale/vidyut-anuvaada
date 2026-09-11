# Sutra प.6.1.86: षत्वतुकोरसिद्धः
# sandhi-sūtra प.6.1.86

from P_6_1 import apply_6_1_86

SUTRA_CODE = "प.6.1.86"
SUTRA_TEXT = "षत्वतुकोरसिद्धः"
SUTRA_DESC = "sandhi-sūtra प.6.1.86"


class Sutra6186:
	def apply(self, word, pos):
		return apply_6_1_86(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.86:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.86:marker=padartha;input=रामः'),
		('सीता', '', '6.1.86:marker=padartha;input=सीता'),
	]
