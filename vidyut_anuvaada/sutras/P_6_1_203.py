# Sutra प.6.1.203: वृषादीनां च
# sandhi-sūtra प.6.1.203

from P_6_1 import apply_6_1_203

SUTRA_CODE = "प.6.1.203"
SUTRA_TEXT = "वृषादीनां च"
SUTRA_DESC = "sandhi-sūtra प.6.1.203"


class Sutra61203:
	def apply(self, word, pos):
		return apply_6_1_203(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.203:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.203:marker=padartha;input=रामः'),
		('सीता', '', '6.1.203:marker=padartha;input=सीता'),
	]
