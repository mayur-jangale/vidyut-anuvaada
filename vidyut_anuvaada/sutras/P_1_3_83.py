# Sutra प.1.3.83: व्याङ्परिभ्यो रमः
from P_1_3 import apply_1_3_83


class Sutra1383:
	def apply(self, word, pos):
		return apply_1_3_83(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_83:अग्निः'),
		('रामः', '', 'sutra_83:रामः'),
		('सीता', '', 'sutra_83:सीता'),
	]

