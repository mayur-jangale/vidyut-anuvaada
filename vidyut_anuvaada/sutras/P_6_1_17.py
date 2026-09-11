# Sutra प.6.1.17: लिट्यभ्यासस्योभयेषाम्
# sandhi-sūtra प.6.1.17

from P_6_1 import apply_6_1_17

SUTRA_CODE = "प.6.1.17"
SUTRA_TEXT = "लिट्यभ्यासस्योभयेषाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.17"


class Sutra6117:
	def apply(self, word, pos):
		return apply_6_1_17(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.17:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.17:marker=padartha;input=रामः'),
		('सीता', '', '6.1.17:marker=padartha;input=सीता'),
	]
