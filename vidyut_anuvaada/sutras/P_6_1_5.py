# Sutra प.6.1.5: उभे अभ्यस्तम्
# sandhi-sūtra प.6.1.5

from P_6_1 import apply_6_1_5

SUTRA_CODE = "प.6.1.5"
SUTRA_TEXT = "उभे अभ्यस्तम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.5"


class Sutra615:
	def apply(self, word, pos):
		return apply_6_1_5(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.5:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.5:marker=padartha;input=रामः'),
		('सीता', '', '6.1.5:marker=padartha;input=सीता'),
	]
