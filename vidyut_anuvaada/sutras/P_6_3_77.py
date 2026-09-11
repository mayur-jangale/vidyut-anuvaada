# Sutra प.6.3.77: नगोऽप्राणिष्वन्यतरस्याम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.77"
SUTRA_TEXT = "नगोऽप्राणिष्वन्यतरस्याम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6377:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.77: अग्निः'),
		('रामः', '', 'प.6.3.77: रामः'),
		('सीता', '', 'प.6.3.77: सीता'),
	]

