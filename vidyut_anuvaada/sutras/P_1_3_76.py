# Sutra प.1.3.76: अनुपसर्गाज्ज्ञः
from P_1_3 import apply_1_3_76


class Sutra1376:
	def apply(self, word, pos):
		return apply_1_3_76(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_76:अग्निः'),
		('रामः', '', 'sutra_76:रामः'),
		('सीता', '', 'sutra_76:सीता'),
	]

