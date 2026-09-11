# Sutra प38: snehane pizaH
# snehane pizaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_38

SUTRA_CODE = "प38"
SUTRA_TEXT = "snehane pizaH"
SUTRA_DESC = "snehane pizaH"


class Sutra3438:
	def apply(self, word, pos):
		return apply_3_4_38(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-038:snehane pizaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-038:snehane pizaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-038:snehane pizaH;input=सीता;stem=सीता;ending=-;pos='),
	]

