# Sutra प.6.1.201: क्षयो निवासे
# sandhi-sūtra प.6.1.201

from P_6_1 import apply_6_1_201

SUTRA_CODE = "प.6.1.201"
SUTRA_TEXT = "क्षयो निवासे"
SUTRA_DESC = "sandhi-sūtra प.6.1.201"


class Sutra61201:
	def apply(self, word, pos):
		return apply_6_1_201(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.201:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.201:marker=padartha;input=रामः'),
		('सीता', '', '6.1.201:marker=padartha;input=सीता'),
	]
