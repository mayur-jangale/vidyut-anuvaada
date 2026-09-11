# Sutra प.8.3.54: इडाया वा
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.54"
SUTRA_TEXT = "इडाया वा"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8354:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.54: अग्निः'),
		('रामः', '', 'प.8.3.54: रामः'),
		('सीता', '', 'प.8.3.54: सीता'),
	]

