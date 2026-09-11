# Sutra प.1.3.84: उपाच्च
from P_1_3 import apply_1_3_84


class Sutra1384:
	def apply(self, word, pos):
		return apply_1_3_84(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_84:अग्निः'),
		('रामः', '', 'sutra_84:रामः'),
		('सीता', '', 'sutra_84:सीता'),
	]

