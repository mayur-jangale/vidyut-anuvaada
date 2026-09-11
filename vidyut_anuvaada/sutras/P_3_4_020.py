# Sutra प20: parAvarayoge
# parAvara-yoge ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_20

SUTRA_CODE = "प20"
SUTRA_TEXT = "parAvarayoge"
SUTRA_DESC = "parAvara-yoge ca"


class Sutra3420:
	def apply(self, word, pos):
		return apply_3_4_20(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-020:parAvara-yoge ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-020:parAvara-yoge ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-020:parAvara-yoge ca;input=सीता;stem=सीता;ending=-;pos='),
	]

