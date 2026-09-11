# Sutra प.6.1.113: अतो रोरप्लुतादप्लुते
# sandhi-sūtra प.6.1.113

from P_6_1 import apply_6_1_113

SUTRA_CODE = "प.6.1.113"
SUTRA_TEXT = "अतो रोरप्लुतादप्लुते"
SUTRA_DESC = "sandhi-sūtra प.6.1.113"


class Sutra61113:
	def apply(self, word, pos):
		return apply_6_1_113(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.113:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.113:marker=padartha;input=रामः'),
		('सीता', '', '6.1.113:marker=padartha;input=सीता'),
	]
