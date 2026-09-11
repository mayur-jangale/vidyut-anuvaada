# Sutra प.1.4.70: अदोऽनुपदेशे
# (Samjna (technical definitions)) — ado'nupadeSe

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.70"
SUTRA_TEXT = "अदोऽनुपदेशे"
SUTRA_DESC = "(Samjna (technical definitions)) — ado'nupadeSe"


class Sutra1470:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_70
		return apply_1_4_70(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-adas:अग्निः'),
		('रामः', '', 'not-adas:रामः'),
		('सीता', '', 'not-adas:सीता'),
	]

