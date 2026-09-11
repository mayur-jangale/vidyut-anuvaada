# Sutra प.6.1.2: अजादेर्द्वितीयस्य
# sandhi-sūtra प.6.1.2

from P_6_1 import apply_6_1_2

SUTRA_CODE = "प.6.1.2"
SUTRA_TEXT = "अजादेर्द्वितीयस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.2"


class Sutra612:
	def apply(self, word, pos):
		return apply_6_1_2(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.2:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.2:marker=padartha;input=रामः'),
		('सीता', '', '6.1.2:marker=padartha;input=सीता'),
	]
