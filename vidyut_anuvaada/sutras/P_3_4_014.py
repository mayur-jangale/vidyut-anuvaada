# Sutra प14: kftyArTe tavya
# kfty-arTe tavya

from sutra_engines import apply_general
from P_3_4 import apply_3_4_14

SUTRA_CODE = "प14"
SUTRA_TEXT = "kftyArTe tavya"
SUTRA_DESC = "kfty-arTe tavya"


class Sutra3414:
	def apply(self, word, pos):
		return apply_3_4_14(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-014:kfty-arTe tavya;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-014:kfty-arTe tavya;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-014:kfty-arTe tavya;input=सीता;stem=सीता;ending=-;pos='),
	]

