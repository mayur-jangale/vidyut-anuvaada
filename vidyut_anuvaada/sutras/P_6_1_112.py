# Sutra प.6.1.112: ख्यत्यात् परस्य
# sandhi-sūtra प.6.1.112

from P_6_1 import apply_6_1_112

SUTRA_CODE = "प.6.1.112"
SUTRA_TEXT = "ख्यत्यात् परस्य"
SUTRA_DESC = "sandhi-sūtra प.6.1.112"


class Sutra61112:
	def apply(self, word, pos):
		return apply_6_1_112(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.112:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.112:marker=padartha;input=रामः'),
		('सीता', '', '6.1.112:marker=padartha;input=सीता'),
	]
