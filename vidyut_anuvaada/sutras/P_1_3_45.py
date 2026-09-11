# Sutra प.1.3.45: अकर्मकाच्च
from P_1_3 import apply_1_3_45


class Sutra1345:
	def apply(self, word, pos):
		return apply_1_3_45(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_45:अग्निः'),
		('रामः', '', 'sutra_45:रामः'),
		('सीता', '', 'sutra_45:सीता'),
	]

