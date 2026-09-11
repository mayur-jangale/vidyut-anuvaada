# Sutra प117: CandasyuBayatTA
# CandasyuBayatTA

from sutra_engines import apply_general
from P_3_4 import apply_3_4_117

SUTRA_CODE = "प117"
SUTRA_TEXT = "CandasyuBayatTA"
SUTRA_DESC = "CandasyuBayatTA"


class Sutra34117:
	def apply(self, word, pos):
		return apply_3_4_117(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-117:CandasyuBayatTA;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-117:CandasyuBayatTA;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-117:CandasyuBayatTA;input=सीता;stem=सीता;ending=-;pos='),
	]

