# Sutra प.1.3.37: कर्तृस्थे चाशरीरे कर्मणि
from P_1_3 import apply_1_3_37


class Sutra1337:
	def apply(self, word, pos):
		return apply_1_3_37(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_37:अग्निः'),
		('रामः', '', 'sutra_37:रामः'),
		('सीता', '', 'sutra_37:सीता'),
	]

