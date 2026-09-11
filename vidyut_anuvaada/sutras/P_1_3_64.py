# Sutra प.1.3.64: प्रोपाभ्यां युजेरयज्ञपात्रेषु
from P_1_3 import apply_1_3_64


class Sutra1364:
	def apply(self, word, pos):
		return apply_1_3_64(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_64:अग्निः'),
		('रामः', '', 'sutra_64:रामः'),
		('सीता', '', 'sutra_64:सीता'),
	]

