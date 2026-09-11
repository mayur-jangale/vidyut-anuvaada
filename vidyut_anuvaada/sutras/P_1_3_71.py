# Sutra प.1.3.71: मिथ्योपपदात् कृञोऽभ्यासे
from P_1_3 import apply_1_3_71


class Sutra1371:
	def apply(self, word, pos):
		return apply_1_3_71(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_71:अग्निः'),
		('रामः', '', 'sutra_71:रामः'),
		('सीता', '', 'sutra_71:सीता'),
	]

