# Sutra प.1.3.90: वा क्यषः
from P_1_3 import apply_1_3_90


class Sutra1390:
	def apply(self, word, pos):
		return apply_1_3_90(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'vA-kyzaH:अग्निः;optional=no'),
		('रामः', '', 'vA-kyzaH:रामः;optional=no'),
		('सीता', '', 'vA-kyzaH:सीता;optional=no'),
	]

