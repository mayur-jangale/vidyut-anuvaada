# Sutra प.1.3.53: उदश्चरः सकर्मकात्
from P_1_3 import apply_1_3_53


class Sutra1353:
	def apply(self, word, pos):
		return apply_1_3_53(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_53:अग्निः'),
		('रामः', '', 'sutra_53:रामः'),
		('सीता', '', 'sutra_53:सीता'),
	]

