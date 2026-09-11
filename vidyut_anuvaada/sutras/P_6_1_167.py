# Sutra प.6.1.167: चतुरः शसि
# sandhi-sūtra प.6.1.167

from P_6_1 import apply_6_1_167

SUTRA_CODE = "प.6.1.167"
SUTRA_TEXT = "चतुरः शसि"
SUTRA_DESC = "sandhi-sūtra प.6.1.167"


class Sutra61167:
	def apply(self, word, pos):
		return apply_6_1_167(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.167:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.167:marker=padartha;input=रामः'),
		('सीता', '', '6.1.167:marker=padartha;input=सीता'),
	]
