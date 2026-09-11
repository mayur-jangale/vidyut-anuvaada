# Sutra प.6.1.56: बिभेतेर्हेतुभये
# sandhi-sūtra प.6.1.56

from P_6_1 import apply_6_1_56

SUTRA_CODE = "प.6.1.56"
SUTRA_TEXT = "बिभेतेर्हेतुभये"
SUTRA_DESC = "sandhi-sūtra प.6.1.56"


class Sutra6156:
	def apply(self, word, pos):
		return apply_6_1_56(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.56:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.56:marker=padartha;input=रामः'),
		('सीता', '', '6.1.56:marker=padartha;input=सीता'),
	]
