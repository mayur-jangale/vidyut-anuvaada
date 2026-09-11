# Sutra प.1.3.70: लियः सम्माननशालीनीकरणयोश्च
from P_1_3 import apply_1_3_70


class Sutra1370:
	def apply(self, word, pos):
		return apply_1_3_70(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_70:अग्निः'),
		('रामः', '', 'sutra_70:रामः'),
		('सीता', '', 'sutra_70:सीता'),
	]

