# Sutra प.8.3.31: शि तुक्
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.31"
SUTRA_TEXT = "शि तुक्"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8331:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.31: अग्निः'),
		('रामः', '', 'प.8.3.31: रामः'),
		('सीता', '', 'प.8.3.31: सीता'),
	]

