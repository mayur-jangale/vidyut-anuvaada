# Sutra प.6.1.30: विभाषा श्वेः
# sandhi-sūtra प.6.1.30

from P_6_1 import apply_6_1_30

SUTRA_CODE = "प.6.1.30"
SUTRA_TEXT = "विभाषा श्वेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.30"


class Sutra6130:
	def apply(self, word, pos):
		return apply_6_1_30(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.30:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.30:marker=padartha;input=रामः'),
		('सीता', '', '6.1.30:marker=padartha;input=सीता'),
	]
