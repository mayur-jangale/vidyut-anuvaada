# Sutra प.6.1.48: क्रीङ्जीनां णौ
# sandhi-sūtra प.6.1.48

from P_6_1 import apply_6_1_48

SUTRA_CODE = "प.6.1.48"
SUTRA_TEXT = "क्रीङ्जीनां णौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.48"


class Sutra6148:
	def apply(self, word, pos):
		return apply_6_1_48(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.48:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.48:marker=padartha;input=रामः'),
		('सीता', '', '6.1.48:marker=padartha;input=सीता'),
	]
