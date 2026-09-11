# Sutra प.6.1.196: थलि च सेटीडन्तो वा
# sandhi-sūtra प.6.1.196

from P_6_1 import apply_6_1_196

SUTRA_CODE = "प.6.1.196"
SUTRA_TEXT = "थलि च सेटीडन्तो वा"
SUTRA_DESC = "sandhi-sūtra प.6.1.196"


class Sutra61196:
	def apply(self, word, pos):
		return apply_6_1_196(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.196:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.196:marker=padartha;input=रामः'),
		('सीता', '', '6.1.196:marker=padartha;input=सीता'),
	]
