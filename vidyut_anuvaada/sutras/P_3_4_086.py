# Sutra प86: eruH
# vidhiliN eruH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_86

SUTRA_CODE = "प86"
SUTRA_TEXT = "eruH"
SUTRA_DESC = "vidhiliN eruH"


class Sutra3486:
	def apply(self, word, pos):
		return apply_3_4_86(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-086:vidhiliN eruH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-086:vidhiliN eruH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-086:vidhiliN eruH;input=सीता;stem=सीता;ending=-;pos='),
	]

