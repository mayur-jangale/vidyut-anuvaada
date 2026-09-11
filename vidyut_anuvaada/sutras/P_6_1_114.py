# Sutra प.6.1.114: हशि च
# sandhi-sūtra प.6.1.114

from P_6_1 import apply_6_1_114

SUTRA_CODE = "प.6.1.114"
SUTRA_TEXT = "हशि च"
SUTRA_DESC = "sandhi-sūtra प.6.1.114"


class Sutra61114:
	def apply(self, word, pos):
		return apply_6_1_114(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.114:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.114:marker=padartha;input=रामः'),
		('सीता', '', '6.1.114:marker=padartha;input=सीता'),
	]
