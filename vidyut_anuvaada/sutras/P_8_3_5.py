# Sutra प.8.3.5: समः सुटि
# aṅgasya — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.5"
SUTRA_TEXT = "समः सुटि"
SUTRA_DESC = "aṅgasya — repeated"


class Sutra835:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.5: अग्निः'),
		('रामः', '', 'प.8.3.5: रामः'),
		('सीता', '', 'प.8.3.5: सीता'),
	]

