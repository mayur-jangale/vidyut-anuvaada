# Sutra प.7.4.41: शाच्छोरन्यतरस्याम्
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.41"
SUTRA_TEXT = "शाच्छोरन्यतरस्याम्"
SUTRA_DESC = "taddhita — continued"


class Sutra7441:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.41: अग्निः'),
		('रामः', '', 'प.7.4.41: रामः'),
		('सीता', '', 'प.7.4.41: सीता'),
	]

