# Sutra प.6.1.220: अन्तोऽवत्याः
# sandhi-sūtra प.6.1.220

from P_6_1 import apply_6_1_220

SUTRA_CODE = "प.6.1.220"
SUTRA_TEXT = "अन्तोऽवत्याः"
SUTRA_DESC = "sandhi-sūtra प.6.1.220"


class Sutra61220:
	def apply(self, word, pos):
		return apply_6_1_220(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.220:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.220:marker=padartha;input=रामः'),
		('सीता', '', '6.1.220:marker=padartha;input=सीता'),
	]
