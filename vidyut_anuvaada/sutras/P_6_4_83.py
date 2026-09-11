# Sutra प.6.4.83: ओः सुपि
# samprasāraṇa — continued

from sutra_engines import apply_general

SUTRA_CODE = "प.6.4.83"
SUTRA_TEXT = "ओः सुपि"
SUTRA_DESC = "samprasāraṇa — continued"


class Sutra6483:
	def apply(self, word, pos):
		return apply_general(word, pos, SUTRA_CODE)

	EXAMPLES = [
	('अग्निः', '', 'प.6.4.83: अग्निः'),
		('रामः', '', 'प.6.4.83: रामः'),
		('सीता', '', 'प.6.4.83: सीता'),
	]

