# Sutra प.1.3.68: भीस्म्योर्हेतुभये
from P_1_3 import apply_1_3_68


class Sutra1368:
	def apply(self, word, pos):
		return apply_1_3_68(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_68:अग्निः'),
		('रामः', '', 'sutra_68:रामः'),
		('सीता', '', 'sutra_68:सीता'),
	]

