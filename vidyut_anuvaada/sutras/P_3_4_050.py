# Sutra प50: samAsattO
# samAsattO

from sutra_engines import apply_general
from P_3_4 import apply_3_4_50

SUTRA_CODE = "प50"
SUTRA_TEXT = "samAsattO"
SUTRA_DESC = "samAsattO"


class Sutra3450:
	def apply(self, word, pos):
		return apply_3_4_50(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-050:samAsattO;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-050:samAsattO;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-050:samAsattO;input=सीता;stem=सीता;ending=-;pos='),
	]

