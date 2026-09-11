# Sutra प.1.3.12: अनुदात्तङित आत्मनेपदम्
from P_1_3 import apply_1_3_12


class Sutra1312:
	def apply(self, word, pos):
		return apply_1_3_12(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'anudAttaiit-Atmanepadam:अग्निः;Atmanepada=no'),
		('रामः', '', 'anudAttaiit-Atmanepadam:रामः;Atmanepada=no'),
		('सीता', '', 'anudAttaiit-Atmanepadam:सीता;Atmanepada=no'),
	]

