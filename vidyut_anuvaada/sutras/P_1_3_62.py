# Sutra प.1.3.62: पूर्ववत् सनः
from P_1_3 import apply_1_3_62


class Sutra1362:
	def apply(self, word, pos):
		return apply_1_3_62(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_62:अग्निः'),
		('रामः', '', 'sutra_62:रामः'),
		('सीता', '', 'sutra_62:सीता'),
	]

