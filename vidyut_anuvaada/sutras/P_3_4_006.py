# Sutra प6: Candasi luN laN liTaH
# Candasi luN laN liT

from sutra_engines import apply_general
from P_3_4 import apply_3_4_6

SUTRA_CODE = "प6"
SUTRA_TEXT = "Candasi luN laN liTaH"
SUTRA_DESC = "Candasi luN laN liT"


class Sutra3406:
	def apply(self, word, pos):
		return apply_3_4_6(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-006:Candasi luN laN liT;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-006:Candasi luN laN liT;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-006:Candasi luN laN liT;input=सीता;stem=सीता;ending=-;pos='),
	]

