# Sutra प.1.3.47: भासनोपसम्भाषाज्ञानयत्नविमत्युपमन्त्रणेषु वदः
from P_1_3 import apply_1_3_47


class Sutra1347:
	def apply(self, word, pos):
		return apply_1_3_47(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_47:अग्निः'),
		('रामः', '', 'sutra_47:रामः'),
		('सीता', '', 'sutra_47:सीता'),
	]

