# Sutra प.6.1.23: स्त्यः प्रपूर्वस्य
# sandhi-sūtra प.6.1.23

from P_6_1 import apply_6_1_23

SUTRA_CODE = "प.6.1.23"
SUTRA_TEXT = "स्त्यः प्रपूर्वस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.23"


class Sutra6123:
	def apply(self, word, pos):
		return apply_6_1_23(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.23:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.23:marker=padartha;input=रामः'),
		('सीता', '', '6.1.23:marker=padartha;input=सीता'),
	]
