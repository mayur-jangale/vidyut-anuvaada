# Sutra प.1.4.15: नः क्ये
# (Samjna (technical definitions)) — naH kye

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.15"
SUTRA_TEXT = "नः क्ये"
SUTRA_DESC = "(Samjna (technical definitions)) — naH kye"


class Sutra1415:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_15
		return apply_1_4_15(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'ok:अग्निः'),
		('रामः', '', 'ok:रामः'),
		('सीता', '', 'ok:सीता'),
	]

