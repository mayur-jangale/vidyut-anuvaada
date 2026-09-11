# Sutra प.6.1.205: निष्ठा च द्व्यजनात्
# sandhi-sūtra प.6.1.205

from P_6_1 import apply_6_1_205

SUTRA_CODE = "प.6.1.205"
SUTRA_TEXT = "निष्ठा च द्व्यजनात्"
SUTRA_DESC = "sandhi-sūtra प.6.1.205"


class Sutra61205:
	def apply(self, word, pos):
		return apply_6_1_205(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.205:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.205:marker=padartha;input=रामः'),
		('सीता', '', '6.1.205:marker=padartha;input=सीता'),
	]
