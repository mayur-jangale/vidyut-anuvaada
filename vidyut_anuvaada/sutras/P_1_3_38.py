# Sutra प.1.3.38: वृत्तिसर्गतायनेषु क्रमः
from P_1_3 import apply_1_3_38


class Sutra1338:
	def apply(self, word, pos):
		return apply_1_3_38(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_38:अग्निः'),
		('रामः', '', 'sutra_38:रामः'),
		('सीता', '', 'sutra_38:सीता'),
	]

