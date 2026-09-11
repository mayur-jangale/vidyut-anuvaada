# Sutra प107: suT TitoH
# suT TitoH svAsryAH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_107

SUTRA_CODE = "प107"
SUTRA_TEXT = "suT TitoH"
SUTRA_DESC = "suT TitoH svAsryAH"


class Sutra34107:
	def apply(self, word, pos):
		return apply_3_4_107(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-107:suT TitoH svAsryAH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-107:suT TitoH svAsryAH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-107:suT TitoH svAsryAH;input=सीता;stem=सीता;ending=-;pos='),
	]

