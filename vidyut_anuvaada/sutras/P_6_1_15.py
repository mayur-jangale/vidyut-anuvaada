# Sutra प.6.1.15: वचिस्वपियजादीनां किति
# sandhi-sūtra प.6.1.15

from P_6_1 import apply_6_1_15

SUTRA_CODE = "प.6.1.15"
SUTRA_TEXT = "वचिस्वपियजादीनां किति"
SUTRA_DESC = "sandhi-sūtra प.6.1.15"


class Sutra6115:
	def apply(self, word, pos):
		return apply_6_1_15(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.15:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.15:marker=padartha;input=रामः'),
		('सीता', '', '6.1.15:marker=padartha;input=सीता'),
	]
