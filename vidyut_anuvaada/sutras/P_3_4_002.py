# Sutra प2: kriyAsamaBihAre low
# kriya-samuccaya low

from sutra_engines import apply_general
from P_3_4 import apply_3_4_2

SUTRA_CODE = "प2"
SUTRA_TEXT = "kriyAsamaBihAre low"
SUTRA_DESC = "kriya-samuccaya low"


class Sutra3402:
	def apply(self, word, pos):
		return apply_3_4_2(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-002:kriya-samuccaya low;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-002:kriya-samuccaya low;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-002:kriya-samuccaya low;input=सीता;stem=सीता;ending=-;pos='),
	]

