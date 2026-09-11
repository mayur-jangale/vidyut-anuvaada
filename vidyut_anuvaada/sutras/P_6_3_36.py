# Sutra प.6.3.36: क्यङ्मानिनोश्च
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.36"
SUTRA_TEXT = "क्यङ्मानिनोश्च"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6336:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.36: अग्निः'),
		('रामः', '', 'प.6.3.36: रामः'),
		('सीता', '', 'प.6.3.36: सीता'),
	]

