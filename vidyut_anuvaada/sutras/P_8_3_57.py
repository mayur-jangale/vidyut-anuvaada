# Sutra प.8.3.57: इण्कोः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.57"
SUTRA_TEXT = "इण्कोः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8357:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.57: अग्निः'),
		('रामः', '', 'प.8.3.57: रामः'),
		('सीता', '', 'प.8.3.57: सीता'),
	]

