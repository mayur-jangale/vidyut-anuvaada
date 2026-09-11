# Sutra प.6.1.207: आशितः कर्ता
# sandhi-sūtra प.6.1.207

from P_6_1 import apply_6_1_207

SUTRA_CODE = "प.6.1.207"
SUTRA_TEXT = "आशितः कर्ता"
SUTRA_DESC = "sandhi-sūtra प.6.1.207"


class Sutra61207:
	def apply(self, word, pos):
		return apply_6_1_207(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.207:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.207:marker=padartha;input=रामः'),
		('सीता', '', '6.1.207:marker=padartha;input=सीता'),
	]
