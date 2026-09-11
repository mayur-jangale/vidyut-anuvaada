# Sutra प.6.1.8: लिटि धातोरनभ्यासस्य
# sandhi-sūtra प.6.1.8

from P_6_1 import apply_6_1_8

SUTRA_CODE = "प.6.1.8"
SUTRA_TEXT = "लिटि धातोरनभ्यासस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.8"


class Sutra618:
	def apply(self, word, pos):
		return apply_6_1_8(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.8:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.8:marker=padartha;input=रामः'),
		('सीता', '', '6.1.8:marker=padartha;input=सीता'),
	]
