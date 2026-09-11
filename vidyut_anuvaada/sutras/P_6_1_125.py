# Sutra प.6.1.125: प्लुतप्रगृह्या अचि नित्यम्
# sandhi-sūtra प.6.1.125

from P_6_1 import apply_6_1_125

SUTRA_CODE = "प.6.1.125"
SUTRA_TEXT = "प्लुतप्रगृह्या अचि नित्यम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.125"


class Sutra61125:
	def apply(self, word, pos):
		return apply_6_1_125(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.125:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.125:marker=padartha;input=रामः'),
		('सीता', '', '6.1.125:marker=padartha;input=सीता'),
	]
