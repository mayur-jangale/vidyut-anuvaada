# Sutra प.8.3.107: सुञः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.107"
SUTRA_TEXT = "सुञः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra83107:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.107: अग्निः'),
		('रामः', '', 'प.8.3.107: रामः'),
		('सीता', '', 'प.8.3.107: सीता'),
	]

