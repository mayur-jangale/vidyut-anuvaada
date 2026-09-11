# Sutra प.6.1.11: चङि
# sandhi-sūtra प.6.1.11

from P_6_1 import apply_6_1_11

SUTRA_CODE = "प.6.1.11"
SUTRA_TEXT = "चङि"
SUTRA_DESC = "sandhi-sūtra प.6.1.11"


class Sutra6111:
	def apply(self, word, pos):
		return apply_6_1_11(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.11:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.11:marker=padartha;input=रामः'),
		('सीता', '', '6.1.11:marker=padartha;input=सीता'),
	]
