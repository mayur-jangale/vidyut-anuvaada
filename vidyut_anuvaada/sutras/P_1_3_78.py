# Sutra प.1.3.78: शेषात् कर्तरि परस्मैपदम्
from P_1_3 import apply_1_3_78


class Sutra1378:
	def apply(self, word, pos):
		return apply_1_3_78(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'SezAt-kartari-parasmEpadam:अग्निः;parasmaipada=yes;default'),
		('रामः', '', 'SezAt-kartari-parasmEpadam:रामः;parasmaipada=yes;default'),
		('सीता', '', 'SezAt-kartari-parasmEpadam:सीता;parasmaipada=yes;default'),
	]

