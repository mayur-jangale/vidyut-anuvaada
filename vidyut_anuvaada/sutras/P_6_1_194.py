# Sutra प.6.1.194: आदिर्णमुल्यन्यतरस्याम्
# sandhi-sūtra प.6.1.194

from P_6_1 import apply_6_1_194

SUTRA_CODE = "प.6.1.194"
SUTRA_TEXT = "आदिर्णमुल्यन्यतरस्याम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.194"


class Sutra61194:
	def apply(self, word, pos):
		return apply_6_1_194(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.194:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.194:marker=padartha;input=रामः'),
		('सीता', '', '6.1.194:marker=padartha;input=सीता'),
	]
