# Sutra प.8.4.37: पदान्तस्य
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.37"
SUTRA_TEXT = "पदान्तस्य"
SUTRA_DESC = "final transformations — continued"


class Sutra8437:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.37: अग्निः'),
		('रामः', '', 'प.8.4.37: रामः'),
		('सीता', '', 'प.8.4.37: सीता'),
	]

