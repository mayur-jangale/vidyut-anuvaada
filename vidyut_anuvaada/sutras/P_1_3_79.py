# Sutra प.1.3.79: अनुपराभ्यां कृञः
from P_1_3 import apply_1_3_79


class Sutra1379:
	def apply(self, word, pos):
		return apply_1_3_79(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_79:अग्निः'),
		('रामः', '', 'sutra_79:रामः'),
		('सीता', '', 'sutra_79:सीता'),
	]

