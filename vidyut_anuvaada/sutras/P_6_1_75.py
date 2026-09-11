# Sutra प.6.1.75: दीर्घात्
# sandhi-sūtra प.6.1.75

from P_6_1 import apply_6_1_75

SUTRA_CODE = "प.6.1.75"
SUTRA_TEXT = "दीर्घात्"
SUTRA_DESC = "sandhi-sūtra प.6.1.75"


class Sutra6175:
	def apply(self, word, pos):
		return apply_6_1_75(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.75:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.75:marker=padartha;input=रामः'),
		('सीता', '', '6.1.75:marker=padartha;input=सीता'),
	]
