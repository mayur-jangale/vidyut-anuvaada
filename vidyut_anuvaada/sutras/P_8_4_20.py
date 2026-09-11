# Sutra प.8.4.20: अन्तः
# final transformations — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.8.4.20"
SUTRA_TEXT = "अन्तः"
SUTRA_DESC = "final transformations — continued"


class Sutra8420:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.4.20: अग्निः'),
		('रामः', '', 'प.8.4.20: रामः'),
		('सीता', '', 'प.8.4.20: सीता'),
	]

