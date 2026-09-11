# Sutra प.6.1.150: विष्किरः शकुनौ वा
# sandhi-sūtra प.6.1.150

from P_6_1 import apply_6_1_150

SUTRA_CODE = "प.6.1.150"
SUTRA_TEXT = "विष्किरः शकुनौ वा"
SUTRA_DESC = "sandhi-sūtra प.6.1.150"


class Sutra61150:
	def apply(self, word, pos):
		return apply_6_1_150(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.150:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.150:marker=padartha;input=रामः'),
		('सीता', '', '6.1.150:marker=padartha;input=सीता'),
	]
