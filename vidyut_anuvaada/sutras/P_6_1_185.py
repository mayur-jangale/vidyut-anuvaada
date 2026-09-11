# Sutra प.6.1.185: तित्स्वरितम्
# sandhi-sūtra प.6.1.185

from P_6_1 import apply_6_1_185

SUTRA_CODE = "प.6.1.185"
SUTRA_TEXT = "तित्स्वरितम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.185"


class Sutra61185:
	def apply(self, word, pos):
		return apply_6_1_185(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.185:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.185:marker=padartha;input=रामः'),
		('सीता', '', '6.1.185:marker=padartha;input=सीता'),
	]
