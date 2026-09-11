# Sutra प.8.3.89: निनदीभ्यां स्नातेः कौशले
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.89"
SUTRA_TEXT = "निनदीभ्यां स्नातेः कौशले"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8389:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.89: अग्निः'),
		('रामः', '', 'प.8.3.89: रामः'),
		('सीता', '', 'प.8.3.89: सीता'),
	]

