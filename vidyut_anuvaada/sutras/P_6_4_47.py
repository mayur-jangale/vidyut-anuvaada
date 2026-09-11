# Sutra प.6.4.47: भ्रस्जो रोपधयोः रमन्यतरस्याम्
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.47"
SUTRA_TEXT = "भ्रस्जो रोपधयोः रमन्यतरस्याम्"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6447:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.47: अग्निः'),
		('रामः', '', 'प.6.4.47: रामः'),
		('सीता', '', 'प.6.4.47: सीता'),
	]

