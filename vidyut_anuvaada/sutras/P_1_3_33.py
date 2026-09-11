# Sutra प.1.3.33: अधेः प्रसहने
from P_1_3 import apply_1_3_33


class Sutra1333:
	def apply(self, word, pos):
		return apply_1_3_33(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_33:अग्निः'),
		('रामः', '', 'sutra_33:रामः'),
		('सीता', '', 'sutra_33:सीता'),
	]

