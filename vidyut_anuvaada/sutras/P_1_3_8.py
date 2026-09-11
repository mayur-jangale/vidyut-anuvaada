# Sutra प.1.3.8: लशक्वतद्धिते
from P_1_3 import apply_1_3_8


class Sutra138:
	def apply(self, word, pos):
		return apply_1_3_8(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'laShakvataDDhite:अग्निः;no'),
		('रामः', '', 'laShakvataDDhite:रामः;no'),
		('सीता', '', 'laShakvataDDhite:सीता;no'),
	]

