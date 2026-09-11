# Sutra प.7.3.9: पदान्तस्यान्यतरस्याम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.3.9"
SUTRA_TEXT = "पदान्तस्यान्यतरस्याम्"
SUTRA_DESC = "taddhita — continued"


class Sutra739:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.3.9: अग्निः'),
		('रामः', '', 'प.7.3.9: रामः'),
		('सीता', '', 'प.7.3.9: सीता'),
	]

