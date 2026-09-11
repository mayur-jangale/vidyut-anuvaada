# Sutra प.6.1.80: धातोस्तन्निमित्तस्यैव
# sandhi-sūtra प.6.1.80

from P_6_1 import apply_6_1_80

SUTRA_CODE = "प.6.1.80"
SUTRA_TEXT = "धातोस्तन्निमित्तस्यैव"
SUTRA_DESC = "sandhi-sūtra प.6.1.80"


class Sutra6180:
	def apply(self, word, pos):
		return apply_6_1_80(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.80:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.80:marker=padartha;input=रामः'),
		('सीता', '', '6.1.80:marker=padartha;input=सीता'),
	]
