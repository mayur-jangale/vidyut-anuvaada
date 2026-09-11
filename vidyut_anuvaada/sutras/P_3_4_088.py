# Sutra प88: vA Candasi
# vA Candasi luG

from sutra_engines import apply_general
from P_3_4 import apply_3_4_88

SUTRA_CODE = "प88"
SUTRA_TEXT = "vA Candasi"
SUTRA_DESC = "vA Candasi luG"


class Sutra3488:
	def apply(self, word, pos):
		return apply_3_4_88(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-088:vA Candasi luG;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-088:vA Candasi luG;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-088:vA Candasi luG;input=सीता;stem=सीता;ending=-;pos='),
	]

