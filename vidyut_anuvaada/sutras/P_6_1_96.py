# Sutra प.6.1.96: उस्यपदान्तात्
# sandhi-sūtra प.6.1.96

from P_6_1 import apply_6_1_96

SUTRA_CODE = "प.6.1.96"
SUTRA_TEXT = "उस्यपदान्तात्"
SUTRA_DESC = "sandhi-sūtra प.6.1.96"


class Sutra6196:
	def apply(self, word, pos):
		return apply_6_1_96(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.96:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.96:marker=padartha;input=रामः'),
		('सीता', '', '6.1.96:marker=padartha;input=सीता'),
	]
