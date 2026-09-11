# Sutra प.1.4.12: दीर्घं च
# (Samjna (technical definitions)) — dIrGaM ca

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.12"
SUTRA_TEXT = "दीर्घं च"
SUTRA_DESC = "(Samjna (technical definitions)) — dIrGaM ca"


class Sutra1412:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_12
		return apply_1_4_12(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-dirgha-guru:अग्निः'),
		('रामः', '', 'not-dirgha-guru:रामः'),
		('सीता', '', 'not-dirgha-guru:सीता'),
	]

