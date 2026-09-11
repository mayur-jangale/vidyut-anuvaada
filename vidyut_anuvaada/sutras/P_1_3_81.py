# Sutra प.1.3.81: प्राद्वहः
from P_1_3 import apply_1_3_81


class Sutra1381:
	def apply(self, word, pos):
		return apply_1_3_81(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_81:अग्निः'),
		('रामः', '', 'sutra_81:रामः'),
		('सीता', '', 'sutra_81:सीता'),
	]

