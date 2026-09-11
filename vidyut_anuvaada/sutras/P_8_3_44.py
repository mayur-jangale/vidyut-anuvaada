# Sutra प.8.3.44: इसुसोः सामर्थ्ये
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.44"
SUTRA_TEXT = "इसुसोः सामर्थ्ये"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8344:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.44: अग्निः'),
		('रामः', '', 'प.8.3.44: रामः'),
		('सीता', '', 'प.8.3.44: सीता'),
	]

