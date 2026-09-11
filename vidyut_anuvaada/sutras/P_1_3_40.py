# Sutra प.1.3.40: आङ उद्गमने
from P_1_3 import apply_1_3_40


class Sutra1340:
	def apply(self, word, pos):
		return apply_1_3_40(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_40:अग्निः'),
		('रामः', '', 'sutra_40:रामः'),
		('सीता', '', 'sutra_40:सीता'),
	]

