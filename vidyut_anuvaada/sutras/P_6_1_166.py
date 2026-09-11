# Sutra प.6.1.166: तिसृभ्यो जसः
# sandhi-sūtra प.6.1.166

from P_6_1 import apply_6_1_166

SUTRA_CODE = "प.6.1.166"
SUTRA_TEXT = "तिसृभ्यो जसः"
SUTRA_DESC = "sandhi-sūtra प.6.1.166"


class Sutra61166:
	def apply(self, word, pos):
		return apply_6_1_166(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.166:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.166:marker=padartha;input=रामः'),
		('सीता', '', '6.1.166:marker=padartha;input=सीता'),
	]
