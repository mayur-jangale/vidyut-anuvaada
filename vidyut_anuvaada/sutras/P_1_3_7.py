# Sutra प.1.3.7: चुटू
from P_1_3 import apply_1_3_7


class Sutra137:
	def apply(self, word, pos):
		return apply_1_3_7(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'cutU:अग्निः;not-cutU'),
		('रामः', '', 'cutU:रामः;not-cutU'),
		('सीता', '', 'cutU:सीता;not-cutU'),
	]

