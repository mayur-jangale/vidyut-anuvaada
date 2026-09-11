# Sutra प.6.1.122: सर्वत्र विभाषा गोः
# sandhi-sūtra प.6.1.122

from P_6_1 import apply_6_1_122

SUTRA_CODE = "प.6.1.122"
SUTRA_TEXT = "सर्वत्र विभाषा गोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.122"


class Sutra61122:
	def apply(self, word, pos):
		return apply_6_1_122(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.122:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.122:marker=padartha;input=रामः'),
		('सीता', '', '6.1.122:marker=padartha;input=सीता'),
	]
