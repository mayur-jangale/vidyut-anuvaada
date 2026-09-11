# Sutra प.1.3.46: सम्प्रतिभ्यामनाध्याने
from P_1_3 import apply_1_3_46


class Sutra1346:
	def apply(self, word, pos):
		return apply_1_3_46(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_46:अग्निः'),
		('रामः', '', 'sutra_46:रामः'),
		('सीता', '', 'sutra_46:सीता'),
	]

