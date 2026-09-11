# Sutra प.1.3.30: निसमुपविभ्यो ह्वः
from P_1_3 import apply_1_3_30


class Sutra1330:
	def apply(self, word, pos):
		return apply_1_3_30(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'nisamupavibhyo-hvaH:अग्निः;n/a'),
		('रामः', '', 'nisamupavibhyo-hvaH:रामः;n/a'),
		('सीता', '', 'nisamupavibhyo-hvaH:सीता;n/a'),
	]

