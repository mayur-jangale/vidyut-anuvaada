# Sutra प.1.3.42: प्रोपाभ्यां समर्थाभ्याम्
from P_1_3 import apply_1_3_42


class Sutra1342:
	def apply(self, word, pos):
		return apply_1_3_42(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_42:अग्निः'),
		('रामः', '', 'sutra_42:रामः'),
		('सीता', '', 'sutra_42:सीता'),
	]

