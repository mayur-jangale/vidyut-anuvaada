# Sutra प.6.1.152: प्रतिष्कशश्च कशेः
# sandhi-sūtra प.6.1.152

from P_6_1 import apply_6_1_152

SUTRA_CODE = "प.6.1.152"
SUTRA_TEXT = "प्रतिष्कशश्च कशेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.152"


class Sutra61152:
	def apply(self, word, pos):
		return apply_6_1_152(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.152:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.152:marker=padartha;input=रामः'),
		('सीता', '', '6.1.152:marker=padartha;input=सीता'),
	]
