# Sutra प.6.3.71: श्येनतिलस्य पाते ञे
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.71"
SUTRA_TEXT = "श्येनतिलस्य पाते ञे"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6371:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.71: अग्निः'),
		('रामः', '', 'प.6.3.71: रामः'),
		('सीता', '', 'प.6.3.71: सीता'),
	]

