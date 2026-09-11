# Sutra प.6.1.159: कर्षात्वतो घञोऽन्त उदात्तः
# sandhi-sūtra प.6.1.159

from P_6_1 import apply_6_1_159

SUTRA_CODE = "प.6.1.159"
SUTRA_TEXT = "कर्षात्वतो घञोऽन्त उदात्तः"
SUTRA_DESC = "sandhi-sūtra प.6.1.159"


class Sutra61159:
	def apply(self, word, pos):
		return apply_6_1_159(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.159:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.159:marker=padartha;input=रामः'),
		('सीता', '', '6.1.159:marker=padartha;input=सीता'),
	]
