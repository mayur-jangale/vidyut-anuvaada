# Sutra प.6.1.223: समासस्य
# sandhi-sūtra प.6.1.223

from P_6_1 import apply_6_1_223

SUTRA_CODE = "प.6.1.223"
SUTRA_TEXT = "समासस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.223"


class Sutra61223:
	def apply(self, word, pos):
		return apply_6_1_223(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.223:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.223:marker=padartha;input=रामः'),
		('सीता', '', '6.1.223:marker=padartha;input=सीता'),
	]
