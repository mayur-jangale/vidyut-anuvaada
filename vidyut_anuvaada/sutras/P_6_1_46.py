# Sutra प.6.1.46: न व्यो लिटि
# sandhi-sūtra प.6.1.46

from P_6_1 import apply_6_1_46

SUTRA_CODE = "प.6.1.46"
SUTRA_TEXT = "न व्यो लिटि"
SUTRA_DESC = "sandhi-sūtra प.6.1.46"


class Sutra6146:
	def apply(self, word, pos):
		return apply_6_1_46(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.46:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.46:marker=padartha;input=रामः'),
		('सीता', '', '6.1.46:marker=padartha;input=सीता'),
	]
