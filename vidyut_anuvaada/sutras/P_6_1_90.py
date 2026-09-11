# Sutra प.6.1.90: आटश्च
# sandhi-sūtra प.6.1.90

from P_6_1 import apply_6_1_90

SUTRA_CODE = "प.6.1.90"
SUTRA_TEXT = "आटश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.90"


class Sutra6190:
	def apply(self, word, pos):
		return apply_6_1_90(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.90:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.90:marker=padartha;input=रामः'),
		('सीता', '', '6.1.90:marker=padartha;input=सीता'),
	]
