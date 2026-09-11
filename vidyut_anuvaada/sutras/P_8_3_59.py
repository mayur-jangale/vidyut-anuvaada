# Sutra प.8.3.59: आदेशप्रत्यययोः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.59"
SUTRA_TEXT = "आदेशप्रत्यययोः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8359:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.59: अग्निः'),
		('रामः', '', 'प.8.3.59: रामः'),
		('सीता', '', 'प.8.3.59: सीता'),
	]

