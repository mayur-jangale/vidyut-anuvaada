# Sutra प.6.1.158: अनुदात्तं पदमेकवर्जम्
# sandhi-sūtra प.6.1.158

from P_6_1 import apply_6_1_158

SUTRA_CODE = "प.6.1.158"
SUTRA_TEXT = "अनुदात्तं पदमेकवर्जम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.158"


class Sutra61158:
	def apply(self, word, pos):
		return apply_6_1_158(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.158:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.158:marker=padartha;input=रामः'),
		('सीता', '', '6.1.158:marker=padartha;input=सीता'),
	]
