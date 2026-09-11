# Sutra प.7.4.71: तस्मान्नुड् द्विहलः
# taddhita — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.7.4.71"
SUTRA_TEXT = "तस्मान्नुड् द्विहलः"
SUTRA_DESC = "taddhita — continued"


class Sutra7471:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.7.4.71: अग्निः'),
		('रामः', '', 'प.7.4.71: रामः'),
		('सीता', '', 'प.7.4.71: सीता'),
	]

