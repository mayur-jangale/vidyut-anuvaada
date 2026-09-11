# Sutra प.6.1.174: उदात्तयणो हल्पूर्वात्
# sandhi-sūtra प.6.1.174

from P_6_1 import apply_6_1_174

SUTRA_CODE = "प.6.1.174"
SUTRA_TEXT = "उदात्तयणो हल्पूर्वात्"
SUTRA_DESC = "sandhi-sūtra प.6.1.174"


class Sutra61174:
	def apply(self, word, pos):
		return apply_6_1_174(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.174:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.174:marker=padartha;input=रामः'),
		('सीता', '', '6.1.174:marker=padartha;input=सीता'),
	]
