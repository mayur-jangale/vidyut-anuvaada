# Sutra प.6.1.163: चितः
# sandhi-sūtra प.6.1.163

from P_6_1 import apply_6_1_163

SUTRA_CODE = "प.6.1.163"
SUTRA_TEXT = "चितः"
SUTRA_DESC = "sandhi-sūtra प.6.1.163"


class Sutra61163:
	def apply(self, word, pos):
		return apply_6_1_163(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.163:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.163:marker=padartha;input=रामः'),
		('सीता', '', '6.1.163:marker=padartha;input=सीता'),
	]
