# Sutra प102: liNas sI yuT
# liNas sI yuT

from sutra_engines import apply_general
from P_3_4 import apply_3_4_102

SUTRA_CODE = "प102"
SUTRA_TEXT = "liNas sI yuT"
SUTRA_DESC = "liNas sI yuT"


class Sutra34102:
	def apply(self, word, pos):
		return apply_3_4_102(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-102:liNas sI yuT;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-102:liNas sI yuT;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-102:liNas sI yuT;input=सीता;stem=सीता;ending=-;pos='),
	]

