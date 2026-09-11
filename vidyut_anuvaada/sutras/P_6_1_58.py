# Sutra प.6.1.58: सृजिदृशोर्झल्यमकिति
# sandhi-sūtra प.6.1.58

from P_6_1 import apply_6_1_58

SUTRA_CODE = "प.6.1.58"
SUTRA_TEXT = "सृजिदृशोर्झल्यमकिति"
SUTRA_DESC = "sandhi-sūtra प.6.1.58"


class Sutra6158:
	def apply(self, word, pos):
		return apply_6_1_58(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.58:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.58:marker=padartha;input=रामः'),
		('सीता', '', '6.1.58:marker=padartha;input=सीता'),
	]
