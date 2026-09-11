# Sutra प.6.1.183: दिवो झल्
# sandhi-sūtra प.6.1.183

from P_6_1 import apply_6_1_183

SUTRA_CODE = "प.6.1.183"
SUTRA_TEXT = "दिवो झल्"
SUTRA_DESC = "sandhi-sūtra प.6.1.183"


class Sutra61183:
	def apply(self, word, pos):
		return apply_6_1_183(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.183:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.183:marker=padartha;input=रामः'),
		('सीता', '', '6.1.183:marker=padartha;input=सीता'),
	]
