# Sutra प.1.3.85: विभाषाऽकर्मकात्
from P_1_3 import apply_1_3_85


class Sutra1385:
	def apply(self, word, pos):
		return apply_1_3_85(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_85:अग्निः'),
		('रामः', '', 'sutra_85:रामः'),
		('सीता', '', 'sutra_85:सीता'),
	]

