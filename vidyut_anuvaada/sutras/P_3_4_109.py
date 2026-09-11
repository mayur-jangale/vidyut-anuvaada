# Sutra प109: sij aByasta vidiByaSca
# sij aByasta vidiByaSca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_109

SUTRA_CODE = "प109"
SUTRA_TEXT = "sij aByasta vidiByaSca"
SUTRA_DESC = "sij aByasta vidiByaSca"


class Sutra34109:
	def apply(self, word, pos):
		return apply_3_4_109(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-109:sij aByasta vidiByaSca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-109:sij aByasta vidiByaSca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-109:sij aByasta vidiByaSca;input=सीता;stem=सीता;ending=-;pos='),
	]

