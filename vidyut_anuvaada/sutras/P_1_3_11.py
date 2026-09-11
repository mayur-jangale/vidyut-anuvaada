# Sutra प.1.3.11: स्वरितेनाधिकारः
from P_1_3 import apply_1_3_11


class Sutra1311:
	def apply(self, word, pos):
		return apply_1_3_11(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'prefix_11:अग्निः;flag=yes'),
		('रामः', '', 'prefix_11:रामः;flag=yes'),
		('सीता', '', 'prefix_11:सीता;flag=yes'),
	]

