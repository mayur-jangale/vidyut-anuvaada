# Sutra प.1.3.89: न पादम्याङ्यमाङ्यसपरिमुहरुचिनृतिवदवसः
from P_1_3 import apply_1_3_89


class Sutra1389:
	def apply(self, word, pos):
		return apply_1_3_89(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_89:अग्निः'),
		('रामः', '', 'sutra_89:रामः'),
		('सीता', '', 'sutra_89:सीता'),
	]

