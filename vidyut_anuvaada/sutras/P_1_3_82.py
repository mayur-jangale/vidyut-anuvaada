# Sutra प.1.3.82: परेर्मृषः
from P_1_3 import apply_1_3_82


class Sutra1382:
	def apply(self, word, pos):
		return apply_1_3_82(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_82:अग्निः'),
		('रामः', '', 'sutra_82:रामः'),
		('सीता', '', 'sutra_82:सीता'),
	]

