# Sutra प.1.3.10: यथासंख्यमनुदेशः समानाम्
from P_1_3 import apply_1_3_10


class Sutra1310:
	def apply(self, word, pos):
		return apply_1_3_10(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'prefix_10:अग्निः;flag=yes'),
		('रामः', '', 'prefix_10:रामः;flag=yes'),
		('सीता', '', 'prefix_10:सीता;flag=yes'),
	]

