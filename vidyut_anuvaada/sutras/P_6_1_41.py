# Sutra प.6.1.41: ल्यपि च
# sandhi-sūtra प.6.1.41

from P_6_1 import apply_6_1_41

SUTRA_CODE = "प.6.1.41"
SUTRA_TEXT = "ल्यपि च"
SUTRA_DESC = "sandhi-sūtra प.6.1.41"


class Sutra6141:
	def apply(self, word, pos):
		return apply_6_1_41(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.41:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.41:marker=padartha;input=रामः'),
		('सीता', '', '6.1.41:marker=padartha;input=सीता'),
	]
