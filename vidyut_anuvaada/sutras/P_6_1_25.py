# Sutra प.6.1.25: प्रतेश्च
# sandhi-sūtra प.6.1.25

from P_6_1 import apply_6_1_25

SUTRA_CODE = "प.6.1.25"
SUTRA_TEXT = "प्रतेश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.25"


class Sutra6125:
	def apply(self, word, pos):
		return apply_6_1_25(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.25:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.25:marker=padartha;input=रामः'),
		('सीता', '', '6.1.25:marker=padartha;input=सीता'),
	]
