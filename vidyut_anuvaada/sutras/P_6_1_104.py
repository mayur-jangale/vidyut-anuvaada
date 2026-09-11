# Sutra प.6.1.104: नादिचि
# sandhi-sūtra प.6.1.104

from P_6_1 import apply_6_1_104

SUTRA_CODE = "प.6.1.104"
SUTRA_TEXT = "नादिचि"
SUTRA_DESC = "sandhi-sūtra प.6.1.104"


class Sutra61104:
	def apply(self, word, pos):
		return apply_6_1_104(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.104:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.104:marker=padartha;input=रामः'),
		('सीता', '', '6.1.104:marker=padartha;input=सीता'),
	]
