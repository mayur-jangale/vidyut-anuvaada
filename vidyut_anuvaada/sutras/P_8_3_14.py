# Sutra प.8.3.14: रो रि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.14"
SUTRA_TEXT = "रो रि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8314:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.14: अग्निः'),
		('रामः', '', 'प.8.3.14: रामः'),
		('सीता', '', 'प.8.3.14: सीता'),
	]

