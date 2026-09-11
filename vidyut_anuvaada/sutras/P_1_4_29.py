# Sutra प.1.4.29: आख्यातोपयोगे
# (Samjna (technical definitions)) — AKyAtopayoge

from sutra_engines import apply_general

SUTRA_CODE = "प.1.4.29"
SUTRA_TEXT = "आख्यातोपयोगे"
SUTRA_DESC = "(Samjna (technical definitions)) — AKyAtopayoge"


class Sutra1429:
	def apply(self, word, pos):
		from P_1_4 import apply_1_4_29
		return apply_1_4_29(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'not-akhyAta-kartA:अग्निः'),
		('रामः', '', 'not-akhyAta-kartA:रामः'),
		('सीता', '', 'not-akhyAta-kartA:सीता'),
	]

