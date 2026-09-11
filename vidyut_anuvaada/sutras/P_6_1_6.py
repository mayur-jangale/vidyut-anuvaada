# Sutra प.6.1.6: जक्षित्यादयः षट्
# sandhi-sūtra प.6.1.6

from P_6_1 import apply_6_1_6

SUTRA_CODE = "प.6.1.6"
SUTRA_TEXT = "जक्षित्यादयः षट्"
SUTRA_DESC = "sandhi-sūtra प.6.1.6"


class Sutra616:
	def apply(self, word, pos):
		return apply_6_1_6(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.6:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.6:marker=padartha;input=रामः'),
		('सीता', '', '6.1.6:marker=padartha;input=सीता'),
	]
