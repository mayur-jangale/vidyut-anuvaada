# Sutra प7: liNarTe leT
# liN-arTe leT

from sutra_engines import apply_general
from P_3_4 import apply_3_4_7

SUTRA_CODE = "प7"
SUTRA_TEXT = "liNarTe leT"
SUTRA_DESC = "liN-arTe leT"


class Sutra3407:
	def apply(self, word, pos):
		return apply_3_4_7(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-007:liN-arTe leT;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-007:liN-arTe leT;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-007:liN-arTe leT;input=सीता;stem=सीता;ending=-;pos='),
	]

