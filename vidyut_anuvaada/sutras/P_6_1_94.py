# Sutra प.6.1.94: एङि पररूपम्
# sandhi-sūtra प.6.1.94

from P_6_1 import apply_6_1_94

SUTRA_CODE = "प.6.1.94"
SUTRA_TEXT = "एङि पररूपम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.94"


class Sutra6194:
	def apply(self, word, pos):
		return apply_6_1_94(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.94:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.94:marker=padartha;input=रामः'),
		('सीता', '', '6.1.94:marker=padartha;input=सीता'),
	]
