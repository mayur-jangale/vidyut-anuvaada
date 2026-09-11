# Sutra प.1.3.75: समुदाङ्भ्यो यमोऽग्रन्थे
from P_1_3 import apply_1_3_75


class Sutra1375:
	def apply(self, word, pos):
		return apply_1_3_75(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_75:अग्निः'),
		('रामः', '', 'sutra_75:रामः'),
		('सीता', '', 'sutra_75:सीता'),
	]

