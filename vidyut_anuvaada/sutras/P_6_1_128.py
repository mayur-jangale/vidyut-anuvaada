# Sutra प.6.1.128: ऋत्यकः
# sandhi-sūtra प.6.1.128

from P_6_1 import apply_6_1_128

SUTRA_CODE = "प.6.1.128"
SUTRA_TEXT = "ऋत्यकः"
SUTRA_DESC = "sandhi-sūtra प.6.1.128"


class Sutra61128:
	def apply(self, word, pos):
		return apply_6_1_128(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.128:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.128:marker=padartha;input=रामः'),
		('सीता', '', '6.1.128:marker=padartha;input=सीता'),
	]
