# Sutra प.6.1.141: हिंसायां प्रतेश्च
# sandhi-sūtra प.6.1.141

from P_6_1 import apply_6_1_141

SUTRA_CODE = "प.6.1.141"
SUTRA_TEXT = "हिंसायां प्रतेश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.141"


class Sutra61141:
	def apply(self, word, pos):
		return apply_6_1_141(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.141:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.141:marker=padartha;input=रामः'),
		('सीता', '', '6.1.141:marker=padartha;input=सीता'),
	]
