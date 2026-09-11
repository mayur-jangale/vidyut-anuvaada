# Sutra प.6.1.208: रिक्ते विभाषा
# sandhi-sūtra प.6.1.208

from P_6_1 import apply_6_1_208

SUTRA_CODE = "प.6.1.208"
SUTRA_TEXT = "रिक्ते विभाषा"
SUTRA_DESC = "sandhi-sūtra प.6.1.208"


class Sutra61208:
	def apply(self, word, pos):
		return apply_6_1_208(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.208:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.208:marker=padartha;input=रामः'),
		('सीता', '', '6.1.208:marker=padartha;input=सीता'),
	]
