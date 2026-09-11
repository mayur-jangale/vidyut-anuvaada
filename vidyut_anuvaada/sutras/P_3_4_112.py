# Sutra प112: dviSaz ca
# dviSaz ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_112

SUTRA_CODE = "प112"
SUTRA_TEXT = "dviSaz ca"
SUTRA_DESC = "dviSaz ca"


class Sutra34112:
	def apply(self, word, pos):
		return apply_3_4_112(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-112:dviSaz ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-112:dviSaz ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-112:dviSaz ca;input=सीता;stem=सीता;ending=-;pos='),
	]

