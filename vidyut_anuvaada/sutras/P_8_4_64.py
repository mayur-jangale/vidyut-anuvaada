# Sutra प.8.4.64: हलो यमां यमि लोपः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.64"
SUTRA_TEXT = "हलो यमां यमि लोपः"
SUTRA_DESC = "final transformations — continued"


class Sutra8464:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.64: अग्निः'),
		('रामः', '', 'प.8.4.64: रामः'),
		('सीता', '', 'प.8.4.64: सीता'),
	]

