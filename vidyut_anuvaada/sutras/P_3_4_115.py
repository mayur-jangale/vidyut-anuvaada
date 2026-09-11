# Sutra प115: liT ca
# liT ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_115

SUTRA_CODE = "प115"
SUTRA_TEXT = "liT ca"
SUTRA_DESC = "liT ca"


class Sutra34115:
	def apply(self, word, pos):
		return apply_3_4_115(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-115:liT ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-115:liT ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-115:liT ca;input=सीता;stem=सीता;ending=-;pos='),
	]

