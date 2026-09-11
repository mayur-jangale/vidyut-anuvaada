# Sutra प.7.4.15: आपोऽन्यतरस्याम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.15"
SUTRA_TEXT = "आपोऽन्यतरस्याम्"
SUTRA_DESC = "taddhita — continued"


class Sutra7415:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.15: अग्निः'),
		('रामः', '', 'प.7.4.15: रामः'),
		('सीता', '', 'प.7.4.15: सीता'),
	]

