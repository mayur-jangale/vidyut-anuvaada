# Sutra प.6.1.37: न सम्प्रसारणे सम्प्रसारणम्
# sandhi-sūtra प.6.1.37

from P_6_1 import apply_6_1_37

SUTRA_CODE = "प.6.1.37"
SUTRA_TEXT = "न सम्प्रसारणे सम्प्रसारणम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.37"


class Sutra6137:
	def apply(self, word, pos):
		return apply_6_1_37(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.37:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.37:marker=padartha;input=रामः'),
		('सीता', '', '6.1.37:marker=padartha;input=सीता'),
	]
