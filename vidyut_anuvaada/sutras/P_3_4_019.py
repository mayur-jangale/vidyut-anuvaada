# Sutra प19: udIcAM mANo
# udIcAM mANo vyatIhAre

from sutra_engines import apply_general
from P_3_4 import apply_3_4_19

SUTRA_CODE = "प19"
SUTRA_TEXT = "udIcAM mANo"
SUTRA_DESC = "udIcAM mANo vyatIhAre"


class Sutra3419:
	def apply(self, word, pos):
		return apply_3_4_19(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-019:udIcAM mANo vyatIhAre;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-019:udIcAM mANo vyatIhAre;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-019:udIcAM mANo vyatIhAre;input=सीता;stem=सीता;ending=-;pos='),
	]

