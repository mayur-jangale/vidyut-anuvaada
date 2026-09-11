# Sutra प.6.1.102: प्रथमयोः पूर्वसवर्णः
# sandhi-sūtra प.6.1.102

from P_6_1 import apply_6_1_102

SUTRA_CODE = "प.6.1.102"
SUTRA_TEXT = "प्रथमयोः पूर्वसवर्णः"
SUTRA_DESC = "sandhi-sūtra प.6.1.102"


class Sutra61102:
	def apply(self, word, pos):
		return apply_6_1_102(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.102:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.102:marker=padartha;input=रामः'),
		('सीता', '', '6.1.102:marker=padartha;input=सीता'),
	]
