# Sutra प.6.1.69: एङ्ह्रस्वात् सम्बुद्धेः
# sandhi-sūtra प.6.1.69

from P_6_1 import apply_6_1_69

SUTRA_CODE = "प.6.1.69"
SUTRA_TEXT = "एङ्ह्रस्वात् सम्बुद्धेः"
SUTRA_DESC = "sandhi-sūtra प.6.1.69"


class Sutra6169:
	def apply(self, word, pos):
		return apply_6_1_69(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.69:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.69:marker=padartha;input=रामः'),
		('सीता', '', '6.1.69:marker=padartha;input=सीता'),
	]
