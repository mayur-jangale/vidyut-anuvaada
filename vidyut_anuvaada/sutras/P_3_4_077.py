# Sutra प77: lasya
# lasya

from sutra_engines import apply_general
from P_3_4 import apply_3_4_77

SUTRA_CODE = "प77"
SUTRA_TEXT = "lasya"
SUTRA_DESC = "lasya"


class Sutra3477:
	def apply(self, word, pos):
		return apply_3_4_77(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-077:lasya;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-077:lasya;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-077:lasya;input=सीता;stem=सीता;ending=-;pos='),
	]

