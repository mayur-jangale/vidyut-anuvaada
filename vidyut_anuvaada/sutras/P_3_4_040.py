# Sutra प40: sve puzaH
# sve puzaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_40

SUTRA_CODE = "प40"
SUTRA_TEXT = "sve puzaH"
SUTRA_DESC = "sve puzaH"


class Sutra3440:
	def apply(self, word, pos):
		return apply_3_4_40(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-040:sve puzaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-040:sve puzaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-040:sve puzaH;input=सीता;stem=सीता;ending=-;pos='),
	]

