# Sutra प.6.1.57: नित्यं स्मयतेः
# sandhi-sūtra प.6.1.57

from P_6_1 import apply_6_1_57

SUTRA_CODE = "प.6.1.57"
SUTRA_TEXT = "नित्यं स्मयतेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.57"


class Sutra6157:
	def apply(self, word, pos):
		return apply_6_1_57(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.57:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.57:marker=padartha;input=रामः'),
		('सीता', '', '6.1.57:marker=padartha;input=सीता'),
	]
