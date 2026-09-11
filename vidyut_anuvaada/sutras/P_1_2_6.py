# Sutra प.1.2.6: इन्धिभवतिभ्यां च
# (Samjna (technical definitions)) — inDiBavatiByAM ca

from P_1_2 import apply_1_2_6

SUTRA_CODE = "प.1.2.6"
SUTRA_TEXT = "इन्धिभवतिभ्यां च"
SUTRA_DESC = "(Samjna (technical definitions)) — inDiBavatiByAM ca"


class Sutra126:
	def apply(self, word, pos):
		return apply_1_2_6(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-indhi-bhavati:अग्निः'),
		('रामः', '', 'non-indhi-bhavati:रामः'),
		('सीता', '', 'non-indhi-bhavati:सीता'),
	]

