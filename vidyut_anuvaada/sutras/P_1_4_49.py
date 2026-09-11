# Sutra प.1.4.49: कर्तुरीप्सिततमं कर्म
# (Samjna (technical definitions)) — karturIpsitatamaM karma

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.49"
SUTRA_TEXT = "कर्तुरीप्सिततमं कर्म"
SUTRA_DESC = "(Samjna (technical definitions)) — karturIpsitatamaM karma"


class Sutra1449:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_49
		return apply_1_4_49(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-ipsitatama-karman:अग्निः'),
		('रामः', '', 'not-ipsitatama-karman:रामः'),
		('सीता', '', 'not-ipsitatama-karman:सीता'),
	]

