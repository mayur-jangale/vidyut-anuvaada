# Sutra प.6.2.45: क्ते च
# hal-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.2.45"
SUTRA_TEXT = "क्ते च"
SUTRA_DESC = "hal-sandhi — continued"


class Sutra6245:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.2.45: अग्निः'),
		('रामः', '', 'प.6.2.45: रामः'),
		('सीता', '', 'प.6.2.45: सीता'),
	]

