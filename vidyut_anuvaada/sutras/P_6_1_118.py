# Sutra प.6.1.118: आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे
# sandhi-sūtra प.6.1.118

from P_6_1 import apply_6_1_118

SUTRA_CODE = "प.6.1.118"
SUTRA_TEXT = "आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे"
SUTRA_DESC = "sandhi-sūtra प.6.1.118"


class Sutra61118:
	def apply(self, word, pos):
		return apply_6_1_118(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.118:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.118:marker=padartha;input=रामः'),
		('सीता', '', '6.1.118:marker=padartha;input=सीता'),
	]
