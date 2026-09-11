# Sutra प.1.3.14: कर्तरि कर्मव्यतिहारे
from P_1_3 import apply_1_3_14


class Sutra1314:
	def apply(self, word, pos):
		return apply_1_3_14(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'kartari-karmavyatihAre:अग्निः;Atmanepada=no'),
		('रामः', '', 'kartari-karmavyatihAre:रामः;Atmanepada=no'),
		('सीता', '', 'kartari-karmavyatihAre:सीता;Atmanepada=no'),
	]

