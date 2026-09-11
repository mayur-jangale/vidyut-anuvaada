# Sutra प.8.4.59: वा पदान्तस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.59"
SUTRA_TEXT = "वा पदान्तस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8459:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.59: अग्निः'),
		('रामः', '', 'प.8.4.59: रामः'),
		('सीता', '', 'प.8.4.59: सीता'),
	]

