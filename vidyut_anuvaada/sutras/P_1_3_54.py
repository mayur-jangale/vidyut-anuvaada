# Sutra प.1.3.54: समस्तृतीयायुक्तात्
from P_1_3 import apply_1_3_54


class Sutra1354:
	def apply(self, word, pos):
		return apply_1_3_54(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_54:अग्निः'),
		('रामः', '', 'sutra_54:रामः'),
		('सीता', '', 'sutra_54:सीता'),
	]

