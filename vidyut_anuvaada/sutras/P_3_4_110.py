# Sutra प110: AtaH
# AtaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_110

SUTRA_CODE = "प110"
SUTRA_TEXT = "AtaH"
SUTRA_DESC = "AtaH"


class Sutra34110:
	def apply(self, word, pos):
		return apply_3_4_110(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-110:AtaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-110:AtaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-110:AtaH;input=सीता;stem=सीता;ending=-;pos='),
	]

