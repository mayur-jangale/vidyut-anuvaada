# Sutra प.6.1.171: ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः
# sandhi-sūtra प.6.1.171

from P_6_1 import apply_6_1_171

SUTRA_CODE = "प.6.1.171"
SUTRA_TEXT = "ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः"
SUTRA_DESC = "sandhi-sūtra प.6.1.171"


class Sutra61171:
	def apply(self, word, pos):
		return apply_6_1_171(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.171:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.171:marker=padartha;input=रामः'),
		('सीता', '', '6.1.171:marker=padartha;input=सीता'),
	]
