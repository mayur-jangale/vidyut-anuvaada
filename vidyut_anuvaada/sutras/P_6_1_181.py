# Sutra प.6.1.181: विभाषा भाषायाम्
# sandhi-sūtra प.6.1.181

from P_6_1 import apply_6_1_181

SUTRA_CODE = "प.6.1.181"
SUTRA_TEXT = "विभाषा भाषायाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.181"


class Sutra61181:
	def apply(self, word, pos):
		return apply_6_1_181(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.181:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.181:marker=padartha;input=रामः'),
		('सीता', '', '6.1.181:marker=padartha;input=सीता'),
	]
