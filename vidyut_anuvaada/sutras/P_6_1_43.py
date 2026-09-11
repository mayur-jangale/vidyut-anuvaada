# Sutra प.6.1.43: व्यश्च
# sandhi-sūtra प.6.1.43

from P_6_1 import apply_6_1_43

SUTRA_CODE = "प.6.1.43"
SUTRA_TEXT = "व्यश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.43"


class Sutra6143:
	def apply(self, word, pos):
		return apply_6_1_43(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.43:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.43:marker=padartha;input=रामः'),
		('सीता', '', '6.1.43:marker=padartha;input=सीता'),
	]
