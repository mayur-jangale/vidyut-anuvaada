# Sutra प.7.4.87: चरफलोश्च
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.87"
SUTRA_TEXT = "चरफलोश्च"
SUTRA_DESC = "taddhita — continued"


class Sutra7487:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.87: अग्निः'),
		('रामः', '', 'प.7.4.87: रामः'),
		('सीता', '', 'प.7.4.87: सीता'),
	]

