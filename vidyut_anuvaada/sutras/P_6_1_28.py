# Sutra प.6.1.28: प्यायः पी
# sandhi-sūtra प.6.1.28

from P_6_1 import apply_6_1_28

SUTRA_CODE = "प.6.1.28"
SUTRA_TEXT = "प्यायः पी"
SUTRA_DESC = "sandhi-sūtra प.6.1.28"


class Sutra6128:
	def apply(self, word, pos):
		return apply_6_1_28(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.28:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.28:marker=padartha;input=रामः'),
		('सीता', '', '6.1.28:marker=padartha;input=सीता'),
	]
