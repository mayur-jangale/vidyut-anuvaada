# Sutra प.6.1.210: नित्यं मन्त्रे
# sandhi-sūtra प.6.1.210

from P_6_1 import apply_6_1_210

SUTRA_CODE = "प.6.1.210"
SUTRA_TEXT = "नित्यं मन्त्रे"
SUTRA_DESC = "sandhi-sūtra प.6.1.210"


class Sutra61210:
	def apply(self, word, pos):
		return apply_6_1_210(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.210:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.210:marker=padartha;input=रामः'),
		('सीता', '', '6.1.210:marker=padartha;input=सीता'),
	]
