# Sutra प.6.1.13: ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे
# sandhi-sūtra प.6.1.13

from P_6_1 import apply_6_1_13

SUTRA_CODE = "प.6.1.13"
SUTRA_TEXT = "ष्यङः सम्प्रसारणं पुत्रपत्योस्तत्पुरुषे"
SUTRA_DESC = "sandhi-sūtra प.6.1.13"


class Sutra6113:
	def apply(self, word, pos):
		return apply_6_1_13(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.13:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.13:marker=padartha;input=रामः'),
		('सीता', '', '6.1.13:marker=padartha;input=सीता'),
	]
