# Sutra प.6.1.155: कास्तीराजस्तुन्दे नगरे
# sandhi-sūtra प.6.1.155

from P_6_1 import apply_6_1_155

SUTRA_CODE = "प.6.1.155"
SUTRA_TEXT = "कास्तीराजस्तुन्दे नगरे"
SUTRA_DESC = "sandhi-sūtra प.6.1.155"


class Sutra61155:
	def apply(self, word, pos):
		return apply_6_1_155(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.155:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.155:marker=padartha;input=रामः'),
		('सीता', '', '6.1.155:marker=padartha;input=सीता'),
	]
