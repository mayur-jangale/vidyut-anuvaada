# Sutra प.1.3.56: उपाद्यमः स्वकरणे
from P_1_3 import apply_1_3_56


class Sutra1356:
	def apply(self, word, pos):
		return apply_1_3_56(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_56:अग्निः'),
		('रामः', '', 'sutra_56:रामः'),
		('सीता', '', 'sutra_56:सीता'),
	]

