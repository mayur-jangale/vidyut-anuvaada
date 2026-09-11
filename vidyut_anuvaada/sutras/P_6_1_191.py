# Sutra प.6.1.191: सर्वस्य सुपि
# sandhi-sūtra प.6.1.191

from P_6_1 import apply_6_1_191

SUTRA_CODE = "प.6.1.191"
SUTRA_TEXT = "सर्वस्य सुपि"
SUTRA_DESC = "sandhi-sūtra प.6.1.191"


class Sutra61191:
	def apply(self, word, pos):
		return apply_6_1_191(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.191:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.191:marker=padartha;input=रामः'),
		('सीता', '', '6.1.191:marker=padartha;input=सीता'),
	]
