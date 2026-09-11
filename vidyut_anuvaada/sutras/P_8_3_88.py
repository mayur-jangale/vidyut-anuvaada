# Sutra प.8.3.88: सुविनिर्दुर्भ्यः सुपिसूतिसमाः
# ordīrghājjasaḥ — repeated

from sutra_engines import apply_general

SUTRA_CODE = "प.8.3.88"
SUTRA_TEXT = "सुविनिर्दुर्भ्यः सुपिसूतिसमाः"
SUTRA_DESC = "ordīrghājjasaḥ — repeated"


class Sutra8388:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.8.3.88: अग्निः'),
		('रामः', '', 'प.8.3.88: रामः'),
		('सीता', '', 'प.8.3.88: सीता'),
	]

