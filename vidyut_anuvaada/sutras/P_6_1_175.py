# Sutra प.6.1.175: नोङ्धात्वोः
# sandhi-sūtra प.6.1.175

from P_6_1 import apply_6_1_175

SUTRA_CODE = "प.6.1.175"
SUTRA_TEXT = "नोङ्धात्वोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.175"


class Sutra61175:
	def apply(self, word, pos):
		return apply_6_1_175(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.175:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.175:marker=padartha;input=रामः'),
		('सीता', '', '6.1.175:marker=padartha;input=सीता'),
	]
