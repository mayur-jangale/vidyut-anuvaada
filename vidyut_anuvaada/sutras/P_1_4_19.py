# Sutra प.1.4.19: तसौ मत्वर्थे
# (Samjna (technical definitions)) — tasO matvarTe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.19"
SUTRA_TEXT = "तसौ मत्वर्थे"
SUTRA_DESC = "(Samjna (technical definitions)) — tasO matvarTe"


class Sutra1419:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_19
		return apply_1_4_19(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-mat-artha:अग्निः'),
		('रामः', '', 'not-mat-artha:रामः'),
		('सीता', '', 'not-mat-artha:सीता'),
	]

