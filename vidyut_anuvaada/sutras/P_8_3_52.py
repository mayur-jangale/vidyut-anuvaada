# Sutra प.8.3.52: पातौ च बहुलम्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.52"
SUTRA_TEXT = "पातौ च बहुलम्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8352:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.52: अग्निः'),
		('रामः', '', 'प.8.3.52: रामः'),
		('सीता', '', 'प.8.3.52: सीता'),
	]

