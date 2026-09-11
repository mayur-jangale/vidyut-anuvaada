# Sutra प.1.3.39: उपपराभ्याम्
from P_1_3 import apply_1_3_39


class Sutra1339:
	def apply(self, word, pos):
		return apply_1_3_39(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_39:अग्निः'),
		('रामः', '', 'sutra_39:रामः'),
		('सीता', '', 'sutra_39:सीता'),
	]

