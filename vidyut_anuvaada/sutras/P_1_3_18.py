# Sutra प.1.3.18: परिव्यवेभ्यः क्रियः
from P_1_3 import apply_1_3_18


class Sutra1318:
	def apply(self, word, pos):
		return apply_1_3_18(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'parivyaveByaH-kriyaH:अग्निः;n/a'),
		('रामः', '', 'parivyaveByaH-kriyaH:रामः;n/a'),
		('सीता', '', 'parivyaveByaH-kriyaH:सीता;n/a'),
	]

