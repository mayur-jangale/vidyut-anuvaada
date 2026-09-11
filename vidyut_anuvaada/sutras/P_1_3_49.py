# Sutra प.1.3.49: अनोरकर्मकात्
from P_1_3 import apply_1_3_49


class Sutra1349:
	def apply(self, word, pos):
		return apply_1_3_49(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_49:अग्निः'),
		('रामः', '', 'sutra_49:रामः'),
		('सीता', '', 'sutra_49:सीता'),
	]

