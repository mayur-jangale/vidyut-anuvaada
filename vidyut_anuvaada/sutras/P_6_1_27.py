# Sutra प.6.1.27: शृतं पाके
# sandhi-sūtra प.6.1.27

from P_6_1 import apply_6_1_27

SUTRA_CODE = "प.6.1.27"
SUTRA_TEXT = "शृतं पाके"
SUTRA_DESC = "sandhi-sūtra प.6.1.27"


class Sutra6127:
	def apply(self, word, pos):
		return apply_6_1_27(word, pos)

	EXAMPLES = [
	('अग्निः', '', '6.1.27:marker=padartha;input=अग्निः'),
		('रामः', '', '6.1.27:marker=padartha;input=रामः'),
		('सीता', '', '6.1.27:marker=padartha;input=सीता'),
	]
