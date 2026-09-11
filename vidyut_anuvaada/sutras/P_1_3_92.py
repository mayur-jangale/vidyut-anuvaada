# Sutra प.1.3.92: वृद्भ्यः स्यसनोः
from P_1_3 import apply_1_3_92


class Sutra1392:
	def apply(self, word, pos):
		return apply_1_3_92(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_92:अग्निः'),
		('रामः', '', 'sutra_92:रामः'),
		('सीता', '', 'sutra_92:सीता'),
	]

