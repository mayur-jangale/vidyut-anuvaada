# Sutra प9: tumarTe sesenase
# tum-arTe sesenase

from sutra_engines import apply_general
from P_3_4 import apply_3_4_9

SUTRA_CODE = "प9"
SUTRA_TEXT = "tumarTe sesenase"
SUTRA_DESC = "tum-arTe sesenase"


class Sutra3409:
	def apply(self, word, pos):
		return apply_3_4_9(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-009:tum-arTe sesenase;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-009:tum-arTe sesenase;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-009:tum-arTe sesenase;input=सीता;stem=सीता;ending=-;pos='),
	]

