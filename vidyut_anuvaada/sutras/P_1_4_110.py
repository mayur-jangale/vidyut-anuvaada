# Sutra प.1.4.110: विरामोऽवसानम्
# (Samjna (technical definitions)) — virAmo'vasAnam

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.110"
SUTRA_TEXT = "विरामोऽवसानम्"
SUTRA_DESC = "(Samjna (technical definitions)) — virAmo'vasAnam"


class Sutra14110:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_110
		return apply_1_4_110(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'normal:अग्निः'),
		('रामः', '', 'normal:रामः'),
		('सीता', '', 'normal:सीता'),
	]

