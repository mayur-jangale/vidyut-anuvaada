# Sutra प33: cele knopeH
# cele knopeH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_33

SUTRA_CODE = "प33"
SUTRA_TEXT = "cele knopeH"
SUTRA_DESC = "cele knopeH"


class Sutra3433:
	def apply(self, word, pos):
		return apply_3_4_33(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-033:cele knopeH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-033:cele knopeH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-033:cele knopeH;input=सीता;stem=सीता;ending=-;pos='),
	]

