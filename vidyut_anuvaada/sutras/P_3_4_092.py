# Sutra प92: ADuttamasya picca
# AD uttamasya picca

from sutra_engines import apply_general
from P_3_4 import apply_3_4_92

SUTRA_CODE = "प92"
SUTRA_TEXT = "ADuttamasya picca"
SUTRA_DESC = "AD uttamasya picca"


class Sutra3492:
	def apply(self, word, pos):
		return apply_3_4_92(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-092:AD uttamasya picca;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-092:AD uttamasya picca;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-092:AD uttamasya picca;input=सीता;stem=सीता;ending=-;pos='),
	]

