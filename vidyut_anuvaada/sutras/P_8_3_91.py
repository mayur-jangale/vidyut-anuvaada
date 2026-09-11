# Sutra प.8.3.91: कपिष्ठलो गोत्रे
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.91"
SUTRA_TEXT = "कपिष्ठलो गोत्रे"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8391:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.91: अग्निः'),
		('रामः', '', 'प.8.3.91: रामः'),
		('सीता', '', 'प.8.3.91: सीता'),
	]

