# Sutra प.1.3.73: अपाद्वदः
from P_1_3 import apply_1_3_73


class Sutra1373:
	def apply(self, word, pos):
		return apply_1_3_73(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_73:अग्निः'),
		('रामः', '', 'sutra_73:रामः'),
		('सीता', '', 'sutra_73:सीता'),
	]

