# Sutra प.6.1.40: वेञः
# sandhi-sūtra प.6.1.40

from P_6_1 import apply_6_1_40

SUTRA_CODE = "प.6.1.40"
SUTRA_TEXT = "वेञः"
SUTRA_DESC = "sandhi-sūtra प.6.1.40"


class Sutra6140:
	def apply(self, word, pos):
		return apply_6_1_40(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.40:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.40:marker=padartha;input=रामः'),
		('सीता', '', '6.1.40:marker=padartha;input=सीता'),
	]
