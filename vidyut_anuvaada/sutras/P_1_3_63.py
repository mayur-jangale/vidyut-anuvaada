# Sutra प.1.3.63: आम्प्रत्ययवत् कृञोऽनुप्रयोगस्य
from P_1_3 import apply_1_3_63


class Sutra1363:
	def apply(self, word, pos):
		return apply_1_3_63(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_63:अग्निः'),
		('रामः', '', 'sutra_63:रामः'),
		('सीता', '', 'sutra_63:सीता'),
	]

