# Sutra प.7.2.8: नेड् वशि कृति
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.2.8"
SUTRA_TEXT = "नेड् वशि कृति"
SUTRA_DESC = "taddhita — continued"


class Sutra728:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.2.8: अग्निः'),
		('रामः', '', 'प.7.2.8: रामः'),
		('सीता', '', 'प.7.2.8: सीता'),
	]

