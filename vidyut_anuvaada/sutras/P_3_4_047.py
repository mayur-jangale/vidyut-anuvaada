# Sutra प47: upadaMSa tfIyA
# upadaMSa tfIyAyAm

from sutra_engines import apply_general
from P_3_4 import apply_3_4_47

SUTRA_CODE = "प47"
SUTRA_TEXT = "upadaMSa tfIyA"
SUTRA_DESC = "upadaMSa tfIyAyAm"


class Sutra3447:
	def apply(self, word, pos):
		return apply_3_4_47(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-047:upadaMSa tfIyAyAm;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-047:upadaMSa tfIyAyAm;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-047:upadaMSa tfIyAyAm;input=सीता;stem=सीता;ending=-;pos='),
	]

