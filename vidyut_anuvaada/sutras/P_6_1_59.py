# Sutra प.6.1.59: अनुदात्तस्य चर्दुपधस्यान्यतरस्याम्
# sandhi-sūtra प.6.1.59

from P_6_1 import apply_6_1_59

SUTRA_CODE = "प.6.1.59"
SUTRA_TEXT = "अनुदात्तस्य चर्दुपधस्यान्यतरस्याम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.59"


class Sutra6159:
	def apply(self, word, pos):
		return apply_6_1_59(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.59:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.59:marker=padartha;input=रामः'),
		('सीता', '', '6.1.59:marker=padartha;input=सीता'),
	]
