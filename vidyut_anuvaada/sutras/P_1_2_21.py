# Sutra प.1.2.21: उदुपधाद्भावादिकर्मणोरन्यतरस्याम्
# (Samjna (technical definitions)) — udupaDAdBAvAdikarmaRoranyatarasyAm

from P_1_2 import apply_1_2_21

SUTRA_CODE = "प.1.2.21"
SUTRA_TEXT = "उदुपधाद्भावादिकर्मणोरन्यतरस्याम्"
SUTRA_DESC = "(Samjna (technical definitions)) — udupaDAdBAvAdikarmaRoranyatarasyAm"


class Sutra1221:
	def apply(self, word, pos):
		return apply_1_2_21(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-bhāva:अग्निः'),
		('रामः', '', 'non-bhāva:रामः'),
		('सीता', '', 'non-bhāva:सीता'),
	]

