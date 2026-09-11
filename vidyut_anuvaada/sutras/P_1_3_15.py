# Sutra प.1.3.15: न गतिहिंसार्थेभ्यः
from P_1_3 import apply_1_3_15


class Sutra1315:
	def apply(self, word, pos):
		return apply_1_3_15(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'na-gati-hiMsArTeByaH:अग्निः;depends'),
		('रामः', '', 'na-gati-hiMsArTeByaH:रामः;depends'),
		('सीता', '', 'na-gati-hiMsArTeByaH:सीता;depends'),
	]

