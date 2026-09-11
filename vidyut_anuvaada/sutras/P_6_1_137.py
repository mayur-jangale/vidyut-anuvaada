# Sutra प.6.1.137: सम्पर्युपेभ्यः करोतौ भूषणे
# sandhi-sūtra प.6.1.137

from P_6_1 import apply_6_1_137

SUTRA_CODE = "प.6.1.137"
SUTRA_TEXT = "सम्पर्युपेभ्यः करोतौ भूषणे"
SUTRA_DESC = "sandhi-sūtra प.6.1.137"


class Sutra61137:
	def apply(self, word, pos):
		return apply_6_1_137(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.137:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.137:marker=padartha;input=रामः'),
		('सीता', '', '6.1.137:marker=padartha;input=सीता'),
	]
