# Sutra प.6.1.79: वान्तो यि प्रत्यये
# sandhi-sūtra प.6.1.79

from P_6_1 import apply_6_1_79

SUTRA_CODE = "प.6.1.79"
SUTRA_TEXT = "वान्तो यि प्रत्यये"
SUTRA_DESC = "sandhi-sūtra प.6.1.79"


class Sutra6179:
	def apply(self, word, pos):
		return apply_6_1_79(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.79:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.79:marker=padartha;input=रामः'),
		('सीता', '', '6.1.79:marker=padartha;input=सीता'),
	]
