# Sutra प.6.1.180: झल्युपोत्तमम्
# sandhi-sūtra प.6.1.180

from P_6_1 import apply_6_1_180

SUTRA_CODE = "प.6.1.180"
SUTRA_TEXT = "झल्युपोत्तमम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.180"


class Sutra61180:
	def apply(self, word, pos):
		return apply_6_1_180(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.180:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.180:marker=padartha;input=रामः'),
		('सीता', '', '6.1.180:marker=padartha;input=सीता'),
	]
