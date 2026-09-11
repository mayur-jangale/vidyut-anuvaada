# Sutra प.6.1.100: नित्यमाम्रेडिते डाचि
# sandhi-sūtra प.6.1.100

from P_6_1 import apply_6_1_100

SUTRA_CODE = "प.6.1.100"
SUTRA_TEXT = "नित्यमाम्रेडिते डाचि"
SUTRA_DESC = "sandhi-sūtra प.6.1.100"


class Sutra61100:
	def apply(self, word, pos):
		return apply_6_1_100(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.100:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.100:marker=padartha;input=रामः'),
		('सीता', '', '6.1.100:marker=padartha;input=सीता'),
	]
