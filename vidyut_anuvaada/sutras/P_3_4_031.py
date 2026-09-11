# Sutra प31: carmodarayoH pUraH
# carmodarayoH pUraH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_31

SUTRA_CODE = "प31"
SUTRA_TEXT = "carmodarayoH pUraH"
SUTRA_DESC = "carmodarayoH pUraH"


class Sutra3431:
	def apply(self, word, pos):
		return apply_3_4_31(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-031:carmodarayoH pUraH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-031:carmodarayoH pUraH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-031:carmodarayoH pUraH;input=सीता;stem=सीता;ending=-;pos='),
	]

