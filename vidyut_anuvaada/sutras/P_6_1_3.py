# Sutra प.6.1.3: न न्द्राः संयोगादयः
# sandhi-sūtra प.6.1.3

from P_6_1 import apply_6_1_3

SUTRA_CODE = "प.6.1.3"
SUTRA_TEXT = "न न्द्राः संयोगादयः"
SUTRA_DESC = "sandhi-sūtra प.6.1.3"


class Sutra613:
	def apply(self, word, pos):
		return apply_6_1_3(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.3:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.3:marker=padartha;input=रामः'),
		('सीता', '', '6.1.3:marker=padartha;input=सीता'),
	]
