# Sutra प.6.1.108: सम्प्रसारणाच्च
# sandhi-sūtra प.6.1.108

from P_6_1 import apply_6_1_108

SUTRA_CODE = "प.6.1.108"
SUTRA_TEXT = "सम्प्रसारणाच्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.108"


class Sutra61108:
	def apply(self, word, pos):
		return apply_6_1_108(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.108:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.108:marker=padartha;input=रामः'),
		('सीता', '', '6.1.108:marker=padartha;input=सीता'),
	]
