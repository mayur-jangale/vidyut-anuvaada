# Sutra प.6.1.147: आश्चर्यमनित्ये
# sandhi-sūtra प.6.1.147

from P_6_1 import apply_6_1_147

SUTRA_CODE = "प.6.1.147"
SUTRA_TEXT = "आश्चर्यमनित्ये"
SUTRA_DESC = "sandhi-sūtra प.6.1.147"


class Sutra61147:
	def apply(self, word, pos):
		return apply_6_1_147(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.147:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.147:marker=padartha;input=रामः'),
		('सीता', '', '6.1.147:marker=padartha;input=सीता'),
	]
