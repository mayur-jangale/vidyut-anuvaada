# Sutra प.6.1.111: ऋत उत्
# sandhi-sūtra प.6.1.111

from P_6_1 import apply_6_1_111

SUTRA_CODE = "प.6.1.111"
SUTRA_TEXT = "ऋत उत्"
SUTRA_DESC = "sandhi-sūtra प.6.1.111"


class Sutra61111:
	def apply(self, word, pos):
		return apply_6_1_111(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.111:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.111:marker=padartha;input=रामः'),
		('सीता', '', '6.1.111:marker=padartha;input=सीता'),
	]
