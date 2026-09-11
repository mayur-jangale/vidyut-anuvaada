# Sutra प.6.1.7: तुजादीनां दीर्घोऽभ्यासस्य
# sandhi-sūtra प.6.1.7

from P_6_1 import apply_6_1_7

SUTRA_CODE = "प.6.1.7"
SUTRA_TEXT = "तुजादीनां दीर्घोऽभ्यासस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.7"


class Sutra617:
	def apply(self, word, pos):
		return apply_6_1_7(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.7:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.7:marker=padartha;input=रामः'),
		('सीता', '', '6.1.7:marker=padartha;input=सीता'),
	]
