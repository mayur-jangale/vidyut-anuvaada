# Sutra प.1.4.102: तान्येकवचनद्विवचनबहुवचनान्येकशः
# (Samjna (technical definitions)) — tAnyekavacanadvivacanabahuvacanAnyekaSaH

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.102"
SUTRA_TEXT = "तान्येकवचनद्विवचनबहुवचनान्येकशः"
SUTRA_DESC = "(Samjna (technical definitions)) — tAnyekavacanadvivacanabahuvacanAnyekaSaH"


class Sutra14102:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_102
		return apply_1_4_102(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'no-saMkhyA:अग्निः'),
		('रामः', '', 'no-saMkhyA:रामः'),
		('सीता', '', 'no-saMkhyA:सीता'),
	]

