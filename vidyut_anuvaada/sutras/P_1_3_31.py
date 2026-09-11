# Sutra प.1.3.31: स्पर्द्धायामाङः
from P_1_3 import apply_1_3_31


class Sutra1331:
	def apply(self, word, pos):
		return apply_1_3_31(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'spardhAyAmANaH:अग्निः;n/a'),
		('रामः', '', 'spardhAyAmANaH:रामः;n/a'),
		('सीता', '', 'spardhAyAmANaH:सीता;n/a'),
	]

