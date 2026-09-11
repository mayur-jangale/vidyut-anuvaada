# Sutra प.1.3.87: निगरणचलनार्थेभ्यश्च
from P_1_3 import apply_1_3_87


class Sutra1387:
	def apply(self, word, pos):
		return apply_1_3_87(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'sutra_87:अग्निः'),
		('रामः', '', 'sutra_87:रामः'),
		('सीता', '', 'sutra_87:सीता'),
	]

