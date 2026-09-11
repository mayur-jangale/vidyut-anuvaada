# Sutra प.8.3.24: नश्चापदान्तस्य झलि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.24"
SUTRA_TEXT = "नश्चापदान्तस्य झलि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8324:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.24: अग्निः'),
		('रामः', '', 'प.8.3.24: रामः'),
		('सीता', '', 'प.8.3.24: सीता'),
	]

