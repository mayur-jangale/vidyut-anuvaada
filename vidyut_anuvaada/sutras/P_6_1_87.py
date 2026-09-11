# Sutra प.6.1.87: आद्गुणः
# sandhi-sūtra प.6.1.87

from P_6_1 import apply_6_1_87

SUTRA_CODE = "प.6.1.87"
SUTRA_TEXT = "आद्गुणः"
SUTRA_DESC = "sandhi-sūtra प.6.1.87"


class Sutra6187:
	def apply(self, word, pos):
		return apply_6_1_87(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.87:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.87:marker=padartha;input=रामः'),
		('सीता', '', '6.1.87:marker=padartha;input=सीता'),
	]
