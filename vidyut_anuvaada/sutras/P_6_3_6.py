# Sutra प.6.3.6: आत्मनश्च पूरणे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.6"
SUTRA_TEXT = "आत्मनश्च पूरणे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra636:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.6: अग्निः'),
		('रामः', '', 'प.6.3.6: रामः'),
		('सीता', '', 'प.6.3.6: सीता'),
	]

