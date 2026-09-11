# Sutra प.8.3.55: अपदान्तस्य मूर्धन्यः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.55"
SUTRA_TEXT = "अपदान्तस्य मूर्धन्यः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8355:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.55: अग्निः'),
		('रामः', '', 'प.8.3.55: रामः'),
		('सीता', '', 'प.8.3.55: सीता'),
	]

