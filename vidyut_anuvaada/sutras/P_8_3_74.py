# Sutra प.8.3.74: परेश्च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.74"
SUTRA_TEXT = "परेश्च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8374:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.74: अग्निः'),
		('रामः', '', 'प.8.3.74: रामः'),
		('सीता', '', 'प.8.3.74: सीता'),
	]

