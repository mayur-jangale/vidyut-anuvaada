# Sutra प.1.3.35: अकर्मकाच्च
from P_1_3 import apply_1_3_35


class Sutra1335:
	def apply(self, word, pos):
		return apply_1_3_35(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_35:अग्निः'),
		('रामः', '', 'sutra_35:रामः'),
		('सीता', '', 'sutra_35:सीता'),
	]

