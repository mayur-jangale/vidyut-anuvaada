# Sutra प.7.4.89: ति च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.89"
SUTRA_TEXT = "ति च"
SUTRA_DESC = "taddhita — continued"


class Sutra7489:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.89: अग्निः'),
		('रामः', '', 'प.7.4.89: रामः'),
		('सीता', '', 'प.7.4.89: सीता'),
	]

