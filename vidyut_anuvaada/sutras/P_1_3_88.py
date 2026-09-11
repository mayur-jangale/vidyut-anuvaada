# Sutra प.1.3.88: अणावकर्मकाच्चित्तवत्कर्तृकात्
from P_1_3 import apply_1_3_88


class Sutra1388:
	def apply(self, word, pos):
		return apply_1_3_88(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_88:अग्निः'),
		('रामः', '', 'sutra_88:रामः'),
		('सीता', '', 'sutra_88:सीता'),
	]

