# Sutra प.6.1.33: अभ्यस्तस्य च
# sandhi-sūtra प.6.1.33

from P_6_1 import apply_6_1_33

SUTRA_CODE = "प.6.1.33"
SUTRA_TEXT = "अभ्यस्तस्य च"
SUTRA_DESC = "sandhi-sūtra प.6.1.33"


class Sutra6133:
	def apply(self, word, pos):
		return apply_6_1_33(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.33:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.33:marker=padartha;input=रामः'),
		('सीता', '', '6.1.33:marker=padartha;input=सीता'),
	]
