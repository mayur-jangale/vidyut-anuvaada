# Sutra प.1.3.26: अकर्मकाच्च
from P_1_3 import apply_1_3_26


class Sutra1326:
	def apply(self, word, pos):
		return apply_1_3_26(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'akarmakAcca:अग्निः;n/a'),
		('रामः', '', 'akarmakAcca:रामः;n/a'),
		('सीता', '', 'akarmakAcca:सीता;n/a'),
	]

