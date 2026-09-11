# Sutra प73: dASa goGnO sampradAne
# dASa goGnO sampradAne

from sutra_engines import apply_general
from P_3_4 import apply_3_4_73

SUTRA_CODE = "प73"
SUTRA_TEXT = "dASa goGnO sampradAne"
SUTRA_DESC = "dASa goGnO sampradAne"


class Sutra3473:
	def apply(self, word, pos):
		return apply_3_4_73(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-073:dASa goGnO sampradAne;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-073:dASa goGnO sampradAne;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-073:dASa goGnO sampradAne;input=सीता;stem=सीता;ending=-;pos='),
	]

