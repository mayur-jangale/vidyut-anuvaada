# Sutra प.1.4.23: कारके
# (Samjna (technical definitions)) — kArake

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.23"
SUTRA_TEXT = "कारके"
SUTRA_DESC = "(Samjna (technical definitions)) — kArake"


class Sutra1423:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_23
		return apply_1_4_23(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-karaka:अग्निः'),
		('रामः', '', 'not-karaka:रामः'),
		('सीता', '', 'not-karaka:सीता'),
	]

