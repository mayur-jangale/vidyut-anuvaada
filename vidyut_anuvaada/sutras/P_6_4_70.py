# Sutra प.6.4.70: मयतेरिदन्यतरस्याम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.70"
SUTRA_TEXT = "मयतेरिदन्यतरस्याम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6470:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.70: अग्निः'),
		('रामः', '', 'प.6.4.70: रामः'),
		('सीता', '', 'प.6.4.70: सीता'),
	]

