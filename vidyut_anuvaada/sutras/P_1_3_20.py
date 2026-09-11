# Sutra प.1.3.20: आङो दोऽनास्यविहरणे
from P_1_3 import apply_1_3_20


class Sutra1320:
	def apply(self, word, pos):
		return apply_1_3_20(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'ANo-doAsyaviharaNe:अग्निः;n/a'),
		('रामः', '', 'ANo-doAsyaviharaNe:रामः;n/a'),
		('सीता', '', 'ANo-doAsyaviharaNe:सीता;n/a'),
	]

