# Sutra प.1.3.25: उपान्मन्त्रकरणे
from P_1_3 import apply_1_3_25


class Sutra1325:
	def apply(self, word, pos):
		return apply_1_3_25(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'upAnmantrakaraNe:अग्निः;n/a'),
		('रामः', '', 'upAnmantrakaraNe:रामः;n/a'),
		('सीता', '', 'upAnmantrakaraNe:सीता;n/a'),
	]

