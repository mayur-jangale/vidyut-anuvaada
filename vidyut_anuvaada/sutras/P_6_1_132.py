# Sutra प.6.1.132: एतत्तदोः सुलोपोऽकोरनञ्समासे हलि
# sandhi-sūtra प.6.1.132

from P_6_1 import apply_6_1_132

SUTRA_CODE = "प.6.1.132"
SUTRA_TEXT = "एतत्तदोः सुलोपोऽकोरनञ्समासे हलि"
SUTRA_DESC = "sandhi-sūtra प.6.1.132"


class Sutra61132:
	def apply(self, word, pos):
		return apply_6_1_132(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.132:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.132:marker=padartha;input=रामः'),
		('सीता', '', '6.1.132:marker=padartha;input=सीता'),
	]
