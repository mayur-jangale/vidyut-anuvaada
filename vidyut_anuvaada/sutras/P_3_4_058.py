# Sutra प58: nAmnyAdi Si grahaH
# nAmnyAdi Si grahoH

from sutra_engines import apply_general
from P_3_4 import apply_3_4_58

SUTRA_CODE = "प58"
SUTRA_TEXT = "nAmnyAdi Si grahaH"
SUTRA_DESC = "nAmnyAdi Si grahoH"


class Sutra3458:
	def apply(self, word, pos):
		return apply_3_4_58(word, pos)

	EXAMPLES = [
	('अग्निः', '', 'p34-058:nAmnyAdi Si grahoH;input=अग्निः;stem=अग्निः;ending=-;pos='),
		('रामः', '', 'p34-058:nAmnyAdi Si grahoH;input=रामः;stem=रामः;ending=-;pos='),
		('सीता', '', 'p34-058:nAmnyAdi Si grahoH;input=सीता;stem=सीता;ending=-;pos='),
	]

