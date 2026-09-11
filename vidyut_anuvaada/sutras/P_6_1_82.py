# Sutra प.6.1.82: क्रय्यस्तदर्थे
# sandhi-sūtra प.6.1.82

from P_6_1 import apply_6_1_82

SUTRA_CODE = "प.6.1.82"
SUTRA_TEXT = "क्रय्यस्तदर्थे"
SUTRA_DESC = "sandhi-sūtra प.6.1.82"


class Sutra6182:
	def apply(self, word, pos):
		return apply_6_1_82(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.82:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.82:marker=padartha;input=रामः'),
		('सीता', '', '6.1.82:marker=padartha;input=सीता'),
	]
