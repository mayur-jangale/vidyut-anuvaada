# Sutra प.6.1.18: स्वापेश्चङि
# sandhi-sūtra प.6.1.18

from P_6_1 import apply_6_1_18

SUTRA_CODE = "प.6.1.18"
SUTRA_TEXT = "स्वापेश्चङि"
SUTRA_DESC = "sandhi-sūtra प.6.1.18"


class Sutra6118:
	def apply(self, word, pos):
		return apply_6_1_18(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.18:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.18:marker=padartha;input=रामः'),
		('सीता', '', '6.1.18:marker=padartha;input=सीता'),
	]
