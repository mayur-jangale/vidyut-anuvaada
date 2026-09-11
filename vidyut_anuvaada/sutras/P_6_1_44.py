# Sutra प.6.1.44: विभाषा परेः
# sandhi-sūtra प.6.1.44

from P_6_1 import apply_6_1_44

SUTRA_CODE = "प.6.1.44"
SUTRA_TEXT = "विभाषा परेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.44"


class Sutra6144:
	def apply(self, word, pos):
		return apply_6_1_44(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.44:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.44:marker=padartha;input=रामः'),
		('सीता', '', '6.1.44:marker=padartha;input=सीता'),
	]
