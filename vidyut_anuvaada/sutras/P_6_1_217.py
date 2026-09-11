# Sutra प.6.1.217: उपोत्तमं रिति
# sandhi-sūtra प.6.1.217

from P_6_1 import apply_6_1_217

SUTRA_CODE = "प.6.1.217"
SUTRA_TEXT = "उपोत्तमं रिति"
SUTRA_DESC = "sandhi-sūtra प.6.1.217"


class Sutra61217:
	def apply(self, word, pos):
		return apply_6_1_217(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.217:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.217:marker=padartha;input=रामः'),
		('सीता', '', '6.1.217:marker=padartha;input=सीता'),
	]
