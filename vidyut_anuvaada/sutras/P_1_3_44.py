# Sutra प.1.3.44: अपह्नवे ज्ञः
from P_1_3 import apply_1_3_44


class Sutra1344:
	def apply(self, word, pos):
		return apply_1_3_44(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_44:अग्निः'),
		('रामः', '', 'sutra_44:रामः'),
		('सीता', '', 'sutra_44:सीता'),
	]

