# Sutra प.6.1.110: ङसिङसोश्च
# sandhi-sūtra प.6.1.110

from P_6_1 import apply_6_1_110

SUTRA_CODE = "प.6.1.110"
SUTRA_TEXT = "ङसिङसोश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.110"


class Sutra61110:
	def apply(self, word, pos):
		return apply_6_1_110(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.110:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.110:marker=padartha;input=रामः'),
		('सीता', '', '6.1.110:marker=padartha;input=सीता'),
	]
