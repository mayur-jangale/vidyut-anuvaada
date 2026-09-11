# Sutra प.6.1.10: श्लौ
# sandhi-sūtra प.6.1.10

from P_6_1 import apply_6_1_10

SUTRA_CODE = "प.6.1.10"
SUTRA_TEXT = "श्लौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.10"


class Sutra6110:
	def apply(self, word, pos):
		return apply_6_1_10(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.10:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.10:marker=padartha;input=रामः'),
		('सीता', '', '6.1.10:marker=padartha;input=सीता'),
	]
