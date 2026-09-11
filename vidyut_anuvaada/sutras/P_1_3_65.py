# Sutra प.1.3.65: समः क्ष्णुवः
from P_1_3 import apply_1_3_65


class Sutra1365:
	def apply(self, word, pos):
		return apply_1_3_65(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_65:अग्निः'),
		('रामः', '', 'sutra_65:रामः'),
		('सीता', '', 'sutra_65:सीता'),
	]

