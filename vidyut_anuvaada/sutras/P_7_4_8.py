# Sutra प.7.4.8: नित्यं छन्दसि
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.8"
SUTRA_TEXT = "नित्यं छन्दसि"
SUTRA_DESC = "taddhita — continued"


class Sutra748:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.8: अग्निः'),
		('रामः', '', 'प.7.4.8: रामः'),
		('सीता', '', 'प.7.4.8: सीता'),
	]

