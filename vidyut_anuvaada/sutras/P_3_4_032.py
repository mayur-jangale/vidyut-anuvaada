# Sutra प32: varzapramARa Ulopa
# varza-pramARa Ulopa ca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_32

SUTRA_CODE = "प32"
SUTRA_TEXT = "varzapramARa Ulopa"
SUTRA_DESC = "varza-pramARa Ulopa ca"


class Sutra3432:
	def apply(self, word, pos):
		return apply_3_4_32(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-032:varza-pramARa Ulopa ca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-032:varza-pramARa Ulopa ca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-032:varza-pramARa Ulopa ca;input=सीता;stem=सीता;ending=-;pos='),
	]

