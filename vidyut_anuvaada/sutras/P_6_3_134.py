# Sutra प.6.3.134: इकः सुञि
# final-sandhi — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.3.134"
SUTRA_TEXT = "इकः सुञि"
SUTRA_DESC = "final-sandhi — continued"


class Sutra63134:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.3.134: अग्निः'),
		('रामः', '', 'प.6.3.134: रामः'),
		('सीता', '', 'प.6.3.134: सीता'),
	]

