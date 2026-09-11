# Sutra प.1.3.5: आदिर्ञिटुडवः
from P_1_3 import apply_1_3_5


class Sutra135:
	def apply(self, word, pos):
		return apply_1_3_5(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'adir-nitidudavah:अग्निः;it=no'),
		('रामः', '', 'adir-nitidudavah:रामः;it=no'),
		('सीता', '', 'adir-nitidudavah:सीता;it=no'),
	]

