# Sutra प17: sfpitfdoH kasun
# sfpi tfdoH kasun

from sutra_engines import apply_general
from P_3_4 import apply_3_4_17

SUTRA_CODE = "प17"
SUTRA_TEXT = "sfpitfdoH kasun"
SUTRA_DESC = "sfpi tfdoH kasun"


class Sutra3417:
	def apply(self, word, pos):
		return apply_3_4_17(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-017:sfpi tfdoH kasun;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-017:sfpi tfdoH kasun;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-017:sfpi tfdoH kasun;input=सीता;stem=सीता;ending=-;pos='),
	]

