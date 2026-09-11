# Sutra प34: nimUla samUla kaSaH
# nimUla samUla kaSaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_34

SUTRA_CODE = "प34"
SUTRA_TEXT = "nimUla samUla kaSaH"
SUTRA_DESC = "nimUla samUla kaSaH"


class Sutra3434:
	def apply(self, word, pos):
		return apply_3_4_34(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-034:nimUla samUla kaSaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-034:nimUla samUla kaSaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-034:nimUla samUla kaSaH;input=सीता;stem=सीता;ending=-;pos='),
	]

