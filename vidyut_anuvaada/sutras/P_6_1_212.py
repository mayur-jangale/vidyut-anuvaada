# Sutra प.6.1.212: ङयि च
# sandhi-sūtra प.6.1.212

from P_6_1 import apply_6_1_212

SUTRA_CODE = "प.6.1.212"
SUTRA_TEXT = "ङयि च"
SUTRA_DESC = "sandhi-sūtra प.6.1.212"


class Sutra61212:
	def apply(self, word, pos):
		return apply_6_1_212(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.212:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.212:marker=padartha;input=रामः'),
		('सीता', '', '6.1.212:marker=padartha;input=सीता'),
	]
