# Sutra प.6.4.27: घञि च भावकरणयोः
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.27"
SUTRA_TEXT = "घञि च भावकरणयोः"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6427:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.27: अग्निः'),
		('रामः', '', 'प.6.4.27: रामः'),
		('सीता', '', 'प.6.4.27: सीता'),
	]

