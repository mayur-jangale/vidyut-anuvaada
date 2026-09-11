# Sutra प.1.3.6: षः प्रत्ययस्य
from P_1_3 import apply_1_3_6


class Sutra136:
	def apply(self, word, pos):
		return apply_1_3_6(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sah-pratyayasya:अग्निः;sa-it=no'),
		('रामः', '', 'sah-pratyayasya:रामः;sa-it=no'),
		('सीता', '', 'sah-pratyayasya:सीता;sa-it=no'),
	]

