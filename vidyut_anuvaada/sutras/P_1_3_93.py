# Sutra प.1.3.93: लुटि च कॢपः
from P_1_3 import apply_1_3_93


class Sutra1393:
	def apply(self, word, pos):
		return apply_1_3_93(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_93:अग्निः'),
		('रामः', '', 'sutra_93:रामः'),
		('सीता', '', 'sutra_93:सीता'),
	]

