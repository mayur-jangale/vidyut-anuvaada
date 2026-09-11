# Sutra प116: liN AsiSi
# liN AsiSi

from sutra_engines import apply_general
from P_3_4 import apply_3_4_116

SUTRA_CODE = "प116"
SUTRA_TEXT = "liN AsiSi"
SUTRA_DESC = "liN AsiSi"


class Sutra34116:
	def apply(self, word, pos):
		return apply_3_4_116(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-116:liN AsiSi;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-116:liN AsiSi;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-116:liN AsiSi;input=सीता;stem=सीता;ending=-;pos='),
	]

