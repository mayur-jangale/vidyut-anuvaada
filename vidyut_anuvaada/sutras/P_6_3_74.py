# Sutra प.6.3.74: तस्मान्नुडचि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.74"
SUTRA_TEXT = "तस्मान्नुडचि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra6374:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.74: अग्निः'),
		('रामः', '', 'प.6.3.74: रामः'),
		('सीता', '', 'प.6.3.74: सीता'),
	]

