# Sutra प.6.1.65: णो नः
# sandhi-sūtra प.6.1.65

from P_6_1 import apply_6_1_65

SUTRA_CODE = "प.6.1.65"
SUTRA_TEXT = "णो नः"
SUTRA_DESC = "sandhi-sūtra प.6.1.65"


class Sutra6165:
	def apply(self, word, pos):
		return apply_6_1_65(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.65:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.65:marker=padartha;input=रामः'),
		('सीता', '', '6.1.65:marker=padartha;input=सीता'),
	]
