# Sutra प.6.1.92: वा सुप्यापिशलेः
# sandhi-sūtra प.6.1.92

from P_6_1 import apply_6_1_92

SUTRA_CODE = "प.6.1.92"
SUTRA_TEXT = "वा सुप्यापिशलेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.92"


class Sutra6192:
	def apply(self, word, pos):
		return apply_6_1_92(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.92:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.92:marker=padartha;input=रामः'),
		('सीता', '', '6.1.92:marker=padartha;input=सीता'),
	]
