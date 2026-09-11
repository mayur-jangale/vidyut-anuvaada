# Sutra प.1.4.43: दिवः कर्म च
# (Samjna (technical definitions)) — divaH karma ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.43"
SUTRA_TEXT = "दिवः कर्म च"
SUTRA_DESC = "(Samjna (technical definitions)) — divaH karma ca"


class Sutra1443:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_43
		return apply_1_4_43(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-div-karman:अग्निः'),
		('रामः', '', 'not-div-karman:रामः'),
		('सीता', '', 'not-div-karman:सीता'),
	]

