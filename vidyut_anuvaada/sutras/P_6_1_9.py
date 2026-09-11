# Sutra प.6.1.9: सन्यङोः
# sandhi-sūtra प.6.1.9

from P_6_1 import apply_6_1_9

SUTRA_CODE = "प.6.1.9"
SUTRA_TEXT = "सन्यङोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.9"


class Sutra619:
	def apply(self, word, pos):
		return apply_6_1_9(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.9:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.9:marker=padartha;input=रामः'),
		('सीता', '', '6.1.9:marker=padartha;input=सीता'),
	]
