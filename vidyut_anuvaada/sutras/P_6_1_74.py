# Sutra प.6.1.74: आङ्माङोश्च
# sandhi-sūtra प.6.1.74

from P_6_1 import apply_6_1_74

SUTRA_CODE = "प.6.1.74"
SUTRA_TEXT = "आङ्माङोश्च"
SUTRA_DESC = "sandhi-sūtra प.6.1.74"


class Sutra6174:
	def apply(self, word, pos):
		return apply_6_1_74(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.74:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.74:marker=padartha;input=रामः'),
		('सीता', '', '6.1.74:marker=padartha;input=सीता'),
	]
