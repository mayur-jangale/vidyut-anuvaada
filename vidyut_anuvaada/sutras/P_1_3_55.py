# Sutra प.1.3.55: दाणश्च सा चेच्चतुर्थ्यर्थे
from P_1_3 import apply_1_3_55


class Sutra1355:
	def apply(self, word, pos):
		return apply_1_3_55(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_55:अग्निः'),
		('रामः', '', 'sutra_55:रामः'),
		('सीता', '', 'sutra_55:सीता'),
	]

