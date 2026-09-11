# Sutra प.6.1.19: स्वपिस्यमिव्येञां यङि
# sandhi-sūtra प.6.1.19

from P_6_1 import apply_6_1_19

SUTRA_CODE = "प.6.1.19"
SUTRA_TEXT = "स्वपिस्यमिव्येञां यङि"
SUTRA_DESC = "sandhi-sūtra प.6.1.19"


class Sutra6119:
	def apply(self, word, pos):
		return apply_6_1_19(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.19:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.19:marker=padartha;input=रामः'),
		('सीता', '', '6.1.19:marker=padartha;input=सीता'),
	]
