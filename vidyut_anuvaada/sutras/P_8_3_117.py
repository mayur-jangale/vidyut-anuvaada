# Sutra प.8.3.117: सुनोतेः स्यसनोः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.117"
SUTRA_TEXT = "सुनोतेः स्यसनोः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83117:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.117: अग्निः'),
		('रामः', '', 'प.8.3.117: रामः'),
		('सीता', '', 'प.8.3.117: सीता'),
	]

