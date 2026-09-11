# Sutra प.8.4.10: वा भावकरणयोः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.10"
SUTRA_TEXT = "वा भावकरणयोः"
SUTRA_DESC = "final transformations — continued"


class Sutra8410:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.10: अग्निः'),
		('रामः', '', 'प.8.4.10: रामः'),
		('सीता', '', 'प.8.4.10: सीता'),
	]

