# Sutra प.6.1.143: कुस्तुम्बुरूणि जातिः
# sandhi-sūtra प.6.1.143

from P_6_1 import apply_6_1_143

SUTRA_CODE = "प.6.1.143"
SUTRA_TEXT = "कुस्तुम्बुरूणि जातिः"
SUTRA_DESC = "sandhi-sūtra प.6.1.143"


class Sutra61143:
	def apply(self, word, pos):
		return apply_6_1_143(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.143:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.143:marker=padartha;input=रामः'),
		('सीता', '', '6.1.143:marker=padartha;input=सीता'),
	]
