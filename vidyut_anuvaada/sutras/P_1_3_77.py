# Sutra प.1.3.77: विभाषोपपदेन प्रतीयमाने
from P_1_3 import apply_1_3_77


class Sutra1377:
	def apply(self, word, pos):
		return apply_1_3_77(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_77:अग्निः'),
		('रामः', '', 'sutra_77:रामः'),
		('सीता', '', 'sutra_77:सीता'),
	]

