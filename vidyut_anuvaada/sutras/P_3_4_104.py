# Sutra प104: kid AsiSi
# kid AsiSi

from sutra_engines import apply_general
from P_3_4 import apply_3_4_104

SUTRA_CODE = "प104"
SUTRA_TEXT = "kid AsiSi"
SUTRA_DESC = "kid AsiSi"


class Sutra34104:
	def apply(self, word, pos):
		return apply_3_4_104(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-104:kid AsiSi;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-104:kid AsiSi;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-104:kid AsiSi;input=सीता;stem=सीता;ending=-;pos='),
	]

