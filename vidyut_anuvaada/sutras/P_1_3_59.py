# Sutra प.1.3.59: प्रत्याङ्भ्यां श्रुवः
from P_1_3 import apply_1_3_59


class Sutra1359:
	def apply(self, word, pos):
		return apply_1_3_59(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_59:अग्निः'),
		('रामः', '', 'sutra_59:रामः'),
		('सीता', '', 'sutra_59:सीता'),
	]

