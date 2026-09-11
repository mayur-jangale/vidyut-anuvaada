# Sutra प.1.3.66: भुजोऽनवने
from P_1_3 import apply_1_3_66


class Sutra1366:
	def apply(self, word, pos):
		return apply_1_3_66(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_66:अग्निः'),
		('रामः', '', 'sutra_66:रामः'),
		('सीता', '', 'sutra_66:सीता'),
	]

