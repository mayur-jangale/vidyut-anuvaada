# Sutra प.6.1.24: द्रवमूर्तिस्पर्शयोः श्यः
# sandhi-sūtra प.6.1.24

from P_6_1 import apply_6_1_24

SUTRA_CODE = "प.6.1.24"
SUTRA_TEXT = "द्रवमूर्तिस्पर्शयोः श्यः"
SUTRA_DESC = "sandhi-sūtra प.6.1.24"


class Sutra6124:
	def apply(self, word, pos):
		return apply_6_1_24(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.24:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.24:marker=padartha;input=रामः'),
		('सीता', '', '6.1.24:marker=padartha;input=सीता'),
	]
