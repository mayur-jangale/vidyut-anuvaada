# Sutra प.6.1.76: पदान्ताद्वा
# sandhi-sūtra प.6.1.76

from P_6_1 import apply_6_1_76

SUTRA_CODE = "प.6.1.76"
SUTRA_TEXT = "पदान्ताद्वा"
SUTRA_DESC = "sandhi-sūtra प.6.1.76"


class Sutra6176:
	def apply(self, word, pos):
		return apply_6_1_76(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.76:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.76:marker=padartha;input=रामः'),
		('सीता', '', '6.1.76:marker=padartha;input=सीता'),
	]
