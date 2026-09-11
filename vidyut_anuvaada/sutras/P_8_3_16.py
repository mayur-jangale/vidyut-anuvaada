# Sutra प.8.3.16: रोः सुपि
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.16"
SUTRA_TEXT = "रोः सुपि"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8316:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.16: अग्निः'),
		('रामः', '', 'प.8.3.16: रामः'),
		('सीता', '', 'प.8.3.16: सीता'),
	]

