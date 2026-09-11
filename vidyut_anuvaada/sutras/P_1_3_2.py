# Sutra प.1.3.2: उपदेशेऽजनुनासिक इत्
from P_1_3 import apply_1_3_2


class Sutra132:
	def apply(self, word, pos):
		return apply_1_3_2(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'it-vowel:अग्निः;it=no'),
		('रामः', '', 'it-vowel:रामः;it=no'),
		('सीता', '', 'it-vowel:सीता;it=no'),
	]

