# Sutra प.1.3.69: गृधिवञ्च्योः प्रलम्भने
from P_1_3 import apply_1_3_69


class Sutra1369:
	def apply(self, word, pos):
		return apply_1_3_69(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_69:अग्निः'),
		('रामः', '', 'sutra_69:रामः'),
		('सीता', '', 'sutra_69:सीता'),
	]

