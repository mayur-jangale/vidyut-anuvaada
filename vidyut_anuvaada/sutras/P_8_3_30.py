# Sutra प.8.3.30: नश्च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.30"
SUTRA_TEXT = "नश्च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8330:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.30: अग्निः'),
		('रामः', '', 'प.8.3.30: रामः'),
		('सीता', '', 'प.8.3.30: सीता'),
	]

