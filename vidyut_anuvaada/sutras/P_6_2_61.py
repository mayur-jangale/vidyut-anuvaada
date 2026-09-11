# Sutra प.6.2.61: क्ते नित्यार्थे
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.61"
SUTRA_TEXT = "क्ते नित्यार्थे"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6261:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.61: अग्निः'),
		('रामः', '', 'प.6.2.61: रामः'),
		('सीता', '', 'प.6.2.61: सीता'),
	]

