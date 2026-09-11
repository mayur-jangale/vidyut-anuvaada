# Sutra प.6.1.20: न वशः
# sandhi-sūtra प.6.1.20

from P_6_1 import apply_6_1_20

SUTRA_CODE = "प.6.1.20"
SUTRA_TEXT = "न वशः"
SUTRA_DESC = "sandhi-sūtra प.6.1.20"


class Sutra6120:
	def apply(self, word, pos):
		return apply_6_1_20(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.20:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.20:marker=padartha;input=रामः'),
		('सीता', '', '6.1.20:marker=padartha;input=सीता'),
	]
