# Sutra प75: tAByAm anyatra uNAdi
# tAByAm anyatroNAdayaH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_75

SUTRA_CODE = "प75"
SUTRA_TEXT = "tAByAm anyatra uNAdi"
SUTRA_DESC = "tAByAm anyatroNAdayaH"


class Sutra3475:
	def apply(self, word, pos):
		return apply_3_4_75(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-075:tAByAm anyatroNAdayaH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-075:tAByAm anyatroNAdayaH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-075:tAByAm anyatroNAdayaH;input=सीता;stem=सीता;ending=-;pos='),
	]

