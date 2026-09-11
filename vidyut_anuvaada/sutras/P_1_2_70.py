# Sutra प.1.2.70: पिता मात्रा
# (Samjna (technical definitions)) — pitA mAtrA

from P_1_2 import apply_1_2_70

SUTRA_CODE = "प.1.2.70"
SUTRA_TEXT = "पिता मात्रा"
SUTRA_DESC = "(Samjna (technical definitions)) — pitA mAtrA"


class Sutra1270:
	def apply(self, word, pos):
		return apply_1_2_70(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-pitṛ-mātṛ:अग्निः'),
		('रामः', '', 'non-pitṛ-mātṛ:रामः'),
		('सीता', '', 'non-pitṛ-mātṛ:सीता'),
	]

