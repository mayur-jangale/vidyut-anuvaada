# Sutra प.1.3.50: विभाषा विप्रलापे
from P_1_3 import apply_1_3_50


class Sutra1350:
	def apply(self, word, pos):
		return apply_1_3_50(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'viBAzA-vipralApe:अग्निः;optional=no'),
		('रामः', '', 'viBAzA-vipralApe:रामः;optional=no'),
		('सीता', '', 'viBAzA-vipralApe:सीता;optional=no'),
	]

