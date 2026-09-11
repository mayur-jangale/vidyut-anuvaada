# Sutra प.3.1.106: वदः सुपि क्यप् च
# śnābhyāṃ śnoḥ — repeated pattern

from P_3_1 import apply_3_1_106

SUTRA_CODE = "प.3.1.106"
SUTRA_TEXT = "वदः सुपि क्यप् च"
SUTRA_DESC = "śnābhyāṃ śnoḥ — repeated pattern"


class Sutra31106:
	code = SUTRA_CODE

	def apply(self, word, pos):
		return apply_3_1_106(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'प.3.1.106:root=अग्निः;pos='),
		('रामः', '', 'प.3.1.106:root=रामः;pos='),
		('सीता', '', 'प.3.1.106:root=सीता;pos='),
	]

