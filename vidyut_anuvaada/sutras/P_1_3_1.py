# Sutra प.1.3.1: भूवादयो धातवः
from P_1_3 import apply_1_3_1


class Sutra131:
	def apply(self, word, pos):
		return apply_1_3_1(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'bhU-adi-dhAtu:अग्निः;in-list=no'),
		('रामः', '', 'bhU-adi-dhAtu:रामः;in-list=no'),
		('सीता', '', 'bhU-adi-dhAtu:सीता;in-list=no'),
	]

