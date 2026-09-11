# Sutra प.6.1.99: नाम्रेडितस्यान्त्यस्य तु वा
# sandhi-sūtra प.6.1.99

from P_6_1 import apply_6_1_99

SUTRA_CODE = "प.6.1.99"
SUTRA_TEXT = "नाम्रेडितस्यान्त्यस्य तु वा"
SUTRA_DESC = "sandhi-sūtra प.6.1.99"


class Sutra6199:
	def apply(self, word, pos):
		return apply_6_1_99(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.99:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.99:marker=padartha;input=रामः'),
		('सीता', '', '6.1.99:marker=padartha;input=सीता'),
	]
