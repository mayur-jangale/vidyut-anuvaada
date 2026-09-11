# Sutra प.6.1.177: नामन्यतरस्याम्
# sandhi-sūtra प.6.1.177

from P_6_1 import apply_6_1_177

SUTRA_CODE = "प.6.1.177"
SUTRA_TEXT = "नामन्यतरस्याम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.177"


class Sutra61177:
	def apply(self, word, pos):
		return apply_6_1_177(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.177:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.177:marker=padartha;input=रामः'),
		('सीता', '', '6.1.177:marker=padartha;input=सीता'),
	]
