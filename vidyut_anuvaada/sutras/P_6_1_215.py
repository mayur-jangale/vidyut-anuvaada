# Sutra प.6.1.215: विभाषा वेण्विन्धानयोः
# sandhi-sūtra प.6.1.215

from P_6_1 import apply_6_1_215

SUTRA_CODE = "प.6.1.215"
SUTRA_TEXT = "विभाषा वेण्विन्धानयोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.215"


class Sutra61215:
	def apply(self, word, pos):
		return apply_6_1_215(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.215:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.215:marker=padartha;input=रामः'),
		('सीता', '', '6.1.215:marker=padartha;input=सीता'),
	]
