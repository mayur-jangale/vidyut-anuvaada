# Sutra प.6.1.53: अपगुरो णमुलि
# sandhi-sūtra प.6.1.53

from P_6_1 import apply_6_1_53

SUTRA_CODE = "प.6.1.53"
SUTRA_TEXT = "अपगुरो णमुलि"
SUTRA_DESC = "sandhi-sūtra प.6.1.53"


class Sutra6153:
	def apply(self, word, pos):
		return apply_6_1_53(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.53:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.53:marker=padartha;input=रामः'),
		('सीता', '', '6.1.53:marker=padartha;input=सीता'),
	]
