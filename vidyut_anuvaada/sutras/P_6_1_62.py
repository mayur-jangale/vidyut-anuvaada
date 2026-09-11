# Sutra प.6.1.62: अचि शीर्षः
# sandhi-sūtra प.6.1.62

from P_6_1 import apply_6_1_62

SUTRA_CODE = "प.6.1.62"
SUTRA_TEXT = "अचि शीर्षः"
SUTRA_DESC = "sandhi-sūtra प.6.1.62"


class Sutra6162:
	def apply(self, word, pos):
		return apply_6_1_62(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.62:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.62:marker=padartha;input=रामः'),
		('सीता', '', '6.1.62:marker=padartha;input=सीता'),
	]
