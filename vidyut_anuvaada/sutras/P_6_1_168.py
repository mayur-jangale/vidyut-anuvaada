# Sutra प.6.1.168: सावेकाचस्तृतीयादिर्विभक्तिः
# sandhi-sūtra प.6.1.168

from P_6_1 import apply_6_1_168

SUTRA_CODE = "प.6.1.168"
SUTRA_TEXT = "सावेकाचस्तृतीयादिर्विभक्तिः"
SUTRA_DESC = "sandhi-sūtra प.6.1.168"


class Sutra61168:
	def apply(self, word, pos):
		return apply_6_1_168(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.168:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.168:marker=padartha;input=रामः'),
		('सीता', '', '6.1.168:marker=padartha;input=सीता'),
	]
