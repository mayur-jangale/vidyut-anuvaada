# Sutra प.6.1.31: णौ च संश्चङोः
# sandhi-sūtra प.6.1.31

from P_6_1 import apply_6_1_31

SUTRA_CODE = "प.6.1.31"
SUTRA_TEXT = "णौ च संश्चङोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.31"


class Sutra6131:
	def apply(self, word, pos):
		return apply_6_1_31(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.31:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.31:marker=padartha;input=रामः'),
		('सीता', '', '6.1.31:marker=padartha;input=सीता'),
	]
