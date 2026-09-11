# Sutra प.7.2.1: सिचि वृद्धिः परस्मैपदेषु
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.1"
SUTRA_TEXT = "सिचि वृद्धिः परस्मैपदेषु"
SUTRA_DESC = "taddhita — continued"


class Sutra721:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.1: अग्निः'),
		('रामः', '', 'प.7.2.1: रामः'),
		('सीता', '', 'प.7.2.1: सीता'),
	]

