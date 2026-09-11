# Sutra प.6.1.123: अवङ् स्फोटायनस्य
# sandhi-sūtra प.6.1.123

from P_6_1 import apply_6_1_123

SUTRA_CODE = "प.6.1.123"
SUTRA_TEXT = "अवङ् स्फोटायनस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.123"


class Sutra61123:
	def apply(self, word, pos):
		return apply_6_1_123(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.123:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.123:marker=padartha;input=रामः'),
		('सीता', '', '6.1.123:marker=padartha;input=सीता'),
	]
