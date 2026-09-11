# Sutra प.6.1.22: स्फायः स्फी निष्ठायाम्
# sandhi-sūtra प.6.1.22

from P_6_1 import apply_6_1_22

SUTRA_CODE = "प.6.1.22"
SUTRA_TEXT = "स्फायः स्फी निष्ठायाम्"
SUTRA_DESC = "sandhi-sūtra प.6.1.22"


class Sutra6122:
	def apply(self, word, pos):
		return apply_6_1_22(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.22:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.22:marker=padartha;input=रामः'),
		('सीता', '', '6.1.22:marker=padartha;input=सीता'),
	]
