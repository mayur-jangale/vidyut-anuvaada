# Sutra प.8.4.32: इजादेः सनुमः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.32"
SUTRA_TEXT = "इजादेः सनुमः"
SUTRA_DESC = "final transformations — continued"


class Sutra8432:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.32: अग्निः'),
		('रामः', '', 'प.8.4.32: रामः'),
		('सीता', '', 'प.8.4.32: सीता'),
	]

