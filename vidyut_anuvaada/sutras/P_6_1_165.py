# Sutra प.6.1.165: कितः
# sandhi-sūtra प.6.1.165

from P_6_1 import apply_6_1_165

SUTRA_CODE = "प.6.1.165"
SUTRA_TEXT = "कितः"
SUTRA_DESC = "sandhi-sūtra प.6.1.165"


class Sutra61165:
	def apply(self, word, pos):
		return apply_6_1_165(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.165:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.165:marker=padartha;input=रामः'),
		('सीता', '', '6.1.165:marker=padartha;input=सीता'),
	]
