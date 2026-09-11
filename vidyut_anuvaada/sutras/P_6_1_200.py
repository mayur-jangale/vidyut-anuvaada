# Sutra प.6.1.200: अन्तश्च तवै युगपत्
# sandhi-sūtra प.6.1.200

from P_6_1 import apply_6_1_200

SUTRA_CODE = "प.6.1.200"
SUTRA_TEXT = "अन्तश्च तवै युगपत्"
SUTRA_DESC = "sandhi-sūtra प.6.1.200"


class Sutra61200:
	def apply(self, word, pos):
		return apply_6_1_200(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.200:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.200:marker=padartha;input=रामः'),
		('सीता', '', '6.1.200:marker=padartha;input=सीता'),
	]
