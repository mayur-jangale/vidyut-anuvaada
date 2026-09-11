# Sutra प.1.3.19: विपराभ्यां जेः
from P_1_3 import apply_1_3_19


class Sutra1319:
	def apply(self, word, pos):
		return apply_1_3_19(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'viparAByAM-jeH:अग्निः;n/a'),
		('रामः', '', 'viparAByAM-jeH:रामः;n/a'),
		('सीता', '', 'viparAByAM-jeH:सीता;n/a'),
	]

