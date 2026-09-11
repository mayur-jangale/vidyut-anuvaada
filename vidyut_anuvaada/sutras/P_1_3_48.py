# Sutra प.1.3.48: व्यक्तवाचां समुच्चारणे
from P_1_3 import apply_1_3_48


class Sutra1348:
	def apply(self, word, pos):
		return apply_1_3_48(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_48:अग्निः'),
		('रामः', '', 'sutra_48:रामः'),
		('सीता', '', 'sutra_48:सीता'),
	]

