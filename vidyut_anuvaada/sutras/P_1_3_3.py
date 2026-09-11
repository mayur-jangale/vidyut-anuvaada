# Sutra प.1.3.3: हलन्त्यम्
from P_1_3 import apply_1_3_3


class Sutra133:
	def apply(self, word, pos):
		return apply_1_3_3(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'hal-ityam:अग्निः;final=ः'),
		('रामः', '', 'hal-ityam:रामः;final=ः'),
		('सीता', '', 'hal-ityam:सीता;final=ा'),
	]
