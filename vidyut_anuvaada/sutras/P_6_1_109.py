# Sutra प.6.1.109: एङः पदान्तादति
# sandhi-sūtra प.6.1.109

from P_6_1 import apply_6_1_109

SUTRA_CODE = "प.6.1.109"
SUTRA_TEXT = "एङः पदान्तादति"
SUTRA_DESC = "sandhi-sūtra प.6.1.109"


class Sutra61109:
	def apply(self, word, pos):
		return apply_6_1_109(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.109:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.109:marker=padartha;input=रामः'),
		('सीता', '', '6.1.109:marker=padartha;input=सीता'),
	]
