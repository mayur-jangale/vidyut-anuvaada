# Sutra प.6.1.176: ह्रस्वनुड्भ्यां मतुप्
# sandhi-sūtra प.6.1.176

from P_6_1 import apply_6_1_176

SUTRA_CODE = "प.6.1.176"
SUTRA_TEXT = "ह्रस्वनुड्भ्यां मतुप्"
SUTRA_DESC = "sandhi-sūtra प.6.1.176"


class Sutra61176:
	def apply(self, word, pos):
		return apply_6_1_176(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.176:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.176:marker=padartha;input=रामः'),
		('सीता', '', '6.1.176:marker=padartha;input=सीता'),
	]
