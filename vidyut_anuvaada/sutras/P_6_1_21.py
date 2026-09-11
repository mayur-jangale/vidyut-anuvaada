# Sutra प.6.1.21: चायः की
# sandhi-sūtra प.6.1.21

from P_6_1 import apply_6_1_21

SUTRA_CODE = "प.6.1.21"
SUTRA_TEXT = "चायः की"
SUTRA_DESC = "sandhi-sūtra प.6.1.21"


class Sutra6121:
	def apply(self, word, pos):
		return apply_6_1_21(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.21:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.21:marker=padartha;input=रामः'),
		('सीता', '', '6.1.21:marker=padartha;input=सीता'),
	]
