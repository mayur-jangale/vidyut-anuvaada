# Sutra प.1.3.52: समः प्रतिज्ञाने
from P_1_3 import apply_1_3_52


class Sutra1352:
	def apply(self, word, pos):
		return apply_1_3_52(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_52:अग्निः'),
		('रामः', '', 'sutra_52:रामः'),
		('सीता', '', 'sutra_52:सीता'),
	]

