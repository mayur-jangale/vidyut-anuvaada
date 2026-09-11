# Sutra प.6.3.44: नद्याः शेषस्यान्यतरस्याम्
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.44"
SUTRA_TEXT = "नद्याः शेषस्यान्यतरस्याम्"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.44: अग्निः'),
		('रामः', '', 'प.6.3.44: रामः'),
		('सीता', '', 'प.6.3.44: सीता'),
	]

