# Sutra प93: eta ai
# eta ai liT

from sutra_engines import apply_general
from P_3_4 import apply_3_4_93

SUTRA_CODE = "प93"
SUTRA_TEXT = "eta ai"
SUTRA_DESC = "eta ai liT"


class Sutra3493:
	def apply(self, word, pos):
		return apply_3_4_93(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-093:eta ai liT;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-093:eta ai liT;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-093:eta ai liT;input=सीता;stem=सीता;ending=-;pos='),
	]

