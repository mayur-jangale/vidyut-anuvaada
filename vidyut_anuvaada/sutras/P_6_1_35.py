# Sutra प.6.1.35: चायः की
# sandhi-sūtra प.6.1.35

from P_6_1 import apply_6_1_35

SUTRA_CODE = "प.6.1.35"
SUTRA_TEXT = "चायः की"
SUTRA_DESC = "sandhi-sūtra प.6.1.35"


class Sutra6135:
	def apply(self, word, pos):
		return apply_6_1_35(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.35:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.35:marker=padartha;input=रामः'),
		('सीता', '', '6.1.35:marker=padartha;input=सीता'),
	]
