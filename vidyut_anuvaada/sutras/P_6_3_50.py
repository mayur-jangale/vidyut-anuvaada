# Sutra प.6.3.50: हृदयस्य हृल्लेखयदण्लासेषु
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.50"
SUTRA_TEXT = "हृदयस्य हृल्लेखयदण्लासेषु"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6350:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.50: अग्निः'),
		('रामः', '', 'प.6.3.50: रामः'),
		('सीता', '', 'प.6.3.50: सीता'),
	]

