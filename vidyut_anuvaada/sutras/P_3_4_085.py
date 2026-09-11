# Sutra प85: loTo laNvat
# loTo laNvat

from sutra_engines import apply_general
from P_3_4 import apply_3_4_85

SUTRA_CODE = "प85"
SUTRA_TEXT = "loTo laNvat"
SUTRA_DESC = "loTo laNvat"


class Sutra3485:
	def apply(self, word, pos):
		return apply_3_4_85(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-085:loTo laNvat;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-085:loTo laNvat;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-085:loTo laNvat;input=सीता;stem=सीता;ending=-;pos='),
	]

