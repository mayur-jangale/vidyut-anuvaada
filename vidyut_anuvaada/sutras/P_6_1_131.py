# Sutra प.6.1.131: दिव उत्
# sandhi-sūtra प.6.1.131

from P_6_1 import apply_6_1_131

SUTRA_CODE = "प.6.1.131"
SUTRA_TEXT = "दिव उत्"
SUTRA_DESC = "sandhi-sūtra प.6.1.131"


class Sutra61131:
	def apply(self, word, pos):
		return apply_6_1_131(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.131:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.131:marker=padartha;input=रामः'),
		('सीता', '', '6.1.131:marker=padartha;input=सीता'),
	]
