# Sutra प.1.3.43: अनुपसर्गाद्वा
from P_1_3 import apply_1_3_43


class Sutra1343:
	def apply(self, word, pos):
		return apply_1_3_43(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_43:अग्निः'),
		('रामः', '', 'sutra_43:रामः'),
		('सीता', '', 'sutra_43:सीता'),
	]

