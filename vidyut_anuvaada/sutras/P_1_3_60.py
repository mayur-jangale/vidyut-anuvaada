# Sutra प.1.3.60: शदेः शितः
from P_1_3 import apply_1_3_60


class Sutra1360:
	def apply(self, word, pos):
		return apply_1_3_60(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_60:अग्निः'),
		('रामः', '', 'sutra_60:रामः'),
		('सीता', '', 'sutra_60:सीता'),
	]

