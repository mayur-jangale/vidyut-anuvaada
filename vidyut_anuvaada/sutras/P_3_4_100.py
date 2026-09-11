# Sutra प100: itaSca tNi
# itaSca tNi lopaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_100

SUTRA_CODE = "प100"
SUTRA_TEXT = "itaSca tNi"
SUTRA_DESC = "itaSca tNi lopaH"


class Sutra34100:
	def apply(self, word, pos):
		return apply_3_4_100(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-100:itaSca tNi lopaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-100:itaSca tNi lopaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-100:itaSca tNi lopaH;input=सीता;stem=सीता;ending=-;pos='),
	]

