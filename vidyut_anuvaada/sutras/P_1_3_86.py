# Sutra प.1.3.86: बुधयुधनशजनेङ्प्रुद्रुस्रुभ्यो णेः
from P_1_3 import apply_1_3_86


class Sutra1386:
	def apply(self, word, pos):
		return apply_1_3_86(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_86:अग्निः'),
		('रामः', '', 'sutra_86:रामः'),
		('सीता', '', 'sutra_86:सीता'),
	]

