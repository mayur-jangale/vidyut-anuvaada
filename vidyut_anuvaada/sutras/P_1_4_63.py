# Sutra प.1.4.63: आदरानादरयोः सदसती
# (Samjna (technical definitions)) — AdarAnAdarayoH sadasatI

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.63"
SUTRA_TEXT = "आदरानादरयोः सदसती"
SUTRA_DESC = "(Samjna (technical definitions)) — AdarAnAdarayoH sadasatI"


class Sutra1463:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_63
		return apply_1_4_63(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-sadasatI:अग्निः'),
		('रामः', '', 'not-sadasatI:रामः'),
		('सीता', '', 'not-sadasatI:सीता'),
	]

