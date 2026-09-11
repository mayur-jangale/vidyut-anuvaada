# Sutra प.1.2.50: इद्गोण्याः
# (Samjna (technical definitions)) — idgoRyAH

from P_1_2 import apply_1_2_50

SUTRA_CODE = "प.1.2.50"
SUTRA_TEXT = "इद्गोण्याः"
SUTRA_DESC = "(Samjna (technical definitions)) — idgoRyAH"


class Sutra1250:
	def apply(self, word, pos):
		return apply_1_2_50(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'non-go-ṇya:अग्निः'),
		('रामः', '', 'non-go-ṇya:रामः'),
		('सीता', '', 'non-go-ṇya:सीता'),
	]

