# Sutra प.1.3.80: अभिप्रत्यतिभ्यः क्षिपः
from P_1_3 import apply_1_3_80


class Sutra1380:
	def apply(self, word, pos):
		return apply_1_3_80(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_80:अग्निः'),
		('रामः', '', 'sutra_80:रामः'),
		('सीता', '', 'sutra_80:सीता'),
	]

