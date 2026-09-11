# Sutra प.8.3.21: उञि च पदे
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.21"
SUTRA_TEXT = "उञि च पदे"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8321:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.21: अग्निः'),
		('रामः', '', 'प.8.3.21: रामः'),
		('सीता', '', 'प.8.3.21: सीता'),
	]

