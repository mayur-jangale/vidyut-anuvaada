# Sutra प.6.1.32: ह्वः सम्प्रसारणम्
# sandhi-sūtra प.6.1.32

from P_6_1 import apply_6_1_32

SUTRA_CODE = "प.6.1.32"
SUTRA_TEXT = "ह्वः सम्प्रसारणम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.32"


class Sutra6132:
	def apply(self, word, pos):
		return apply_6_1_32(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.32:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.32:marker=padartha;input=रामः'),
		('सीता', '', '6.1.32:marker=padartha;input=सीता'),
	]
