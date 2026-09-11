# Sutra प.6.1.91: उपसर्गादृति धातौ
# sandhi-sūtra प.6.1.91

from P_6_1 import apply_6_1_91

SUTRA_CODE = "प.6.1.91"
SUTRA_TEXT = "उपसर्गादृति धातौ"
SUTRA_DESC = "sandhi-sūtra प.6.1.91"


class Sutra6191:
	def apply(self, word, pos):
		return apply_6_1_91(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.91:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.91:marker=padartha;input=रामः'),
		('सीता', '', '6.1.91:marker=padartha;input=सीता'),
	]
