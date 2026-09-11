# Sutra प113: tiN Sit sArvadhAtukam
# tiN Sit sArvadhAtukam

from sutra_engines import apply_general
from P_3_4 import apply_3_4_113

SUTRA_CODE = "प113"
SUTRA_TEXT = "tiN Sit sArvadhAtukam"
SUTRA_DESC = "tiN Sit sArvadhAtukam"


class Sutra34113:
	def apply(self, word, pos):
		return apply_3_4_113(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-113:tiN Sit sArvadhAtukam;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-113:tiN Sit sArvadhAtukam;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-113:tiN Sit sArvadhAtukam;input=सीता;stem=सीता;ending=-;pos='),
	]

