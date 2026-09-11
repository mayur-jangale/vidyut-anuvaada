# Sutra प.6.1.81: क्षय्यजय्यौ शक्यार्थे
# sandhi-sūtra प.6.1.81

from P_6_1 import apply_6_1_81

SUTRA_CODE = "प.6.1.81"
SUTRA_TEXT = "क्षय्यजय्यौ शक्यार्थे"
SUTRA_DESC = "sandhi-sūtra प.6.1.81"


class Sutra6181:
	def apply(self, word, pos):
		return apply_6_1_81(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.81:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.81:marker=padartha;input=रामः'),
		('सीता', '', '6.1.81:marker=padartha;input=सीता'),
	]
