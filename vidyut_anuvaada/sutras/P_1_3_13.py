# Sutra प.1.3.13: भावकर्मणोः
from P_1_3 import apply_1_3_13


class Sutra1313:
	def apply(self, word, pos):
		return apply_1_3_13(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'bhAvakarmaNoH:अग्निः;sense=other'),
		('रामः', '', 'bhAvakarmaNoH:रामः;sense=other'),
		('सीता', '', 'bhAvakarmaNoH:सीता;sense=other'),
	]

