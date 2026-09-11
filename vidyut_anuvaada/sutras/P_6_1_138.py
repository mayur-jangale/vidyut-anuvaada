# Sutra प.6.1.138: समवाये च
# sandhi-sūtra प.6.1.138

from P_6_1 import apply_6_1_138

SUTRA_CODE = "प.6.1.138"
SUTRA_TEXT = "समवाये च"
SUTRA_DESC = "sandhi-sūtra प.6.1.138"


class Sutra61138:
	def apply(self, word, pos):
		return apply_6_1_138(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.138:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.138:marker=padartha;input=रामः'),
		('सीता', '', '6.1.138:marker=padartha;input=सीता'),
	]
