# Sutra प.1.3.57: ज्ञाश्रुस्मृदृशां सनः
from P_1_3 import apply_1_3_57


class Sutra1357:
	def apply(self, word, pos):
		return apply_1_3_57(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_57:अग्निः'),
		('रामः', '', 'sutra_57:रामः'),
		('सीता', '', 'sutra_57:सीता'),
	]

