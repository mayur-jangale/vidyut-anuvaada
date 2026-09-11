# Sutra प.6.1.26: विभाषाऽभ्यवपूर्वस्य
# sandhi-sūtra प.6.1.26

from P_6_1 import apply_6_1_26

SUTRA_CODE = "प.6.1.26"
SUTRA_TEXT = "विभाषाऽभ्यवपूर्वस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.26"


class Sutra6126:
	def apply(self, word, pos):
		return apply_6_1_26(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.26:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.26:marker=padartha;input=रामः'),
		('सीता', '', '6.1.26:marker=padartha;input=सीता'),
	]
