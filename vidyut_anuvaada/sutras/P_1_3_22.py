# Sutra प.1.3.22: समवप्रविभ्यः स्थः
from P_1_3 import apply_1_3_22


class Sutra1322:
	def apply(self, word, pos):
		return apply_1_3_22(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'samavapraviByaH-sTaH:अग्निः;n/a'),
		('रामः', '', 'samavapraviByaH-sTaH:रामः;n/a'),
		('सीता', '', 'samavapraviByaH-sTaH:सीता;n/a'),
	]

