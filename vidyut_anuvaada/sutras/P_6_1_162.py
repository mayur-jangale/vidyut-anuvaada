# Sutra प.6.1.162: धातोः
# sandhi-sūtra प.6.1.162

from P_6_1 import apply_6_1_162

SUTRA_CODE = "प.6.1.162"
SUTRA_TEXT = "धातोः"
SUTRA_DESC = "sandhi-sūtra प.6.1.162"


class Sutra61162:
	def apply(self, word, pos):
		return apply_6_1_162(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.162:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.162:marker=padartha;input=रामः'),
		('सीता', '', '6.1.162:marker=padartha;input=सीता'),
	]
