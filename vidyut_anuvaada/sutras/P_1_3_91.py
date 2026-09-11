# Sutra प.1.3.91: द्युद्भ्यो लुङि
from P_1_3 import apply_1_3_91


class Sutra1391:
	def apply(self, word, pos):
		return apply_1_3_91(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_91:अग्निः'),
		('रामः', '', 'sutra_91:रामः'),
		('सीता', '', 'sutra_91:सीता'),
	]

