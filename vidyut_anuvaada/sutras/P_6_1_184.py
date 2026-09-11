# Sutra प.6.1.184: नृ चान्यतरस्याम्
# sandhi-sūtra प.6.1.184

from P_6_1 import apply_6_1_184

SUTRA_CODE = "प.6.1.184"
SUTRA_TEXT = "नृ चान्यतरस्याम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.184"


class Sutra61184:
	def apply(self, word, pos):
		return apply_6_1_184(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.184:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.184:marker=padartha;input=रामः'),
		('सीता', '', '6.1.184:marker=padartha;input=सीता'),
	]
