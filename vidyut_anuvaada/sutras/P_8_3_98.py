# Sutra प.8.3.98: सुषामादिषु च
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.98"
SUTRA_TEXT = "सुषामादिषु च"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8398:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.98: अग्निः'),
		('रामः', '', 'प.8.3.98: रामः'),
		('सीता', '', 'प.8.3.98: सीता'),
	]

