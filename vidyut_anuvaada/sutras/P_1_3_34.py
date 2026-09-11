# Sutra प.1.3.34: वेः शब्दकर्मणः
from P_1_3 import apply_1_3_34


class Sutra1334:
	def apply(self, word, pos):
		return apply_1_3_34(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_34:अग्निः'),
		('रामः', '', 'sutra_34:रामः'),
		('सीता', '', 'sutra_34:सीता'),
	]

