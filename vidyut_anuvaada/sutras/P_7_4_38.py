# Sutra प.7.4.38: देवसुम्नयोर्यजुषि काठके
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.38"
SUTRA_TEXT = "देवसुम्नयोर्यजुषि काठके"
SUTRA_DESC = "taddhita — continued"


class Sutra7438:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.38: अग्निः'),
		('रामः', '', 'प.7.4.38: रामः'),
		('सीता', '', 'प.7.4.38: सीता'),
	]

