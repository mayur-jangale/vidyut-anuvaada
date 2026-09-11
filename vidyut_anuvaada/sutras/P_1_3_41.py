# Sutra प.1.3.41: वेः पादविहरणे
from P_1_3 import apply_1_3_41


class Sutra1341:
	def apply(self, word, pos):
		return apply_1_3_41(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_41:अग्निः'),
		('रामः', '', 'sutra_41:रामः'),
		('सीता', '', 'sutra_41:सीता'),
	]

