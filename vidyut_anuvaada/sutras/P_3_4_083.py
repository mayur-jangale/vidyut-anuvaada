# Sutra प83: vido lawo vA
# vido lawo vA leT

from sutra_engines import apply_general
from P_3_4 import apply_3_4_83

SUTRA_CODE = "प83"
SUTRA_TEXT = "vido lawo vA"
SUTRA_DESC = "vido lawo vA leT"


class Sutra3483:
	def apply(self, word, pos):
		return apply_3_4_83(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-083:vido lawo vA leT;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-083:vido lawo vA leT;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-083:vido lawo vA leT;input=सीता;stem=सीता;ending=-;pos='),
	]

