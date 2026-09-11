# Sutra प.1.3.51: अवाद्ग्रः
from P_1_3 import apply_1_3_51


class Sutra1351:
	def apply(self, word, pos):
		return apply_1_3_51(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_51:अग्निः'),
		('रामः', '', 'sutra_51:रामः'),
		('सीता', '', 'sutra_51:सीता'),
	]

