# Sutra प.1.3.16: इतरेतरान्योन्योपपदाच्च
from P_1_3 import apply_1_3_16


class Sutra1316:
	def apply(self, word, pos):
		return apply_1_3_16(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'itaretarAnyonyopapadAcca:अग्निः;mutual=yes'),
		('रामः', '', 'itaretarAnyonyopapadAcca:रामः;mutual=yes'),
		('सीता', '', 'itaretarAnyonyopapadAcca:सीता;mutual=yes'),
	]

