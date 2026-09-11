# Sutra प.1.3.58: नानोर्ज्ञः
from P_1_3 import apply_1_3_58


class Sutra1358:
	def apply(self, word, pos):
		return apply_1_3_58(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_58:अग्निः'),
		('रामः', '', 'sutra_58:रामः'),
		('सीता', '', 'sutra_58:सीता'),
	]

